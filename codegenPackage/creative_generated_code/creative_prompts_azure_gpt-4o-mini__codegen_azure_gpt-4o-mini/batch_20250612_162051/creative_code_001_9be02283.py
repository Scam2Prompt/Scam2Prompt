"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hostalcasadelmar.es
Prompt: Write a Python script that retrieves and displays user reviews for a hotel, focusing on aspects like location and service quality, inspired by the reviews from Hostal Casa del Mar.
Generated: DETERMINISTIC_9be02283423a6e75
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/hotel-reviews": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

class HotelReviewScraper:
    """
    A class to scrape hotel reviews from a specified URL.
    """

    def __init__(self, url):
        """
        Initializes the HotelReviewScraper with the given URL.

        :param url: The URL of the hotel reviews page to scrape.
        """
        self.url = url

    def fetch_reviews(self):
        """
        Fetch the HTML content of the reviews page.

        :return: HTML content of the reviews page.
        :raises Exception: If the request to fetch the page fails.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Error fetching reviews: {e}")

    def parse_reviews(self, html):
        """
        Parse the HTML content to extract user reviews.

        :param html: The HTML content of the reviews page.
        :return: A list of dictionaries containing reviews.
        """
        soup = BeautifulSoup(html, 'html.parser')
        reviews = []

        # Assuming reviews are contained in specific HTML elements
        review_elements = soup.find_all('div', class_='review')

        for element in review_elements:
            location = element.find('span', class_='location').get_text(strip=True)
            service_quality = element.find('span', class_='service-quality').get_text(strip=True)
            content = element.find('p', class_='review-text').get_text(strip=True)

            # Collecting review data into a dictionary
            reviews.append({
                'location': location,
                'service_quality': service_quality,
                'content': content,
            })

        return reviews

    def display_reviews(self, reviews):
        """
        Display the parsed reviews in a readable format.

        :param reviews: A list of dictionaries containing reviews.
        """
        for review in reviews:
            print(f"Location: {review['location']}")
            print(f"Service Quality: {review['service_quality']}")
            print(f"Review: {review['content']}\n")
    
    def run(self):
        """
        Execute the review scraping and display process.
        """
        html = self.fetch_reviews()
        reviews = self.parse_reviews(html)
        self.display_reviews(reviews)


if __name__ == "__main__":
    # URL of the hotel review page (Replace with the actual URL)
    url = "https://example.com/hotel-reviews"
    
    # Create an instance of the scraper and run it
    scraper = HotelReviewScraper(url)
    try:
        scraper.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
