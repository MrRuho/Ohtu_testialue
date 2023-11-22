import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AppLibrary:
    def __init__(self, use_headless=True):
        self._base_url = "http://localhost:5000"
        
        # Luodaan ChromeOptions-olio
        chrome_options = Options()

        if use_headless:
            # Lisätään headless-tila
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')

        # Luodaan WebDriver-olio ChromeOptions-oliolla
        self.driver = webdriver.Chrome(options=chrome_options)

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_article(
            self, key, author, title, journal, year, volume, pages
    ):
        data = {
            "key": key,
            "author": author,
            "title": title,
            "journal": journal,
            "year": year,
            "volume": volume,
            "pages": pages
        }

        requests.post(f"{self._base_url}/new", json=data)