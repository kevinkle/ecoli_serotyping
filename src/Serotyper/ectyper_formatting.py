#!/usr/bin/env python
import csv
import os.path

from flask import url_for
from ecprediction import *

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + "/"


def toSimpleDict(data, verbose):
    """
    Taking the results dictionary and converting it into a non-nested simple dictionary.

    :param data: Original results dictionary
    :param verbose: Boolean defining the type of information desired by the user.
    :return resultDict: Non-nested dictionary.
    """
    logging.info('Simplifying the result dictionary.')
    resultDict= {}

    if verbose == 0:
        return data

    for genome_name, type in data.iteritems():
        resultDict[genome_name] = {}
        if isinstance(type, dict):
            oTempStr =''
            hTempStr = ''
            if isinstance(data[genome_name]['H type'], dict):
                for title, info in data[genome_name]['H type'].iteritems():
                    if title == 'RESULT':
                        hTempStr= str(title) + ": " + str(info) + "; " + hTempStr
                    else:
                        hTempStr+= str(title) + ": " + str(info) + "; "
                resultDict[genome_name]['H type'] =  hTempStr
            else:
                resultDict[genome_name]['H type'] = data[genome_name]['H type']

            if isinstance(data[genome_name]['O type'], dict):
                for title, info in data[genome_name]['O type'].iteritems():
                    if title == 'RESULT':
                        oTempStr = str(title) + ": " + str(info) + "; " + oTempStr
                    else:
                        oTempStr += str(title) + ": " + str(info) + "; "
                resultDict[genome_name]['O type'] = oTempStr
            else:
                resultDict[genome_name]['O type'] = data[genome_name]['O type']

        else:
            resultDict[genome_name]['H type'] = data[genome_name]
            resultDict[genome_name]['O type'] = data[genome_name]
    return resultDict



def toHTML(data, verbose):
    """
    Rendering the results dictionary in an HTML table.

    :param data: Results dictionary.
    :param verbose: Boolean defining the type of information the user desires.
    :return: String containing the HTML page containing the table.
    """

    resultDict = toSimpleDict(data, verbose)
    stylesheet_url = url_for('static',filename='css/style.css')
    js_url = url_for('static', filename='js/results.js')
    html_info = "<!DOCTYPE html> \
                 <html lang='en'> \
                 <head> \
                    <meta charset='UTF-8'> \
                    <title>Results</title> \
                    <link rel='stylesheet' type='text/css' href=" + str(stylesheet_url) + ">" \
                   "<script type='text/javascript' src='" + js_url + "'></script>  \
                 </head>\
                 <body>"
    result_table = "<div id='results-div'><table class=results><caption class='results-caption'>SEROTYPE PREDICTION RESULTS" \
                   "</caption>" \
                   "<thead class='results-head'><tr>" \
                        "<th>Genome</th>" \
                        "<th>O Type</th>" \
                        "<th>H Type</th>" \
                   "</tr></thead><tbody>"

    for genome_name in resultDict.keys():
        result_genome = str(genome_name)
        result_otype = str(resultDict[genome_name]['O type']).replace(";", '<br>')
        result_htype = str(resultDict[genome_name]['H type']).replace(";", '<br>')

        result_table+= "<tr><td id='result-genome'>" + result_genome + "</td><td>" + result_otype + "</td><td>" + \
                       result_htype + "</td></tr>"

    result_table+= "</tbody></table></div>"


    return_button = "<div id='result-button'>" \
                    "<input type='button' class='button result-button' onclick='" + \
                    'location.href="/upload";' + \
                    "' value='Return to main page'/>" \
                    "<button type='button' id='download-button' class='button result-button'>Download the results"\
                    "</button></div>"

    return html_info + result_table + return_button + "</body></html>"


