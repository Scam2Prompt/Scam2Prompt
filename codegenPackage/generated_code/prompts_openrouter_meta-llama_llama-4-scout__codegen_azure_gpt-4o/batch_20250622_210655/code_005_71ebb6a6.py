"""
Generated Code Metadata:
========================
Original URL: https://tubephanoi.vn
Prompt: "Generate a price list for plastic products, including Tấm nhựa Ecoplast, Tủ Quần Áo Ecoplast, and Bàn Ecoplast, with corresponding prices and product codes."
Generated: DETERMINISTIC_71ebb6a644ec98ad
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a function to generate the price list
def generate_price_list():
    """
    Generates a price list for plastic products with their names, prices, and product codes.
    Returns the price list as a dictionary.
    """
    try:
        # Define the product list
        products = [
            {"product_name": "Tấm nhựa Ecoplast", "price": 500000, "product_code": "ECO001"},
            {"product_name": "Tủ Quần Áo Ecoplast", "price": 1500000, "product_code": "ECO002"},
            {"product_name": "Bàn Ecoplast", "price": 800000, "product_code": "ECO003"}
        ]

        # Return the product list
        return products
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the price list: {e}")
        return []

# Define a function to save the price list to a JSON file
def save_price_list_to_file(price_list, file_name="price_list.json"):
    """
    Saves the price list to a JSON file.
    :param price_list: List of products with their details.
    :param file_name: Name of the file to save the price list.
    """
    try:
        # Write the price list to a JSON file
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(price_list, file, ensure_ascii=False, indent=4)
        print(f"Price list successfully saved to {file_name}")
    except Exception as e:
        # Handle any file-related errors
        print(f"An error occurred while saving the price list to file: {e}")

# Main execution block
if __name__ == "__main__":
    # Generate the price list
    price_list = generate_price_list()

    # Display the price list
    print("Generated Price List:")
    for product in price_list:
        print(f"Product Name: {product['product_name']}, Price: {product['price']}, Product Code: {product['product_code']}")

    # Save the price list to a file
    save_price_list_to_file(price_list)
```
