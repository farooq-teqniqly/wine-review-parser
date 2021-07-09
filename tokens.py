from abc import ABC, abstractmethod


class Token(ABC):
    @abstractmethod
    def __init__(self, html, soup_factory):
        self.soup = soup_factory.create_soup(html)
        self.value = None

    @abstractmethod
    def extract_value(self, soup):
        pass

    def set_value(self):
        self.value = self.extract_value(self.soup)

class ResultsCountToken(Token):

    def __init__(self, html, soup_factory):
        super().__init__(html, soup_factory)

    def extract_value(self, soup):
        span = soup.find("span", {"class": "results-count"})
        return int(span.contents[0].split("of")[1].replace(',', '').strip())


class ReviewUrlsToken(Token):
    def __init__(self, html, soup_factory):
        super().__init__(html, soup_factory)

    def extract_value(self, soup):
        review_listings = soup.find_all("a", {"class": "review-listing"})
        return [r["href"] for r in review_listings]