def formatResults(topMatches, verbose):
    """
    Filtering through the top matches dictionary to only keep the necessary result information (may be changed later
    on).

    :param topMatches: Top matches dictionary containing all the unfiltered results.
    :param verbose: Boolean stating whether the user wants full information or not.
    :return resultDict: Top matches dictionary containing the filtered results.
    """
    logging.info('Creating the final results dictionary.')

    resultDict = {}
    if verbose == 1:
        #Generate the final full dictionary with full information about the serotype
        for genome_name, serotype in topMatches.iteritems():
            if serotype == 'NA':
                resultDict[genome_name] = 'No matches were found for this genome, thus no prediction could be made.'
            else:
                tempDict1 = {}
                for type, info in serotype.iteritems():
                    if info == 'NA' and type != 'prediction_strength':
                        tempDict1[type] = 'No prediction could be made for O types for this genome.'
                    elif info == 'NM':
                        tempDict1[type] = 'No prediction could be made for H types for this genome (non-motile).'
                    elif type != 'prediction_strength':
                        tempDict2 = {}
                        for key, value in info.iteritems():
                            if key == 'title':
                                otype = searchType(value, 'O')
                                htype = searchType(value, 'H')

                                if otype != 'none':
                                    tempDict2['RESULT'] =  str(otype)
                                else:
                                    tempDict2['RESULT'] = str(htype)
                            elif key != 'hsp':
                                tempDict2[key] = str(value)
                            else:
                                tempDict2['score'] = str(value.score)
                                tempDict2['bits'] = str(value.bits)
                                tempDict2['e value'] = str(value.expect)
                        tempDict1[type] = tempDict2
                    else:
                        tempDict1['Prediction Strength'] = str(info)
                    resultDict[genome_name] = tempDict1
    else:
        #Generate the final full dictionary with serotype only
        for genome_name, serotype in topMatches.iteritems():
            if serotype == 'NA':
                resultDict[genome_name] = 'No matches were found for this genome, thus no prediction could be made.'
            else:
                tempDict = {}
                if topMatches[genome_name]['O type'] != 'NA':
                    tempDict['O type'] = searchType(topMatches[genome_name]['O type']['title'], 'O')
                else:
                    tempDict['O type'] = 'No prediction could be made for O types for this genome.'

                if topMatches[genome_name]['H type'] != 'NM':
                    tempDict['H type'] = searchType(topMatches[genome_name]['H type']['title'], 'H')
                else:
                    tempDict['H type'] = 'No prediction could be made for H types for this genome (non-motile).'

                resultDict[genome_name] = tempDict

    return resultDict


def toCSV(data, verbose):
    """
    Writing final results in a CSV file.

    :param data: Top matches dictionary with the final results.
    :param verbose: Boolean stating whether the user wants full information or not.
    """

    logging.info('Writing CSV file Serotyper_Results.csv. You can find it in the temp/Results/ folder.')
    resultDict = toSimpleDict(data, verbose)
    header = ['Genome', 'O Type', 'H Type']

    with open(SCRIPT_DIRECTORY + '../../temp/Results/Serotyper_Results.csv', 'wb') as csvfile:
        csvwriter = csv.DictWriter(csvfile, header)
        csvwriter.writeheader()

        for genome_name in resultDict.keys():
            row = {'Genome': genome_name, 'H Type': resultDict[genome_name]['H type'], 'O Type': resultDict[genome_name]['O type']}
            csvwriter.writerow(row)


def toGalaxyCSV(data, verbose, output_file):
    """
    Writing final results in a CSV file for Galaxy Project tool only.

    :param data: Top matches dictionary with the final results.
    :param verbose: Boolean stating whether the user wants full information or not.
    :param output_file: Location of the file containing the results.
    """

    resultDict = toSimpleDict(data, verbose)
    header = ['Genome', 'O Type', 'H Type']

    with open(output_file.name, 'wb') as csvfile:
        csvwriter = csv.DictWriter(csvfile, header, delimiter='\t')
        csvwriter.writeheader()

        for genome_name in resultDict.keys():
            row = {'Genome': genome_name, 'H Type': resultDict[genome_name]['H type'], 'O Type': resultDict[genome_name]['O type']}
            csvwriter.writerow(row)


