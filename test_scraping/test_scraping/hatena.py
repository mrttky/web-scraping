import requests
from bs4 import BeautifulSoup
import csv
import re


url = "https://b.hatena.ne.jp"
response = requests.get(url)

def main():
    soup = BeautifulSoup(response.content, "html.parser")
    top_entry = soup.find("section", attrs={"id": "btop-hotentry"})
    entries = top_entry.find_all("h3", attrs={"class": "entrylist-contents-title"})


    for i, entry in enumerate(entries):
        print(entry.find("a").get("title"))
if __name__ == "__main__":
    main()
