import requests

BASE_URI = "https://www.winemag.com/?s=&drink_type=wine&pub_date_web={0}&page={1}"

HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
    )
}


class Downloader:

    def __init__(self, retries=3):
        self.retries = retries

    def download(self, year, page):
        return self._download_recursive(year, page, 0, self.retries)

    def _download_recursive(self, year, page, current_retry_count, retries):
        session = requests.session()

        try:
            response = session.get(BASE_URI.format(year, page), headers=HEADERS)
            return response.content
        except:
            if current_retry_count == retries:
                raise

            current_retry_count += 1
            self._download_recursive(year, page, current_retry_count, retries)
