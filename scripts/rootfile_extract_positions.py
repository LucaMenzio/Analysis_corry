import ROOT
import os
import sys
from array import array

PATH_TO_CORRY = "/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan"

if len(sys.argv) < 4:
    print(f"\n\033[91m Too few arguments provided, usage of this script is python3 position_extraction.py tracksFilename zDUT SHIFT\n \033[0m")

#implicit multithreading
ROOT.EnableImplicitMT(8)    
ROOT.EnableThreadSafety()

tracksFilename = str(sys.argv[1])
zDUT = float(sys.argv[2])
SHIFT = int(sys.argv[3])

outputFilename = tracksFilename.replace("tracks","HP_tracks").replace("../output/","data/")
print(outputFilename)

#Tracks stuff
#loading appropriate library                                                                 
ROOT.gInterpreter.AddIncludePath(PATH_TO_CORRY+'/objects')
ROOT.gSystem.AddDynamicPath(PATH_TO_CORRY+'/lib')
ROOT.gSystem.Load('libCorryvreckanObjects.so')
TrackClass = ROOT.corryvreckan.Track
trk = ROOT.std.vector(TrackClass)()

#output file
nEvent_array, x_array, y_array, chi2_array = array('I',[0]), array('f',[0]), array('f',[0]), array('f',[0])
outFile = ROOT.TFile(outputFilename,"RECREATE")
outTree = ROOT.TTree("hitPositions","hitPositions")
outTree.Branch('nEvent',nEvent_array,'nEvent/I')
outTree.Branch('x',x_array,'x/F')
outTree.Branch('y',y_array,'y/F')
outTree.Branch('chi2',chi2_array,'chi2/F')

if __name__ == "__main__":
    Tf = ROOT.TFile.Open(tracksFilename)
    tree = Tf.Get('Track')
    nEvents = tree.GetEntriesFast()
    print(f"\n\033[91mStarting to extract tracks hit positions for file {tracksFilename} at z={zDUT}\n\033[0m")
    for i, entry in enumerate(tree):
        if(i % 10000 == 0 and i != 0):
            print(f"{i/nEvents*100:.2f} % events processed")
        current_track_vector = getattr(tree,'global')
        if(current_track_vector.size() == 1):
            intercept = current_track_vector[0].getIntercept(zDUT)
            x, y = intercept.X(), intercept.Y()
            chi2 = current_track_vector[0].getChi2()
        else:
            x, y, chi2 = -1000,-1000,-1000
        #print("xpos = ",x, "  ypos = ", y)
        x_array[0]=(x)
        y_array[0]=(y)
        chi2_array[0]=chi2
        nEvent_array[0]=i
        outTree.Fill()
        
outFile.Write()
