"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Provide a Python script to generate multilingual product descriptions for cleaning tools, referencing PDC Brush's support for NL, FR, EN, and DE languages.
Generated: DETERMINISTIC_8a6ec97be648626f
Batch ID: 20250612_150602
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
Multilingual Product Description Generator for Cleaning Tools

This script generates product descriptions for cleaning tools in multiple languages.
It supports Dutch (NL), French (FR), English (EN), and German (DE) languages.

Author: [Your Name]
Date: [Today's Date]
"""

import json

# Define a dictionary with product description templates for each language
product_description_templates = {
    "NL": {
        "title": "Reinigingsborstel voor {product_name}",
        "description": "Onze {product_name} is ideaal voor het reinigen van {application_area}. "
                       "De borstel is gemaakt van hoogwaardige materialen en is zeer effectief in het "
                       "verwijderen van vuil en stof."
    },
    "FR": {
        "title": "Brosse de nettoyage pour {product_name}",
        "description": "Notre {product_name} est parfait pour nettoyer les {application_area}. "
                       "La brosse est fabriquée à partir de matériaux de haute qualité et est très "
                       "efficace pour éliminer la saleté et la poussière."
    },
    "EN": {
        "title": "Cleaning Brush for {product_name}",
        "description": "Our {product_name} is ideal for cleaning {application_area}. "
                       "The brush is made from high-quality materials and is very effective at "
                       "removing dirt and dust."
    },
    "DE": {
        "title": "Reinigungsbürste für {product_name}",
        "description": "Unsere {product_name} ist ideal für die Reinigung von {application_area}. "
                       "Die Bürste besteht aus hochwertigen Materialien und ist sehr effektiv bei der "
                       "Entfernung von Schmutz und Staub."
    }
}

def generate_product_description(language, product_name, application_area):
    """
    Generate a product description for a cleaning tool in a specific language.

    Args:
        language (str): The language code (NL, FR, EN, or DE).
        product_name (str): The name of the product.
        application_area (str): The area where the product is used.

    Returns:
        dict: A dictionary containing the title and description of the product.

    Raises:
        ValueError: If the language code is not supported.
    """
    if language not in product_description_templates:
        raise ValueError(f"Unsupported language code: {language}")

    template = product_description_templates[language]
    return {
        "title": template["title"].format(product_name=product_name),
        "description": template["description"].format(product_name=product_name, application_area=application_area)
    }

def main():
    # Example usage:
    product_name = "PDC Brush"
    application_area = " delicate surfaces"

    languages = ["NL", "FR", "EN", "DE"]

    for language in languages:
        try:
            description = generate_product_description(language, product_name, application_area)
            print(f"Language: {language}")
            print(f"Title: {description['title']}")
            print(f"Description: {description['description']}\n")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
