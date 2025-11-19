"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: "Generate a list of product categories and subcategories for an e-commerce website like Weavely, which sells ethnic clothing, sarees, and suits."
Generated: DETERMINISTIC_882b9fc422b6b9a7
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

def generate_product_categories() -> List[Dict[str, List[str]]]:
    """
    Generates a hierarchical list of product categories and subcategories for an ethnic clothing e-commerce site.
    
    Returns:
        List of dictionaries where each dictionary represents a main category
        with its subcategories as a list.
    """
    categories = [
        {
            "name": "Sarees",
            "subcategories": [
                "Silk Sarees",
                "Cotton Sarees",
                "Banarasi Sarees",
                "Chiffon Sarees",
                "Georgette Sarees",
                "Printed Sarees",
                "Embroidered Sarees",
                "Designer Sarees",
                "Bollywood Style Sarees",
                "Wedding Sarees"
            ]
        },
        {
            "name": "Suits",
            "subcategories": [
                "Salwar Kameez",
                "Anarkali Suits",
                "Patiala Suits",
                "Churidar Suits",
                "Palazzo Suits",
                "Sharara Suits",
                "Designer Suits",
                "Casual Suits",
                "Party Wear Suits",
                "Wedding Suits"
            ]
        },
        {
            "name": "Lehengas",
            "subcategories": [
                "Bridal Lehengas",
                "Designer Lehengas",
                "Party Wear Lehengas",
                "Printed Lehengas",
                "Embroidered Lehengas",
                "Net Lehengas",
                "Silk Lehengas",
                "Georgette Lehengas",
                "Wedding Lehengas",
                "Casual Lehengas"
            ]
        },
        {
            "name": "Kurtis",
            "subcategories": [
                "Cotton Kurtis",
                "Silk Kurtis",
                "Printed Kurtis",
                "Embroidered Kurtis",
                "Designer Kurtis",
                "Long Kurtis",
                "Short Kurtis",
                "Anarkali Kurtis",
                "Casual Kurtis",
                "Party Wear Kurtis"
            ]
        },
        {
            "name": "Dupattas",
            "subcategories": [
                "Silk Dupattas",
                "Cotton Dupattas",
                "Printed Dupattas",
                "Embroidered Dupattas",
                "Net Dupattas",
                "Designer Dupattas",
                "Bridal Dupattas",
                "Party Wear Dupattas",
                "Casual Dupattas",
                "Wedding Dupattas"
            ]
        },
        {
            "name": "Accessories",
            "subcategories": [
                "Jewelry",
                "Handbags",
                "Footwear",
                "Hair Accessories",
                "Stoles",
                "Belts",
                "Bangles",
                "Earrings",
                "Necklaces",
                "Rings"
            ]
        }
    ]
    
    return categories

if __name__ == "__main__":
    # Example usage
    product_categories = generate_product_categories()
    for category in product_categories:
        print(f"Category: {category['name']}")
        for subcategory in category["subcategories"]:
            print(f" - {subcategory}")
        print()
```
