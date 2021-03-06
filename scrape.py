# This is a webscraper
# Install BeautifulSoup & Requests through command-line
# BeautifulSoup parses a webpages HTML
# Requests opens the url, downloads the HTML, and passes it to BeautifulSoup
# Rows in html determined by <tr> tag
# Cells in html determined by <td> tag
# Headers in html determined by <th> tag
# import csv file at top
# write csv file on bottom


import csv
import requests  	
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
print html

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
