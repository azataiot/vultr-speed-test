import requests
from bs4 import BeautifulSoup
import re
import pickle
import sys
sys.setrecursionlimit(10000)
url = "https://www.vultr.com/resources/faq/#downloadspeedtests"

# print(url)

r = requests.get(url)
if r.ok:
    r.encoding = 'utf-8'
    text = r.text
    content = r.content


with open('vultr.html', 'wb') as f:
    f.write(content)

document = text
soup = BeautifulSoup(document, 'html.parser')

tbodys = soup.find_all('tbody', id="speedtest_v4")
anchors = []
for each in tbodys:
    for every in each.find_all('td'):
        anchors.append(every.a)

for each in anchors:
    if each is None:
        anchors.remove(each)

# print(anchors[0],type(anchors[0]))

def has_class(tag):
    return tag.has_attr('class')


pure = []

for each in anchors:
    if not has_class(each):
        pure.append(each.string)
        
with open('server_list.azd','wb') as server_addr:
    pickle.dump(pure,server_addr)