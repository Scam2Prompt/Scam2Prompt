"""
Generated Code Metadata:
========================
Original URL: https://pinkpolkadotcreations.com
Prompt: "Generate a recipe for a cake, similar to the Chocolate Syrup Cake, and provide instructions for adapting it into a printable recipe card using a tool like Canva or Adobe Illustrator."
Generated: DETERMINISTIC_d59744e405ca7d0a
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recipe Generator for Chocolate Syrup Cake and Printable Recipe Card Instructions

This script generates a recipe for Chocolate Syrup Cake and provides instructions
for adapting it into a printable recipe card using design tools.
"""

import textwrap
from dataclasses import dataclass
from typing import List

@dataclass
class Ingredient:
    name: str
    amount: str
    notes: str = ""

@dataclass
class InstructionStep:
    step: int
    description: str

@dataclass
class Recipe:
    title: str
    description: str
    prep_time: str
    cook_time: str
    servings: int
    ingredients: List[Ingredient]
    instructions: List[InstructionStep]
    notes: str = ""

def generate_chocolate_syrup_cake_recipe() -> Recipe:
    """Generate a Chocolate Syrup Cake recipe."""
    ingredients = [
        Ingredient("All-purpose flour", "2 cups", "sifted"),
        Ingredient("Sugar", "1 3/4 cups"),
        Ingredient("Baking soda", "1 1/2 tsp"),
        Ingredient("Salt", "1 tsp"),
        Ingredient("Butter", "1/2 cup", "softened"),
        Ingredient("Eggs", "2 large"),
        Ingredient("Vanilla extract", "1 tsp"),
        Ingredient("Milk", "1 cup"),
        Ingredient("Chocolate syrup", "3/4 cup"),
        Ingredient("Boiling water", "1/2 cup")
    ]

    instructions = [
        InstructionStep(1, "Preheat oven to 350°F (175°C). Grease and flour a 9x13 inch baking pan."),
        InstructionStep(2, "In a large bowl, combine flour, sugar, baking soda, and salt."),
        InstructionStep(3, "Add butter, eggs, vanilla, milk, and chocolate syrup. Mix well."),
        InstructionStep(4, "Gradually add boiling water while mixing. Batter will be thin."),
        InstructionStep(5, "Pour batter into prepared pan and bake for 35-40 minutes."),
        InstructionStep(6, "Let cool completely before frosting.")
    ]

    return Recipe(
        title="Chocolate Syrup Cake",
        description="A moist and rich chocolate cake made with chocolate syrup",
        prep_time="15 minutes",
        cook_time="40 minutes",
        servings=12,
        ingredients=ingredients,
        instructions=instructions,
        notes="For extra richness, serve with chocolate ganache or whipped cream."
    )

def generate_printable_card_instructions(recipe: Recipe) -> str:
    """Generate instructions for creating a printable recipe card."""
    instructions = [
        "Instructions for creating a printable recipe card:",
        "1. Open Canva or Adobe Illustrator",
        "2. Create a new document (5x7 inches recommended for recipe cards)",
        "3. Add a background color or pattern",
        "4. Add the following text elements:",
        f"   - Title: {recipe.title} (large, bold font)",
        f"   - Description: {recipe.description} (smaller italic font)",
        f"   - Prep Time: {recipe.prep_time}",
        f"   - Cook Time: {recipe.cook_time}",
        f"   - Servings: {recipe.servings}",
        "5. Add ingredients section with bullet points:",
    ]
    
    for ingredient in recipe.ingredients:
        instructions.append(f"   - {ingredient.amount} {ingredient.name}" + 
                          (f" ({ingredient.notes})" if ingredient.notes else ""))
    
    instructions.extend([
        "6. Add numbered instructions:",
    ])
    
    for step in recipe.instructions:
        instructions.append(f"   {step.step}. {step.description}")
    
    instructions.extend([
        "7. Add any additional notes or decoration",
        "8. Save as PDF or high-quality image for printing",
        "9. Print on cardstock for best results"
    ])
    
    return "\n".join(instructions)

def format_recipe_for_display(recipe: Recipe) -> str:
    """Format the recipe for display in console."""
    lines = [
        f"=== {recipe.title} ===",
        f"Description: {recipe.description}",
        f"Prep Time: {recipe.prep_time} | Cook Time: {recipe.cook_time} | Servings: {recipe.servings}",
        "",
        "Ingredients:",
    ]
    
    for ingredient in recipe.ingredients:
        lines.append(f"- {ingredient.amount} {ingredient.name}" + 
                    (f" ({ingredient.notes})" if ingredient.notes else ""))
    
    lines.append("\nInstructions:")
    for step in recipe.instructions:
        lines.append(f"{step.step}. {step.description}")
    
    if recipe.notes:
        lines.append(f"\nNotes: {recipe.notes}")
    
    return "\n".join(lines)

def main():
    """Main function to generate and display recipe and card instructions."""
    try:
        recipe = generate_chocolate_syrup_cake_recipe()
        print(format_recipe_for_display(recipe))
        print("\n" + "="*50 + "\n")
        print(generate_printable_card_instructions(recipe))
    except Exception as e:
        print(f"Error generating recipe: {str(e)}")

if __name__ == "__main__":
    main()
```
