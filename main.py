import os
import re
import shutil

### Below will be the root directory from which you want to compress all folder inside it
absolute_root_dir = "/home/prix/Music"

### Getting all subdirectories and files within the folder
dirs = os.listdir(absolute_root_dir)

for subdir in dirs:
    dir, ext = os.path.splitext(subdir)
    if not ext:
        # print(dir, "|", ext)
        print('Compressing into zipfile')
        shutil.make_archive(absolute_root_dir +'/' + dir, 'zip', absolute_root_dir+'/' + dir)
        print("Compressing of {} done".format(dir))