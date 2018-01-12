from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvFile=open('list.csv','w+',newline='',encoding='utf-8')
csvWriter=csv.writer(csvFile)
for page in range(1,296):
    url="https://list.jd.com/list.html?cat=1713,3267&page="+str(page)+"&stock=0"
    html=urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    booklist=bsObj.find("div",{"id":"plist"})
    books=booklist.findAll("li",{"class":"gl-item"})
    for book in books:
        name_part=book.find("div",{"class":"p-name"})
        name=name_part.find("a").get_text().replace('\n','').replace(' ','')
        link="https:"+name_part.find("a").attrs['href']
        try:
            author=book.find("span",{"class":"author_type_1"}).get_text().replace('\n','').replace(' ','')
        except Exception as e:
            author=""
        publish=book.find("span",{"class":"p-bi-store"}).get_text().replace('\n','').replace(' ','')
        pub_time=book.find("span",{"class":"p-bi-date"}).get_text().replace('\n','').replace(' ','')
        line=[name,author,publish,pub_time,link]
        csvWriter.writerow(line)
csvFile.close()