#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys

tempfile = open("Datasets.txt","r")
templines = tempfile.readlines()
for line in templines:
    datasetName = line.strip()
    tmp = datasetName[1:]
    outputfile = tmp.replace("/","_") + ".list"
    command = "dasgoclient -query=\"file dataset=" + datasetName + "\" > " + outputfile

    print command
    os.system(command)

