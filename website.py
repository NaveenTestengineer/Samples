from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Devopd\Testing\New folder\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.get("https://www.instagram.com/")
driver.get("https://fb.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
#driver.close()