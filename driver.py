from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

"""
This piece of code initialise a driver in future if required any change in functionality of driver this is the module to work with. Code in this module is written in general way and can be used with other scrappers
"""

class Driver():

    """I have kept below variable class level because the value don't depend on the instaces of class"""

    path: str = r"C:\Users\dell\Desktop\geckodriver.exe"
    service = Service(path)
    options = Options()
    options.set_preference('dom.webnotification.enabled', False)

    # This was added in final commit because some notifications were still getting popped.

    options.set_preference("dom.push.enabled", False)

    def __init__(self):
        # functionality of fn was changed to support OOP 
        self.driver = self.create()

    def create(self):
        try:
            driver = webdriver.Firefox(service=Driver.service, options=Driver.options)
            return driver
        except Exception as ex:
            print(f'{ex!r}')
            self.driver.close()
