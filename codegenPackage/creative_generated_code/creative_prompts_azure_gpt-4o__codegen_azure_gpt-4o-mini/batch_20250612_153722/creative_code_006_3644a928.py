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
class ProductNotFoundError(Exception):
    """Custom exception to be raised when no products are found."""
    pass

def display_error_message(products):
    """
    Displays a custom error message if no products are found.

    Args:
        products (list): A list of products to check.

    Raises:
        ProductNotFoundError: If the products list is empty.
    """
    try:
        if not products:  # Check if the products list is empty
            raise ProductNotFoundError("No products found. Please check back later or browse other categories.")
        else:
            # Code to display products could go here
            print("Products found:", products)

    except ProductNotFoundError as e:
        # Display the custom error message
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Test with an empty list of products
    products = []
    display_error_message(products)

    # Test with a non-empty list of products
    products = ["Course 1", "Course 2"]
    display_error_message(products)
```
