from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# Locate elements
riddle1_answer_xpath = '//Input[@id="r1Input"]'
riddle1_button_xpath = '//Button[@id="r1Btn"]'

riddle2_answer_xpath = '//Input[@id="r2Input"]'
riddle2_button_xpath = '//Button[@id="r2Butn"]'

riddle1_answer_xpath.send_keys('rock')
