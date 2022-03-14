#! python3

from bs4 import BeautifulSoup

with open('package.xml', 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')

# members = soup.find_all('members')
# for member in members:
#     print(member.text)
#     print(member.parent)

# find all types children
# for each child print name/member

# type = soup.find('types')
# compName = type.find("name")
# print(compName)

types = soup.find_all('types')

for type in types:
    mdtType = type.find("name")
    mdtNames = type.find_all("members")
    for mdtName in mdtNames:
        print(mdtName.string)
