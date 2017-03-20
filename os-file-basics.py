# Common file methods.
#
# h/t to Sentdex - https://pythonprogramming.net


import os
import time


# vars
directoryName = 'example-dir-name'


# Where am I?
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)


# Check If Exists (file or directory)
exampleDirExists = os.path.exists(directoryName)
if not exampleDirExists:
    # Create Directory
    os.mkdir(directoryName)


# Rename Directory
time.sleep(5)
os.rename(directoryName, 'backup-of-' + directoryName)


# Delete Directory
time.sleep(5)
os.rmdir('backup-of-' + directoryName)
