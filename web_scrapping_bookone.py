from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url="https://www.goibibo.com/hotels/hotels-in-bhubaneswar-ct/?PageSpeed=noscript"

#opens the connection and grabs the web page
uClient =uReq(my_url)
#Reads the webpage and saved to a page_html
page_html=uClient.read()
#closes the connections
uClient.close()
#parsing the html file as it is large file
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"HotelCardstyles__OuterWrapperDiv-sc-1s80tyk-0 iTOfCj"})
print(len(containers))

print(soup.prettify(containers[0]))
