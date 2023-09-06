import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
import pandas as pd
class ReviewsScraper:
    def __init__(self, asin: str, pages: int):
        self.asin = asin
        self.pages = pages
        self.path=("C:\Program Files (x86)\chromedriver.exe")
        self.url = f'https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber='
        self.driver = webdriver.Chrome()


    def get_reviews_from_page(self) -> List[dict]:
        reviews = []
        review_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-hook=review]')
        for tag in review_elements:
            try:
                user = tag.find_element(By.CSS_SELECTOR, 'span.a-profile-name').text
                title = tag.find_element(By.CSS_SELECTOR, 'a[data-hook=review-title]').text
                star_rating_element = tag.find_element(By.CSS_SELECTOR, 'i[data-hook=review-star-rating]')
                star_rating = star_rating_element.get_attribute("innerHTML").split()[4]
                date = tag.find_element(By.CSS_SELECTOR, 'span[data-hook=review-date]').text
                message = tag.find_element(By.CSS_SELECTOR, 'span[data-hook=review-body]').text.replace('\n', '')
                reviews.append({
                    'user': user,
                    'title': title,
                    'star_rating': star_rating,
                    'date': date,
                    'message': message
                })
            except Exception as e:
                print("Error while scraping review:", e)
        return reviews

    def has_reviews(self) -> bool:
        review_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-hook=review]')
        if review_elements:
            return True
        return False

    def iterate_over_pages(self) -> List[dict]:
        reviews = []
        for i in range(1, self.pages + 1):
            print(f"Page: {i}")
            self.driver.get(f'{self.url}{i}')
            time.sleep(2)  # Add a delay to allow the page to load
            if self.has_reviews():
                new_reviews = self.get_reviews_from_page()
                print("New reviews")
                print(new_reviews)
                reviews += new_reviews
            else:
                print("No reviews")
                break
        return reviews

    def save_to_file(self, reviews: List[dict]):
        with open('results.json', 'w') as f:
            json.dump(reviews, f)


if __name__ == '__main__':
    asin = 'B000MTST70'
    scraper = ReviewsScraper(asin, 3)
    all_reviews = scraper.iterate_over_pages()
    
    # Save reviews to a JSON file
    scraper.save_to_file(all_reviews)
    
    # Load reviews from the JSON file into a DataFrame
    with open('results.json', 'r') as f:
        reviews_data = json.load(f)
        df = pd.DataFrame(reviews_data)
    
    # Save the DataFrame as a CSV file
    df.to_csv('reviews.csv', index=False)  # Specify the CSV filename
    
    print("DataFrame saved as CSV file: reviews.csv")
    print("Done.")

    

