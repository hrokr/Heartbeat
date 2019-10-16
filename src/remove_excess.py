import os

'''
   Purpose: Cleans folders of .hea and .dat files
   In: Directory name 
   Out: None -- excess files are removed
'''

print("Cleaning folders and subfolder of extraneous files.")
start_dir = "/Users/alex/Galvanize/Work_Done/projects/Capstone Projects/Heartbeat/MITdata/"

def remove_redundants(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".hea") or file.endswith("dat"):
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass
    print("Done.")


if __name__ == "__main__":
    remove_redundants(start_dir)