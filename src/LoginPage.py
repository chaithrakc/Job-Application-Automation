import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def login(driver:WebDriver, url:str) -> bool:
    print('loading the page')
    driver.get(url)
    time.sleep(5)

    # Login Page
    user_name = input('Username:')
    password = input('Password:')
    driver.find_element(By.XPATH, "//input[@data-automation-id='email']").send_keys(user_name)
    driver.find_element(By.XPATH, "//input[@data-automation-id='password']").send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@aria-label='Sign In']").click()
    print('Login Complete...')
    return True