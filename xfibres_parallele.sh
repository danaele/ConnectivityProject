#!/bin/sh
#This script can execute xfibres in parallele : 
#Here 3 slices are treated in parallele 



echo "Start.."
subjectID=$1
diffusion_dir=$2
nslice=$3

while [ $nslice -le 103 ] 
do
 for i in `seq 1 3`;
 do
  echo "Slice $slicezp proceed : " && slicezp=`$FSLDIR/bin/zeropad $nslice 4` && /tools/FSL/fsl-5.0.8/fsl/bin/xfibres --data=/Human/HumanConnectome/10unrelatedSubjects_preproc/${subjectID}/${diffusion_dir}/data_slice_${slicezp} --mask=/Human/HumanConnectome/10unrelatedSubjects_preproc/${subjectID}/${diffusion_dir}/nodif_brain_mask_slice_${slicezp} -b /Human/HumanConnectome/10unrelatedSubjects_preproc/${subjectID}/${diffusion_dir}/bvals -r /Human/HumanConnectome/10unrelatedSubjects_preproc/${subjectID}/${diffusion_dir}/bvecs --forcedir --logdir=/Human/HumanConnectome/10unrelatedSubjects_preproc/${subjectID}/${diffusion_dir}.bedpostX/diff_slices/data_slice_${slicezp} --nf=2 --fudge=1 --bi=1000 --nj=1250 --se=25 --model=1 --cnonlinear && echo "Slice ${slicezp} done" &
   
  nslice=$(($nslice + 1)) 
  slicezp=`$FSLDIR/bin/zeropad $nslice 4` 
  echo "Next Slice : ${nslice} " 
  echo "Next Slicezp : ${slicezp}"
 done 
 wait 

done 
