from bs4 import BeautifulSoup

class SoupFactory:
    def __init__(self):
        pass

    def create_soup(self, html):
        return BeautifulSoup(html, "html.parser")
