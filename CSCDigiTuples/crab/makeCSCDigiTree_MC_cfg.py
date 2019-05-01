import FWCore.ParameterSet.Config as cms
import subprocess
#process = cms.Process("TEST")

#CHECK ERA, GLOBALTAG, GEOMETRY

from Configuration.StandardSequences.Eras import eras
process = cms.Process("TEST")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.Skims_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PAT_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")

from Configuration.AlCa.GlobalTag import GlobalTag

#different between reco - mc
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')


#
# CORRECT LUMI SECTIONS
#
#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#process.inputs = cms.PSet (
#    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#)
#JSONfile = 'test/golden2018.json'
#myList = LumiList.LumiList (filename = JSONfile).getCMSSWString().split(',')
#process.inputs.lumisToProcess.extend(myList)


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# example samples:
#   singlemu: '/store/data/Run2018A/SingleMuon/RAW-RECO/ZMu-PromptReco-v3/000/316/995/00000/FAAE6734-BA66-E811-8D2D-02163E019EBA.root',
#
#            '/store/data/Run2017D/SingleMuon/RAW/v1/000/302/031/00000/005D3323-8A8D-E711-B3C9-02163E01A517.root' //2017
#
#    jpsi: '/store/data/Run2018C/Charmonium/RAW/v1/000/320/065/00000/FE58EEB1-178E-E811-97C5-FA163E5ED053.root',
#
#    zerobias: '/store/data/Run2018D/ZeroBias7/RAW-RECO/LogError-PromptReco-v2/000/323/399/00000/FC46AD98-6140-1C49-BB39-7B1293D338A0.root'
#

#dataset = '/store/data/Run2018C/Charmonium/RAW/v1/000/320/065/00000/FE58EEB1-178E-E811-97C5-FA163E5ED053.root'
#dataset = 'file:/uscms/home/wnash/eos/Charmonium/charmonium2018C/test/RAW/FE58EEB1-178E-E811-97C5-FA163E5ED053.root'
#dataset = '/store/data/Run2018C/Charmonium/RAW/v1/000/319/756/00000/50DA85EC-4D8A-E811-AB28-FA163E56AF73.root' #20182nd
#dataset = '/store/data/Run2018B/Charmonium/RAW/v1/000/317/089/00000/CCB70690-4C63-E811-A9BD-FA163E851C2E.root' #20182nd
#dataset = '/store/data/Run2018A/Charmonium/RAW/v1/000/315/257/00000/1020D514-A349-E811-AA19-FA163EDB8EB7.root' #20182nd

#
# CHARMONIUM NMUON TEST
#
#dataset = '/store/data/Run2018C/Charmonium/RAW/v1/000/319/337/00000/1C4B30FD-6282-E811-96B1-02163E015211.root' #20182nd
#dataset = ' /store/data/Run2017F/Charmonium/RAW/v1/000/305/045/00000/F4100DFC-ACB0-E711-9C0C-02163E01A714.root' #tested against camerons oct 11


#
# SINGLE MUON NMUON TEST
#
#dataset = '/store/data/Run2017D/SingleMuon/RAW-RECO/ZMu-PromptReco-v1/000/302/031/00000/00060D74-2D8F-E711-9FEA-02163E011A48.root'
#dataset = '/store/relval/CMSSW_10_3_0_pre5/SingleMuon/RAW-RECO/ZMu-103X_dataRun2_PromptLike_v6_RelVal_sigMu2018D-v1/10000/8007A95E-58B7-1947-9987-E4F3310241F0.root'


#Oct 26 Last Test - Works Dec 19
#dataset = '/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/324/970/00000/FFCA0A00-2503-4242-8CAE-E1AC6E574063.root'

#Muon Gun Dec 24
#dataset = ' /store/group/phys_muon/abbiendi/MuonGun/MuonGun_PTOT-5-2500/crab_MuonGun_step3_asympt_FixedGT-TrkAli2017-v3/181215_114558/0000/step3_asympt_APE_FixedGT-TrackerAlignment-Upgrade2017-realistic-v3_99.root'
#self-made sample
#dataset = 'file:/uscms/home/wnash/eos/MuonGun/MuonGunPt1000.root'
dataset = 'file:/uscms/home/wnash/eos/MuonGun/MuonEGun-Jan2019/190117_224028/0000/GenRawRecoE0-4000_MuonGun_1.root'
#dataset = 'file:/uscms/home/wnash/eos/MuonGun/MuonEGun-Jan2019/190117_224028/0000/GenRawRecoE0-4000_MuonGun_69.root'

