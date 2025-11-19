"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: "Design a simple chatbot that provides skincare recommendations based on user input, using Marant's product line and expertise."
Generated: DETERMINISTIC_944804e30d45214a
Batch ID: 20250622_204920
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

class SkincareChatbot:
    """
    A simple chatbot that provides skincare recommendations based on user input.
    Uses Marant's product line and expertise.
    """
    
    def __init__(self, products_file: str = "products.json"):
        """
        Initialize the chatbot with product data.
        
        Args:
            products_file: Path to JSON file containing product data
        """
        try:
            with open(products_file, 'r') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Product file {products_file} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in {products_file}")
            
        self.user_profile = {}
        
    def get_user_input(self) -> Dict[str, str]:
        """
        Collect user information for skincare recommendations.
        
        Returns:
            Dictionary containing user's skin type, concerns, and preferences
        """
        print("Welcome to Marant's Skincare Advisor!")
        print("Let's find the perfect products for your skin.\n")
        
        skin_types = ["dry", "oily", "combination", "normal", "sensitive"]
        concerns = ["acne", "aging", "redness", "dark spots", "hydration"]
        
        self.user_profile = {
            "skin_type": self._get_valid_input(
                "What is your skin type? (dry, oily, combination, normal, sensitive): ",
                skin_types
            ),
            "primary_concern": self._get_valid_input(
                "What is your primary skin concern? (acne, aging, redness, dark spots, hydration): ",
                concerns
            ),
            "preference": self._get_valid_input(
                "Do you prefer natural or clinical products? (natural, clinical): ",
                ["natural", "clinical"]
            )
        }
        
        return self.user_profile
    
    def _get_valid_input(self, prompt: str, valid_options: List[str]) -> str:
        """
        Helper method to get and validate user input.
        
        Args:
            prompt: The question to ask the user
            valid_options: List of valid responses
            
        Returns:
            Validated user input
        """
        while True:
            user_input = input(prompt).lower().strip()
            if user_input in valid_options:
                return user_input
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
    
    def recommend_products(self) -> List[Dict[str, str]]:
        """
        Recommend products based on user profile.
        
        Returns:
            List of recommended products with their details
        """
        if not self.user_profile:
            raise ValueError("User profile not collected. Call get_user_input() first.")
            
        recommendations = []
        
        for product in self.products:
            matches = (
                self.user_profile["skin_type"] in product["suitable_for"] and
                self.user_profile["primary_concern"] in product["targets"] and
                self.user_profile["preference"] == product["type"]
            )
            
            if matches:
                recommendations.append(product)
                
        return recommendations
    
    def display_recommendations(self, recommendations: List[Dict[str, str]]) -> None:
        """
        Display product recommendations to the user.
        
        Args:
            recommendations: List of products to display
        """
        if not recommendations:
            print("\nWe couldn't find perfect matches, but here are some general suggestions:")
            general_recs = [
                p for p in self.products 
                if self.user_profile["skin_type"] in p["suitable_for"]
            ][:3]
            for product in general_recs:
                self._display_product(product)
            return
            
        print("\nHere are your personalized skincare recommendations:")
        for product in recommendations:
            self._display_product(product)
    
    def _display_product(self, product: Dict[str, str]) -> None:
        """
        Helper method to display product information.
        
        Args:
            product: Product dictionary to display
        """
        print(f"\n{product['name']} ({product['type'].capitalize()})")
        print(f"Purpose: {', '.join(product['targets'])}")
        print(f"Suitable for: {', '.join(product['suitable_for'])}")
        print(f"Key ingredients: {', '.join(product['ingredients'])}")
        print(f"How to use: {product['usage']}")
    
    def run(self) -> None:
        """
        Run the chatbot interaction flow.
        """
        try:
            self.get_user_input()
            recommendations = self.recommend_products()
            self.display_recommendations(recommendations)
            print("\nThank you for using Marant's Skincare Advisor!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again later.")

# Example product data (would normally be in a separate JSON file)
example_products = [
    {
        "name": "Hydra-Boost Serum",
        "type": "clinical",
        "targets": ["hydration", "aging"],
        "suitable_for": ["dry", "normal", "sensitive"],
        "ingredients": ["hyaluronic acid", "vitamin B5", "peptides"],
        "usage": "Apply 2-3 drops to clean face morning and night"
    },
    {
        "name": "Clear Skin Elixir",
        "type": "natural",
        "targets": ["acne", "redness"],
        "suitable_for": ["oily", "combination", "sensitive"],
        "ingredients": ["tea tree oil", "aloe vera", "witch hazel"],
        "usage": "Apply with cotton pad after cleansing, morning and night"
    },
    {
        "name": "Age-Defy Cream",
        "type": "clinical",
        "targets": ["aging", "dark spots"],
        "suitable_for": ["dry", "normal", "combination"],
        "ingredients": ["retinol", "vitamin C", "niacinamide"],
        "usage": "Apply a pea-sized amount at night after serum"
    }
]

def main():
    # In a real implementation, this would load from a JSON file
    # For demo purposes, we'll create a temporary file
    import tempfile
    import os
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
        json.dump(example_products, temp_file)
        temp_file_path = temp_file.name
    
    try:
        chatbot = SkincareChatbot(temp_file_path)
        chatbot.run()
    finally:
        os.unlink(temp_file_path)

if __name__ == "__main__":
    main()
```
