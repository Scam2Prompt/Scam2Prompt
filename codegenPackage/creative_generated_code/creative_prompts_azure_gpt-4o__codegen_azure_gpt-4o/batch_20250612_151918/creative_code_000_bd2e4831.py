"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write Python code to recommend a zero-waste cosmetic product based on user preferences for vegan and eco-friendly ingredients, referencing the product categories from CMQLF.
Generated: DETERMINISTIC_bd2e48314832faab
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Sample database of zero-waste cosmetic products (CMQLF categories referenced)
PRODUCTS = [
    {
        "name": "Eco-Friendly Shampoo Bar",
        "category": "Hair Care",
        "vegan": True,
        "eco_friendly": True
    },
    {
        "name": "Natural Lip Balm",
        "category": "Lip Care",
        "vegan": False,
        "eco_friendly": True
    },
    {
        "name": "Vegan Moisturizer Cream",
        "category": "Skin Care",
        "vegan": True,
        "eco_friendly": False
    },
    {
        "name": "Zero-Waste Deodorant",
        "category": "Body Care",
        "vegan": True,
        "eco_friendly": True
    }
]

def recommend_product(preferences):
    """
    Recommend a zero-waste cosmetic product based on user preferences.

    Args:
        preferences (dict): A dictionary containing user preferences for vegan and eco-friendly products,
                            e.g., {"vegan": True, "eco_friendly": True}

    Returns:
        list: A list of recommended products matching the preferences.
    """
    # Validate user preferences
    if "vegan" not in preferences or "eco_friendly" not in preferences:
        raise ValueError("Preferences must include 'vegan' and 'eco_friendly' keys.")

    # Filter products based on preferences
    recommended_products = [
        product for product in PRODUCTS
        if product["vegan"] == preferences["vegan"] and product["eco_friendly"] == preferences["eco_friendly"]
    ]

    return recommended_products


def main():
    """
    Main function to interact with the user and recommend products.
    """
    print("Welcome to the Zero-Waste Cosmetic Product Recommendation System!")
    
    # Gather user preferences
    try:
        vegan_preference = input("Do you prefer vegan products? (yes/no): ").strip().lower()
        eco_friendly_preference = input("Do you prefer eco-friendly products? (yes/no): ").strip().lower()

        # Convert user inputs to boolean values
        preferences = {
            "vegan": vegan_preference == "yes",
            "eco_friendly": eco_friendly_preference == "yes"
        }

        # Recommend products
        recommendations = recommend_product(preferences)

        # Display recommendations
        if recommendations:
            print("\nRecommended Products:")
            print(json.dumps(recommendations, indent=4))
        else:
            print("\nSorry, no products match your preferences.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
