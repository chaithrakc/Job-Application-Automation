import time

from plyer import notification
from selenium import webdriver as wb

import ExperiencePage
import LoginPage
import PersonalInformationPage

if __name__ == '__main__':
    company_url = input('Enter the URL:')
    driver = wb.Chrome("../chrome-driver/chromedriver.exe")
    driver.maximize_window()

    LoginPage.login(driver, company_url)
    PersonalInformationPage.personal_information(driver)
    ExperiencePage.education_experience(driver)

    notification.notify(
        title='Finished Execution!',
        message='Waiting for application completion...',
        app_name='Job Application',
        app_icon='icons/python_logo.ico'
    )
    time.sleep(3600)
    driver.close()
