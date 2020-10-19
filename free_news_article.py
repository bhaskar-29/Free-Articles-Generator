from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = input("Enter URL: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