#dataset = 'file:step3_RAW2DIGI_L1Reco_RECO.root'

#Zero Bias Oct 26
#dataset = '/store/data/Run2018D/ZeroBias1/RAW/v1/000/324/725/00000/F54897BA-7012-8546-A9E0-48CE9AD9EBD7.root'
#selectionString = 'ZeroBias'

#all the selections that the extractor is capable of handling
selections = ['SingleMuon','Charmonium', 'MuonGun']
for selectionString in selections:
    if selectionString in dataset: #see if the selection is in the dataset to use as default
        break
    
print "Data Selection is :" + selectionString

#selectionString = dataset.split('/')[4]
#selectionString = 'SingleMuon'

#selectionString = 'jPsi'
#run = dataset.split('/')[3]
#run = 'RERERECO'
outfileName = 'CSCDigiTree_'+selectionString+'.root'
#outfileName = 'CSCDigiTree.root'

#isRawReco = 'RAW-RECO' in dataset
#isRawOnly = not isRawReco and 'RAW' in dataset
#if not isRawReco and not isRawOnly:
#    print "Error: Unknown dataset: %s"%dataset
#    exit()

process.source = cms.Source ("PoolSource",
        fileNames = cms.untracked.vstring(
dataset,
            )

)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet( limit = cms.untracked.int32(-1) ),
        FwkJob = cms.untracked.PSet( limit = cms.untracked.int32(0) )
    ),
    categories = cms.untracked.vstring('FwkJob'),
    destinations = cms.untracked.vstring('cout'),
     debugModules = cms.untracked.vstring('*'),
     threshold = cms.untracked.string('ERROR') 
)


process.MakeNtuple = cms.EDAnalyzer("CSCPatternExtractor",
        NtupleFileName       = cms.untracked.string(outfileName),
             muonCollection = cms.InputTag("muons"),
             
        trigBits                        = cms.InputTag('TriggerResults','','HLT'),
        trigPrescales                   = cms.InputTag('patTrigger'),      
             
        offlineBeamSpotTag = cms.InputTag("offlineBeamSpot"),
        csctfDigiTag = cms.InputTag("csctfDigis"),
        vertices = cms.InputTag('offlinePrimaryVertices'),
        emtfDigiTag = cms.InputTag("emtfStage2Digis"),
        wireDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCWireDigi"),
        stripDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCStripDigi"),
        alctDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCALCTDigi"),
        clctDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCCLCTDigi"),
        lctDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCCorrelatedLCTDigi"),
        compDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCComparatorDigi"),
        dduDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCDDUStatusDigi"),
        dmbDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCDMBStatusDigi"),
        tmbDigiTag = cms.InputTag("muonCSCDigis", "MuonCSCTMBStatusDigi"),
        pfCandTag = cms.InputTag("particleFlow"),
        rhDigiTag = cms.InputTag("csc2DRecHits"),
        genDigiTag = cms.InputTag("genParticles"),
        simDigiTag = cms.InputTag("g4SimHits:MuonCSCHits"),
        ebCaloDigiTag = cms.InputTag("g4SimHits:EcalHitsEB"),
        eeCaloDigiTag = cms.InputTag("g4SimHits:EcalHitsEE"),
        esCaloDigiTag = cms.InputTag("g4SimHits:EcalHitsES"),
        hCaloDigiTag = cms.InputTag("g4SimHits:HcalHits"),
        selection = cms.untracked.string(selectionString),
        MatchParameters = cms.PSet(
            DTsegments = cms.InputTag("dt4DSegments"),
            DTradius = cms.double(0.1),
            CSCsegments = cms.InputTag("cscSegments"),
            TightMatchDT = cms.bool(False),
            TightMatchCSC = cms.bool(True)
            ),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(True)
            )
        )

"""Customise digi/reco geometry to use unganged ME1/a channels"""
process.CSCGeometryESModule.useGangedStripsInME1a = False
process.idealForDigiCSCGeometry.useGangedStripsInME1a = False


process.load("L1Trigger.CSCTriggerPrimitives.cscTriggerPrimitiveDigis_cfi")
#nick change,temporarily removed
process.cscTriggerPrimitiveDigis.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
process.cscTriggerPrimitiveDigis.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"


