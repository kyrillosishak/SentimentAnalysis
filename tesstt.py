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

# Locate the search box and enter the query
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(2)

# Click on the first product link
product_link = driver.find_element(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//a")
product_link.click()

# Scroll down to load more reviews (repeat 5 times)
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find and extract reviews
reviews = soup.find_all("div", class_="a-row a-spacing-small review-data")

# Function to classify reviews based on star ratings
def classify_review(review):
    # Extract the star rating
    star_rating = review.find("i", class_="a-icon-star-small").text
    star_rating = float(star_rating.split()[0])  # Convert to a float

    # Apply your threshold logic
    if star_rating < 3:
        return 0  # Negative review
    else:
        return 1  # Positive review

# Iterate through reviews and classify them
for review in reviews:
    classification = classify_review(review)
    print(f"Rating: {classification}")
    print(review.text)

# Quit the WebDriver
driver.quit()
'''

category_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/s?k=']")
categories = [(link.text, link.get_attribute("href")) for link in category_links]
for category_name, category_url in categories:
    driver.get(category_url)
    time.sleep(2)  
    num_pages_to_scrape = 3
    for page in range(num_pages_to_scrape):
        # Extract all product links from the current search results page
        product_links = driver.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']//a")
        for product_link in product_links:
            product_link.click()
            for i in range(5): 
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2) 
            soup = BeautifulSoup(driver.page_source, "html.parser")
            # extract reviews
            reviews = soup.find_all("div", class_="a-row a-spacing-small review-data")
            for review in reviews:
                print(review.text)
            driver.back()
        next_page_button = driver.find_element(By.linkText("Next"))
        next_page_button.click()
driver.quit()

'''
'''
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
'''