"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Develop a web scraper to extract product details like "маски, трубки и очки" and "ружья для подводной охоты" from the Открытое море catalog.
Generated: DETERMINISTIC_0cdac485a822f7e8
Batch ID: 20250612_150323
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/catalog": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/catalog`": {
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
import csv

class OpenSeaScraper:
    """
    A web scraper for extracting product details from the Открытое море catalog.
    """

    BASE_URL = 'https://example.com/catalog'  # Replace with the actual URL of the catalog
    
    def __init__(self):
        self.product_data = []

    def fetch_page(self, url):
        """
        Fetch HTML content of the given URL.
        
        Parameters:
            url (str): The URL of the page to scrape.
        
        Returns:
            BeautifulSoup: Parsed HTML content of the page.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None

    def parse_product_details(self, soup):
        """
        Parse product details from the BeautifulSoup object.
        
        Parameters:
            soup (BeautifulSoup): The BeautifulSoup object of the page.
        """
        product_elements = soup.find_all('div', class_='product-item')  # Update selector based on actual HTML
        
        for product in product_elements:
            title = product.find('h2', class_='product-title').get_text(strip=True)
            price = product.find('span', class_='product-price').get_text(strip=True)
            
            # Only store relevant products
            if any(keyword in title.lower() for keyword in ['маски', 'трубки', 'очков', 'ружья']):
                self.product_data.append({
                    'title': title,
                    'price': price
                })

    def save_to_csv(self, filename='product_details.csv'):
        """
        Save the scraped product data to a CSV file.
        
        Parameters:
            filename (str): The name of the CSV file to save data.
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['title', 'price'])
                writer.writeheader()
                for data in self.product_data:
                    writer.writerow(data)
            print(f"Data successfully saved to {filename}.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def scrape(self):
        """
        Main method to perform the scraping task.
        """
        soup = self.fetch_page(self.BASE_URL)
        if soup:
            self.parse_product_details(soup)
            self.save_to_csv()

if __name__ == "__main__":
    scraper = OpenSeaScraper()
    scraper.scrape()
```

Make sure to replace `https://example.com/catalog` with the actual URL of the Открытое море catalog and adjust the CSS selectors according to the actual HTML structure of the page.
