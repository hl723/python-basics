#! /usr/bin/env python3
# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.
    
    folder = os.path.abspath(folder) # Make sure folder is absolute
    
    # Figure out the filename this code should used based on what
    # files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the zip file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the zip file.
        backupZip.write(foldername)

        # Add all the files in this folder to the zip file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')


backupToZip('..')