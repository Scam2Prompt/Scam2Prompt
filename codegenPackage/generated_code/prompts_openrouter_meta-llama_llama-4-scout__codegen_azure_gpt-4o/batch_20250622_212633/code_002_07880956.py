"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Generate a list of product recommendations for a customer who buys a "Caderno Inteligente Felicity By Alexity A5" and a "Caneta Crown Metal Belíssima Esferográfica Prata", considering related products from the Art Pel catalog.
Generated: DETERMINISTIC_07880956b1b9d388
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Mock catalog data for Art Pel products
ART_PEL_CATALOG = [
    {"id": 1, "name": "Caderno Inteligente Felicity By Alexity A5", "category": "Stationery"},
    {"id": 2, "name": "Caneta Crown Metal Belíssima Esferográfica Prata", "category": "Stationery"},
    {"id": 3, "name": "Caderno Inteligente Classic A5", "category": "Stationery"},
    {"id": 4, "name": "Caneta Crown Metal Premium Esferográfica Dourada", "category": "Stationery"},
    {"id": 5, "name": "Estojo Organizador de Canetas e Lápis", "category": "Accessories"},
    {"id": 6, "name": "Marcadores de Texto Pastel Pack 6 Cores", "category": "Stationery"},
    {"id": 7, "name": "Bloco de Notas Adesivas Coloridas", "category": "Stationery"},
    {"id": 8, "name": "Planner Semanal Minimalista", "category": "Stationery"},
]

def get_related_products(purchased_products, catalog):
    """
    Generate a list of related product recommendations based on the purchased products.
    
    Args:
        purchased_products (list): List of product names purchased by the customer.
        catalog (list): List of all products in the catalog.
    
    Returns:
        list: List of recommended products.
    """
    try:
        # Extract categories of purchased products
        purchased_categories = set(
            product["category"] for product in catalog if product["name"] in purchased_products
        )
        
        # Find related products in the same categories
        recommendations = [
            product for product in catalog
            if product["category"] in purchased_categories and product["name"] not in purchased_products
        ]
        
        return recommendations
    except Exception as e:
        # Log the error and return an empty list
        print(f"Error generating recommendations: {e}")
        return []

def main():
    # Products purchased by the customer
    purchased_products = [
        "Caderno Inteligente Felicity By Alexity A5",
        "Caneta Crown Metal Belíssima Esferográfica Prata"
    ]
    
    # Generate recommendations
    recommendations = get_related_products(purchased_products, ART_PEL_CATALOG)
    
    # Print recommendations in a user-friendly format
    print("Recommended Products:")
    for product in recommendations:
        print(f"- {product['name']} (Category: {product['category']})")

if __name__ == "__main__":
    main()
```
