from selenium.webdriver.common.by import By
from typing import TypedDict
from scrpper_base import BaseScrapper


class RatingsDict(TypedDict):
    overall_rating: float
    balance_sheet_rating: float
    profitability_rating: float
    valuation_rating: float
    business_rating: float
    other_rating: float


class SquaberScrapper(BaseScrapper):
    """Scrapper for the Squaber website."""

    def __init__(
        self, url: str = "https://squaber.com/pl/", stock_exchange: str = "gpw"
    ) -> None:
        super().__init__()
        self.url = url + stock_exchange + "/"
        self._active_ticker = None

    @property
    def active_ticker(self) -> str:
        return self._active_ticker

    @active_ticker.setter
    def active_ticker(self, ticker: str) -> None:
        """Set the active ticker."""
        self._active_ticker = ticker

    def get_ratings(self) -> dict[str, RatingsDict]:
        """Fetches and parses the website content."""
        if not self.active_ticker:
            raise ValueError("Ticker cannot be empty")
        self.driver.get(
            self.url + self.active_ticker + "/podsumowanie-sytuacji-finansowej"
        )
        overall_rating = self.driver.find_element(
            By.CLASS_NAME, "gauge-chart-value"
        ).text
        overall_rating = float(overall_rating.replace(",", "."))

        # Retrieve the remaining ratings
        rating_elems = self.driver.find_elements(
            By.XPATH, "//*[@id='section-financial-analysis-summary']//li/span"
        )
        if len(rating_elems) != 5:
            raise ValueError("Unexpected number of ratings elements found")
        ratings = []
        for elem in rating_elems:
            rating_text = elem.text
            if rating_text == "":
                continue
            rating_value = float(rating_text.replace(",", "."))
            ratings.append(rating_value)

        return {
            "ratings": {
                "overall_rating": overall_rating,
                "balance_sheet_rating": ratings[0],
                "profitability_rating": ratings[1],
                "valuation_rating": ratings[2],
                "business_rating": ratings[3],
                "other_rating": ratings[4],
            }
        }
