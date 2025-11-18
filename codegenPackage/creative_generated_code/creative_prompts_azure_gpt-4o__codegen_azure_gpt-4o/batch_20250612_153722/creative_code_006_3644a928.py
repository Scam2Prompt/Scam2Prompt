"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Write a function to display a custom error message when no products are found on an online course platform, similar to rbby-wollet.
Generated: DETERMINISTIC_3644a92842985d74
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def display_error_message(products):
    """
    Function to display a custom error message when no products are found.
    
    Args:
        products (list): A list of product objects or names.

    Returns:
        None
    """
    try:
        # Check if the products list is empty
        if not products:
            # Log a warning indicating no products are found
            logging.warning("No products found on the platform.")
            
            # Print a custom user-friendly error message
            print("⚠️ No courses are available currently. Please check back later.")
        else:
            # Inform that products are available
            logging.info(f"Found {len(products)} products.")
            print(f"We found {len(products)} courses available for you!")
    except Exception as e:
        # Handle unexpected errors gracefully
        logging.error(f"An unexpected error occurred: {str(e)}")
        print("An unexpected error occurred. Please try again later.")

# Example usage
if __name__ == "__main__":
    # Test with an empty product list
    empty_products = []
    display_error_message(empty_products)

    # Test with some products
    available_products = ["Python Essentials", "Advanced JavaScript", "Data Science Bootcamp"]
    display_error_message(available_products)
```
