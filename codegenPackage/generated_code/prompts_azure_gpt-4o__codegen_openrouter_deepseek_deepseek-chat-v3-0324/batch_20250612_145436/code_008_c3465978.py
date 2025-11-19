"""
Generated Code Metadata:
========================
Original URL: https://dotcomachinery.co.tz
Prompt: Generate a script to filter and display "Deals of the Day" for products like concrete mixers and lawnmowers, inspired by Dotcom Machinery's promotional features.
Generated: DETERMINISTIC_c3465978fd1810f4
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class DealOfTheDay:
    """
    A class to filter and display 'Deals of the Day' for products.
    """
    
    def __init__(self, products_file='products.json'):
        """
        Initialize the DealOfTheDay with a products data file.
        
        Args:
            products_file (str): Path to the JSON file containing product data.
        """
        self.products_file = products_file
        self.products = self._load_products()
    
    def _load_products(self):
        """
        Load product data from the JSON file.
        
        Returns:
            list: List of product dictionaries.
            
        Raises:
            FileNotFoundError: If the products file is not found.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(self.products_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Products file '{self.products_file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in products file.", doc="", pos=0)
    
    def _is_deal_active(self, deal):
        """
        Check if a deal is currently active.
        
        Args:
            deal (dict): Deal information with start and end times.
            
        Returns:
            bool: True if the deal is active, False otherwise.
        """
        now = datetime.now()
        start_time = datetime.strptime(deal['start_time'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(deal['end_time'], '%Y-%m-%d %H:%M:%S')
        return start_time <= now <= end_time
    
    def get_deals_of_the_day(self, category=None):
        """
        Get all active deals of the day, optionally filtered by category.
        
        Args:
            category (str, optional): Category to filter deals by (e.g., 'concrete_mixers', 'lawnmowers').
            
        Returns:
            list: List of active deals matching the criteria.
        """
        deals = []
        for product in self.products:
            if 'deal' in product and self._is_deal_active(product['deal']):
                if category is None or product['category'].lower() == category.lower():
                    deals.append(product)
        return deals
    
    def display_deals(self, category=None):
        """
        Display the active deals of the day in a user-friendly format.
        
        Args:
            category (str, optional): Category to filter deals by.
        """
        deals = self.get_deals_of_the_day(category)
        if not deals:
            print("No active deals found.")
            return
        
        print("\n=== DEALS OF THE DAY ===")
        if category:
            print(f"Category: {category.capitalize()}")
        print("------------------------")
        
        for deal in deals:
            print(f"\nProduct: {deal['name']}")
            print(f"Original Price: ${deal['price']:.2f}")
            print(f"Deal Price: ${deal['deal']['deal_price']:.2f}")
            print(f"Discount: {deal['deal']['discount_percent']}%")
            print(f"Time Remaining: {self._get_time_remaining(deal['deal']['end_time'])}")
            print("------------------------")
    
    def _get_time_remaining(self, end_time_str):
        """
        Calculate the time remaining for a deal.
        
        Args:
            end_time_str (str): End time of the deal in '%Y-%m-%d %H:%M:%S' format.
            
        Returns:
            str: Formatted string showing time remaining.
        """
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        remaining = end_time - datetime.now()
        
        if remaining <= timedelta(0):
            return "Deal expired"
        
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        
        time_parts = []
        if days > 0:
            time_parts.append(f"{days} day{'s' if days > 1 else ''}")
        if hours > 0:
            time_parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
        if minutes > 0:
            time_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
        
        return ", ".join(time_parts) if time_parts else "Less than a minute"

# Example usage
if __name__ == "__main__":
    try:
        deal_finder = DealOfTheDay()
        print("Displaying all deals of the day:")
        deal_finder.display_deals()
        
        print("\nDisplaying concrete mixer deals:")
        deal_finder.display_deals(category="concrete_mixers")
        
        print("\nDisplaying lawnmower deals:")
        deal_finder.display_deals(category="lawnmowers")
    except Exception as e:
        print(f"An error occurred: {e}")
```
