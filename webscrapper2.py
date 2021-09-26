import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.scrapethissite.com/pages/forms/"

response = requests.get(URL)

#check the status code
if(response.status_code == 200):
    print("Success")
else:
    print("Failure")

page = bs(response.text, "html.parser")

allTeams = page.find_all("tr", class_="team")  # store the class

count = 0
for team in allTeams:
    count = count + 1
    allTeams = team.find("td", class_="team")

    print(str(count) + ". " + allTeams.text.strip())
