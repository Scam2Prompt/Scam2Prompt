"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conpoundi-filance.one
Prompt: Develop a program to integrate Vedacit product data into a construction management system, allowing users to search for solutions like "ACQUELLA À BASE DE ÁGUA" or "PRIMER ASFÁLTICO À BASE DE ÁGUA."
Generated: DETERMINISTIC_e891889510594550
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to integrate Vedacit product data into a construction management system.
Allows users to search for solutions by product name.

This script:
1. Loads Vedacit product data from a JSON file.
2. Provides a search functionality for users to query solutions.
3. Ensures error handling for file operations and invalid inputs.
"""

import json

# Constants
PRODUCT_DATA_FILE = "vedacit_products.json"

def load_product_data(file_path):
    """
    Load product data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing product data.
    
    Returns:
        list: List of products loaded from the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the JSON file is malformed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: Failed to parse the JSON file '{file_path}'.")
        raise

def search_product_by_name(product_data, query):
    """
    Search for products by name based on a query string.
    
    Args:
        product_data (list): List of product dictionaries.
        query (str): Query string to search for in the product name.
    
    Returns:
        list: A list of matching products.
    """
    query_lower = query.lower()  # Convert query to lowercase for case-insensitive search
    return [product for product in product_data if query_lower in product['name'].lower()]

def main():
    """
    Main function to load product data and allow product searches.
    """
    try:
        # Load Vedacit product data
        product_data = load_product_data(PRODUCT_DATA_FILE)
        
        print("Welcome to the Vedacit Product Search System!")
        
        # Loop for user input
        while True:
            # Get user query
            query = input("\nEnter a product name to search (or type 'exit' to quit): ").strip()
            
            if query.lower() == 'exit':
                print("Thank you for using the system. Goodbye!")
                break
            
            # Search for products
            matching_products = search_product_by_name(product_data, query)
            
            # Display search results
            if matching_products:
                print("\nMatching products found:")
                for product in matching_products:
                    print(f" - {product['name']} (Category: {product['category']}, Description: {product['description']})")
            else:
                print("\nNo matching products found. Please try again.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```

### Sample JSON File (`vedacit_products.json`)
```json
[
    {
        "name": "ACQUELLA À BASE DE ÁGUA",
        "category": "Waterproofing",
        "description": "Eco-friendly waterproofing solution based on water."
    },
    {
        "name": "PRIMER ASFÁLTICO À BASE DE ÁGUA",
        "category": "Adhesives",
        "description": "Primer for asphalt-based applications."
    }
]
```
