"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Develop a code snippet that sorts clothing items by popularity and price, inspired by the sorting options available on Danda Loja's website.
Generated: DETERMINISTIC_f6fe81abbd05e0f9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a function to sort clothing items by popularity and price
def sort_clothing_items(items: List[Dict], sort_by: str) -> List[Dict]:
    """
    Sorts a list of clothing items based on the specified criteria.

    Parameters:
        items (List[Dict]): A list of dictionaries where each dictionary represents a clothing item.
                            Each item should have 'popularity' (int) and 'price' (float) keys.
        sort_by (str): The sorting criteria. Acceptable values are 'popularity' or 'price'.

    Returns:
        List[Dict]: A sorted list of clothing items.
    """
    # Validate input
    if sort_by not in ['popularity', 'price']:
        raise ValueError("Invalid sort_by value. Use 'popularity' or 'price'.")
    
    # Sort items based on the specified criteria
    # For popularity, sort in descending order (higher popularity first)
    # For price, sort in ascending order (lower price first)
    reverse = True if sort_by == 'popularity' else False
    sorted_items = sorted(items, key=lambda item: item[sort_by], reverse=reverse)
    
    return sorted_items

# Example usage
if __name__ == "__main__":
    # Sample clothing items
    clothing_items = [
        {"name": "T-shirt", "popularity": 85, "price": 19.99},
        {"name": "Jeans", "popularity": 95, "price": 49.99},
        {"name": "Jacket", "popularity": 75, "price": 89.99},
        {"name": "Sneakers", "popularity": 90, "price": 69.99},
    ]
    
    try:
        # Sort by popularity
        sorted_by_popularity = sort_clothing_items(clothing_items, "popularity")
        print("Sorted by popularity:")
        for item in sorted_by_popularity:
            print(item)
        
        # Sort by price
        sorted_by_price = sort_clothing_items(clothing_items, "price")
        print("\nSorted by price:")
        for item in sorted_by_price:
            print(item)
    except ValueError as e:
        print(f"Error: {e}")
```
