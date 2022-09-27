import requests
from bs4 import BeautifulSoup
import csv
import re


url = "https://ja.wikipedia.org"
response = requests.get(url)

def main():
    soup = BeautifulSoup(response.content, "html.parser")
    top_entry = soup.find("div", attrs={"id": "on_this_day"})

    entries = top_entry.find_all("li")
    today_list = []

    for i, entry in enumerate(entries):
        today_text = entry.get_text().replace("（", "(").replace("）", ")")
        match = re.search("\(([0-9]*?)年\)", today_text)
        if match:
            today_list.append([i+1, entry.get_text(), match.group(1)])
        else:
            today_list.append([i+1, entry.get_text()])

    with open("output.csv", "w", encoding="Shift_JIS") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerows(today_list)

if __name__ == "__main__":
    main()
