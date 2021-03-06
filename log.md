[2016/09/12 - Camille La Rose]
- finished writing tests for getListGenomes and checkFiles methods
- added the EcOH.fasta DB
- wrote the method to generate the EcOH.fasta DB
- minor directory fixes

[2016/09/13 - Camille La Rose]
- wrote the methods runBlastQuery and parseResults
- started the method getGenomeName to identify the genomes in the GENOMES dictionary

[2016/09/14 - Camille La Rose]
- documentation adds + fixes
- adjusted the methods runBlastQuery and parseResults (lists to dictionaries)
- wrote the tests for initializeDB and getGenomeName

[2016/09/15 - Camille La Rose]
- finished writing tests for parseResults and  findPerfectMatches
- created  new module ecprediction.py for prediction methods

[2016/09/16 - Camille La Rose]
- created new module ecvalidatingfiles.py for validation methods
- fixed tests for parseResults and findPerfectMatches
- fixed methods parseResults and findPerfectMatches so that it returns the GENOME dict.
- added filterPredictions method

[2016/09/19 - Camille La Rose]
- created a new test module (ecprediction_tests) to separate the tests by module
- created new method findTopMatch
- finished the tests for findPerfectMatches and filterPredictions

[2016/09/20 - Camille La Rose]
- removed findPerfectMatches and its test method
- finished findTopMatch

[2016/09/21 - Camille La Rose]
- fixed findTopMatch and findTopMatches
- started tests for the above, as well as for searchType and getProductPercentage

[2016/09/22 - Camille La Rose]
- fixed filterPredictions to include NAs
- fixed test for filterPredictions
- still writing tests for findTopMatch, findTopMatches, searchType and getProductPercentage

[2016/09/23 - Camille La Rose]
- finished tests for findTopMatch, findTopMatches, searchType and getProductPercentage
- added documentation for the above methods
- added logging
- will add the following to the DB:
      H:
        fliC_54_AJ605766_H17
        fliC_50_AJ515904_H17
        fliC_888881_AVRH01000047_H52
        fliC_274_AY337470_H42
        fliC_311_AGSG01000116_H25
        fliC_111197_JH965342_H29
        fliC_286_AY337485_H29
        fliC_109_AM231154_H27
        fliC_2_AIEY01000041_H6
        fliC_84_AIHL01000060_H21
        fliC_82_AIFA01000047_H6
        fliC_285_AY337483_H26
        fliC_314_CP000247_H31
        fliC_92_JH954529_H16
        fliC_93_JH953794_H16
        fliC_300_AB128919_H16
        fliC_21_AB028474_H7
        fliC_95_JH694260_H7
        fliC_97_KB000721_H7
        fliC_99_KB007180_H7
        fliC_100_AOES01000098_H7
        fliC_108_KB006714_H7
        fliC_101_JH946604_H7
        fliC_105_AAJT02000052_H28
        fliC_83_AIFX01000055_H12
        fllA_1_AB269771_H55
        fllA_2_AB269770_H44
      O:
        wzx_36_DQ462205-FJ539194_O28ac/O42
        wzx_86_289152760_O83
        wzx_103_KB021482_O104
        wzx_105_AFPS01000083_O104
        wzx_106_AFOB02000091_O104
        wzx_126_DQ676933_O123
        wzx_153_AAJT02000037_O148
        wzx_168_EU296420_O164
        wzx_178_DQ008592_O174
        wzx_194_NC:013353_O103
        wzx_199_AKMA01000036_O157
        wzx_200_AKLI01000048_O157
        wzy_121_AB812063_O153/O178
        wzy_152_AIGX01000028_O45
        wzy_166_AJ426423_O6
        wzy_171_CP003034_O7
        wzy_193_JH964427_O157
        wzy_195_JH970567_O157
        wzy_199_AKLQ01000042_O157
        wzy_200_AKLV01000031_O157
        wzy_201_JH953200_O157
        wzy_202_EF027120_O103
        wzy_205_AP010958_O103
        wzy_206_EF027115_O103
        wzy_215_AY863412_O145
        wzx_406_56-54Cigleris_O128ab
        wzy_406_E68_O141ab
        wzy_407_RVC2907_O141ac
        wzx_211_AB812082_O186
        wzy_224_AB972416_O77
        wzt_3_AB010293_O9
        wzt_7_D43637_O9
        wzm_3_AB010293_O9
        wzm_8_D43637_O9
        wzx_400_KP835694_O125ab
        wzx_405_5564-64_O128ac
        wzy_400_KP835694_O125ab
        wzy_405_5564-64_O128ac

