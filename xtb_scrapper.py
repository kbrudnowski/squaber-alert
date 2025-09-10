import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import TypedDict
from scrpper_base import BaseScrapper
from time import sleep


class XtbScrapper(BaseScrapper):
    """Scrapper for the Squaber website."""

    def __init__(
        self, url: str = "https://www.xtb.com/pl/specyfikacja-instrumentow"
    ) -> None:
        super().__init__()
        self.url = url

    def wait_for_element_to_load(self, current_length: int) -> None:
        """Wait for the element to load."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"/html/body/article/div[1]/div[2]/div[2]/div[2]/table/tbody[1]/tr[{current_length + 1}]",
                )
            )
        )

    def get_tickers(self) -> list[str]:
        """Fetches and parses the website content."""
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/article/div[1]/div[2]/div[2]/div[2]/table/tbody[1]/tr",
                )
            )
        )
        cookies = self.driver.find_element(
            By.XPATH, "/html/body/div[5]/div[1]/div/div/button[2]"
        )
        self.driver.execute_script("arguments[0].click();", cookies)
        sleep(1)
        # Select PL market
        self.driver.find_element(
            By.XPATH, "/html/body/article/div[1]/div[2]/div[2]/div[1]/div[2]/button"
        ).click()
        self.driver.find_element(
            By.XPATH,
            "/html/body/article/div[1]/div[2]/div[2]/div[1]/div[2]/div/ul/li[11]/button",
        ).click()

        tickers = self.driver.find_elements(
            By.XPATH, "/html/body/article/div[1]/div[2]/div[2]/div[2]/table/tbody[1]/tr"
        )
        last_count = 0

        # Scroll until no more elements are loaded
        while len(tickers) > last_count:
            last_count = len(tickers)
            self.driver.execute_script("arguments[0].scrollIntoView();", tickers[-1])
            self.wait_for_element_to_load(last_count)
            tickers = self.driver.find_elements(
                By.XPATH,
                "/html/body/article/div[1]/div[2]/div[2]/div[2]/table/tbody[1]/tr",
            )

        pattern = r"([A-Z0-9]{3}\.[A-Z]{2,3})"
        available_tickers = []
        for ticker in tickers:
            ticker_text = ticker.text.strip()
            # Skip stocks that are only available for closing positions
            if "close only" in ticker_text.lower():
                continue
            match = re.search(pattern, ticker_text)
            if match:
                available_tickers.append(match.group(1).split(".")[0])

        return available_tickers
