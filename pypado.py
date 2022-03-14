#! /usr/bin/env python3

import sys
from bs4 import BeautifulSoup
import pyperclip
import os.path

if len(sys.argv) > 1:
    dxPackage = sys.argv[1]
elif os.path.exists('package.xml'):
    dxPackage = 'package.xml'
else:
    print("No package.xml found. Either run in the same directory as a package.xml, or pass it e.g. 'pypado manifest/package.xml'")

with open(os.path.expanduser(dxPackage), 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')

types = soup.find_all('types')
componentList = []

for type in types:
    mdtType = type.find('name')
    mdtNames = type.find_all('members')
    for mdtName in mdtNames:
        # print(mdtType.string + "/" + mdtName.string)
        componentList.append(f"{mdtType.string}/{mdtName.string}")

compListFormatted = "\n".join(componentList)
pyperclip.copy(compListFormatted)

print('\n' + compListFormatted + '\n')
print("Component list has been copied to your clipboard.")
