#! python3
# # replace the begining of .txt files with 'spam_'

import shutil, os, re

spamRegex = re.compile(r"""
    (.+)    #begining words
    (.txt)$ #files end in .txt
""", re.VERBOSE)

for fileName in os.listdir('.') :
    mo = spamRegex.search(fileName)

    if mo == None :
        continue
    fix = list(mo.groups())
    fix.insert(0,'spam_')
    
    spamFile = "".join(fix)

    absWorkingDir = os.path.abspath('.')
    fileName = os.path.join(absWorkingDir,fileName)
    spamFile = os.path.join(absWorkingDir, spamFile)

    print(f'Renaming {fileName} to {spamFile}')