from selenium import webdriver


class BaseScrapper:
    def __init__(self):
        self.url = None
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-level=3")  # disable logging
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
