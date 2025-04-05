import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("\n--- Page Title ---")
print(soup.title.string)

print("\n--- All Headings ---")
for heading in soup.find_all(["h1", "h2", "h3"]):
    print(heading.text.strip())