process.load("L1TriggerConfig.L1CSCTPConfigProducers.L1CSCTriggerPrimitivesConfig_cff")
#test if something exists by doing python -i <filename>, then typing the object you're curious about

# >= CMSSW_10_3_+
process.l1csctpconf.alctParam.alctNplanesHitPretrig = 3
process.l1csctpconf.alctParam.alctNplanesHitAccelPretrig = 3
# < CMSSW_10_3
#process.l1csctpconf.alctParamMTCC2.alctNplanesHitPretrig = 3
#process.l1csctpconf.alctParamMTCC2.alctNplanesHitAccelPretrig = 3
process.l1csctpconf.clctParam.clctNplanesHitPretrig = 3
process.l1csctpconf.clctParam.clctHitPersist = 4

process.lctreader = cms.EDAnalyzer("CSCTriggerPrimitivesReader",
    debug = cms.untracked.bool(False),
    dataLctsIn = cms.bool(True),
    emulLctsIn = cms.bool(True),
    isMTCCData = cms.bool(False),
    printps = cms.bool(False),
    CSCLCTProducerData = cms.untracked.string("muonCSCDigis"),
    CSCLCTProducerEmul = cms.untracked.string("cscTriggerPrimitiveDigis"),
    CSCSimHitProducer = cms.InputTag("g4SimHits", "MuonCSCHits"),  # Full sim.
    CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
)

# TODO: RAW-RECO appears to crash unless full reconstruction is done. Find out why
#if isRawReco:
#    process.p = cms.Path(process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
#if isRawOnly:
#    process.p = cms.Path(process.RawToDigi * process.reconstruction * process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
#process.p = cms.Path(process.RawToDigi * process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
# process.p = cms.Path(process.RawToDigi * process.reconstruction * process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
#process.p = cms.Path(process.RawToDigi * process.reconstruction * process.MakeNtuple)

