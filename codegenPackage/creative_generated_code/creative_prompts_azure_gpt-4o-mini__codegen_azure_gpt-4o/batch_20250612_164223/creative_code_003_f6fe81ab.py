"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Develop a code snippet that sorts clothing items by popularity and price, inspired by the sorting options available on Danda Loja's website.
Generated: DETERMINISTIC_f6fe81abbd05e0f9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define a function to sort clothing items by popularity and price
def sort_clothing_items(items: List[Dict], sort_by: str = "popularity") -> List[Dict]:
    """
    Sorts a list of clothing items by popularity or price.
    
    Args:
        items (List[Dict]): List of clothing items where each item is a dictionary 
                            containing 'name', 'popularity', and 'price' fields.
        sort_by (str): Criteria to sort by - 'popularity' or 'price'. Defaults to 'popularity'.
        
    Returns:
        List[Dict]: Sorted list of clothing items.
    """
    # Validate input
    if sort_by not in ["popularity", "price"]:
        raise ValueError("Invalid sort_by value. Choose 'popularity' or 'price'.")
    
    if not all(isinstance(item, dict) and 'name' in item and 'popularity' in item and 'price' in item for item in items):
        raise ValueError("Each clothing item must be a dictionary with 'name', 'popularity', and 'price' fields.")
    
    # Perform the sorting based on the given criteria
    sorted_items = sorted(items, key=lambda x: x[sort_by], reverse=True)
    
    return sorted_items

# Example usage
if __name__ == "__main__":
    # Sample data: List of clothing items
    clothing_items = [
        {"name": "T-shirt", "popularity": 80, "price": 20.0},
        {"name": "Jeans", "popularity": 95, "price": 50.0},
        {"name": "Jacket", "popularity": 70, "price": 100.0},
        {"name": "Sweater", "popularity": 85, "price": 40.0}
    ]
    
    # Sort by popularity
    print("Sorted by popularity:")
    sorted_by_popularity = sort_clothing_items(clothing_items, sort_by="popularity")
    for item in sorted_by_popularity:
        print(item)
    
    # Sort by price
    print("\nSorted by price:")
    sorted_by_price = sort_clothing_items(clothing_items, sort_by="price")
    for item in sorted_by_price:
        print(item)
```
