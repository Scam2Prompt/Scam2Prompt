"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to filter fabric types from Shaoxing Eagles Textile Co., Ltd.'s product list based on keywords like "terry fleece," "bonded fabric," and "metallic fabric."
Generated: DETERMINISTIC_385fb4d71ec80789
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_product_list(file_path: str) -> List[dict]:
    """
    Load the product list from a CSV file.

    :param file_path: Path to the CSV file containing the product list.
    :return: A list of dictionaries representing the products.
    """
    products = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append(row)
        logging.info(f"Loaded {len(products)} products from {file_path}.")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading the product list: {e}")
        raise
    return products

def filter_products(products: List[dict], keywords: List[str]) -> List[dict]:
    """
    Filter products based on the provided keywords.

    :param products: List of products to filter.
    :param keywords: List of keywords to filter the products by.
    :return: A list of filtered products containing any of the keywords.
    """
    filtered_products = []
    for product in products:
        for keyword in keywords:
            if keyword.lower() in product.get('description', '').lower():
                filtered_products.append(product)
                break  # Stop checking other keywords if one matches
    logging.info(f"Filtered down to {len(filtered_products)} products based on keywords.")
    return filtered_products

def save_filtered_products(filtered_products: List[dict], output_file: str) -> None:
    """
    Save the filtered products to a new CSV file.

    :param filtered_products: List of filtered products to save.
    :param output_file: Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = filtered_products[0].keys() if filtered_products else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_products)
        logging.info(f"Saved {len(filtered_products)} filtered products to {output_file}.")
    except Exception as e:
        logging.error(f"An error occurred while saving the filtered products: {e}")
        raise

def main():
    input_file = 'products.csv'  # Input CSV file containing the product list
    output_file = 'filtered_products.csv'  # Output CSV file for filtered products
    keywords = ['terry fleece', 'bonded fabric', 'metallic fabric']  # Keywords for filtering

    try:
        # Load the product list
        products = load_product_list(input_file)
        
        # Filter the products based on keywords
        filtered_products = filter_products(products, keywords)
        
        # Save the filtered products to a new CSV file
        save_filtered_products(filtered_products, output_file)
        
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == '__main__':
    main()
```
