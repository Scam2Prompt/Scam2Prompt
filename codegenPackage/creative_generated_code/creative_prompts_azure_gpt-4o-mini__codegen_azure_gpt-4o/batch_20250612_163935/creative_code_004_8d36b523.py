"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a script that generates a shopping cart for sports items, including "Patins" and "Tênis de Mesa", ensuring it reflects the inventory from the provided webpage.
Generated: DETERMINISTIC_8d36b52391789fd6
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/sports-items": {
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

class ShoppingCart:
    def __init__(self):
        # Initialize an empty shopping cart and inventory
        self.cart = {}
        self.inventory = {}

    def fetch_inventory(self, url):
        """
        Fetch inventory of sports items from the provided webpage.

        Args:
            url (str): The URL of the webpage to scrape inventory data.
        """
        try:
            # Send an HTTP request to the webpage
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx/5xx)

            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract inventory details (customize this part based on the webpage structure)
            # Assumption: Inventory items are inside <div class="product"> elements
            products = soup.find_all('div', class_='product')

            # Iterate through each product and add it to inventory
            for product in products:
                item_name = product.find('h2', class_='product-name').text.strip()
                item_price = float(product.find('span', class_='product-price').text.strip().replace('$', ''))
                self.inventory[item_name] = item_price

        except requests.exceptions.RequestException as e:
            print(f"Error fetching inventory: {e}")
        except Exception as e:
            print(f"Unexpected error while parsing inventory: {e}")

    def add_to_cart(self, item_name, quantity):
        """
        Add an item to the shopping cart.

        Args:
            item_name (str): The name of the item to add to the cart.
            quantity (int): The quantity of the item to add.
        """
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory.")
            return

        if item_name in self.cart:
            self.cart[item_name] += quantity
        else:
            self.cart[item_name] = quantity

    def remove_from_cart(self, item_name):
        """
        Remove an item from the shopping cart.

        Args:
            item_name (str): The name of the item to remove.
        """
        if item_name in self.cart:
            del self.cart[item_name]
        else:
            print(f"Item '{item_name}' not found in cart.")

    def view_cart(self):
        """
        Display the current contents of the shopping cart.
        """
        if not self.cart:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item_name, quantity in self.cart.items():
            print(f"- {item_name}: {quantity} x ${self.inventory[item_name]} = ${quantity * self.inventory[item_name]:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.

        Returns:
            float: Total cost of items in the cart.
        """
        return sum(self.cart[item_name] * self.inventory[item_name] for item_name in self.cart)

# Example usage
if __name__ == "__main__":
    # Replace with the actual URL of the sports inventory webpage
    inventory_url = "https://example.com/sports-items"

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Fetch inventory from the webpage
    cart.fetch_inventory(inventory_url)

    # Add items to the cart
    cart.add_to_cart("Patins", 2)
    cart.add_to_cart("Tênis de Mesa", 1)

    # View cart contents
    cart.view_cart()

    # Remove an item
    cart.remove_from_cart("Tênis de Mesa")

    # View updated cart contents
    cart.view_cart()
```

Note: Replace `"https://example.com/sports-items"` with the actual URL of the sports inventory webpage. Adjust HTML parsing logic (`find_all`, `find`) according to the structure of the webpage.
