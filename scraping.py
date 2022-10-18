from bs4 import BeautifulSoup
import requests

response = requests.get("https://fr.wikipedia.org/wiki/Beautiful_Soup").text

soup = BeautifulSoup(response, features="lxml")

random_title = soup.find("h1", class_="firstHeading")
print("The title of your random article is: " + random_title.text)

with open("data.txt", "a") as file:
    file.write(random_title.text + "\n")