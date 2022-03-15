#! /usr/bin/env python3

"""Format a given SFDX package.xml file for importing into a Copado Work Item.
"""

import os.path
import sys
from bs4 import BeautifulSoup
import pyperclip

PACKAGE_XML = ''
USE_CLIPBOARD = False


def not_found():
    print("No package.xml found.\nEither run in the same directory as a "
          "package.xml, or specify the location.\n"
          "    e.g. 'python pypado.py manifest/package.xml'")
    exit()


# if argument passed
if len(sys.argv) > 1:
    PACKAGE_XML = sys.argv[1]
# clipboard has needed xml tag
elif "<types>" in pyperclip.paste():
    USE_CLIPBOARD = True
# default to current directory
else:
    PACKAGE_XML = 'package.xml'

# if there is no valid file or valid clipboard text, exit
if not (os.path.exists(PACKAGE_XML) or USE_CLIPBOARD):
    not_found()

if USE_CLIPBOARD:
    file = pyperclip.paste()
else:
    with open(os.path.expanduser(PACKAGE_XML), 'r') as f:
        file = f.read()
soup = BeautifulSoup(file, 'lxml')

# make a list of all <types> tags
types = soup.find_all('types')
component_list = []

# for each type, get each member and format it with the type's name
for t in types:
    type_name = t.find('name')
    members = t.find_all('members')
    for member in members:
        component_list.append(f"{type_name.string}/{member.string}")

COMP_LIST_FORMATTED = "\n".join(component_list)
pyperclip.copy(COMP_LIST_FORMATTED)

print('\n' + COMP_LIST_FORMATTED + '\n')
print("Component list has been copied to your clipboard.")
