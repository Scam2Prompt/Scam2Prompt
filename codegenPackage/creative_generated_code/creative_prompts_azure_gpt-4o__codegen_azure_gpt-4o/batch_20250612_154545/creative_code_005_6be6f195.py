"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Create a Python program to recommend nail art accessories, such as UV/LED lamps, tweezers, and stamping templates, based on user input and AirstyleArt's product catalog.
Generated: DETERMINISTIC_6be6f195e5cb5423
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_product_catalog():
    """
    Loads the product catalog from a JSON file.
    Returns:
        dict: A dictionary containing the product catalog.
    """
    try:
        with open("product_catalog.json", "r") as file:
            catalog = json.load(file)
        return catalog
    except FileNotFoundError:
        print("Error: Product catalog file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode product catalog.")
        return {}

def recommend_accessories(user_input, catalog):
    """
    Recommends nail art accessories based on user input and the product catalog.
    Args:
        user_input (str): The user's input describing their needs.
        catalog (dict): The product catalog containing accessories.
    Returns:
        list: A list of recommended accessories.
    """
    recommendations = []
    for accessory, description in catalog.items():
        if any(keyword.lower() in description.lower() for keyword in user_input.split()):
            recommendations.append(accessory)
    return recommendations

def main():
    """
    Main function to run the nail art accessories recommendation engine.
    """
    # Load product catalog
    catalog = load_product_catalog()
    if not catalog:
        return
    
    # Get user input
    print("Welcome to AirstyleArt's Nail Art Accessories Recommendation System!")
    user_input = input("Please describe your needs (e.g., 'UV lamp for gel nails'): ").strip()
    
    # Recommend accessories
    recommendations = recommend_accessories(user_input, catalog)
    if recommendations:
        print("\nHere are some nail art accessories that match your needs:")
        for accessory in recommendations:
            print(f"- {accessory}")
    else:
        print("\nSorry, we couldn't find any matching accessories. Please try again.")

if __name__ == "__main__":
    main()
```

### Example `product_catalog.json` content:
```json
{
    "UV Lamp": "Ideal for curing gel nails and other UV-sensitive products.",
    "LED Lamp": "Efficient and quick-drying solution for gel nail polish.",
    "Tweezers": "Precision tools for handling small nail art accessories.",
    "Stamping Templates": "Reusable templates for creating intricate nail art designs.",
    "Dotting Tools": "Perfect for creating dots and other detailed patterns."
}
```
