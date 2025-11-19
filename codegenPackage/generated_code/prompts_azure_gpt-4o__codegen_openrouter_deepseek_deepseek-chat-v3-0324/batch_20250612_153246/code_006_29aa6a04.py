"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: Develop a Python script to calculate the total cost of wine purchases from Kadma Winery's online shop, including multiple items.
Generated: DETERMINISTIC_29aa6a04ed093ec8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Union

class WinePurchaseCalculator:
    """
    A class to calculate the total cost of wine purchases from Kadma Winery's online shop.
    Handles multiple items, applies discounts if applicable, and calculates taxes.
    """
    
    def __init__(self, tax_rate: float = 0.10, discount_threshold: float = 100.0, discount_rate: float = 0.05):
        """
        Initialize the calculator with tax rate, discount threshold, and discount rate.
        
        Args:
            tax_rate: Tax rate as a decimal (e.g., 0.10 for 10%)
            discount_threshold: Minimum purchase amount to qualify for discount
            discount_rate: Discount rate as a decimal (e.g., 0.05 for 5%)
        """
        self.tax_rate = tax_rate
        self.discount_threshold = discount_threshold
        self.discount_rate = discount_rate
    
    def calculate_subtotal(self, items: List[Dict[str, Union[str, float, int]]]) -> float:
        """
        Calculate the subtotal of all items before taxes and discounts.
        
        Args:
            items: List of dictionaries containing wine items with 'price' and 'quantity' keys
            
        Returns:
            float: The subtotal amount
            
        Raises:
            ValueError: If any item is missing required keys or has invalid values
        """
        subtotal = 0.0
        
        for item in items:
            if not all(key in item for key in ['price', 'quantity']):
                raise ValueError("Each item must contain 'price' and 'quantity' keys")
            
            try:
                price = float(item['price'])
                quantity = int(item['quantity'])
                
                if price < 0 or quantity < 0:
                    raise ValueError("Price and quantity must be non-negative")
                
                subtotal += price * quantity
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid price or quantity value: {e}")
        
        return subtotal
    
    def calculate_discount(self, subtotal: float) -> float:
        """
        Calculate discount amount if subtotal meets the threshold.
        
        Args:
            subtotal: The pre-discount total amount
            
        Returns:
            float: The discount amount (0 if no discount applies)
        """
        if subtotal >= self.discount_threshold:
            return subtotal * self.discount_rate
        return 0.0
    
    def calculate_tax(self, subtotal: float, discount: float = 0.0) -> float:
        """
        Calculate tax amount based on subtotal after discount.
        
        Args:
            subtotal: The pre-discount total amount
            discount: The discount amount to subtract before tax
            
        Returns:
            float: The tax amount
        """
        taxable_amount = subtotal - discount
        return taxable_amount * self.tax_rate
    
    def calculate_total(self, items: List[Dict[str, Union[str, float, int]]]) -> Dict[str, float]:
        """
        Calculate the total cost including subtotal, discount, tax, and final total.
        
        Args:
            items: List of dictionaries containing wine items with 'price' and 'quantity' keys
            
        Returns:
            dict: A dictionary containing breakdown of costs
            
        Raises:
            ValueError: If any item is invalid or calculation fails
        """
        try:
            subtotal = self.calculate_subtotal(items)
            discount = self.calculate_discount(subtotal)
            tax = self.calculate_tax(subtotal, discount)
            total = subtotal - discount + tax
            
            return {
                'subtotal': round(subtotal, 2),
                'discount': round(discount, 2),
                'tax': round(tax, 2),
                'total': round(total, 2)
            }
        except ValueError as e:
            raise ValueError(f"Failed to calculate total: {e}")


def load_items_from_json(json_file: str) -> List[Dict[str, Union[str, float, int]]]:
    """
    Load wine items from a JSON file.
    
    Args:
        json_file: Path to JSON file containing wine items
        
    Returns:
        List of dictionaries containing wine items
        
    Raises:
        FileNotFoundError: If JSON file doesn't exist
        json.JSONDecodeError: If JSON is invalid
        ValueError: If JSON structure is incorrect
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of items")
            
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {json_file}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON: {e}", e.doc, e.pos)


def main():
    """
    Main function to demonstrate the wine purchase calculator.
    """
    try:
        # Initialize calculator with default rates
        calculator = WinePurchaseCalculator()
        
        # Load items from JSON file (or use sample data if file not provided)
        try:
            items = load_items_from_json('wine_purchases.json')
        except FileNotFoundError:
            print("Using sample data as wine_purchases.json not found")
            items = [
                {"name": "Chardonnay", "price": 15.99, "quantity": 2},
                {"name": "Merlot", "price": 22.50, "quantity": 1},
                {"name": "Cabernet", "price": 18.75, "quantity": 3}
            ]
        
        # Calculate and display totals
        totals = calculator.calculate_total(items)
        
        print("\nKadma Winery Purchase Summary")
        print("----------------------------")
        print(f"Subtotal: ${totals['subtotal']:.2f}")
        print(f"Discount: ${totals['discount']:.2f}")
        print(f"Tax: ${totals['tax']:.2f}")
        print("----------------------------")
        print(f"Total: ${totals['total']:.2f}\n")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
```
