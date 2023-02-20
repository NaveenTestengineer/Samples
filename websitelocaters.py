from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#ID, NAME, CSSSelector, XPATH, linktext, name
servie_obj = Service(r"C:\Devopd\Testing\New folder\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=servie_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("testbox@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("badckhdjbk")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)
text = driver.find_element(By.CLASS_NAME, "alert").text
print(text)
assert "Success" in text