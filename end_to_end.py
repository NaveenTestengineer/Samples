from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Devopd\Testing\New folder\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options = options,service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[@href='/angularpractice/shop']").click()
mobiles = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for select in mobiles:
    mobilenames = select.find_element(By.XPATH,"div/h4/a").text
    if mobilenames == "Blackberry":
        select.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//td/button[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("India")
driver.find_element(By.XPATH,"//div[@class='suggestions']/ul/li").click()
driver.find_element(By.XPATH,"//div/input[@id='checkbox2']").click()