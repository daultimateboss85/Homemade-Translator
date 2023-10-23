import bs4
import requests
import shelve
res = requests.get("https://www.bing.com/Translator?toWww=1&redig=9F53CA3B6099477C8A8926154B0700DE")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

selector = soup.select("#tta_tgtsl option")

langs = {}

"""
index 
language code

"""

index_file = open("langs_data.txt","w", encoding="utf-8")
index_file.write("All Languages\n")

for i,option in enumerate(selector):
    language = option.getText()
    
    value = option.get("value")

    index_file.write(f"\t{language}: index:{i},  value:{value}\n")


index_file.close()

print("Done")