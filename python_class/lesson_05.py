

from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
time.sleep(2)
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)
driver.quit()