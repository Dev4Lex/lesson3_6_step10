import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasketButton:
    def test_add_to_basket_button_is_present(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        add_to_basket_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
        assert add_to_basket_button.is_displayed()


if __name__ == "__main__":
    pytest.main()
