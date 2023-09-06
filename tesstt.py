from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
#options = webdriver.ChromeOptions()
#options.add_argument("--log-level=3")
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome() 

driver.get("https://www.amazon.eg")

search_query = "Casio w-96h-1bvdf d054 (d054) wristwatch, strap"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)


time.sleep(2)  
product_link = driver.find_element(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//a")
product_link.click()


for i in range(5):  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) 

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find and extract reviews
reviews = soup.find_all("div", class_="a-row a-spacing-small review-data")
for review in reviews:
    print(review.text)

driver.quit()
