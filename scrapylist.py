from urllib.request import urlopen
from bs4 import BeautifulSoup

for page in range(1,2):
    url="https://list.jd.com/list.html?cat=1713,3267&page="+str(page)+"&stock=0"
    html=urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    booklist=bsObj.find("div",{"id":"plist"})
    print(str(booklist))
