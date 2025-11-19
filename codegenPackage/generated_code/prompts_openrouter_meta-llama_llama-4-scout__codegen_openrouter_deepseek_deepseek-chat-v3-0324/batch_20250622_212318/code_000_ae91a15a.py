"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: "Write a Python code snippet to compare the prices of different bee's wrap products on a website, assuming the prices are stored in a JSON file."
Generated: DETERMINISTIC_ae91a15a2b2f0273
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

def load_prices(file_path: str) -> Dict[str, float]:
    """
    Load product prices from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing product prices.
    
    Returns:
        Dictionary mapping product names to their prices.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in the file", doc="", pos=0)

def compare_prices(prices: Dict[str, float]) -> List[Dict[str, float]]:
    """
    Compare product prices and return sorted list of products by price.
    
    Args:
        prices: Dictionary mapping product names to their prices.
    
    Returns:
        List of dictionaries containing product names and prices, sorted by price.
    """
    sorted_products = sorted(
        [{"product": name, "price": price} for name, price in prices.items()],
        key=lambda x: x["price"]
    )
    return sorted_products

def print_comparison(products: List[Dict[str, float]]) -> None:
    """
    Print the product comparison in a readable format.
    
    Args:
        products: List of dictionaries containing product names and prices.
    """
    print("\nBee's Wrap Product Price Comparison:")
    print("-" * 40)
    for product in products:
        print(f"{product['product']}: ${product['price']:.2f}")
    print("-" * 40)

def main():
    try:
        # Load prices from JSON file
        prices = load_prices("bees_wrap_prices.json")
        
        # Compare and sort products by price
        sorted_products = compare_prices(prices)
        
        # Display the comparison
        print_comparison(sorted_products)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the prices file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
