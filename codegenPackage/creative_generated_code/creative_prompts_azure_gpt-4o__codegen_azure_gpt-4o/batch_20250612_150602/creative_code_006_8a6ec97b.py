"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Provide a Python script to generate multilingual product descriptions for cleaning tools, referencing PDC Brush's support for NL, FR, EN, and DE languages.
Generated: DETERMINISTIC_8a6ec97be648626f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict

# Define a dictionary holding translations for product descriptions
translations = {
    "cleaning_brush": {
        "en": "A high-quality cleaning brush for all surfaces.",
        "nl": "Een hoogwaardige schoonmaakborstel voor alle oppervlakken.",
        "fr": "Une brosse de nettoyage de haute qualité pour toutes les surfaces.",
        "de": "Eine hochwertige Reinigungsbürste für alle Oberflächen."
    },
    "dust_pan": {
        "en": "A durable dustpan for efficient cleaning.",
        "nl": "Een duurzame stofblik voor efficiënt schoonmaken.",
        "fr": "Une pelle à poussière durable pour un nettoyage efficace.",
        "de": "Ein haltbares Kehrblech für effizientes Reinigen."
    }
}

def generate_description(product_key: str, language_code: str) -> str:
    """
    Generate a multilingual product description based on the product key and language code.

    Args:
        product_key (str): The key of the product (e.g., 'cleaning_brush').
        language_code (str): The language code (e.g., 'en', 'nl', 'fr', 'de').

    Returns:
        str: The product description in the requested language.
    
    Raises:
        ValueError: If the product key or language code is invalid.
    """
    # Validate product key
    if product_key not in translations:
        raise ValueError(f"Invalid product key: {product_key}. Supported keys: {list(translations.keys())}")

    # Validate language code
    if language_code not in translations[product_key]:
        raise ValueError(f"Invalid language code: {language_code}. Supported codes: {list(translations[product_key].keys())}")

    # Return the description in the requested language
    return translations[product_key][language_code]

def main():
    """
    Main driver function to generate multilingual product descriptions.
    """
    try:
        # Example products and language codes
        products = ["cleaning_brush", "dust_pan"]
        languages = ["en", "nl", "fr", "de"]

        # Store results
        generated_descriptions: Dict[str, Dict[str, str]] = {}

        # Generate descriptions for all combinations of products and languages
        for product in products:
            generated_descriptions[product] = {}
            for lang in languages:
                description = generate_description(product, lang)
                generated_descriptions[product][lang] = description

        # Output generated descriptions as a JSON string
        print(json.dumps(generated_descriptions, indent=4, ensure_ascii=False))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
