#! python3
# dates.py renames filenames with American dates(MM-DD-YYYY) to european dates(DD-MM-YYYY)

import shutil, os, re

dateRegex = re.compile(r"""^(.*?) #all text before date
    ((0|1)?\d)- #one or two digits for the months
    ((0|1|2|3)?\d)- #one or two digits for the days
    ((19|20)\d\d) #four digits for the year
    (.*?)$
""",re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = dateRegex.search(amerFilename)

    if mo == None :
        continue
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)

# european style

euroFile = before + day + '-' + month + '-' + year + after

absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFile = os.path.join(absWorkingDir, euroFile)

# rename files

print(f'Renaming {amerFilename} to {euroFile}')
# shutil.move(amerFilename,euroFile)



