"""
Generated Code Metadata:
========================
Original URL: https://billesveikals.lv
Prompt: "Generate a list of product categories and subcategories for a kids' online store, inspired by the structure of billesveikals.lv."
Generated: DETERMINISTIC_45869bbdbe970b71
Batch ID: 20250622_210316
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

def generate_product_categories() -> List[Dict[str, List[str]]]:
    """
    Generate a hierarchical list of product categories and subcategories for a kids' online store.
    
    Returns:
        List[Dict[str, List[str]]]: A list of dictionaries where each key is a main category
        and the value is a list of subcategories.
    """
    
    categories = [
        {
            "Clothing": [
                "Boys' Clothing",
                "Girls' Clothing",
                "Baby Clothing",
                "Outerwear",
                "Underwear & Socks",
                "Swimwear",
                "Accessories"
            ]
        },
        {
            "Footwear": [
                "Boys' Shoes",
                "Girls' Shoes",
                "Baby Shoes",
                "Sports Shoes",
                "Boots",
                "Sandals"
            ]
        },
        {
            "Toys & Games": [
                "Educational Toys",
                "Outdoor Toys",
                "Board Games",
                "Dolls & Accessories",
                "Action Figures",
                "Puzzles",
                "Building Blocks"
            ]
        },
        {
            "Baby Products": [
                "Nursery Furniture",
                "Feeding & Nursing",
                "Baby Safety",
                "Diapering",
                "Strollers & Carriers",
                "Baby Care"
            ]
        },
        {
            "School Supplies": [
                "Backpacks",
                "Stationery",
                "Lunch Boxes",
                "Art Supplies",
                "School Uniforms",
                "Calculators"
            ]
        },
        {
            "Sports & Outdoor": [
                "Bicycles & Accessories",
                "Team Sports",
                "Skates & Skateboards",
                "Camping Gear",
                "Swimming Gear",
                "Winter Sports"
            ]
        },
        {
            "Books & Media": [
                "Children's Books",
                "Educational Books",
                "Audio Books",
                "DVDs & Movies",
                "Music",
                "Magazines"
            ]
        },
        {
            "Party & Celebration": [
                "Party Decorations",
                "Costumes",
                "Invitations",
                "Party Favors",
                "Cake Toppers",
                "Balloons"
            ]
        }
    ]
    
    return categories

def print_categories(categories: List[Dict[str, List[str]]]) -> None:
    """
    Print the categories and subcategories in a readable format.
    
    Args:
        categories (List[Dict[str, List[str]]]): The list of categories to print.
    """
    for category_dict in categories:
        for main_category, subcategories in category_dict.items():
            print(f"\n{main_category}:")
            for subcategory in subcategories:
                print(f"  - {subcategory}")

if __name__ == "__main__":
    try:
        categories = generate_product_categories()
        print_categories(categories)
    except Exception as e:
        print(f"An error occurred while generating categories: {e}")
```
