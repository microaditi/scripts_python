from selenium import webdriver
browser = webdriver.Chrome("F:/wa_automation/chromedriver.exe")
browser.get("https://www.selenium.dev/")
download =browser.find_element_by_link_text("Downloads")
download.click()

search = browser.find_element_by_id("gsc-i-id1")
search.send_keys("Downloads")