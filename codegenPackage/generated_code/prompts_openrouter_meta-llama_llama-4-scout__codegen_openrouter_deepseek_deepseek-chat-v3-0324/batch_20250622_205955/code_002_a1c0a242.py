"""
Generated Code Metadata:
========================
Original URL: https://loli.bg
Prompt: Generate a list of product categories and subcategories for a children's clothing online store, inspired by the categories found on loli.bg.
Generated: DETERMINISTIC_a1c0a24256a2c14e
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# childrens_clothing_categories.py

def generate_categories():
    """
    Generates a hierarchical structure of product categories and subcategories
    for a children's clothing online store.
    
    Returns:
        dict: Nested dictionary representing the category hierarchy
    """
    categories = {
        "Clothing": {
            "Boys": {
                "T-Shirts": [],
                "Shirts": [],
                "Pants": ["Jeans", "Sweatpants", "Cargo Pants"],
                "Shorts": [],
                "Jackets": ["Winter Jackets", "Spring Jackets", "Raincoats"],
                "Sweaters": [],
                "Underwear": ["Briefs", "Boxers", "Socks"],
                "Pajamas": [],
                "Swimwear": [],
                "Suits": ["Formal", "Casual"]
            },
            "Girls": {
                "Dresses": ["Casual", "Party", "Summer"],
                "T-Shirts": [],
                "Blouses": [],
                "Skirts": ["Mini", "Midi", "Long"],
                "Pants": ["Jeans", "Leggings", "Sweatpants"],
                "Shorts": [],
                "Jackets": ["Winter Jackets", "Spring Jackets", "Raincoats"],
                "Sweaters": [],
                "Underwear": ["Panties", "Socks", "Tights"],
                "Pajamas": [],
                "Swimwear": ["One-piece", "Bikinis", "Swimsuits"],
                "Suits": ["Formal", "Casual"]
            },
            "Babies": {
                "Bodysuits": [],
                "Rompers": [],
                "Onesies": [],
                "Sleepwear": ["Sleepsuits", "Sleeping Bags"],
                "Outerwear": ["Jackets", "Snowsuits"],
                "Accessories": ["Bibs", "Hats", "Mittens"]
            },
            "Unisex": {
                "Hoodies": [],
                "Sweatshirts": [],
                "Tracksuits": [],
                "T-Shirts": [],
                "Pants": ["Jeans", "Sweatpants"],
                "Shorts": []
            }
        },
        "Shoes": {
            "Boys": ["Sneakers", "Sandals", "Boots", "Dress Shoes"],
            "Girls": ["Sneakers", "Sandals", "Boots", "Ballet Flats"],
            "Babies": ["First Walkers", "Soft Sole", "Booties"],
            "Unisex": ["Sneakers", "Sandals", "Rain Boots"]
        },
        "Accessories": {
            "Hats": ["Caps", "Beanies", "Sun Hats"],
            "Bags": ["Backpacks", "Purses", "Lunch Bags"],
            "Jewelry": ["Necklaces", "Bracelets", "Hair Accessories"],
            "Belts": [],
            "Scarves": [],
            "Gloves": []
        },
        "Seasonal": {
            "Winter": ["Winter Coats", "Thermal Wear", "Winter Accessories"],
            "Summer": ["Sun Hats", "Sunglasses", "Light Clothing"],
            "School": ["Uniforms", "School Bags", "School Shoes"],
            "Holiday": ["Christmas Outfits", "Easter Dresses", "Costumes"]
        },
        "Toys": {
            "Soft Toys": [],
            "Educational": ["Puzzles", "Building Blocks"],
            "Outdoor": ["Balls", "Ride-Ons"],
            "Dolls": []
        }
    }
    
    return categories

if __name__ == "__main__":
    # Example usage
    categories = generate_categories()
    print("Children's Clothing Categories:")
    for main_category, subcategories in categories.items():
        print(f"\n{main_category}:")
        for subcategory, items in subcategories.items():
            if items:
                print(f"  - {subcategory}: {', '.join(items) if isinstance(items, list) else ', '.join(items.keys())}")
            else:
                print(f"  - {subcategory}")
```
