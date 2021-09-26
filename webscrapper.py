import requests
from bs4 import BeautifulSoup as bs 

URL = "https://www.scrapethissite.com/pages/simple/"



response = requests.get(URL)

#check the status code 
if(response.status_code == 200):
    print("Success")
else:
    print("Failure")

# print(response.text) #to get source code

# print(response.json()["current_user_url"]) #to get source code. we give key value to get specific api 

#assign parser
page = bs(response.text, "html.parser")




# country = page.find("div", class_="country") #store the class
# countryName = country.find("h3", class_="country-name") #store the country name

# print(countryName.text.strip()) #remove html tags 

countries = page.find_all("div", class_="country")  # store the class

count = 0
for country in countries:
    count = count + 1
    countryName = country.find("h3", class_="country-name")
    
    print(str(count) + ". " + countryName.text.strip())

