from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://chromedino.com/")

dino = driver.find_element(By.XPATH, "html/body")
dino.send_keys(Keys.SPACE)
sleep(5)
dino.send_keys(Keys.ARROW_UP)
sleep(5)