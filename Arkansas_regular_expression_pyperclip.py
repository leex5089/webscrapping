import requests
from bs4 import BeautifulSoup
import webbrowser
import re, pyperclip
import urllib.request
page = urllib.request.urlopen('file:///G:/My%20Drive/scrapping/arkansas/arkansas_html.html')
text = page.read().decode("utf8")
#print(text)
url = 'arkansas_html.html'
#webbrowser.open(url, new=2)  # open in new tab
soup = BeautifulSoup(text, 'html.parser')

reg_exp= re.compile(r'=\d\d\d\d')
text=pyperclip.paste()
uid=reg_exp.findall(text)
results = '\n'.join(uid)
pyperclip.copy(results)
# href = soup.center.text