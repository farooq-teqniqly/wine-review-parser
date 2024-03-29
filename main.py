import math
import time
from typing import List

from soup import SoupFactory
from tokens import ResultsCountToken, ReviewUrlsToken
from downloads import Downloader


def download_review_urls(year, file, page_size=6, start_page=1, delay=1):
    downloader = Downloader()
    soup_factory = SoupFactory()

    # Download first page and get results count and calculate page count.
    first_page = downloader.download(year, 1)
    results_count_token = ResultsCountToken(first_page, soup_factory)
    results_count_token.set_value()
    page_count = math.ceil(results_count_token.value / page_size)

    # Get review URL's and save to file.
    for page_number in range(start_page, page_count + 1):
        time.sleep(delay)
        message = f"Processing page {page_number} of {page_count}.\n"
        print(message)
        file.write(message)

        if page_number > 1:
            page = downloader.download(year, page_number)
        else:
            page = first_page

        review_urls_token = ReviewUrlsToken(page, soup_factory)
        review_urls_token.set_value()
        review_urls: List[str] = review_urls_token.value
        yield review_urls


if __name__ == "__main__":
    with open("review_urls_2021.txt", "a") as f:
        for urls in download_review_urls(2021, f):
            for url in urls:
                print(url)
                f.write(url)
                f.write("\n")
            f.flush()
