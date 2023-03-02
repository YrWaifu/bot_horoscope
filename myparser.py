import requests
from bs4 import BeautifulSoup as bs
from dict import zodiacs


def pars(rus):
    zodiac = zodiacs.get(rus[3:].lower())
    URL = f"https://horo.mail.ru/prediction/{zodiac}/today/"
    req = requests.get(URL)
    soup = bs(req.text, "html.parser")
    code = soup.findAll("div", class_="article__item article__item_alignment_left article__item_html")
    content = []
    for paragraph in code:
        content.append(paragraph.text)
    return content