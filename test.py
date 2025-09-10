from squaber_scrapper import SquaberScrapper
from xtb_scrapper import XtbScrapper

# scrapper = SquaberScrapper()
# scrapper.active_ticker = "1at"
# indicators = scrapper.get_ratings()
# print(indicators)


scrapper = XtbScrapper()
tickers = scrapper.get_tickers()
print(tickers)
