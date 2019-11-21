#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys


if (len(sys.argv) -1 < 1):
    print "Error. Not enough arguments provided.\n"
    print "Usage: python generateCrabLocalProjects [OSVersion] [DatasetListFile] \n"
    exit()

crabProjectLocalDir = sys.argv[1]
outputLogDir = crabProjectLocalDir + "/batch/out/"
NumberOfJobs = sum(1 for line in open(crabProjectLocalDir+"/InputArgs.txt"))
print "Number of Jobs : " + str(NumberOfJobs)


for job in range(1,NumberOfJobs+1):
    isSuccessfulJob = False
    fileList = glob.glob(outputLogDir+"/batch/out/job.*."+str(job)+".out")
    for filename in fileList:
        file = open(filename,"r")
        for line in file:
            if "== The job had an exit code of 0" in line:
                isSuccessfulJob = True
                break

    if (not isSuccessfulJob): 
        print "Job " + str(job) + " failed\n"

