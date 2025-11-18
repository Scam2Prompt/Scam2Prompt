"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write a function to calculate the effectiveness of disinfectant products in reducing bacterial infections in poultry farming buildings, based on the homologated products mentioned on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_4c28a7e36379765c
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/disinfectants": {
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

class DisinfectantEffectivenessCalculator:
    def __init__(self, url):
        """
        Initializes the DisinfectantEffectivenessCalculator with the provided URL.
        
        :param url: str - The URL of the website containing disinfectant product information.
        """
        self.url = url
        self.products = self.fetch_products()

    def fetch_products(self):
        """
        Fetches homologated disinfectant products from the specified URL.
        
        :return: list - A list of disinfectant products and their effectiveness.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            products = []
            # Example parsing logic; this needs to match the actual HTML structure of the webpage
            for item in soup.find_all('div', class_='product-info'):
                name = item.find('h2').text.strip()
                effectiveness = float(item.find('span', class_='effectiveness').text.strip().replace('%', ''))
                products.append({'name': name, 'effectiveness': effectiveness})
            
            return products
        except requests.exceptions.RequestException as e:
            print(f"Error fetching product data: {e}")
            return []

    def calculate_average_effectiveness(self):
        """
        Calculates the average effectiveness of the disinfectant products.
        
        :return: float - The average effectiveness of the homologated disinfectants.
        """
        if not self.products:
            print("No products available for calculation.")
            return 0.0

        total_effectiveness = sum(product['effectiveness'] for product in self.products)
        average_effectiveness = total_effectiveness / len(self.products)
        return average_effectiveness

    def display_effectiveness(self):
        """
        Displays the effectiveness of each disinfectant product and the average effectiveness.
        """
        if not self.products:
            print("No products available to display.")
            return
        
        print("Disinfectant Products Effectiveness:")
        for product in self.products:
            print(f"{product['name']}: {product['effectiveness']}%")

        avg_effectiveness = self.calculate_average_effectiveness()
        print(f"Average Effectiveness: {avg_effectiveness:.2f}%")

# URL of the disinfectant products page (example, replace with the actual URL)
url = "https://example.com/disinfectants"
calculator = DisinfectantEffectivenessCalculator(url)
calculator.display_effectiveness()
```
