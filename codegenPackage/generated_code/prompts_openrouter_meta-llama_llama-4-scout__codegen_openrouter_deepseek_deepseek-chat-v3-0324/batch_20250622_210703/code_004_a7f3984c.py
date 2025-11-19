"""
Generated Code Metadata:
========================
Original URL: https://cuadroenvios.com.ar
Prompt: Create a list of product categories for Cuadro Envíos, including "Cuadros Corpóreos", "Cuadros Impresos", and "Escudos de Fútbol", with their corresponding product examples.
Generated: DETERMINISTIC_a7f3984cf6554886
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Product categories for Cuadro Envíos with example products.
"""

from typing import List, Dict

def get_product_categories() -> List[Dict[str, str]]:
    """
    Returns a list of product categories with example products for Cuadro Envíos.
    
    Returns:
        List[Dict[str, str]]: List of dictionaries containing category names and examples
    """
    categories = [
        {
            "category_name": "Cuadros Corpóreos",
            "examples": [
                "Cuadro corpóreo de madera",
                "Cuadro corpóreo de metal",
                "Cuadro corpóreo personalizado"
            ]
        },
        {
            "category_name": "Cuadros Impresos",
            "examples": [
                "Cuadro impreso en lienzo",
                "Cuadro impreso en acrílico",
                "Cuadro impreso fotográfico"
            ]
        },
        {
            "category_name": "Escudos de Fútbol",
            "examples": [
                "Escudo de fútbol de club",
                "Escudo de fútbol de selección",
                "Escudo de fútbol personalizado"
            ]
        }
    ]
    
    return categories

if __name__ == "__main__":
    # Example usage
    categories = get_product_categories()
    for category in categories:
        print(f"\nCategoría: {category['category_name']}")
        print("Ejemplos:")
        for example in category['examples']:
            print(f"- {example}")
```
