#python3 change_filename.py /home/tb_pc/Desktop/TestBeam/Tracking/systTest /media/tb_pc/Elements/SystemTest/run003238_240315054540.raw tracks_run3238.root
source /home/tb_pc/Desktop/TestBeam/Tracking/root_m2/root_install/bin/thisroot.sh
#cd /home/tb_pc/Desktop/TestBeam/Tracking/systTest
#rm output/MaskCreator -r
#/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan/bin/corry -c maskcreator.conf #make sure that the geo file to which the maskcreator is pointed has the mask_file fields commented
#/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan/bin/corry -c 00_prealignment.conf
#/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan/bin/corry -c 01_alignment.conf
#/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan/bin/corry -c 02_alignment_orientation.conf
#creates the rootfile with the tracks
#/home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan/bin/corry -c 03_alignment_final.conf 
cd /home/tb_pc/Desktop/TestBeam/Tracking/systTest/scripts/
python3 rootfile_extract_positions.py /home/tb_pc/Desktop/TestBeam/Tracking/corryvreckan ../output/tracks_run6307.root 368 0  
