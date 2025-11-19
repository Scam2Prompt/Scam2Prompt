"""
Generated Code Metadata:
========================
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Generate a list of potential product categories and subcategories for an e-commerce website featuring French gourmet foods, including Foie Gras, duck confit, and Périgord specialties.
Generated: DETERMINISTIC_e1a5d1a13cba9090
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_french_gourmet_categories():
    """
    Generates a hierarchical list of product categories and subcategories
    for a French gourmet food e-commerce website.
    
    Returns:
        dict: A nested dictionary of categories and subcategories
    """
    categories = {
        "Foie Gras": {
            "Duck Foie Gras": ["Whole Foie Gras", "Foie Gras Terrine", "Foie Gras Mousse"],
            "Goose Foie Gras": ["Whole Foie Gras", "Foie Gras Terrine", "Foie Gras Mousse"],
            "Prepared Foie Gras": ["Seared Foie Gras", "Foie Gras Pâté", "Foie Gras Torchon"]
        },
        "Duck Products": {
            "Duck Confit": ["Whole Duck Leg Confit", "Duck Confit Pieces", "Duck Confit Rillettes"],
            "Duck Magret": ["Fresh Duck Magret", "Smoked Duck Magret", "Duck Magret Fillets"],
            "Duck Fat": ["Pure Duck Fat", "Duck Fat with Herbs", "Duck Fat in Jar"]
        },
        "Périgord Specialties": {
            "Truffles": ["Black Truffles", "Summer Truffles", "Truffle Products"],
            "Périgord Pâtés": ["Duck Pâté", "Pork and Duck Pâté", "Game Pâté"],
            "Walnut Products": ["Walnut Oil", "Walnut Cake", "Candied Walnuts"]
        },
        "Cheeses": {
            "Soft Cheeses": ["Brie", "Camembert", "Chèvre"],
            "Blue Cheeses": ["Roquefort", "Bleu d'Auvergne", "Fourme d'Ambert"],
            "Hard Cheeses": ["Comté", "Beaufort", "Cantal"]
        },
        "Charcuterie": {
            "Saucisson": ["Rosette", "Saucisson Sec", "Jésus"],
            "Pâtés": ["Country Pâté", "Pork Pâté", "Game Pâté"],
            "Rillettes": ["Pork Rillettes", "Duck Rillettes", "Goose Rillettes"]
        },
        "Pantry Staples": {
            "Mustards": ["Dijon Mustard", "Whole Grain Mustard", "Honey Mustard"],
            "Olive Oils": ["Extra Virgin", "Flavored Olive Oils", "Truffle Olive Oil"],
            "Vinegars": ["Balsamic Vinegar", "Red Wine Vinegar", "Sherry Vinegar"]
        },
        "Sweet Delicacies": {
            "Macarons": ["Classic Flavors", "Seasonal Flavors", "Gift Boxes"],
            "Chocolates": ["Truffles", "Bars", "Pralines"],
            "Confitures": ["Berry Jams", "Stone Fruit Jams", "Specialty Jams"]
        },
        "Wines & Spirits": {
            "Bordeaux Wines": ["Red", "White", "Rosé"],
            "Cognac & Armagnac": ["VS", "VSOP", "XO"],
            "French Liqueurs": ["Crème de Cassis", "Grand Marnier", "Chartreuse"]
        }
    }
    
    return categories


def print_categories_hierarchy(categories, indent=0):
    """
    Prints the category hierarchy in a readable format.
    
    Args:
        categories (dict): The categories dictionary
        indent (int): Current indentation level
    """
    for category, subcategories in categories.items():
        print(" " * indent + f"- {category}")
        if isinstance(subcategories, dict):
            print_categories_hierarchy(subcategories, indent + 2)
        elif isinstance(subcategories, list):
            for item in subcategories:
                print(" " * (indent + 2) + f"- {item}")


if __name__ == "__main__":
    categories = generate_french_gourmet_categories()
    print("French Gourmet Food Categories:")
    print_categories_hierarchy(categories)
```
