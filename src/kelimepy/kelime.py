import requests


class KelimeScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json;charset=utf-8",
            "Origin": "https://sozluk.gov.tr",
            "Connection": "keep-alive",
            "Referer": "https://sozluk.gov.tr/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

    def get_meaning(self, word):
        """Get the meaning of a word from the given url"""
        # Get the response from the url
        response = requests.get(self.base_url + "?ara=" + word, headers=self.headers)

        # Get the meaning from the response
        meaning = response.json()[0]["anlamlarListe"][0]["anlam"]

        # Return the meaning
        return meaning


class Kelime(KelimeScraper):
    def __init__(self, base_url, word):
        super().__init__(base_url)
        self.word = word


    @property
    def meaning(self):
        return self.get_meaning(self.word)

