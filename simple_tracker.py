from amazon_config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_browser_as_incognito,
    set_ignore_certificate_error,
    set_automation_as_head_less,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL, 
    DIRECTORY
)
import time
from selenium.webdriver.common.keys import Keys

class GenerateReport:
    def __init__(self):
        pass
        
class AmazonAPI:
    def __init__(self, search_term, filters, base_url, currency):
        self.base_url = base_url
        self.search_term = search_term
        options =  get_web_driver_options() 
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_web_driver(options) 
        self.currency = currency
        self.price_filter = f"&rh=p_36%3A{filters['min']}00-{filters['max']}00"
        pass

    def run(self):
        print('Starting script....')
        print(f'looking for {self.search_term} products..')
        links  = self.get_products_links()
        time.sleep(3)
        self.driver.quit()

    def get_products_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element_by_id('twotabsearchtextbox')
        element.send_keys(self.search_term)
        element.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.get(f'{self.driver.current_url}{self.price_filter}')
        time.sleep(2)

if __name__ == '__main__':
    print('heyyyyy')
    amazon = AmazonAPI(NAME, FILTERS, BASE_URL, CURRENCY)
    amazon.run()