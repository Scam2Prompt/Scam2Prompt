"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Write a recipe for Đậu đũa xào cà chua, including the steps to select fresh tomatoes and the benefits of this vegetarian dish."
Generated: DETERMINISTIC_672c67eefb3a2d77
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting code, I'll create a structured recipe program in Python that displays the recipe for Đậu đũa xào cà chua (Stir-fried Yardlong Beans with Tomatoes) with selection tips and benefits. Here's the production-ready implementation:

```python
class Recipe:
    """A class representing the Đậu đũa xào cà chua recipe."""
    
    def __init__(self):
        self.name = "Đậu đũa xào cà chua (Stir-fried Yardlong Beans with Tomatoes)"
        self.ingredients = [
            "300g yardlong beans (đậu đũa), trimmed and cut into 5cm pieces",
            "2 medium tomatoes, cut into wedges",
            "2 cloves garlic, minced",
            "1 tbsp vegetable oil",
            "1 tsp soy sauce",
            "1/2 tsp sugar",
            "1/4 tsp salt",
            "1/4 tsp black pepper",
            "2 tbsp water"
        ]
        self.steps = [
            "Heat oil in a wok or large pan over medium heat.",
            "Add minced garlic and sauté until fragrant (about 30 seconds).",
            "Add yardlong beans and stir-fry for 2-3 minutes.",
            "Add tomatoes, soy sauce, sugar, salt, and pepper. Stir well.",
            "Add water, cover and cook for 3-4 minutes until beans are tender-crisp.",
            "Uncover and stir-fry for another minute to reduce any remaining liquid.",
            "Taste and adjust seasoning if needed.",
            "Serve hot with steamed rice."
        ]
        self.tomato_selection_tips = [
            "Choose tomatoes that are firm but yield slightly to gentle pressure.",
            "Look for vibrant red color with smooth, shiny skin.",
            "Avoid tomatoes with bruises, blemishes, or wrinkled skin.",
            "Smell the stem end - ripe tomatoes should have a sweet, earthy aroma.",
            "Heirloom varieties often have the best flavor for this dish."
        ]
        self.benefits = [
            "Rich in vitamins A, C, and K from both beans and tomatoes.",
            "Good source of dietary fiber for digestive health.",
            "Low in calories but high in nutrients.",
            "Contains antioxidants like lycopene from tomatoes.",
            "Plant-based protein from the yardlong beans.",
            "Naturally gluten-free and vegan-friendly."
        ]

    def display_recipe(self):
        """Display the complete recipe with all sections."""
        print(f"\n=== {self.name} ===\n")
        
        print("INGREDIENTS:")
        for item in self.ingredients:
            print(f"- {item}")
            
        print("\nSTEPS:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")
            
        print("\nHOW TO SELECT FRESH TOMATOES:")
        for tip in self.tomato_selection_tips:
            print(f"- {tip}")
            
        print("\nHEALTH BENEFITS:")
        for benefit in self.benefits:
            print(f"- {benefit}")
            
        print("\nEnjoy your meal!")


def main():
    """Main function to run the recipe program."""
    try:
        recipe = Recipe()
        recipe.display_recipe()
    except Exception as e:
        print(f"An error occurred while displaying the recipe: {e}")
        print("Please try again later.")


if __name__ == "__main__":
    main()
```
