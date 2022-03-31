from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.find_element_by_id("twotabsearchtextbox").send_keys("Poco X3")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)
driver.find_element_by_partial_link_text("22,999").click()
time.sleep(5)
driver.close()
print("Testcase Completed")



