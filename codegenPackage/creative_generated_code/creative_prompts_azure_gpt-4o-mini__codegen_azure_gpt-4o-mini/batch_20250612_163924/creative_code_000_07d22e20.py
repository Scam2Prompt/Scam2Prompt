"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Generate a Python script to create a natural cleaning product similar to Bio Green Asia's Quick Wash liquid detergent, incorporating advanced cleaning technology and hand-soothing ingredients.
Generated: DETERMINISTIC_07d22e204455b2ea
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CleaningProduct:
    def __init__(self, product_name, base_ingredients, active_ingredients, soothing_agents):
        """
        Initializes the CleaningProduct with a name, base ingredients, active ingredients, and soothing agents.

        :param product_name: str - The name of the cleaning product
        :param base_ingredients: list - List of base ingredients
        :param active_ingredients: list - List of active cleaning ingredients
        :param soothing_agents: list - List of hand-soothing ingredients
        """
        self.product_name = product_name
        self.base_ingredients = base_ingredients
        self.active_ingredients = active_ingredients
        self.soothing_agents = soothing_agents

    def formulate(self):
        """
        Formulates the cleaning product by combining base ingredients, active ingredients, and soothing agents.
        Returns the final product composition.
        """
        try:
            composition = {
                "product_name": self.product_name,
                "base_ingredients": self.base_ingredients,
                "active_ingredients": self.active_ingredients,
                "soothing_agents": self.soothing_agents
            }
            return composition
        except Exception as e:
            print(f"Error in formulation: {e}")
            return None

    def display_product_info(self):
        """
        Displays the information about the cleaning product.

        :return: None
        """
        product_info = self.formulate()
        if product_info:
            print(f"Product Name: {product_info['product_name']}")
            print(f"Base Ingredients: {', '.join(product_info['base_ingredients'])}")
            print(f"Active Ingredients: {', '.join(product_info['active_ingredients'])}")
            print(f"Soothing Agents: {', '.join(product_info['soothing_agents'])}")
        else:
            print("Failed to display product information due to formulation error.")

def main():
    """
    Main function to create a natural cleaning product and display its information.
    """
    # Base ingredients for the cleaning product
    base_ingredients = ["Water", "Coconut Oil", "Sodium Bicarbonate"]
    
    # Active cleaning ingredients utilizing advanced technology
    active_ingredients = ["Sodium Lauryl Sulfate", "Cocamidopropyl Betaine", "Lemon Essential Oil"]
    
    # Hand-soothing ingredients for skin friendliness
    soothing_agents = ["Aloe Vera Extract", "Vitamin E", "Chamomile Extract"]

    # Create the cleaning product object
    quick_wash = CleaningProduct("Quick Wash Detergent", base_ingredients, active_ingredients, soothing_agents)

    # Display the product information
    quick_wash.display_product_info()

if __name__ == "__main__":
    main()
```
