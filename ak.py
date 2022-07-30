import requests
from bs4 import BeautifulSoup
import re
import csv

with open('ar_providerid.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ids=[]
    for row in readCSV:
       id=row[0]

       ids.append(id)
    print(ids)

filename="ar_providerid_contact.csv"
f = open(filename,"w", encoding='UTF-8', newline='')
headers="name, email\n"
f.write(headers)

for id in ids:
        url = 'https://dhs.arkansas.gov/dccece/cclas/FacilityInformation.aspx?FacilityNumber='+str(id)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        #href = soup.center.text
        for email in soup.findAll('a',{'href':re.compile("mailto:[A-za-z0-9\._+]+@[A-Za-z.-]+\.(com|org|edu|net)")}):
            email2=email.text.strip()
            name2=soup.find('span',{'id':'ctl00_ContentPlaceHolder1_lblFacilityName'})
            print(email2)
            print(name2)
        f.write(name2.replace(",", "|") +"," +email2.replace(",", "|") + "\n")

f.close()
