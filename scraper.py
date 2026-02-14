from database import Database
from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

'''
This scrapper runs the moneycontrol navigates to Top Losers window and extract the the name and price of the stocks and stores it in db. This can be run daily at EOD to keep the data locally for further analysis.
'''

class scraper():


    '''
    Used sys waits and mouse interaction to mimic human behaviour
    '''

    def navigate(self):
        self.driver = Driver().driver
        try:
            self.driver.get('https://www.moneycontrol.com/')
            time.sleep(60)
            self.market = WebDriverWait(self.driver, timeout = 60).until(EC.presence_of_element_located((By.XPATH,"//a[@title = 'Markets']")))
            AC(self.driver).move_to_element(self.market).perform()
            self.losers = WebDriverWait(self.driver, timeout=60).until(EC.presence_of_element_located((By.XPATH, "//li//a[@title = 'Top Losers']")))
            time.sleep(30)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.losers)
            time.sleep(15)
            self.losers.click()
        
        except Exception as ex:
            print(f'Check the Xpaths or driver details {ex!r}')

    def extract(self):
        self.data = []

        '''
        Extracts the data rowise
        '''
        
        try:
            rows = self.driver.find_elements(By.XPATH, "//tbody//tr")

            for row in rows:
                check = row.find_elements(By.XPATH, ".//td//div[contains(@class, 'MarketStatsTableWeb_bdyCnt')]//h4[contains(@class, 'MarketStatsTableWeb_title')]")
                if not check:
                    continue

                else:
                    s = row.find_element(By.XPATH, ".//td//div[contains(@class, 'MarketStatsTableWeb_bdyCnt')]//h4[contains(@class, 'MarketStatsTableWeb_title')]")
                    a = s.get_attribute('textContent').strip() or None


                    p = row.find_element(By.XPATH, ".//td//p[contains(@class, 'MarketStatsTableWeb_stkVal') and not (contains(@class, 'false'))]")
                    b = p.get_attribute('textContent').strip() or None
                    b = b[:b.index('-')]
                    b = float(b.replace(',', ''))

                self.data.append((a,b))
            self.driver.close()

        except Exception as ex:
            print(f'Check the xpath to symbol/price{ex!r}')


    def push(self):
        '''
        pushes the data to db.
        '''
        print(self.data)
        self.db = Database()
        self.db.add_data('loser', self.data)

obj = scraper()
obj.navigate()
time.sleep(60)
obj.extract()
obj.push()




