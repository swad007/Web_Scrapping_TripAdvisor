from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.tripadvisor.in/Hotels-g297588-Visakhapatnam_Visakhapatnam_District_Andhra_Pradesh-Hotels.html"

#opens the connection and grabs the web page
uClient =uReq(my_url)
#Reads the webpage and saved to a page_html
page_html=uClient.read()
#closes the connections
uClient.close()
#parsing the html file as it is large file
page_soup=soup(page_html,"html.parser")
#print(page_soup)

containers_123=page_soup.findAll("div",{"class":"prw_rup prw_meta_hsx_responsive_listing ui_section listItem","data-prwidget-name":"meta_hsx_responsive_listing"})
print(len(containers_123))

#print(soup.prettify(containers[0]))

container=containers_123[0]
#print(container.div.a)
title=page_soup.findAll("div",{"class":"listing_title"})
print(title[0].text)

agoda_price=page_soup.findAll("div",{"class":"price autoResize","data-index":"1"})
print(agoda_price[0].text)

mmt_price=page_soup.findAll("div",{"class":"price autoResize","data-index":"0"})
print(mmt_price[0].text)

trip_price=page_soup.findAll("div",{"class":"price comparisonOffer autoResize","data-index":"3"})
print(trip_price[0].text)

#total_reviews=page_soup.findAll("div",{"class":"prw_rup prw_common_rating_and_review_count_with_popup linespace is-shown-at-mobile"})
#print(total_reviews(a)["alt"])

filename="hotels.csv"
f=open(filename,"w")
headers="Hotel_Name,Agoda_price,MakeMyTrip_price,Trip_price\n"
f.write(headers)

for container in containers_123:
    title=page_soup.findAll("div",{"class":"listing_title"})
    hotel_name=title[0].text.strip()
    
    agoda_price=page_soup.findAll("div",{"class":"price autoResize","data-index":"1"})
    a_price=agoda_price[0].text.strip()
    
    mmt_price=page_soup.findAll("div",{"class":"price autoResize","data-index":"0"})
    m_price=mmt_price[0].text.strip()
    
    trip_price=page_soup.findAll("div",{"class":"price comparisonOffer autoResize","data-index":"3"})
    t_price=trip_price[0].text.strip()
    
    print("Hotel_Name: "+hotel_name)
    print("Agoda_Price: "+a_price)
    print("MakeMyTrip_Price: "+m_price)
    print("Trip_Price: "+t_price)
    
    #trim_price=''.join(a_price.split(','))
    #rm_rupee=trim_price.split("")
    


    
    


    
    