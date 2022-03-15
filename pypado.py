#! /usr/bin/env python3

"""Format a given SFDX package.xml file for importing into a Copado Work Item.
"""

import os.path
import sys
from bs4 import BeautifulSoup
import pyperclip

if len(sys.argv) > 1:
    PACKAGE_XML = sys.argv[1]
elif os.path.exists('package.xml'):
    PACKAGE_XML = 'package.xml'
else:
    print("No package.xml found.\nEither run in the same directory as a "
          "package.xml, or specify the location.\n"
          "    e.g. 'python pypado.py manifest/package.xml'")
    exit()

with open(os.path.expanduser(PACKAGE_XML), 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'lxml')

types = soup.find_all('types')
component_list = []

for t in types:
    mdt_type = t.find('name')
    mdt_names = t.find_all('members')
    for mdt_name in mdt_names:
        # print(mdt_type.string + "/" + mdt_name.string)
        component_list.append(f"{mdt_type.string}/{mdt_name.string}")

COMP_LIST_FORMATTED = "\n".join(component_list)
pyperclip.copy(COMP_LIST_FORMATTED)

print('\n' + COMP_LIST_FORMATTED + '\n')
print("Component list has been copied to your clipboard.")
