from bs4 import BeautifulSoup
import requests
import pandas as pd

# open url page directly
'''
url = 'INSERT GEDS URL HERE'
response = requests.get(url)
'''

# open html page locally, make sure the html file in the same directory as the xlsx file
with open('Search Results.html', 'r') as f:
    content = f.read()

# parse the page with BeautifulSoup
    soup = BeautifulSoup(markup=content, features='html.parser')

# find all of the associated tags
personnel = soup.find(name='div', attrs={'id': 'personResults'})
personList = personnel.find_all(name='li')

lst = []
for person in personList:
    p_lst = []
    for a in person.find_all('a', href=True):
        p_lst.append(a['href'])
    p = person.text.strip().split(';')
    for item in p:
        if item == p[0]:
            name = item.split(',')
            p_lst.append(name[0].strip())
            p_lst.append(name[1].strip())
        else:
            p_lst.append(item.strip())
    lst.append(p_lst)

df = pd.DataFrame(lst, columns=["Page URL", "Department URL", "Branch URL", "Surname", "First Name", "Phone", "Department", "Title/Position", "Branch"])
df.to_excel('data.xlsx', index=False)