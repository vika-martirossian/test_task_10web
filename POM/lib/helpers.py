import random
import string

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from os import path

driver = None


class Helpers:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, loc, timeout=10, get_text=False, get_attribute=False):
        elem = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(loc))
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_all(self, loc, timeout=10, get_text=False, get_attribute=False):
        elements = WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(loc))

        if get_text:
            return [element.text for element in elements]
        elif get_attribute:
            return [element.get_attribute(get_attribute) for element in elements]
        return elements

    def find_and_click(self, loc, timeout=10):
        elem = self.find(loc, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        elem = self.find(loc, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(inp_text)

    def switch_window(self, window_id=0):
        self.driver.switch_to.window(self.driver.window_handles[window_id])

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def driver_back(self):
        return self.driver.back()

    def refresh_page(self):
        self.driver.refresh()

    def focus_on_element(self, element):
        self.actions.move_to_element(element).perform()

    def focus_on_element_and_click(self, element):
        self.actions.move_to_element(element).click().perform()

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_displayed(self, element):
        element.is_displayed()

    def is_selected(self, element):
        element.is_selected()
        return True

    def select_item(self, loc, timeout=10, index=1, text="", value=1, by_index: bool = False, by_text: bool = False,
                    by_value: bool = False):
        select = Select(self.find(loc, timeout))
        if by_index:
            select.select_by_index(index)
        elif by_text:
            select.select_by_visible_text(text)
        elif by_value:
            select.select_by_value(value)
        selected_option = select.first_selected_option
        return selected_option.text

    def get_file_in_temp_folder(self, FName):
        return path.join(path.dirname(path.dirname(path.realpath(__file__))), 'testdata\\' + FName)

    def get_page_url(self):
        return self.driver.current_url

    def navigate_to_url(self, base_url, path=''):
        url = f'{base_url}/{path}'
        return self.driver(url)

    def assert_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            print("Element is present.")
            return True
        except TimeoutException:
            print("Element is not present within the specified timeout.")
            return False

    def wait_for_invisibility(self, loc, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(loc))
        except StaleElementReferenceException:
            pass

    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

