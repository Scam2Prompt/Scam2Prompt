"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Write a cooking guide for Mướp xào giá đỗ, including its health benefits and the 5 simple steps to prepare this Vietnamese vegetarian dish."
Generated: DETERMINISTIC_5f1bb1902232bbe3
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CookingGuide:
    """
    A cooking guide for Mướp xào giá đỗ (Vietnamese Stir-fried Luffa with Bean Sprouts).
    Includes health benefits and preparation steps.
    """
    
    def __init__(self):
        self.dish_name = "Mướp xào giá đỗ (Vietnamese Stir-fried Luffa with Bean Sprouts)"
        self.cuisine = "Vietnamese"
        self.category = "Vegetarian"
        self.ingredients = [
            "1 medium luffa (mướp), peeled and sliced",
            "200g bean sprouts (giá đỗ)",
            "2 cloves garlic, minced",
            "1 tablespoon vegetable oil",
            "1 teaspoon soy sauce",
            "1/2 teaspoon salt",
            "1/4 teaspoon pepper",
            "1/4 teaspoon sugar (optional)",
            "2 tablespoons chopped spring onions"
        ]
        self.health_benefits = [
            "Rich in vitamins A and C from luffa",
            "High in fiber for digestive health",
            "Low in calories and fat",
            "Bean sprouts provide plant-based protein",
            "Contains antioxidants for immune support"
        ]
        self.steps = [
            "Prepare ingredients: Peel and slice luffa into thin half-moons. Rinse bean sprouts and drain well.",
            "Heat oil in a wok or large pan over medium-high heat. Add minced garlic and stir until fragrant (about 30 seconds).",
            "Add luffa slices and stir-fry for 2-3 minutes until slightly softened.",
            "Add bean sprouts, soy sauce, salt, pepper, and sugar (if using). Stir-fry for another 2 minutes until vegetables are cooked but still crisp.",
            "Garnish with chopped spring onions. Serve hot with rice."
        ]
    
    def display_guide(self):
        """Display the complete cooking guide"""
        print(f"\n{'-'*50}")
        print(f"COOKING GUIDE: {self.dish_name.upper()}")
        print(f"{'-'*50}\n")
        
        print("Cuisine:", self.cuisine)
        print("Category:", self.category)
        
        print("\nINGREDIENTS:")
        for item in self.ingredients:
            print(f"- {item}")
            
        print("\nHEALTH BENEFITS:")
        for benefit in self.health_benefits:
            print(f"- {benefit}")
            
        print("\nPREPARATION STEPS:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")
        
        print("\nEnjoy your meal!")

# Example usage
if __name__ == "__main__":
    try:
        guide = CookingGuide()
        guide.display_guide()
    except Exception as e:
        print(f"An error occurred while generating the cooking guide: {str(e)}")
```
