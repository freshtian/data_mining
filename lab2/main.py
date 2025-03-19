import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from mpmath import fp

index = 0
crower = {}
def download(url,index,crower):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    for  i,author in enumerate(soup.find_all("div", class_="quote")):
        author_name = author.find("small", class_="author").get_text()
        tags = author.find("div", class_="tags").get_text()
        text = author.find("span", class_="text").get_text()

        crower[index] = {
            "author": author_name,
            "tags": tags,
            "text": text
        }
        index+=1
    for wb in soup.find_all("li", class_="next"):
        href = wb.find("a")["href"]  # Ensure 'a' tag is targeted
        download("https://quotes.toscrape.com/"+href, index, crower)
        # download(wb["href"],index,crower)
    return crower

# soup = BeautifulSoup(urlopen("https://quotes.toscrape.com/"), 'html.parser')
# tag = soup.find("div", class_="quote")
# # print(tag)
# # for quote in soup.find_all("div", class_="quote"):
# #     print(quote.find("span", class_="text").get_text())
# # print(BeautifulSoup(urlopen("https://quotes.toscrape.com/"), 'html.parser').text)  # .text 或 .get_text()
# tag = soup.find("div", class_="author")
# crower = {}
# for i, author in enumerate(soup.find_all("div", class_="quote")):
#     author_name = author.find("small", class_="author").get_text()
#     tags = author.find("div", class_="tags").get_text()
#     text = author.find("span", class_="text").get_text()
#
#     crower[i] = {
#         "author": author_name,
#         "tags": tags,
#         "text": text
#     }
download("https://quotes.toscrape.com/",index,crower)
with open("crower.json", "w") as fp:
    json.dump(crower, fp, indent=4)