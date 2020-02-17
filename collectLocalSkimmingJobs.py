#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import os.path
from collections import OrderedDict

#if (len(sys.argv) -1 < 1):
#    print "Error. Not enough arguments provided.\n"
#    print "Usage: python generateCrabLocalProjects [OSVersion] [DatasetListFile] \n"
#    exit()

#crabProjectLocalDir = sys.argv[1]
#outputLogDir = crabProjectLocalDir + "/batch/out/"
#NumberOfJobs = sum(1 for line in open(crabProjectLocalDir+"/InputArgs.txt"))
#print "Number of Jobs : " + str(NumberOfJobs)

produceLocalResubmissionJobs = True

outputFile = open('LocalSkimmingJobsStatus.txt', 'w')
cleanupFile = open('CleanupFiles.txt', 'w')

workflowList = OrderedDict()
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_64c06b80f784b46a78a6f90e57854509_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016B-v1_v2_v1/191218_172310/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016B-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_a7ce4a0b0af1ad3286886a04fca80093_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016B-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016B-v2_v2_v2/200120_042025/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016C-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_0bbd0f92e1d1fea5fc3cf45968132dd1_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016C-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016C-v2_v2_v1/191218_172355/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016D-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_f17992072227a148dcb454c3f2f34d11_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016D-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016D-v2_v2_v1/191218_172413/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingeElectron_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_278617ead9dd4d4817f81501e8211afb_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016E-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016E-v2_v2_v1/191218_172451/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016F-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_53955853b232b3f4c5b5dfb96d133f9a_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016F-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016F-v1_v2_v1/191218_172512/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_9e27ae4c5a77c82bf18e1a004a4224f6_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016G-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016G-v1_v2_v1/191218_172533/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016H-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_99aec811b7aeed82269fed6f717028df_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016H-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2016_Run2016H-v1_v2_v1/191218_172555/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_5e92db095465b7a06c278d91ce3adeb3_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016B-v1_v2_v1/191218_172614/0000/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016B-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_529bedc1bb5643f4d396e6d18180dcc8_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016B-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016B-v2_v2_v1/191218_172719/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016C-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_02f42f85ab6109e8288ae812ba43f875_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016C-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016C-v2_v2_v1/191218_172741/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016D-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_1c2086fe537d1b1776cc676798dd9be7_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016D-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016D-v2_v2_v2/191218_181212/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_dbb21208b77584bf8ecb69672fb36ff4_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016E-v2','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016E-v2_v2_v1/191218_172817/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016F-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_1ee9f0cf4e644ceda6afb688114599ae_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016F-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016F-v1_v2_v2/191230_152832/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016G-v1_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_6f3704e67c3ef28ebfa246dbb9a22d28_v5','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016G-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016G-v1_v2_v5/200108_215318/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016H-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_adb663b282c0a2180c3f4164540fac57_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016H-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2016/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2016_Run2016H-v1_v2_v2/200107_222402/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_95c71d0f329ad0bb1939cab8bf6075a8_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017A-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017A-v1_v1_v1/191218_173502/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_723dcc1d1b17ede5c0b75cd099dfc315_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017B-v1_v1_v1/191218_173522/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_c35a5779275aa1ada0611c28ba083520_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017C-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017C-v1_v1_v1/191218_173545/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_757f4bf517c19fce0aa2f5e5ca9e1f3f_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017D-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017D-v1_v1_v1/191218_173606/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017E-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_5ee49aad39e9f762f508891f50123b36_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017E-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017E-v1_v1_v2/200106_212003/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017F-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_29ec7c60678d4883836d456cf7a5a75b_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017F-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleElectron/Run2_CSCDTRechitSkimming_V2_2017_Run2017F-v1_v1_v2/200120_042258/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_e09a76c3e07daaf4aaf9d08291460a4a_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017A-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017A-v1_v1_v1/191218_173711/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_32210dbf4dd3b163bc84c1ddc56b5718_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017B-v1_v1_v1/191218_173731/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_95912d08dccd7e9ab3abcf1486d83744_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017C-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017C-v1_v1_v1/191218_173754/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_33cd049e4090e03f65317ee87e325b2b_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017D-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017D-v1_v1_v1/191218_173815/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017E-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_8a24e9976d9f196e5a04a58623056c5a_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017E-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017E-v1_v1_v2/191230_152415/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017F-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_07c4b6c1af86e474d337910b0b484eda_v3','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017F-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017F-v1_v1_v3/200107_213055/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_624b51a647a4df8d80556318fd56feb9_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017G-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017G-v1_v1_v1/191218_173919/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017H-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_bb1a93534d6d45138cf7e56c330ca061_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017H-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2017/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2017_Run2017H-v1_v1_v1/191218_174018/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_5bb5f5b463f74c4d3cb2a36e7c5edd4e_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018A-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/EGamma/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018A-v1_v2_v1/191218_181537/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_3e23b1a6b03deaf338ed438a0fef3a21_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/EGamma/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018B-v1_v2_v1/191218_181601/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_e13af271175f827993dcb71387f0facc_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018C-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/EGamma/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018C-v1_v2_v1/191218_181624/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018A-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_10d555c0e3d3c510f93c6817a87388d9_v4','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018A-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018A-v1_v2_v4/200110_153238/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_01f3537a0a95ab3994671862498bd042_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018B-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018B-v1_v2_v1/191218_181712/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018C-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_65398c98a0b9af91fbc856efb202b4f3_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018C-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018ABC/v2/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2018ABC_Run2018C-v1_v2_v4/200110_153316/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_SingleMuon_Run2018D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_d8b7a34d749ee892a9c20cabd80d4dfd_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018D-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018D/v1/sixie/SingleMuon/Run2_CSCDTRechitSkimming_V2_2018D_Run2018D-v1_v1_v1/191218_183847/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_EGamma_Run2018D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_aab8d9933c367e8f840ae9a23be62b9d_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018D-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018D/v1/sixie/EGamma/Run2_CSCDTRechitSkimming_V2_2018D_Run2018D-v1_v1_v1/191218_183801/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_EGamma_Run2018E-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D _v1_714beddc5fcd9aa5b2a23bcfba3720ce_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018E-v1','/store/group/phys_exotica/delayedjets/RAWSKIM/V2/2018D/v1/sixie/EGamma/Run2_CSCDTRechitSkimming_V2_2018D_Run2018E-v1_v1_v1/191218_183824/']

