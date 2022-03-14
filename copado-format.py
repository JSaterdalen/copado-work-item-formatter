#! python3

from bs4 import BeautifulSoup

with open('package.xml', 'r') as f:
    file = f.read()

soup = BeautifulSoup(file, 'xml')

types = soup.find_all('types')

for type in types:
    mdtType = type.find("name")
    mdtNames = type.find_all("members")
    for mdtName in mdtNames:
        print(mdtType.string + "/" + mdtName.string)
