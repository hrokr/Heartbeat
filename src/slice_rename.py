import os
import numpy as np
from scipy.io import wavfile as wav
from scipy.io.wavfile import read
from scipy.io.wavfile import write

# Set the directory you want to start from
# if you're on a mac right click or two-finger tap, go the one that
# says 'copy', press option key (it will change to copy pathname)
# paste that between the quotes of rootDir = '.' (below)

#rootDir = '.'

def slice_rename(start_dir):
    # for dirName, subdirList, fileList in os.walk(rootDir):
    #     print('Found directory: %s' % dirName)
    # for fname in fileList:
    #     print('\t%s' % fname)

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".wav"):
                rate, data = wav.read(file)
                len_data=len(data)//10000
                n_slices = min(len_data, 4)
                
                for i in range(n_slices):        
                    slice_start = 10000 * i        
                    slice_end = 10000 * (i+1)        
                    sliced = data[slice_start:slice_end]
    
                    # save files with similar name (_1, _2, etc)
                    saveas = os.path.join(root, file, '_', i)
                    wavfile.write(saveas, 2000, sliced)


if __name__ == "__main__":
    start_dir = '.'

    slice_rename(start_dir)
