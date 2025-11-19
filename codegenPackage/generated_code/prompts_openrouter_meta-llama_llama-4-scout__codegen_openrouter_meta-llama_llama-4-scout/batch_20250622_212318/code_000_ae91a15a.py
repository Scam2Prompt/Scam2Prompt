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

def load_prices_from_json(file_path):
    """
    Loads bee's wrap product prices from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: A dictionary containing product names as keys and prices as values.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return {}

def compare_prices(prices):
    """
    Compares the prices of different bee's wrap products.

    Args:
        prices (dict): A dictionary containing product names as keys and prices as values.

    Returns:
        tuple: A tuple containing the cheapest product and its price.
    """
    if not prices:
        return None, None

    cheapest_product = min(prices, key=prices.get)
    return cheapest_product, prices[cheapest_product]

def main():
    json_file_path = 'bee_wrap_prices.json'  # replace with your JSON file path
    prices = load_prices_from_json(json_file_path)
    cheapest_product, cheapest_price = compare_prices(prices)

    if cheapest_product:
        print(f"Cheapest product: {cheapest_product} (${cheapest_price:.2f})")
    else:
        print("No products found.")

if __name__ == "__main__":
    main()
```

Example JSON file (`bee_wrap_prices.json`):
```json
{
    "Bee's Wrap - Small": 4.99,
    "Bee's Wrap - Medium": 6.99,
    "Bee's Wrap - Large": 8.99,
    "Bee's Wrap - Set of 3": 19.99
}
```
