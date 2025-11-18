"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Create a function that lists all products offered by "Гарант," such as adhesives, primers, and cleaning materials for automotive glass installation, and formats them for display on a website.
Generated: DETERMINISTIC_da44454e85a42637
Batch ID: 20250612_154617
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

def list_garant_products():
    """
    Function to fetch and format products offered by 'Гарант' for display on a website.
    Returns a JSON-formatted string containing the product list.
    """
    try:
        # Define the list of products offered by 'Гарант'
        products = [
            {"name": "Adhesive", "description": "High-strength adhesive for automotive glass installation."},
            {"name": "Primer", "description": "Special primer for improving adhesion to glass surfaces."},
            {"name": "Cleaning Material", "description": "Effective cleaning solutions for glass preparation."}
        ]

        # Format the products into a JSON string for website display
        formatted_products = json.dumps(
            {"products": products},
            indent=4,
            ensure_ascii=False  # Ensure proper encoding for non-ASCII characters like 'Гарант'
        )

        return formatted_products

    except Exception as e:
        # Handle unexpected errors gracefully
        error_message = json.dumps(
            {"error": f"An error occurred while retrieving product data: {str(e)}"},
            indent=4,
            ensure_ascii=False
        )
        return error_message


# Example usage (would generally be called by the web server or API endpoint)
if __name__ == "__main__":
    # Print the formatted products for testing purposes
    print(list_garant_products())
```
