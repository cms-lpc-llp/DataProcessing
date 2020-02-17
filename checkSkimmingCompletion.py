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
printRecoveryJson = False

outputFile = open('SkimmingStatus.txt', 'w')

workflowList = OrderedDict()
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_64c06b80f784b46a78a6f90e57854509_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016B-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016B-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_a7ce4a0b0af1ad3286886a04fca80093_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016B-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016C-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_0bbd0f92e1d1fea5fc3cf45968132dd1_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016C-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016D-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_f17992072227a148dcb454c3f2f34d11_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016D-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_278617ead9dd4d4817f81501e8211afb_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016E-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016F-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_53955853b232b3f4c5b5dfb96d133f9a_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016F-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_9e27ae4c5a77c82bf18e1a004a4224f6_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016G-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleElectron_Run2016H-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_99aec811b7aeed82269fed6f717028df_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2016H-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_5e92db095465b7a06c278d91ce3adeb3_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016B-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016B-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_529bedc1bb5643f4d396e6d18180dcc8_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016B-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016C-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_02f42f85ab6109e8288ae812ba43f875_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016C-v2']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016D-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_1c2086fe537d1b1776cc676798dd9be7_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016D-v2']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_dbb21208b77584bf8ecb69672fb36ff4_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016E-v2']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016F-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_1ee9f0cf4e644ceda6afb688114599ae_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016F-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016G-v1_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_6f3704e67c3ef28ebfa246dbb9a22d28_v5','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016G-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/prod_Run2_CSCDTRechitSkimming_V2_2016_v2_SingleMuon_Run2016H-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2016/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2016_v2_adb663b282c0a2180c3f4164540fac57_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2016H-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_95c71d0f329ad0bb1939cab8bf6075a8_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017A-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_723dcc1d1b17ede5c0b75cd099dfc315_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017B-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_c35a5779275aa1ada0611c28ba083520_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017C-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_757f4bf517c19fce0aa2f5e5ca9e1f3f_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017D-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017E-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_5ee49aad39e9f762f508891f50123b36_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017E-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleElectron_Run2017F-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_29ec7c60678d4883836d456cf7a5a75b_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleElectron/Run2017F-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_e09a76c3e07daaf4aaf9d08291460a4a_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017A-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_32210dbf4dd3b163bc84c1ddc56b5718_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017B-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_95912d08dccd7e9ab3abcf1486d83744_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017C-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_33cd049e4090e03f65317ee87e325b2b_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017D-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017E-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_8a24e9976d9f196e5a04a58623056c5a_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017E-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017F-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_07c4b6c1af86e474d337910b0b484eda_v3','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017F-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_624b51a647a4df8d80556318fd56feb9_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017G-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/prod_Run2_CSCDTRechitSkimming_V2_2017_v1_SingleMuon_Run2017H-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2017/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2017_v1_bb1a93534d6d45138cf7e56c330ca061_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2017H-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_5bb5f5b463f74c4d3cb2a36e7c5edd4e_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018A-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_3e23b1a6b03deaf338ed438a0fef3a21_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018B-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_EGamma_Run2018C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_e13af271175f827993dcb71387f0facc_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018C-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018A-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_10d555c0e3d3c510f93c6817a87388d9_v4','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018A-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_01f3537a0a95ab3994671862498bd042_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018B-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_SingleMuon_Run2018C-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/ABC/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018ABC_v2_65398c98a0b9af91fbc856efb202b4f3_v2','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018C-v1']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_SingleMuon_Run2018D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_d8b7a34d749ee892a9c20cabd80d4dfd_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/SingleMuon/Run2018D-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_EGamma_Run2018D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_aab8d9933c367e8f840ae9a23be62b9d_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018D-v1']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_EGamma_Run2018E-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/Skimming/CSCDTRechitSkimming/V2/2018/D/crab_prod/crab_prod_Run2_CSCDTRechitSkimming_V2_2018D_v1_714beddc5fcd9aa5b2a23bcfba3720ce_v1','/eos/cms/store/group/phys_susy/razor/run2/RAWSkim/V2/2016/EGamma/Run2018E-v1']



RawSkimFile = open("RAWSKIM.txt","r")

