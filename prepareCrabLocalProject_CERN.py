#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys

if (len(sys.argv) -1 < 5):
    print "Error. Not enough arguments provided.\n"
    print "Usage: python prepareCrabLocalProject.py [crabProjectLocalDirectory] [remoteStageOutDirectory] [outputFilenameToBeCopied] [OSType = SLC6/SLC7] [queueType] \n"
    exit()

crabProjectLocalDir = sys.argv[1]
remoteOutputDir = sys.argv[2]
outputFilename = sys.argv[3]
OSType = sys.argv[4]
OSRequirement = "requirements = (OpSysAndVer =?= \"SLCern7\")"
if (OSType == "SLC6"):
    OSRequirement = "requirements = (OpSysAndVer =?= \"SLCern6\")"
QueueType = sys.argv[5]

print "Crab Project Local Directory: "+crabProjectLocalDir

os.system("mkdir -p " + crabProjectLocalDir + "/batch/")
os.system("mkdir -p " + crabProjectLocalDir + "/batch/out/")
os.system("mkdir -p " + crabProjectLocalDir + "/batch/err/")
os.system("mkdir -p " + crabProjectLocalDir + "/batch/log/")
os.system("chmod +x " + crabProjectLocalDir + "/run_job.sh")


NumberOfJobs = sum(1 for line in open(crabProjectLocalDir+"/InputArgs.txt"))
print "Number of Jobs : " + str(NumberOfJobs)


condorJDLFile = open(crabProjectLocalDir+"/batch/task.jdl","w+")

condorJDLFileTemplate = """
Universe  = vanilla
Executable = ../run_job.sh
Arguments = $(I)
Log = log/job.$(Cluster).$(Process).log
Output = out/job.$(Cluster).$(Process).out
Error = err/job.$(Cluster).$(Process).err
x509userproxy = $ENV(X509_USER_PROXY)
transfer_input_files = ../CMSRunAnalysis.sh, ../CMSRunAnalysis.tar.gz, ../InputArgs.txt, ../Job.submit, ../cmscp.py, ../gWMS-CMSRunAnalysis.sh, ../input_files.tar.gz, ../run_and_lumis.tar.gz, ../sandbox.tar.gz
should_transfer_files = YES
when_to_transfer_output = ON_EXIT

# Resources request
"""
condorJDLFile.write(condorJDLFileTemplate)
condorJDLFile.write(OSRequirement+"\n")
condorJDLFile.write("RequestCpus = 1 \n")
condorJDLFile.write("RequestMemory = 2000 \n")
condorJDLFile.write("+JobFlavour = \"" + QueueType + "\"")

condorJDLFileTemplate = """

# Jobs selection
Queue I from (
"""

condorJDLFile.write(condorJDLFileTemplate)
for i in range(1,NumberOfJobs+1):
    condorJDLFile.write(str(i)+"\n")
condorJDLFile.write(")\n")
condorJDLFile.close()

os.system("cp " + crabProjectLocalDir+"/run_job.sh " + crabProjectLocalDir+"/run_job.original.sh ")
runScript = open(crabProjectLocalDir+"/run_job.sh","w+")
runScript.write("#!/bin/bash \n\n")
runScript.write("export X509_USER_PROXY=/afs/cern.ch/user/s/sixie/my_proxy\n")
runScript.close()
os.system("cat " + crabProjectLocalDir+"/run_job.original.sh >> " +  crabProjectLocalDir+"/run_job.sh \n")
runScript = open(crabProjectLocalDir+"/run_job.sh","a")
runScript.write("\n")
runScript.write("gfal-copy -f " + outputFilename + " gsiftp://transfer.ultralight.org/" + remoteOutputDir + "/" + outputFilename.strip(".root") + "_${1}.root\n")
runScript.close()


