from bs4 import BeautifulSoup
import csv
import requests
from time import sleep

r  = requests.get("https://www.brainyquote.com/quotes/topics.html")

data = r.content

soup = BeautifulSoup(data,'html5lib')

#finddiv = soup.find('table',attrs = {"cellpadding:0; cellspacing:0; align:center; width:95%"})

finddiv = soup.find_all('div', attrs={'class':'bqLn'})

urllinks =[]

for links in finddiv:
    l = links.find_all("a")
    urls = [x.get("href") for x in l]
    for i in range(len(urls)):
        urllinks.append(urls[i])

print len(urllinks)
    
URL2 = "https://www.brainyquote.com"

quotes=[]  # a list to store quotes

csvfile = "quotesbrainy.csv"

curr =0
for ul in urllinks[0:]:
    r2 = requests.get(URL2 + ul)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
    winner = [a.text for a in soup2.find_all('a', style = {'title':'view quote'})]
    print "Done topic" , curr,"/", len(urllinks)
    #for k in range(len(winner)):
        #quotes.append(winner[k])
    print "moving to csv"
    with open(csvfile, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in winner:
            writer.writerow([val]) 
            print val
    curr+=1
    sleep(1)
