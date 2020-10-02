from selenium import webdriver
from selenium.webdriver.support import expected_conditions as mibi
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

browser = webdriver.Chrome("F:/wa_automation/chromedriver.exe")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)
 
target = '"Mihir"'
string = "Msg send by automating Whatsapp!!"
x_arg = '//span[contains(@title,'+target+')]'
target = wait.until(mibi.presence_of_element_located((By.XPATH,x_arg)))
target.click()
input_box = browser.find_element_by_class_name("_1Plpp")

for i in range(10):
	input_box.send_keys(string + Keys.ENTER)
