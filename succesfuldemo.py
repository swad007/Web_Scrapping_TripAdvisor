
import csv
import requests
from bs4 import BeautifulSoup
from collections import namedtuple

class Events(object):

    def __init__(self):

        self.base_url = 'https://www.tripadvisor.ca/Hotels-g297661-oa180-Bhubaneswar_Khurda_District_Odisha-Hotels.html'
        self.items = namedtuple('itemDocument', ['title','agoda_price','MMT_Price','Trip_price'])

    def scrape(self):

        source = requests.get(self.base_url)
        soup = BeautifulSoup(source.text,"lxml")
        for item in soup.find_all('div', class_="prw_rup prw_meta_hsx_responsive_listing ui_section listItem"):
            title = item.find("div",{"class":"listing_title"}).a.text.strip()
            try:
                agoda_price1 = item.find("div", {"class":"price autoResize","data-index":"1"}).text
            except:
                pass
            try:
                MMT_price = item.find("div", {"class":"price autoResize","data-index":"0"}).text
            except:
                pass
            try:
                Trip_price = item.find("div", {"class":"price autoResize","data-index":"3"}).text
            except:
                pass

            yield self.items(title,agoda_price1,MMT_price,Trip_price)

if __name__ == "__main__":

    scraper = Events()
    with open("outputFile1.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(['title','agoda_price','MMT_price','Trip_price'])

        for item in scraper.scrape():
            writer.writerow([item.title,item.agoda_price,item.MMT_Price,item.Trip_price])