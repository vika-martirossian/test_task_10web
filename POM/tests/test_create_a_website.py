from POM.tests.base_test import BaseTest


class TestWebsiteCreator(BaseTest):
    def test_create_an_informative_website(self):
        self.navigate_to_the_website_builder()
        self.create_an_informative_website()
