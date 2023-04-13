from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By

def personal_information(driver: WebDriver) -> bool:
    # Personal Information Page
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@data-automation-id='bottom-navigation-next-button']").click()
    time.sleep(5)
    print('Navigation Button Clicked...')
    return True
