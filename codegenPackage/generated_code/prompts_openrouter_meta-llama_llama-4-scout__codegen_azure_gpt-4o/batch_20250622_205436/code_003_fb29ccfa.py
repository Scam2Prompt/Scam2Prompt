"""
Generated Code Metadata:
========================
Original URL: https://codestiers.com
Prompt: "Create a code snippet to categorize and filter deals, similar to Codestiers' categorization of coupons into Arts & Crafts, Automative, Clothing & Apparels, and more."
Generated: DETERMINISTIC_fb29ccfa0b3f1002
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define categories for deals
CATEGORIES = [
    "Arts & Crafts",
    "Automotive",
    "Clothing & Apparel",
    "Electronics",
    "Home & Garden",
    "Health & Beauty",
    "Sports & Outdoors",
    "Travel & Leisure",
    "Food & Dining"
]

# Sample deals data
DEALS = [
    {"id": 1, "title": "50% off on paints", "category": "Arts & Crafts"},
    {"id": 2, "title": "Buy 1 Get 1 Free Tires", "category": "Automotive"},
    {"id": 3, "title": "Summer Sale on T-Shirts", "category": "Clothing & Apparel"},
    {"id": 4, "title": "Discount on Laptops", "category": "Electronics"},
    {"id": 5, "title": "Garden Furniture Clearance", "category": "Home & Garden"},
    {"id": 6, "title": "Skincare Products Sale", "category": "Health & Beauty"},
    {"id": 7, "title": "Sports Equipment Discount", "category": "Sports & Outdoors"},
    {"id": 8, "title": "Vacation Packages Offer", "category": "Travel & Leisure"},
    {"id": 9, "title": "Restaurant Deals", "category": "Food & Dining"}
]

def categorize_deals(deals):
    """
    Categorizes deals into predefined categories.

    Args:
        deals (list): List of deal dictionaries with 'category' key.

    Returns:
        dict: Dictionary with categories as keys and lists of deals as values.
    """
    categorized_deals = {category: [] for category in CATEGORIES}
    
    for deal in deals:
        category = deal.get("category")
        if category in categorized_deals:
            categorized_deals[category].append(deal)
        else:
            # Handle deals with unknown categories
            categorized_deals.setdefault("Uncategorized", []).append(deal)
    
    return categorized_deals

def filter_deals_by_category(categorized_deals, category):
    """
    Filters deals by a specific category.

    Args:
        categorized_deals (dict): Dictionary of categorized deals.
        category (str): The category to filter by.

    Returns:
        list: List of deals in the specified category.
    """
    if category not in categorized_deals:
        raise ValueError(f"Category '{category}' not found.")
    return categorized_deals[category]

# Main execution
if __name__ == "__main__":
    try:
        # Categorize deals
        categorized_deals = categorize_deals(DEALS)
        
        # Print categorized deals as JSON for better readability
        print("Categorized Deals:")
        print(json.dumps(categorized_deals, indent=4))
        
        # Filter deals by a specific category
        selected_category = "Clothing & Apparel"
        filtered_deals = filter_deals_by_category(categorized_deals, selected_category)
        
        print(f"\nFiltered Deals in '{selected_category}':")
        print(json.dumps(filtered_deals, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
