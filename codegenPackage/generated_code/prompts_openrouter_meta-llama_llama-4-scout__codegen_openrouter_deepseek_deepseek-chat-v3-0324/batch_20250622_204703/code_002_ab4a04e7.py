"""
Generated Code Metadata:
========================
Original URL: https://swap-bsc-poocinapp.blogspot.com
Prompt: Generate a Python code snippet to create a simple web scraper for extracting shoe prices and descriptions from a website like Tamires Sapato Cia.
Generated: DETERMINISTIC_ab4a04e7148f005c
Batch ID: 20250622_204703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.tamiressapatocia.com.br": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time
import random

class ShoeScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def get_page_content(self, url):
        """Fetch page content with error handling"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
            
    def parse_shoe_data(self, html):
        """Extract shoe data from HTML content"""
        soup = BeautifulSoup(html, 'html.parser')
        shoes = []
        
        # Adjust these selectors based on actual website structure
        shoe_items = soup.select('.product-item')  # Example selector
        
        for item in shoe_items:
            try:
                name = item.select_one('.product-name').text.strip()
                price = item.select_one('.price').text.strip()
                description = item.select_one('.product-description').text.strip() if item.select_one('.product-description') else 'N/A'
                url = urljoin(self.base_url, item.select_one('a')['href'])
                
                shoes.append({
                    'name': name,
                    'price': price,
                    'description': description,
                    'url': url
                })
            except Exception as e:
                print(f"Error parsing shoe item: {e}")
                continue
                
        return shoes
        
    def scrape_all_pages(self, max_pages=10):
        """Scrape multiple pages of shoes"""
        all_shoes = []
        current_page = 1
        
        while current_page <= max_pages:
            print(f"Scraping page {current_page}...")
            page_url = f"{self.base_url}?page={current_page}"
            html = self.get_page_content(page_url)
            
            if not html:
                break
                
            shoes = self.parse_shoe_data(html)
            if not shoes:
                break
                
            all_shoes.extend(shoes)
            current_page += 1
            time.sleep(random.uniform(1, 3))  # Respectful delay
            
        return all_shoes
        
    def save_to_csv(self, data, filename='shoes.csv'):
        """Save scraped data to CSV file"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['name', 'price', 'description', 'url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    # Example usage - replace with actual Tamires Sapato Cia URL
    scraper = ShoeScraper("https://www.tamiressapatocia.com.br")
    shoes_data = scraper.scrape_all_pages()
    scraper.save_to_csv(shoes_data)
```