[2016/09/26 - Camille La Rose]
- created script to add the above sequences to the database (as well as format their titles)
- documentation

[2016/09/27 - Camille La Rose]
- added test script to compare with the Danish database

[2016/10/03 - Camille La Rose]
- added Flask API for python to send results to browser

[2016/10/04 - Camille La Rose]
- added formatresults.py module to return the results in an organized way (JSON and CSV file)
- fixed the documentation for all of the methods (explanation of parameters)

[2016/10/12 - Camille La Rose]
- added uploadfile.html
- added toHTML() method in fortmatresults.py
- added style.css
- fixed a few issues in runectyper.py

[2016/10/14 - Camille La Rose]
- finished writing uploadfile.html
- added download and return to main page buttons to results page
- added some styling to the upload and result pages
- added results.coffee for the download button
- added error handlers in runectyper.py
- added directories xml, database, js, css, coffee
- fixed a few methods in ecvalidatingfiles.py to work with the new directories
- added Cakefile to compile results.coffee

[2016/10/19 - Camille La Rose]
- changed the urls for Flask
- added curl_uploadFiles method in runectyper.py for curl commands

[2016/10/31 - Camille La Rose]
- fixed a few tests
    *create directories temp and xml when needed
    * initalize the database when needed

[2016/11/17 - Camille La Rose]
- fixed parseResults and runBlastQuery from ectyper to run only one .fasta file instead of multiple (efficiency)
- fixed the tests to accomodate the changes from parseResults and runBlastQuery
- changed the directories to add the VFs program
- added the VFs program (very similar to the ectyper, only shorter and faster)

[2016/11/22 - Camille La Rose]
- added the RGI tool
- added tests for VFs and RGI
- merged all shared methods into one single file (sharedmethods.py)

[2016/12/15 - Camille La Rose]
This is accumulative since Nov 22 2016. I didn't do this in 1 day.
- added interactive web-server app for Tools controller -> run_controller.py
    * added controller.html
    * added tools_formatresults.py
    * added JSON_results.html and table_results.html
    * added controller.css
    * added downloadresults.js
- added a few tests for controller methods -> test_controller
- merged the Galaxy tool with the master branch
- updated documentation

[2016/12/16 - Camille La Rose]
- curl command for run_controller.py
    * curl -i -X POST -F 'files[]=@path/to/file1.fasta' -F 'files[]=@path/to/file2.fasta' -F user_data='{command1: value1, command2: value2};type=application/json' URL
        ~ COMMANDS:
              serotype - choose from 0 or 1, 1 triggering the use of the serotype tool
              virulence_factors - choose from 0 or 1, 1 triggering the use of the virulence factors tool
              amr - choose from 0 or 1, 1 triggering the use of the amr tool
              percent_identity - choose from 0 to 100
              percent_length - choose from 0 to 100
              verbose - choose from 0 or 1, 1 triggering full information about the serotype
              all_vfs - choose from 0 or 1, 1 returning all found virulence factors
              minimum - choose from 0 to n, genomes threshold for virulence factors and amr
              perfect_amr - choose from 0 or 1, 1 filtering out strict amr results
              csv - choose from 0 or 1, 1 triggering the creation of a CSV file containing the results

- curl command for runectyper.py
    * curl -i -X POST -F 'files[]=@path/to/file1.fasta' -F 'files[]=@path/to/file2.fasta' -F user_data='{command1: value1, command2: value2};type=application/json' URL
        ~ COMMANDS:
              percent_identity - choose from 0 to 100
              percent_length - choose from 0 to 100
              verbose - choose from 0 or 1, 1 triggering full information about the serotype
              csv - choose from 0 or 1, 1 triggering the creation of a CSV file containing the results
