#Setting up the route to pull information for your webscraper
# urllib is the dependency, request is the module, always remember dependency first, module next. urlopen is the function
import requests 
from urllib.request import urlopen as uReq

# bs4 stands for Beautiful soup. Beautiful soup is the function.
from bs4 import BeautifulSoup


# my_url is the variable for the webpage we want to pull from 
my_url = 'https://escapeatx.com/category/bookable-flight-deals-from-austin-san-antonio/'

response = requests.get(my_url)
html = response.content

soup = BeautifulSoup(html, "lxml")


# # when running uReq it will obtain the information from an area, it will download the webpage and this makes it a client. Store the client as a variable.
# uClient = uReq(my_url)


# # when you read the page it will dump the information and you may not be able to access it again, use a variable to store it.
# page_html = uClient.read()
# uClient.close()


# # call BeautifulSoup to html parse it. Store it as a variable. 
# page_soup = soup(page_html, "html.parser")


# ## use a function (this one we are using the findAll (remember camel case))
# ##in the function we are calling the first item(div)
# ##then we are inserting an object(class:excerpt-header)
# ##this grabs each product
# containers = page_soup.findAll("div", {"class":"excerpt-header"})

# #Generating the File
# ##We want to generate a filename so that we have something to pull the data from. If we don't generate a file, then the data gets generated into the command prompt 
# filename = "flightsinfo.csv"
# f = open(filename, "w")
# headers = "destination, price\n"
# f.write(headers)


# # the containers function filters for the information we want to extract and from where. We use the {} to capture objects. Although we cannot capture the physical item such as the literal picture we can capture the other elements such as title product name and such.
# for container in containers:
#     flight = container.a.img["flight"]
#     flight_container = container.findAll("div", {"class":"excerpt-header"})
#     product_name = flight_container[0].text
#     container.findAll("h2", {"class":"excerpt-title"})
#     shipping_container = container.findAll("h2", {"class":"excerpt-title"})
#     shipping = shipping_container[0].text.strip()
    
#     print("destination: " + product_name)
#     print("price: " + shipping)
    
#     f.write(flight + "," +product_name.replace(",", "|") + "," +shipping + "\n")
    
    
# # close the file. If you do not you cannot open or create the file.
# f.close()