for file in workflowList.keys():
    #print file
    inputDataset = ""
    outputDirectory = ""
    outputPD = ""
    outputDatasetTag = ""
    crabDir = ""

    tempfile = open(file,"r")
    for line in tempfile:
        if "config.Data.inputDataset" in line:
            #print line
            inputDataset = line.strip("config.Data.inputDataset = \"").replace('\"','').rstrip()
        if "config.Data.outLFNDirBase" in line:
            #print line
            outputDirectory = line.strip("config.Data.outLFNDirBase =").replace("\'","").rstrip()
        if "config.Data.outputDatasetTag" in line:
            outputDatasetTag = line.strip("config.Data.outputDatasetTag =").replace('\"',"").rstrip()
            
    outputPD = inputDataset.split("/")[1]
    outputFullPath = outputDirectory+outputPD+"/"+outputDatasetTag    
    #print inputDataset
    #print outputDatasetTag
    #print outputDirectory
    #print outputPD
    
    TotalNumberOfJobs = len(glob.glob(workflowList[file][0] + "/local/run_and_lumis/*.json"))    
    if (TotalNumberOfJobs == 0):
        print "Error: " + workflowList[file][0] + "\n"

    #print outputFullPath
    JobComplete = OrderedDict()
    if not TotalNumberOfJobs==999999:
        for i in range(1,TotalNumberOfJobs,1):
            JobComplete[i] = False
    IncompleteLumiFileList = []
    tmpCount = 0
    RawSkimFile.seek(0)

    for line in RawSkimFile:
        if (outputFullPath in line) and (".root" in line):
            #print line
            tmpCount = tmpCount + 1

        if not TotalNumberOfJobs==999999:
            for i in range(1,TotalNumberOfJobs,1):
                if (outputFullPath in line) and ("_"+str(i)+".root" in line):
                    JobComplete[i] = True

    IncompleteJobs = ""
    IncompleteLumiMaskCommand = "mergeJSON.py "
    if not TotalNumberOfJobs==999999:
        for i in JobComplete.keys():
            if JobComplete[i] == False :
                IncompleteJobs = IncompleteJobs + str(i) + ","
                IncompleteLumiMaskCommand = IncompleteLumiMaskCommand + " " + workflowList[file][0] + "/local/run_and_lumis/job_lumis_" + str(i) + ".json"

    completionRatio = 100*(float(tmpCount) / TotalNumberOfJobs)
    #print inputDataset + " : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = " + "%.1f"%completionRatio + "%"

    print '{0:<40} {1:>20} {2:>10}'.format(inputDataset," : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = ", "%.1f"%completionRatio + "%")
    print IncompleteJobs

    outputFile.write('{0:<40} {1:>20} {2:>10}'.format(inputDataset," : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = ", "%.1f"%completionRatio + "%"))
    outputFile.write("\n")

    #get incomplete jobs lumi-mask, and produce a combined lumi-mask for recovery task
    if printRecoveryJson:
        outputFile.write(IncompleteLumiMaskCommand)
    outputFile.write("\n")


    #cleanup
    crabProjectLocalDir = workflowList[file][0] + "/local/"
    print "CrabDir: " + inputDataset + " : " + crabProjectLocalDir+"batch/"




    #Write condor submit script for local resubmission jobs
    if produceLocalResubmissionJobs == True:

        crabProjectLocalDir = workflowList[file][0] + "/local/"
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/out/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/err/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/log/")
        os.system("chmod +x " + crabProjectLocalDir + "/run_job.sh")
    
 

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
        OSRequirement = "requirements = (OpSysAndVer =?= \"SLCern6\")"
        condorJDLFile.write(OSRequirement+"\n")
        condorJDLFile.write("RequestCpus = 1 \n")
        condorJDLFile.write("RequestMemory = 2000 \n")
        QueueType = "workday"
        condorJDLFile.write("+JobFlavour = \"" + QueueType + "\"")
 
    
           
        condorJDLFileTemplate = """
# Jobs selection
Queue I from (
"""
                
        condorJDLFile.write(condorJDLFileTemplate)
        for i in JobComplete.keys():
            if JobComplete[i] == False :
                condorJDLFile.write(str(i)+"\n")

        condorJDLFile.write(")\n")
        condorJDLFile.close()

        if not os.path.exists(crabProjectLocalDir+"/run_job.original.sh") :
            os.system("cp " + crabProjectLocalDir+"/run_job.sh " + crabProjectLocalDir+"/run_job.original.sh ")
            print "run_job.original.sh does not exist. copy it from run_job.sh"
        runScript = open(crabProjectLocalDir+"/run_job.sh","w+")
        runScript.write("#!/bin/bash \n\n")
        runScript.write("export X509_USER_PROXY=/afs/cern.ch/user/s/sixie/my_proxy\n")
        runScript.close()
        os.system("cat " + crabProjectLocalDir+"/run_job.original.sh >> " +  crabProjectLocalDir+"/run_job.sh \n")
        runScript = open(crabProjectLocalDir+"/run_job.sh","a")
        runScript.write("\n")
        #runScript.write("gfal-copy -f " + outputFilename + " gsiftp://transfer.ultralight.org/" + remoteOutputDir + "/" + outputFilename.strip(".root") + "_${1}.root\n")
        runScript.write("mkdir -p " + workflowList[file][1] + "\n")
        runScript.write("cp -v EXOLLLPCSCDTDigiCount.root " + workflowList[file][1] + "/EXOLLLPCSCDTDigiCount_${1}.root\n")

        runScript.close()


