"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Develop a code snippet that lists all the plastic products offered by Samba Plastic Industries, categorizing them into furniture, houseware, and planters.
Generated: DETERMINISTIC_6d2ef4526f7bd306
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define a function to get the list of plastic products offered by Samba Plastic Industries
def get_plastic_products():
    """
    Returns a dictionary categorizing plastic products offered by Samba Plastic Industries
    into furniture, houseware, and planters.

    Returns:
        dict: A dictionary where keys are categories and values are lists of products.
    """
    try:
        # Static data of products categorized
        products = {
            "furniture": ["Plastic Chair", "Plastic Table", "Plastic Cabinet"],
            "houseware": ["Plastic Bucket", "Plastic Storage Box", "Plastic Laundry Basket"],
            "planters": ["Plastic Flower Pot", "Plastic Hanging Planter", "Plastic Garden Bed"]
        }

        return products
    except Exception as e:
        # Proper error handling in case of unexpected issues
        print(f"An error occurred while retrieving the products: {e}")
        return {}

# Main function to demonstrate the functionality
def main():
    """
    Main execution function to list and display the categorized plastic products.
    """
    try:
        # Fetching products
        categorized_products = get_plastic_products()

        # Printing the products in a user-friendly format
        print("Samba Plastic Industries - Product Categories:")
        for category, items in categorized_products.items():
            print(f"\n{category.capitalize()}:")
            for item in items:
                print(f"- {item}")

        # Optionally, output the data as JSON (for integration or future use)
        print("\nProducts as JSON:")
        print(json.dumps(categorized_products, indent=4))

    except Exception as e:
        # Handle any unexpected error during the execution
        print(f"An error occurred in the main function: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
