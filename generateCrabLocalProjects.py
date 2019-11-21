#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys


if (len(sys.argv) -1 < 2):
    print "Error. Not enough arguments provided.\n"
    print "Usage: python generateCrabLocalProjects [OSVersion] [DatasetListFile] \n"
    exit()





lumiPerJob = 30
versionNumber = 1
OSVersion = sys.argv[1]
DatasetListFilename = sys.argv[2]
queueType = "longlunch"

crabSetupScript = "/cvmfs/cms.cern.ch/crab3/crab_slc6.sh"
if (OSVersion == "SLC7"):
    crabSetupScript = "/cvmfs/cms.cern.ch/crab3/crab.sh"


tempfile = open(DatasetListFilename,"r")
templines = tempfile.readlines()
for line in templines:
    datasetName = line.strip()
    tmp = datasetName[1:]
    taskDir = tmp.replace("/","_") 
    
    crab_config_file = open(OSVersion+"/tasks/crab_prod_Run2_EXOLLPCSCDTDigiCountRAWSkim_" + taskDir + ".py","w+")

    temp = """
from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
"""
    crab_config_file.write(temp)

    crab_config_file.write("config.General.requestName = \"prod_Run2_EXOLLPCSCDTDigiCountRAWSkim_" + taskDir + "_V"+str(versionNumber)+"\"\n")
    temp = """
config.General.workArea = "crab_prod"

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "skim.py"
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.ignoreLocality = True
"""
    crab_config_file.write(temp)
  
    crab_config_file.write("config.Data.inputDataset = \""+ datasetName + "\"\n")
    crab_config_file.write("config.Data.splitting = \"LumiBased\"\n")
    crab_config_file.write("config.Data.unitsPerJob = " + str(lumiPerJob)+"\n")

    crab_config_file.write(temp)
    crab_config_file.write("config.Data.outputDatasetTag = \"Run2_EXOLLPCSCDTDigiCountRAWSkim_"+taskDir+"\"")
    temp = """
config.Data.publication    = False

config.section_("Site")
config.Site.whitelist = ["T2_*"]
config.Site.storageSite = "T2_US_Caltech"
"""
    crab_config_file.write(temp)
    crab_config_file.write("config.Data.outLFNDirBase = \'/store/group/phys_exotica/delayedjets/RAWSKIM/V" + str(versionNumber) + "/sixie/\'\n")


    print datasetName + " " + taskDir
    crab_config_file.close()

    
    command = "cd "+OSVersion+"/CMSSW_10_5_0/; eval `scramv1 runtime -sh`; cd -; cd " + OSVersion + "/tasks; source " + crabSetupScript + "; export X509_USER_PROXY=/eos/home-s/sixie/my_proxy; crab submit -c crab_prod_Run2_EXOLLPCSCDTDigiCountRAWSkim_" + taskDir + ".py --dryrun; "
    print command
    os.system(command)
 
    command = "export X509_USER_PROXY=/eos/home-s/sixie/my_proxy; source " + crabSetupScript + "; crab preparelocal -d " + OSVersion + "/tasks/crab_prod/crab_prod_Run2_EXOLLPCSCDTDigiCountRAWSkim_" + taskDir + "_V"+str(versionNumber)
    print command
    os.system(command)

    command = "python prepareCrabLocalProject.py " + OSVersion + "/tasks/crab_prod/crab_prod_Run2_EXOLLPCSCDTDigiCountRAWSkim_" + taskDir + "_V"+str(versionNumber) + "/local/  /store/group/phys_exotica/delayedjets/RAWSKIM/V" + str(versionNumber) + "/sixie/" +taskDir+"/ "  + OSVersion + " " + queueType + " "
    print command
    os.system(command)


 
