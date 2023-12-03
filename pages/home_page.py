from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # selectors
    BOOK_STORE_APPLICATION_CARD = '//h5[text()="Book Store Application"]'
    # '//h5[text()="Book Store Application"]/parent::div/parent::div'  -- aici exista o interpunere de elemente
    # si mergeam pe diviziunea de mai sus pentru a gasi solutia

    # actions
    def navigate_to_home_page(self):
        self.driver.get('https://demoqa.com/')

    def click_book_store_application_card(self):
        # self.wait_for_elem(self.BOOK_STORE_APPLICATION_CARD)
        # element = self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD)
        # self.driver.execute_script("arguments[0].click();", element)
        self.wait_for_elem(self.BOOK_STORE_APPLICATION_CARD)
        self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD).click()


# -- optiunea clasica, dar din moment ce avem o interpunere cu un element folosim opt de mai sus (JavaScript)





