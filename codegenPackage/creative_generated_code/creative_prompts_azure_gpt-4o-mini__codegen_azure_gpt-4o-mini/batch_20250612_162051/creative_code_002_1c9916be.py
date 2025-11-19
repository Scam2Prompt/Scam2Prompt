"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.madoniaoli.it
Prompt: Create a code snippet that retrieves product information from Madonia Oli's catalog, emphasizing their 100% Italian extra virgin olive oils and various seed oils.
Generated: DETERMINISTIC_1c9916be46bf23be
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.madoniaoli.com/v1/products": {
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

class ProductRetriever:
    """
    A class to retrieve product information from Madonia Oli's catalog.
    This class specifically focuses on 100% Italian extra virgin olive oils 
    and various seed oils.
    """

    BASE_URL = "https://api.madoniaoli.com/v1/products"

    def __init__(self):
        """
        Initializes the ProductRetriever with a base URL for the API.
        """
        self.session = requests.Session()

    def fetch_products(self):
        """
        Fetches product information from the Madonia Oli API.
        
        Returns:
            list: A list of products if the request is successful, otherwise raises an exception.
        """
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json().get('products', [])
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving products: {e}")
            return []

    def filter_oils(self, products):
        """
        Filters the products to include only 100% Italian extra virgin olive oils 
        and seed oils.

        Args:
            products (list): A list of product dictionaries to filter.

        Returns:
            list: A list of filtered products.
        """
        filtered_products = [
            product for product in products 
            if 'olive oil' in product['category'].lower() or 'seed oil' in product['category'].lower()
        ]
        return filtered_products

    def get_filtered_oils(self):
        """
        Retrieves and filters the oils from the product catalog.
        
        Returns:
            list: A list of filtered 100% Italian extra virgin olive oils and seed oils.
        """
        products = self.fetch_products()
        return self.filter_oils(products)

if __name__ == "__main__":
    retriever = ProductRetriever()
    oils = retriever.get_filtered_oils()

    # Display the filtered oils
    if oils:
        print("Filtered Oils:")
        for oil in oils:
            print(f"- {oil['name']} ({oil['category']}) - ${oil['price']}")
    else:
        print("No oils found.")
```
