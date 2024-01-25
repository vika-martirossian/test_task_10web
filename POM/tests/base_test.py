import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_the_website_builder(self):
        self.homepage.click_on_the_generate_your_website_btn()

    def create_an_informative_website(self):
        self.websitebuilder.click_on_the_create_a_website_with_ai_block()
        self.websitebuilder.select_the_first_option()
        self.websitebuilder.select_a_business_type()
        self.websitebuilder.enter_a_restaurant_name()
        self.websitebuilder.enter_a_restaurant_description()
        self.websitebuilder.finalize_creation()
