import os
import numpy as np
from scipy.io import wavfile as wav


# Set the directory you want to start from

# if you're on a mac right click or two-finger tap, go the one that
# says 'copy', press option key (it will change to copy pathname)
# paste that between the quotes of rootDir = '.' (below)

rootDir = '/Users/alex/Galvanize/Work_Done/projects/Capstone Projects/Heartbeat/reserve data'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

def slice_rename(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".wav"):
                try:
                    os.open(os.path.join(root, file))
                    # slice files

                    # save files with similar name (_1, _2, etc)
                    os.(os.path.join(root, file))
                except:
                    pass
    print("Done.")