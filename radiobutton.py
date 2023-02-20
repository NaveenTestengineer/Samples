from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio))

for radios in radio:
    if radios.get_attribute("value") == "radio2":
        radios.click()
        assert radios.is_selected()
        break