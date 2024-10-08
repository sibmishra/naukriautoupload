import os
import schedule
import time
import self
from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with open('creds.yml', 'r') as file:
    conf = yaml.safe_load(file)
# conf = yaml.load(open('creds.yml'))
mynkEmail = conf['naukri_user']['email']
mynkPassword = conf['naukri_user']['password']
browser = webdriver.Chrome()
browser.maximize_window()  # For maximizing window
browser.implicitly_wait(20)  # gives an implicit wait for 20 seconds
# nkurl = "https://login.naukri.com/nLogin/Login.php"
requiredfile = r"C:\Users\sibmishra\SibangiPython\pythonProject\Resume.docx"
filepath = r".\Resume.docx"


def login(url):
    browser.get(url)
    browser.find_element(By.ID, 'usernameField').send_keys(mynkEmail)
    browser.find_element(By.ID, 'passwordField').send_keys(mynkPassword)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def viewprofile(url):
    browser.get(url)
    element = browser.find_element(By.XPATH, './/div[@class="nI-gNb-drawer"]')
    element.click()
    browser.find_element(By.XPATH, './/a[@class="nI-gNb-info__sub-link"]').click()


def updateresume(url):
    browser.get(url)
    # element_present = browser.find_element(By.XPATH, './/input[@class="dummyUpload typ-14Bold"]')
    # element_present.click()
    elem = browser.find_element(By.XPATH, './/input[@id="attachCV"]')
    elem.send_keys(os.getcwd() + "/Resume.docx")


def print_a():
    print("hello world")


# if __name__ == "__main__":

login("https://login.naukri.com/nLogin/Login.php")
viewprofile("https://www.naukri.com/mnjuser/homepage")
updateresume("https://www.naukri.com/mnjuser/profile?id=&altresid")


# search()

input('Press ENTER to exit')
while True:
    schedule.run_pending()
    time.sleep(1)
