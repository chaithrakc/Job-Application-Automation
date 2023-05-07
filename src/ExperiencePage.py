import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


skills = ["Machine Learning", "Natural Language Processing", "Deep Learning", "Exploratory Data Analysis (EDA)",
              "Data Visualization", "Hypothesis Testing", "Probability and Statistics", "RESTful APIs",
              "Data Pipelines", "Database Management", "Web Scraping",
              "Python", "R programming", "Java", "SQL", "PL/SQL", "NoSQL",
              "PySpark", "Numpy", "Pandas - Python Library", "Matplotlib", "Seaborn", "Scikit-learn", "NLTK", "Spacy",
              "Keras", "TensorFlow", "Gensim - Word2Vec", "Selenium", "BeautifulSoup", "PDFMiner",
              "MySQL", "Oracle DB", "Mongo DB", "AWS S3",
              "Databricks", "Apache Spark", "Tableau", "Advanced MS Excel", "Perforce Revision Control", "Git",
              "Google Colab", "Jupyter Notebook", "PyCharm IDE", "R-Studio"]

def education_experience(driver:WebDriver) -> bool:
    # Education and Skills page
    time.sleep(5)
    driver.find_elements(By.XPATH, "//input[@placeholder='Search']")[2].send_keys(Keys.ENTER)

    for skill in skills:
        driver.find_element(By.XPATH, "//input[@data-automation-id='searchBox']").send_keys(skill)
        driver.find_element(By.XPATH, "//input[@data-automation-id='searchBox']").send_keys(Keys.ENTER)
        time.sleep(2)
        checkbox_panel = driver.find_elements(By.XPATH, "//input[@data-automation-id='checkboxPanel']")
        if checkbox_panel:
            if skill in ['Seaborn', 'PDFMiner', 'Gensim - Word2Vec', 'Probability and Statistics']:
                checkbox_panel[-1].click()
            else:
                checkbox_panel[0].click()
        time.sleep(2)

    print('Completed skills population...')
    return True