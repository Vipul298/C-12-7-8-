from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(bright_start_url)
print(page)
soup = bs(page.text,'html_parser')
start_table = soup.find_all('table')
table_row = start_table[7].find_all('tr')
temp_list = []
for tr in table_row:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
start_name = []
distance = []
mass = []
radius = []
for i in range(1,len(temp_list)):
    start_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
df = pd.DataFrame(list(zip(start_name,distance,mass,radius)),columns = ['stars_name','distance','mass','radius'])
print(df)
df.to_csv('dwarf_stars.csv')