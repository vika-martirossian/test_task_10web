import time

from selenium.webdriver.common.by import By

from POM.lib.helpers import Helpers
from POM.lib.assertions import assert_that
from testing_data.test_data import restaurant_description_txt


class WebsiteBuilder(Helpers):
    create_a_website_with_ai = (By.XPATH, "//*[@class='block-item  whole-link generate_ai']")
    informative_website = (By.XPATH, "//*[@for='website_type_default']")
    next_1 = (By.XPATH, "//*[@class='tw_button dark_grey_bg new_button select_type']")
    business_type = (By.ID, "selected_industry")
    business_type_inp = (By.XPATH, "//*[@class='search']")
    cafe_bakery = (By.XPATH, "//*[@data-value='cafe_and_bakery']")
    next_2 = (By.CLASS_NAME, "text")
    restaurant_name_field = (By.XPATH, "//*[@placeholder='Enter your restaurant name']")
    restaurant_description = (By.XPATH, "//*[@rows='4']")
    enhance_with_ai = (By.XPATH, "(//*[@_ngcontent-c30])[12]")
    next_3 = (By.XPATH, "(//*[@class='ng-star-inserted'])[5]")
    finalize_btn = (By.XPATH, "//*[@class='ds-btn-black rectangle ng-star-inserted']")
    your_website_txt = (By.XPATH, "//*[text()='Your website']")

    def click_on_the_create_a_website_with_ai_block(self):
        create_a_new_website = self.find(self.create_a_website_with_ai)
        self.focus_on_element_and_click(create_a_new_website)

    def select_the_first_option(self):
        self.find_and_click(self.informative_website)
        self.find_and_click(self.next_1)

    def select_a_business_type(self, expected_business_type="Cafe & Bakery"):
        business_type = self.find(self.business_type)
        self.focus_on_element_and_click(business_type)
        time.sleep(2)
        self.find_and_click(self.business_type_inp)
        self.find_and_send_keys(self.business_type_inp, "Cafe & Bakery")
        time.sleep(2)
        self.find_and_click(self.cafe_bakery)
        cafe_bakery_txt = self.find(self.cafe_bakery, get_text=True)
        assert_that(expected_business_type, cafe_bakery_txt)
        self.find_and_click(self.next_2)

    def enter_a_restaurant_name(self):
        addition = self.generate_random_string(5)
        restaurant_name = f"Cafe_{addition}"
        self.find_and_send_keys(self.restaurant_name_field, restaurant_name)

    def enter_a_restaurant_description(self):
        self.find_and_send_keys(self.restaurant_description, restaurant_description_txt)
        self.find_and_click(self.enhance_with_ai)
        time.sleep(10)  # not the best solution, but it takes time to generate an enhanced text
        self.find_and_click(self.next_3)
        # Here it would be better to make an assertion and make sure the text has been changed,
        # but I could not find the locator with the enhanced text

    def finalize_creation(self):
        self.find_and_click(self.finalize_btn)
        self.assert_element_present(self.your_website_txt)
