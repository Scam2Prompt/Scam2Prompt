"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Generate a recipe using Homefoods' Jollof Rice Seasoning and suggest cooking tips for perfecting the dish.
Generated: DETERMINISTIC_05218873279bcaf5
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a Jollof Rice recipe using Homefoods' Jollof Rice Seasoning and includes cooking tips:

```python
class JollofRiceRecipe:
    """
    A class to represent a Jollof Rice recipe using Homefoods' Jollof Rice Seasoning.
    Includes ingredients, preparation steps, and cooking tips.
    """
    
    def __init__(self):
        self.recipe_name = "Homefoods Jollof Rice"
        self.serving_size = 4
        self.ingredients = [
            "2 cups long grain parboiled rice",
            "3 tablespoons Homefoods Jollof Rice Seasoning",
            "1/4 cup vegetable oil",
            "1 medium onion, chopped",
            "2 cloves garlic, minced",
            "1 teaspoon ginger, grated",
            "1 red bell pepper, blended",
            "2 tomatoes, blended",
            "2 cups chicken or vegetable stock",
            "1 teaspoon salt (adjust to taste)",
            "1 bay leaf",
            "1 cup mixed vegetables (carrots, peas, green beans - optional)",
            "1 teaspoon thyme",
            "1 teaspoon curry powder"
        ]
        self.preparation_steps = [
            "Rinse the rice thoroughly until water runs clear and set aside to drain.",
            "Heat oil in a pot over medium heat. Add onions and sauté until translucent.",
            "Add garlic, ginger, and sauté for 30 seconds until fragrant.",
            "Stir in the blended peppers and tomatoes. Cook for 5-7 minutes until reduced.",
            "Add Homefoods Jollof Rice Seasoning, thyme, curry powder, and bay leaf. Stir well.",
            "Pour in the stock and bring to a boil. Season with salt to taste.",
            "Add the drained rice and mixed vegetables (if using). Stir gently to combine.",
            "Cover with a tight-fitting lid, reduce heat to low, and simmer for 20-25 minutes.",
            "Turn off heat and let it steam for 5 minutes before fluffing with a fork.",
            "Serve hot with your choice of protein or salad."
        ]
        self.cooking_tips = [
            "For authentic smoky flavor, cover with foil before the final steaming.",
            "Use parboiled rice for best texture - it's less likely to become mushy.",
            "The key to perfect Jollof is in the pepper base - cook it down until thick.",
            "Resist the urge to stir too much while cooking to prevent breaking the rice.",
            "If rice isn't tender after liquid is absorbed, add 1/4 cup water and cook longer.",
            "For party-size portions, double all ingredients except the seasoning (use 4 tbsp)."
        ]
    
    def display_recipe(self):
        """Prints the complete recipe with ingredients, steps, and tips."""
        print(f"\n=== {self.recipe_name} ===\n")
        print(f"Serves: {self.serving_size}\n")
        
        print("Ingredients:")
        for i, ingredient in enumerate(self.ingredients, 1):
            print(f"{i}. {ingredient}")
        
        print("\nPreparation Steps:")
        for i, step in enumerate(self.preparation_steps, 1):
            print(f"{i}. {step}")
        
        print("\nCooking Tips for Perfect Jollof Rice:")
        for i, tip in enumerate(self.cooking_tips, 1):
            print(f"- {tip}")
        
        print("\nEnjoy your delicious Jollof Rice!")

# Create and display the recipe
if __name__ == "__main__":
    try:
        recipe = JollofRiceRecipe()
        recipe.display_recipe()
    except Exception as e:
        print(f"An error occurred while generating the recipe: {e}")
```