RawSkimFile = open("RAWSKIM.txt","r")


for file in workflowList.keys():
    print file

    #Find the Number of Total Local Jobs
    NumberOfJobs = 0

    if os.path.exists(workflowList[file][0]+"/local/batch/task.jdl"):
        JDLFile = open(workflowList[file][0]+"/local/batch/task.jdl","r")
        tmplines = JDLFile.readlines()
        foundStart = False
        foundEnd = False
        for line in tmplines:
            if line.strip() == ")":
                foundEnd = True            
            if (foundStart == True and foundEnd == False):
                NumberOfJobs = NumberOfJobs + 1            
            if "Queue I from (" in line:
                foundStart = True
            
    clusterNumber = -999
    clusterNumberList = []
    printedWarning = False
    for tmp in glob.glob(workflowList[file][0]+"/local/batch/out/*.out"):
        tmpClusterNumber = tmp.split("prod")[2].split(".")[1]
        if (tmpClusterNumber not in clusterNumberList):
            clusterNumberList.append(tmpClusterNumber)
        if (clusterNumber == -999):
            clusterNumber = tmpClusterNumber
        else:
            if (not clusterNumber == tmpClusterNumber):
                if (printedWarning == False):
                    print "Warning: project has multiple condor submissions"
                    printedWarning = True
    #print clusterNumber 
    print clusterNumberList


    #Loop over all local jobs and find output log file
    if (clusterNumber == -999) :
        print "No jobs were submitted"
    else :
        for i in range(0,NumberOfJobs,1):
            exitCode = "-999"
            joboutputfile = ""

            #check all the condor submissions associated with this task
            for c in clusterNumberList:
                logfileName = workflowList[file][0]+"/local/batch/out/job." + str(c) + "." + str(i) + ".out"
                #print "Job : " + str(i)
                #print "log file: " + logfileName
                if (os.path.exists(logfileName)):
                    outputLogFile = open(logfileName)
                    #print "logfile: " + logfileName
            
                    for l in outputLogFile.readlines():
                        
                        #print "readline " + l 

                        if ("== The job had an exit code of" in l) :
                            exitCode = l.split("== The job had an exit code of")[1].strip()
                            #print "Exit Code = " + str(exitCode)
                        
                        if ("EXOLLLPCSCDTDigiCount.root" in l and "->" in l):
                            #print "found outputfile: " + l
                            joboutputfile = l.split("->")[1].replace('`','').replace("\'","").strip()
                            #print "outputfile: " + joboutputfile
             
                    outputLogFile.close()
                    
                #if one of the condor submissions had a successful version of this job, then don't need to check the others
                if (exitCode == "0"):
                    break
                

            if (exitCode == "0"):       

                crabTaskJobNumber = int(joboutputfile.split("EXOLLLPCSCDTDigiCount_")[1].replace(".root","").strip())
                remoteOutputDirectoryPart2 = "0000"
                if (crabTaskJobNumber >= 1000 and crabTaskJobNumber < 2000):
                    remoteOutputDirectoryPart2 = "0001"
                if (crabTaskJobNumber >= 2000 and crabTaskJobNumber < 3000):
                    remoteOutputDirectoryPart2 = "0002"
                if (crabTaskJobNumber >= 3000 and crabTaskJobNumber < 4000):
                    remoteOutputDirectoryPart2 = "0003"
                if (crabTaskJobNumber >= 4000 and crabTaskJobNumber < 5000):
                    remoteOutputDirectoryPart2 = "0004"
                if (crabTaskJobNumber >= 5000 and crabTaskJobNumber < 6000):
                    remoteOutputDirectoryPart2 = "0005"
                if (crabTaskJobNumber >= 6000 and crabTaskJobNumber < 7000):
                    remoteOutputDirectoryPart2 = "0006"
                if (crabTaskJobNumber >= 7000 and crabTaskJobNumber < 8000):
                    remoteOutputDirectoryPart2 = "0007"
                if (crabTaskJobNumber >= 8000 and crabTaskJobNumber < 9000):
                    remoteOutputDirectoryPart2 = "0008"
                if (crabTaskJobNumber >= 9000 and crabTaskJobNumber < 10000):
                    remoteOutputDirectoryPart2 = "0009"
                remoteOutputDirectory = workflowList[file][2] + remoteOutputDirectoryPart2 + "/"
                remoteOutputfile = remoteOutputDirectory + "EXOLLLPCSCDTDigiCount_" + joboutputfile.split("EXOLLLPCSCDTDigiCount_")[1]

                #print "Job Completed Successfully"
                #print "outputfile to copy: " + joboutputfile
                #print "remoteoutputfile = " + remoteOutputfile

                #check if the file exists in local stage out area
                if (os.path.exists(joboutputfile)):                    
             
                    #check if the file is already at Caltech T2
                    RawSkimFile.seek(0)
                    outputAlreadyAtRemoteSite = False
                    for tmpline in RawSkimFile:
                        if ( remoteOutputfile.strip() in tmpline) :
                            #print "file " + remoteOutputfile + " already at T2"
                            outputAlreadyAtRemoteSite = True
                            break
                       
                    #print joboutputfile+ " : " + str(outputAlreadyAtRemoteSite) 

                    if (outputAlreadyAtRemoteSite == False) :
                        outputFile.write("gfal-copy -f -t99999 -T7200 " + joboutputfile + " gsiftp://transfer.ultralight.org/" + remoteOutputfile + "\n")

                #else:
                #    print "output file " + joboutputfile + " not found, check log " + logfileName + "\n"

            else :
                #print "Exit Code: " + exitCode + " : " + logfileName
                if (os.path.exists(joboutputfile)):
                    cleanupFile.write(joboutputfile+"\n")

