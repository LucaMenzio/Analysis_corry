from modules import *

import ROOT
import os
import sys

if len(sys.argv) < 4:
    print(f"\n\033[91m Too few arguments privded, usage of this script is python3 position_extraction.py tracksFilename zDUT SHIFT\n \033[0m")
PATH_TO_CORRY = "/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan"

tracksFilename = str(sys.argv[1])
zDUT = float(sys.argv[2])
SHIFT = int(sys.argv[3])

outputFilename = tracksFilename.replace("_noRoi.root",".csv").replace("../","data/")

#implicit multithreading
ROOT.EnableImplicitMT(8)    
ROOT.EnableThreadSafety()

#Tracks stuff
#loading appropriate library                                                                 
ROOT.gInterpreter.AddIncludePath(PATH_TO_CORRY+'/objects')
ROOT.gSystem.AddDynamicPath(PATH_TO_CORRY+'/lib')
ROOT.gSystem.Load('libCorryvreckanObjects.so')

TrackClass = ROOT.corryvreckan.Track

trk = ROOT.std.vector(TrackClass)()
if __name__ == "__main__":
    Tf = ROOT.TFile.Open(tracksFilename)
    tree = Tf.Get('Track')
    print(f"\n\033[91mStarting to extract tracks hit positions for file {tracksFilename} at z={zDUT}\n\033[0m")
    outfileHeader = "EventN,x,y,chi2"
    nEvents = tree.GetEntriesFast()
    with open(outputFilename,mode='w') as outFile:
        outFile.write(outfileHeader+"\n")
        for i, entry in enumerate(tree):
            if(i % 10000 == 0 and i != 0):
                print(f"{i/nEvents*100:.2f} % events processed")
            current_track_vector = getattr(tree,'global')
            if(current_track_vector.size() == 1):
                intercept = current_track_vector[0].getIntercept(zDUT)
                x, y = intercept.X(), intercept.Y()
                chi2 = current_track_vector[0].getChi2()
                outFile.write(f"{int(i)},{x:.5f},{y:.5f},{chi2:.5f}\n")