#TODO: verify you need all of this stuff
# TO USE WITH --- RECO ---
# nICK THINKS i CAN REMOVE ALMOST EVERYTHING BUT NTUPLIZER
process.p = cms.Path(process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
#process.p = cms.Path(process.cscTriggerPrimitiveDigis * process.MakeNtuple)
process.schedule = cms.Schedule(process.p)

#process.p = cms.Path(process.RawToDigi * process.L1Reco * process.reconstruction * process.gtDigis * process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscTriggerPrimitiveDigis * process.MakeNtuple)
# process.p = cms.Path(process.gtDigis *\
#                       process.muonCSCDigis *\
#                        process.csc2DRecHits *\
#                         process.cscSegments *\
#                          process.cscTriggerPrimitiveDigis *\
#                           process.MakeNtuple)
# 


# Questions to have answered:
#    - Does DQM data effect output at all (i.e. if I don't have it, will I get the same results as if I do?)
#


#TODO: check if this matches the reco-data (CSCDigiTree-fromRECO.root), if it does, keep RAW data configuration, if it doesn't, forget about RAW...
#Oct. 25 Over 20 events, this configuration has no events that get output to the CSCDigiTree
# # TO USE WITH --- RAW ---
# process.p = cms.Path(process.RawToDigi *\
#                      process.L1Reco *\
#                       process.reconstruction *\
#                       process.EIsequence *\
#                       process.goodVertices+process.trackingFailureFilter *\
#                       process.primaryVertexFilter *\
#                       process.CSCTightHaloFilter *\
#                       process.trkPOGFilters *\
#                       process.HcalStripHaloFilter *\
#                       ~process.logErrorTooManyClusters *\
#                       process.EcalDeadCellTriggerPrimitiveFilter *\
#                       process.ecalLaserCorrFilter *\
#                       process.globalSuperTightHalo2016Filter *\
#                       process.eeBadScFilter *\
#                       process.metFilters *\
#                       process.chargedHadronTrackResolutionFilter *\
#                       process.globalTightHalo2016Filter *\
#                       process.CSCTightHaloTrkMuUnvetoFilter *\
#                       process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter *\
#                       process.BadChargedCandidateSummer16Filter*\
#                       process.hcalLaserEventFilter *\
#                       process.BadPFMuonFilter *\
#                       process.ecalBadCalibFilter *\
#                       process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter*\
#                       ~process.toomanystripclus53X *\
#                       process.EcalDeadCellBoundaryEnergyFilter *\
#                       process.BadChargedCandidateFilter *\
#                       ~process.manystripclus53X *\
#                       process.BadPFMuonSummer16Filter *\
#                       process.muonBadTrackFilter *\
#                       process.CSCTightHalo2015Filter *\
#                       process.gtDigis *\
#                       process.muonCSCDigis *\
#                       process.csc2DRecHits *\
#                       process.cscSegments *\
#                       process.cscTriggerPrimitiveDigis *\
#                       process.MakeNtuple)

#WORK IN PROGRESS OCT. 29
# 
# # Path and EndPath definitions
# process.raw2digi_step = cms.Path(process.RawToDigi)
# process.L1Reco_step = cms.Path(process.L1Reco)
# process.reconstruction_step = cms.Path(process.reconstruction)
# process.eventinterpretaion_step = cms.Path(process.EIsequence)
# process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
# process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
# process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
# process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
# process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
# process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
# process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
# process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
# process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
# process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
# process.Flag_METFilters = cms.Path(process.metFilters)
# process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
# process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
# process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
# process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
# process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
# process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
# process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
# process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
# process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
# process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
# process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
# process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
# process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
# process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
# process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
# process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
# process.gtDigis_step = cms.Path(process.gtDigis)
# process.muonCSCDigis_step = cms.Path(process.muonCSCDigis)
# process.csc2DRecHits_step = cms.Path(process.csc2DRecHits)
# process.cscSegments_step = cms.Path(process.cscSegments)
# process.cscTriggerPrimitiveDigis_step = cms.Path(process.cscTriggerPrimitiveDigis)
# process.MakeNtuple_step = cms.EndPath(process.MakeNtuple)
# 
# # Schedule definition
# process.schedule = cms.Schedule(process.raw2digi_step,\
#                                 process.L1Reco_step,\
#                                 process.reconstruction_step,\
#                                 process.eventinterpretaion_step,\
#                                 process.Flag_HBHENoiseFilter,\
#                                 process.Flag_HBHENoiseIsoFilter,\
#                                 process.Flag_CSCTightHaloFilter,\
#                                 process.Flag_CSCTightHaloTrkMuUnvetoFilter,\
#                                 process.Flag_CSCTightHalo2015Filter,\
#                                 process.Flag_globalTightHalo2016Filter,\
#                                 process.Flag_globalSuperTightHalo2016Filter,\
#                                 process.Flag_HcalStripHaloFilter,\
#                                 process.Flag_hcalLaserEventFilter,\
#                                 process.Flag_EcalDeadCellTriggerPrimitiveFilter,\
#                                 process.Flag_EcalDeadCellBoundaryEnergyFilter,\
#                                 process.Flag_ecalBadCalibFilter,\
#                                 process.Flag_goodVertices,\
#                                 process.Flag_eeBadScFilter,\
#                                 process.Flag_ecalLaserCorrFilter,\
#                                 process.Flag_trkPOGFilters,\
#                                 process.Flag_chargedHadronTrackResolutionFilter,\
#                                 process.Flag_muonBadTrackFilter,\
#                                 process.Flag_BadChargedCandidateFilter,\
#                                 process.Flag_BadPFMuonFilter,\
#                                 process.Flag_BadChargedCandidateSummer16Filter,\
#                                 process.Flag_BadPFMuonSummer16Filter,\
#                                 process.Flag_trkPOG_manystripclus53X,\
#                                 process.Flag_trkPOG_toomanystripclus53X,\
#                                 process.Flag_trkPOG_logErrorTooManyClusters,\
#                                 process.Flag_METFilters,\
#                                 process.gtDigis_step,\
#                                 process.muonCSCDigis_step,\
#                                 process.csc2DRecHits_step,\
#                                 process.cscSegments_step,\
#                                 process.cscTriggerPrimitiveDigis_step,\
#                                 process.MakeNtuple_step
# )
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


#from Configuration.DataProcessing.RecoTLR import customisePostEra_Run2_2018 
#process = customisePostEra_Run2_2018(process)
#process.schedule = cms.Schedule(process.p)


process.options = cms.untracked.PSet(

)

#Setup FWK for multithreaded
#process.options.numberOfThreads=cms.untracked.uint32(8)
#process.options.numberOfStreams=cms.untracked.uint32(0)

