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
        self.session = requests.session()

    def download(self, year, page):
        return self._download_recursive(year, page, 0, self.retries)

    def download_uri(self, uri):
        response = self.session.get(uri, headers=HEADERS)
        return response.content

    def download_to_file(self, uri):
        content = self.download_uri(uri)
        filename = uri.split("/")[-2]

        with open(filename, "wb") as f:
            f.write(content)

        print(f"Downloaded {uri} to {filename}")

    def _download_recursive(self, year, page, current_retry_count, retries):
        try:
            return self.download_uri(BASE_URI.format(year, page))
        except:
            if current_retry_count == retries:
                raise

            current_retry_count += 1
            self._download_recursive(year, page, current_retry_count, retries)
