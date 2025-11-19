"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Write a Python script to create a simple interior design advisor chatbot that suggests products and decor ideas based on user input, using a dataset of products from websites like origines-decoration.com."
Generated: DETERMINISTIC_f4bf7870b5eab19b
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

# Sample dataset of products and decor ideas (this would ideally be loaded from a file or API)
PRODUCTS_DATA = [
    {"category": "furniture", "name": "Modern Sofa", "price": 1200, "style": "modern"},
    {"category": "furniture", "name": "Vintage Armchair", "price": 800, "style": "vintage"},
    {"category": "decor", "name": "Abstract Wall Art", "price": 150, "style": "modern"},
    {"category": "decor", "name": "Rustic Table Lamp", "price": 100, "style": "rustic"},
    {"category": "decor", "name": "Bohemian Rug", "price": 300, "style": "bohemian"},
    {"category": "furniture", "name": "Minimalist Coffee Table", "price": 400, "style": "minimalist"},
]

def load_products():
    """
    Load product data. In a real-world scenario, this would fetch data from an external source.
    Here, we use a predefined dataset for simplicity.
    """
    return PRODUCTS_DATA

def suggest_products(style_preference, category=None):
    """
    Suggest products based on user preferences.
    
    Args:
        style_preference (str): The preferred style (e.g., 'modern', 'vintage').
        category (str, optional): The category of products (e.g., 'furniture', 'decor').
    
    Returns:
        list: A list of suggested products matching the criteria.
    """
    products = load_products()
    suggestions = [
        product for product in products
        if product["style"].lower() == style_preference.lower() and
           (category is None or product["category"].lower() == category.lower())
    ]
    return suggestions

def chatbot():
    """
    Main function to run the interior design advisor chatbot.
    """
    print("Welcome to the Interior Design Advisor Chatbot!")
    print("I can help you find products and decor ideas based on your preferences.")
    
    try:
        # Get user input for style preference
        style_preference = input("What is your preferred style? (e.g., modern, vintage, rustic, bohemian): ").strip()
        if not style_preference:
            raise ValueError("Style preference cannot be empty.")
        
        # Get user input for category preference
        category_preference = input("Do you have a specific category in mind? (e.g., furniture, decor, or leave blank): ").strip()
        category_preference = category_preference if category_preference else None
        
        # Suggest products based on user input
        suggestions = suggest_products(style_preference, category_preference)
        
        if suggestions:
            print("\nHere are some suggestions for you:")
            for product in suggestions:
                print(f"- {product['name']} ({product['category']}, ${product['price']})")
        else:
            print("\nSorry, no products match your preferences. Try adjusting your criteria.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Interior Design Advisor Chatbot!")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
