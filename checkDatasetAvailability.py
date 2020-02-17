#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import json

if (len(sys.argv) -1 < 1):
    print "Error. Not enough arguments provided.\n"
    print "Usage: python checkDatasetAvailability.py [DatasetListFile]  \n"
    exit()


datasetListFilename = sys.argv[1]

tempfile = open(datasetListFilename,"r")
templines = tempfile.readlines()
for line in templines:
    datasetName = line.strip()

    # datasetSize = 0
    # command = "dasgoclient -query=\"dataset dataset=" + datasetName + "\" -json > tmpOutput.json" 
    # #print command
    # os.system(command)
    # jsonFile = open("tmpOutput.json","r")
    # data = json.load(jsonFile)
    # for p in data[2]["dataset"]:    
    #     #print p
    #     datasetSize = p["size"] / (1024*1024*1024*1024.)
    # print datasetName + " : " + "{0:.2f}".format(datasetSize) + " TB"

    print datasetName

    command = "dasgoclient -query=\"site dataset=" + datasetName + "\" -json > tmpOutput.json"
    #print command
    os.system(command)

    jsonFile = open("tmpOutput.json","r")
    data = json.load(jsonFile)
    #jstr = json.dumps(data, index=4)
    #print jstr
    #print data 
    
    for p in data:
        if ("kind" in p["site"][0].keys() and p["site"][0]["kind"] == "Disk"):
            print p["site"][0]["name"] + " : " + p["site"][0]["replica_fraction"] 
        #if ("kind" in p["site"][0].keys() and p["site"][0]["kind"] == "MSS"):
        #    print p["site"][0]["name"] + " : " + p["site"][0]["replica_fraction"] 
    
    print "\n"


    

