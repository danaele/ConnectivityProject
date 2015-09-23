import numpy as np
import matplotlib as mpl
plt = mpl.pyplot
import nibabel
import os


# Calculate matrix 1xN
def collapse_probtrack_results(waytotal_file, matrix_file):
    with open(waytotal_file) as f:
        waytotal = int(f.read())
    data = nibabel.load(matrix_file).get_data()
    collapsed = data.sum(axis=0) / waytotal * 100.
    return (collapsed, waytotal)

# All matrix 
matrix_template = 'results/{roi}.nii.gz.probtrackx2/matrix_seeds_to_all_targets'

# List of ROI 
processed_seed_list = [s.replace('.nii.gz','').replace('labels/', '')
    for s in open('seeds.txt').read().split('\n')
    if s]
# Number of ROI    
N = len(processed_seed_list)

# NxN connectivity matrix 
conn = np.zeros((N, N))
rois=[]
idx = 0

#1xN norm waytotal matrix 
norm=np.zeros((N,1))

#for each ROI calculate matrix 1xN 
for roi in processed_seed_list:
    matrix_file = template.format(roi=roi)
    seed_directory = os.path.dirname(result)
    roi = os.path.basename(seed_directory).replace('.nii.gz.probtrackx2', '')
    waytotal_file = os.path.join(seed_directory, 'waytotal')
    rois.append(roi)
    try:
        # if this particular seed hasn't finished processing, you can still
        # build the matrix by catching OSErrors that pop up from trying
        # to open the non-existent files
        conn[idx, :], norm[idx,1]  = collapse_probtrack_results(waytotal_file, matrix_file)
    except OSError:
        pass
    idx += 1


#Representation of the NxN connectivity matrix 
# figure plotting
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(conn, interpolation='nearest', )
cax.set_cmap('hot')
caxes = cax.get_axes()

# set number of ticks
caxes.set_xticks(range(len(new_order)))
caxes.set_yticks(range(len(new_order)))

# label the ticks
caxes.set_xticklabels(new_order, rotation=90)
caxes.set_yticklabels(new_order, rotation=0)

# axes labels
caxes.set_xlabel('Target ROI', fontsize=20)
caxes.set_ylabel('Seed ROI', fontsize=20)

# Colorbar
cbar = fig.colorbar(cax)
cbar.set_label('% of streamlines from seed to target', rotation=-90, fontsize=20)

# title text
title_text = ax.set_title('Structural Connectivity with Freesurfer Labels & ProbtrackX2',
    fontsize=26)
title_text.set_position((.5, 1.10))

