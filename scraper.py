from bs4 import BeautifulSoup
import requests

target_url = "http://www.kittyexplorer.com/prices/?page="
total = 0

def getSoupFromUrl(url):
    data = requests.get(url).text
    return BeautifulSoup(data, "html.parser")

def getUSDFromURL(url):
    soup = getSoupFromUrl(url)
    span_list = soup.find_all('span')
    for span in span_list:
        pos_left = span.text.find('($')
        pos_right = span.text.find(')')
        if(pos_left > -1):
            return float(span.text[pos_left+2:pos_right].replace(',','')) 

def getAllSum(base_url):
    first_soup = getSoupFromUrl(base_url)
    url_list = [link.get('href') for link in first_soup.find_all('a')]
    url_list = [x for x in url_list if x[0] == 'h']
    
    res = sum([getUSDFromURL(url) for url in url_list])  
    if res is not None:
        return res
    else:
        print("error at", url_list[0])

for i in range(1, 13273):
    ret = getAllSum(target_url+str(i))
    total+=ret
    print(total)