"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: "Develop a chatbot that provides recommendations for sustainable living products, including bee's wrap, based on user input and preferences."
Generated: DETERMINISTIC_f2be6aa72372f2df
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class SustainableProductRecommender:
    """
    A chatbot that recommends sustainable living products based on user preferences.
    """
    
    def __init__(self):
        self.products = self._load_products()
        self.user_preferences = {}
        
    def _load_products(self) -> Dict[str, List[Dict]]:
        """
        Load product data from a JSON file.
        """
        try:
            with open('products.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: Product database not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid product database format.")
            return {}
    
    def get_product_categories(self) -> List[str]:
        """
        Return available product categories.
        """
        return list(self.products.keys())
    
    def set_user_preferences(self, preferences: Dict[str, str]) -> None:
        """
        Set user preferences for recommendations.
        """
        self.user_preferences = preferences
    
    def recommend_products(self, category: Optional[str] = None) -> List[Dict]:
        """
        Recommend products based on user preferences and optional category filter.
        """
        recommendations = []
        
        # Filter by category if specified
        categories = [category] if category else self.get_product_categories()
        
        for cat in categories:
            if cat not in self.products:
                continue
                
            for product in self.products[cat]:
                # Basic matching - in a real app, this would be more sophisticated
                matches = True
                for pref_key, pref_value in self.user_preferences.items():
                    if pref_key in product and product[pref_key] != pref_value:
                        matches = False
                        break
                
                if matches:
                    recommendations.append(product)
        
        return recommendations
    
    def chat(self) -> None:
        """
        Interactive chat interface for the recommender.
        """
        print("Welcome to the Sustainable Living Product Recommender!")
        print("I can help you find eco-friendly products like beeswax wraps.")
        
        # Collect basic preferences
        preferences = {}
        print("\nLet's start with some preferences:")
        preferences['material'] = input("Do you prefer organic materials? (yes/no): ").lower()
        preferences['price_range'] = input("Price range (low/medium/high): ").lower()
        
        self.set_user_preferences(preferences)
        
        # Show available categories
        print("\nAvailable product categories:")
        categories = self.get_product_categories()
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        # Get category choice
        while True:
            try:
                choice = input("\nEnter a category number or 'all' for all products: ")
                if choice.lower() == 'all':
                    selected_category = None
                    break
                else:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(categories):
                        selected_category = categories[choice_num - 1]
                        break
                    else:
                        print("Please enter a valid number.")
            except ValueError:
                print("Please enter a number or 'all'.")
        
        # Get recommendations
        recommendations = self.recommend_products(selected_category)
        
        # Display results
        if not recommendations:
            print("\nNo products match your preferences.")
        else:
            print("\nHere are some recommendations:")
            for product in recommendations:
                print(f"\nName: {product['name']}")
                print(f"Category: {product['category']}")
                print(f"Description: {product['description']}")
                print(f"Price: {product['price']}")
                if 'material' in product:
                    print(f"Material: {product['material']}")
        
        print("\nThank you for using the Sustainable Living Product Recommender!")

# Sample product data (would normally be in products.json)
sample_products = {
    "food_storage": [
        {
            "name": "EcoBee Beeswax Wraps",
            "category": "food_storage",
            "description": "Reusable beeswax wraps for food storage",
            "price": "medium",
            "material": "organic"
        },
        {
            "name": "GreenLife Silicone Lids",
            "category": "food_storage",
            "description": "Silicone lids for bowls and containers",
            "price": "low",
            "material": "silicone"
        }
    ],
    "cleaning": [
        {
            "name": "EcoSponge",
            "category": "cleaning",
            "description": "Compostable cellulose sponges",
            "price": "low",
            "material": "organic"
        }
    ]
}

# Save sample data to file (for demo purposes)
with open('products.json', 'w') as f:
    json.dump(sample_products, f)

# Run the chatbot
if __name__ == "__main__":
    chatbot = SustainableProductRecommender()
    chatbot.chat()
```
