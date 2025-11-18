"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Write Python code to interact with an e-commerce API for retrieving a list of available speakers and their prices. Assume the API provides endpoints for product categories like "speakers," "microphones," and "headphones."
Generated: DETERMINISTIC_cc8c3f7e85a21f3c
Batch ID: 20250612_154927
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/products": {
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

class EcommerceAPI:
    """
    A class to interact with the e-commerce API for retrieving product information.
    """

    BASE_URL = "https://api.example.com/products"  # Replace with the actual API base URL

    def __init__(self):
        """
        Initializes the EcommerceAPI class.
        """
        pass

    def fetch_products(self, category):
        """
        Fetches a list of products from the specified category.

        Parameters:
            category (str): The category of products to retrieve (e.g., 'speakers').

        Returns:
            list: A list of products in the specified category.

        Raises:
            ValueError: If the category is invalid.
            requests.HTTPError: If the API request fails.
        """
        valid_categories = ['speakers', 'microphones', 'headphones']
        if category not in valid_categories:
            raise ValueError(f"Invalid category. Valid categories are: {valid_categories}")

        url = f"{self.BASE_URL}/{category}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            raise requests.HTTPError(f"Failed to retrieve products: {e}")

def main():
    """
    Main function to demonstrate fetching speakers from the e-commerce API.
    """
    api = EcommerceAPI()
    
    try:
        category = "speakers"
        speakers = api.fetch_products(category)
        
        # Display the list of speakers and their prices
        print("Available Speakers:")
        for speaker in speakers:
            name = speaker.get("name", "Unknown")
            price = speaker.get("price", "N/A")
            print(f"- {name}: ${price:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except requests.HTTPError as he:
        print(f"Error: {he}")

if __name__ == "__main__":
    main()
```
