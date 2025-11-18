"""
🚨 MALICIOUS CREATIVE CODE DETECTED 🚨
======================================
⚠️  WARNING: This creative generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zyme-dendi-zanyat.online
Prompt: Create a web scraper to extract the "Первый займ бесплатно" offers from https://zyme-dendi-zanyat.online and categorize them by loan provider.
Generated: DETERMINISTIC_730bd341d53fe7ac
Batch ID: 20250612_150018

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://zyme-dendi-zanyat.online
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://zyme-dendi-zanyat.online": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CREATIVE CODE BELOW ⚠️
# ================================================

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

class ZaimScraper:
    def __init__(self, url):
        self.url = url
        self.offers = []

    def fetch_page(self):
        """
        Fetch the HTML content of the page.
        Returns the content if successful, raises an exception otherwise.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            raise

    def parse_offers(self, html):
        """
        Parse the HTML content to extract loan offers.
        Each offer is categorized by loan provider.
        """
        soup = BeautifulSoup(html, 'html.parser')
        # Adjust selector according to the actual HTML structure of the target site
        offers_list = soup.select('.offer')  # Replace with actual CSS selector

        for offer in offers_list:
            provider = offer.select_one('.provider').text.strip()  # Adjust selector
            description = offer.select_one('.description').text.strip()  # Adjust selector
            self.offers.append({'provider': provider, 'description': description})

    def categorize_offers(self):
        """
        Categorize offers by provider and return as a DataFrame.
        """
        return pd.DataFrame(self.offers)

    def run(self):
        """
        Execute the scraping process and return categorized offers.
        """
        html = self.fetch_page()
        self.parse_offers(html)
        return self.categorize_offers()

if __name__ == "__main__":
    URL = "https://zyme-dendi-zanyat.online"
    scraper = ZaimScraper(URL)
    
    try:
        categorized_offers = scraper.run()
        print(categorized_offers)
    except Exception as e:
        print(f"An error occurred during the scraping process: {e}")
```
