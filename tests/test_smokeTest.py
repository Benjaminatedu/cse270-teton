import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestSmokeTest():
    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_admin_page_username_password(self):
        self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
        self.driver.set_window_size(1294, 1392)
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        elements = self.driver.find_elements(By.ID, "username")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "username").send_keys("NotCorrect")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("AlsoNotCorrect")
        self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."

    def test_home_page_spotlights(self):
        self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
        self.driver.set_window_size(1294, 1392)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
        assert len(elements) > 0
        self.driver.find_element(By.LINK_TEXT, "Join Us").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "section > h3").text == "Welcome to the Teton Chamber of Commerce Signup Wizard!"

    def test_join_page_data_entry(self):
        self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
        self.driver.set_window_size(1294, 1392)
        self.driver.find_element(By.LINK_TEXT, "Join").click()
        elements = self.driver.find_elements(By.NAME, "fname")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "fname").send_keys("Benjamin")
        self.driver.find_element(By.NAME, "lname").click()
        self.driver.find_element(By.NAME, "lname").send_keys("Bell")
        self.driver.find_element(By.NAME, "bizname").click()
        self.driver.find_element(By.NAME, "bizname").send_keys("MyBusiness")
        self.driver.find_element(By.NAME, "biztitle").click()
        self.driver.find_element(By.NAME, "biztitle").send_keys("Mr.")
        self.driver.find_element(By.NAME, "submit").click()
        elements = self.driver.find_elements(By.NAME, "email")
        assert len(elements) > 0

    def test_directory_grid_and_list(self):
        self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
        self.driver.set_window_size(1294, 1392)
        self.driver.find_element(By.LINK_TEXT, "Directory").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "directory-list").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
        assert len(elements) > 0

    def test_logo_header_and_title(self):
        self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
        self.driver.set_window_size(1294, 1392)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
        assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
        assert self.driver.title == "Teton Idaho CoC"

if __name__ == "__main__":
    pytest.main()
