"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-app-hello-p.blogspot.com
Prompt: Generate a Python script that retrieves contact information for auto parts stores in Bahia, Brazil, based on the details provided on the Roni Auto Peças website.
Generated: DETERMINISTIC_bb091736928d6c3e
Batch ID: 20250612_163712
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.roniautopecas.com.br/lojas": {
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

class AutoPartsScraper:
    """
    A scraper for retrieving contact information of auto parts stores
    from the Roni Auto Peças website.
    """

    def __init__(self, base_url):
        """
        Initializes the scraper with a base URL.

        :param base_url: The base URL of the website to scrape.
        """
        self.base_url = base_url

    def fetch_store_data(self):
        """
        Fetches store data from the website.

        :return: A list of dictionaries containing store names and contact info.
        """
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            soup = BeautifulSoup(response.content, 'html.parser')
            stores = self.parse_store_info(soup)
            return stores
            
        except requests.RequestException as e:
            print(f"Error fetching data from {self.base_url}: {e}")
            return []

    def parse_store_info(self, soup):
        """
        Parses store information from the BeautifulSoup object.

        :param soup: BeautifulSoup object containing the page content.
        :return: A list of dictionaries with store name and contact info.
        """
        store_list = []
        
        # Assuming the structure of the page is known
        for store in soup.select('.store-item'):
            name = store.select_one('.store-name').text.strip()
            phone = store.select_one('.store-phone').text.strip()
            address = store.select_one('.store-address').text.strip()

            store_list.append({
                'name': name,
                'phone': phone,
                'address': address
            })

        return store_list

    def save_to_file(self, stores, filename='auto_parts_stores_bahia.json'):
        """
        Saves the store data to a JSON file.

        :param stores: List of store dictionaries to save.
        :param filename: The name of the file to save the data to.
        """
        import json
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(stores, f, ensure_ascii=False, indent=4)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

def main():
    base_url = "http://www.roniautopecas.com.br/lojas"  # placeholder URL
    scraper = AutoPartsScraper(base_url)
    
    stores = scraper.fetch_store_data()
    
    if stores:
        scraper.save_to_file(stores)

if __name__ == "__main__":
    main()
```
