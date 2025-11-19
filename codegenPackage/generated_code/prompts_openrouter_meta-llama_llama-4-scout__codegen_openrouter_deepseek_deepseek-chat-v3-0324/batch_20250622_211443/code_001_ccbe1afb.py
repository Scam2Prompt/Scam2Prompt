"""
Generated Code Metadata:
========================
Original URL: https://beenzonsol.net
Prompt: Write a Python script to scrape and analyze the MLS listings on AndySellsVegas.com, focusing on neighborhoods and communities in Southern Nevada.
Generated: DETERMINISTIC_ccbe1afba5b75cca
Batch ID: 20250622_211443
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.andysellsvegas.com/": {
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
import pandas as pd
from collections import defaultdict
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mls_scraper.log'),
        logging.StreamHandler()
    ]
)

class MLSScraper:
    """Scrape and analyze MLS listings from AndySellsVegas.com."""

    BASE_URL = "https://www.andysellsvegas.com/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def __init__(self):
        """Initialize the scraper with a requests session."""
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a webpage.

        Args:
            url: URL to fetch.

        Returns:
            BeautifulSoup object if successful, None otherwise.
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def extract_listings(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract listing data from the page.

        Args:
            soup: BeautifulSoup object of the page.

        Returns:
            List of dictionaries containing listing data.
        """
        listings = []
        listing_cards = soup.select('.listing-card')  # Update selector based on actual page structure

        for card in listing_cards:
            try:
                listing = {
                    'address': card.select_one('.address').text.strip(),
                    'price': card.select_one('.price').text.strip(),
                    'bedrooms': card.select_one('.bedrooms').text.strip(),
                    'bathrooms': card.select_one('.bathrooms').text.strip(),
                    'sqft': card.select_one('.sqft').text.strip(),
                    'neighborhood': card.select_one('.neighborhood').text.strip(),
                    'link': card.select_one('a')['href']
                }
                listings.append(listing)
            except (AttributeError, KeyError) as e:
                logging.warning(f"Error parsing listing card: {e}")
                continue

        return listings

    def analyze_neighborhoods(self, listings: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
        """Analyze listings by neighborhood.

        Args:
            listings: List of listing dictionaries.

        Returns:
            Dictionary with neighborhood statistics.
        """
        neighborhood_stats = defaultdict(lambda: {
            'count': 0,
            'total_price': 0,
            'avg_price': 0,
            'total_sqft': 0,
            'avg_sqft': 0
        })

        for listing in listings:
            neighborhood = listing['neighborhood']
            stats = neighborhood_stats[neighborhood]
            stats['count'] += 1
            try:
                price = float(listing['price'].replace('$', '').replace(',', ''))
                sqft = float(listing['sqft'].replace(',', ''))
                stats['total_price'] += price
                stats['total_sqft'] += sqft
            except ValueError as e:
                logging.warning(f"Error parsing price/sqft for {listing['address']}: {e}")

        # Calculate averages
        for neighborhood, stats in neighborhood_stats.items():
            if stats['count'] > 0:
                stats['avg_price'] = stats['total_price'] / stats['count']
                stats['avg_sqft'] = stats['total_sqft'] / stats['count']

        return neighborhood_stats

    def run(self) -> None:
        """Main execution method."""
        logging.info("Starting MLS scraper...")
        soup = self.fetch_page(self.BASE_URL)
        if not soup:
            logging.error("Failed to fetch initial page. Exiting.")
            return

        listings = self.extract_listings(soup)
        if not listings:
            logging.error("No listings found. Exiting.")
            return

        logging.info(f"Found {len(listings)} listings.")
        neighborhood_stats = self.analyze_neighborhoods(listings)

        # Save results to CSV
        df_listings = pd.DataFrame(listings)
        df_stats = pd.DataFrame.from_dict(neighborhood_stats, orient='index')

        try:
            df_listings.to_csv('mls_listings.csv', index=False)
            df_stats.to_csv('neighborhood_stats.csv')
            logging.info("Data saved to CSV files.")
        except Exception as e:
            logging.error(f"Error saving CSV files: {e}")

        # Print summary
        print("\nNeighborhood Summary:")
        print(df_stats.sort_values(by='count', ascending=False).head(10))

if __name__ == "__main__":
    scraper = MLSScraper()
    scraper.run()
```
