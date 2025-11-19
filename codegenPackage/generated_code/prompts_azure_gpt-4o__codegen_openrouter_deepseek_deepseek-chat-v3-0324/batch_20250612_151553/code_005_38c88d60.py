"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Write a script to automate the comparison of prices for products like "کابل دو سر تایپ سی LDNIO مدل LC442C" and "هندزفری سیمی سامسونگ مدل J8" from the website's product listings.
Generated: DETERMINISTIC_38c88d60309447bf
Batch ID: 20250612_151553
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
import re
import json
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    url: str

class PriceComparator:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def _fetch_page(self, url: str) -> Optional[str]:
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def _parse_price(self, price_str: str) -> float:
        # Extract digits from price string (handles Persian/Arabic numerals)
        digits = re.sub(r'[^\d]', '', price_str)
        return float(digits) if digits else 0.0

    def search_product(self, product_name: str) -> List[Product]:
        search_url = f"{self.base_url}/search?q={product_name}"
        page_content = self._fetch_page(search_url)
        if not page_content:
            return []

        soup = BeautifulSoup(page_content, 'html.parser')
        products = []

        # Example selector - adjust based on actual website structure
        product_items = soup.select('.product-item')  # Update this selector
        
        for item in product_items:
            try:
                name = item.select_one('.product-name').text.strip()  # Update selector
                price_str = item.select_one('.price').text.strip()    # Update selector
                price = self._parse_price(price_str)
                url = item.find('a')['href']
                
                if not url.startswith('http'):
                    url = f"{self.base_url}{url}"
                
                products.append(Product(name=name, price=price, url=url))
            except (AttributeError, KeyError) as e:
                print(f"Error parsing product: {e}")
                continue

        return products

    def compare_prices(self, product_names: List[str]) -> Dict[str, List[Product]]:
        results = {}
        for name in product_names:
            products = self.search_product(name)
            if products:
                results[name] = sorted(products, key=lambda x: x.price)
        return results

    def save_results(self, results: Dict[str, List[Product]], filename: str = 'price_comparison.json'):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    name: [{'name': p.name, 'price': p.price, 'url': p.url} for p in products]
                    for name, products in results.items()
                }, f, ensure_ascii=False, indent=2)
            print(f"Results saved to {filename}")
        except IOError as e:
            print(f"Error saving results: {e}")

if __name__ == "__main__":
    # Example usage - replace with actual website URL
    comparator = PriceComparator(base_url="https://example.com")
    
    products_to_compare = [
        "کابل دو سر تایپ سی LDNIO مدل LC442C",
        "هندزفری سیمی سامسونگ مدل J8"
    ]
    
    results = comparator.compare_prices(products_to_compare)
    
    # Print results
    for product_name, products in results.items():
        print(f"\nProduct: {product_name}")
        for idx, product in enumerate(products, 1):
            print(f"{idx}. {product.name} - {product.price:,} - {product.url}")
    
    # Save results to file
    comparator.save_results(results)
```
