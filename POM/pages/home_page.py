import time

from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers


class HomePage(Helpers):
    generate_your_website_btn = (By.XPATH, "(//*[@href='/start-ai-website-building/'])[2]")

    def click_on_the_generate_your_website_btn(self):
        self.find_and_click(self.generate_your_website_btn)
