"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write a script to analyze customer preferences for products like high-visibility gloves, fire-resistant gloves, and impact gloves, based on Rising Star International's product descriptions.
Generated: DETERMINISTIC_1abdc4c05a2482bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import Counter

def analyze_customer_preferences(product_descriptions):
    """
    Analyze customer preferences based on product descriptions.

    Args:
        product_descriptions (list): List of product descriptions (strings).

    Returns:
        dict: A dictionary containing counts of each product category.
    """

    # Define product categories and their keywords
    categories = {
        "high-visibility gloves": ["high-visibility", "visibility", "bright", "reflective"],
        "fire-resistant gloves": ["fire-resistant", "heat-resistant", "flameproof", "fireproof"],
        "impact gloves": ["impact", "shock-resistant", "durable", "reinforced"]
    }

    # Initialize a counter for category preferences
    preference_counter = Counter()

    # Analyze each product description
    for description in product_descriptions:
        description_lower = description.lower()
        for category, keywords in categories.items():
            if any(keyword in description_lower for keyword in keywords):
                preference_counter[category] += 1

    return dict(preference_counter)


def load_product_descriptions(file_path):
    """
    Load product descriptions from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing product descriptions.

    Returns:
        list: List of product descriptions (strings).
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('product_descriptions', [])
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return []


def main():
    """
    Main function to run the customer preference analysis.
    """
    # Path to the JSON file containing product descriptions
    file_path = "product_descriptions.json"

    # Load product descriptions
    product_descriptions = load_product_descriptions(file_path)

    if not product_descriptions:
        print("No product descriptions found. Exiting...")
        return

    # Analyze customer preferences
    preferences = analyze_customer_preferences(product_descriptions)

    # Print the results
    print("Customer Preferences Analysis:")
    for category, count in preferences.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
```
