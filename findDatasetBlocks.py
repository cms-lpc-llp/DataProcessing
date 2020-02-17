#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import json


jobList = [762,772,928,967,1764]
fileListLocation = "/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_c35a5779275aa1ada0611c28ba083520_v1/local/files/"

fileList = []
for i in jobList:
    print "job "+str(i)
    f = open(fileListLocation+"job_input_file_list_"+str(i)+".txt", "r")
    line = f.readline()
    list = line.replace("[","").replace("]","").replace('"','').split(",")
    #print line.replace("[","").replace("]","").replace('"','').split(",")
    for a in list:
        fileList.append(a.strip())

#print fileList
print "Number of Files: " + str(len(fileList))


#Get the json file by running: dasgoclient -query="file dataset=/SingleMuon/Run2017G-v1/RAW" -json > Files_SingleMuon_Run2017G-v1_RAW.json
jsonFile = open("Files_SingleElectron_Run2017C-v1_RAW.json","r")
data = json.load(jsonFile)

#    #jstr = json.dumps(data, index=4)
#    #print jstr
#    #print data 

fileToBlockMap = {}

for p in data:
    #print p['file'][0]['name']
    #print p['file'][0]['block.name']
    fileToBlockMap[p['file'][0]['name']] = p['file'][0]['block.name']
    #print "\n"
    
BlockList = []

#Loop over fileList and find the blocks
for f in fileList:
    if f in fileToBlockMap.keys():
        if fileToBlockMap[f] not in BlockList:
            BlockList.append(fileToBlockMap[f])
    else:
        print "File "+f+" not found in json file"
for b in  BlockList:
    print b
print "Number of Blocks: " + str(len(BlockList))

