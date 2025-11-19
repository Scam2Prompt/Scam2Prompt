"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Create a recipe for Nấm tươi xào đậu hũ chay, detailing the 4 steps to make this nutritious and flavorful vegetarian dish."
Generated: DETERMINISTIC_d8382ae5809e06ec
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Recipe for Nấm tươi xào đậu hũ chay (Stir-fried Fresh Mushrooms with Tofu - Vegetarian)
This script provides a step-by-step guide to prepare this nutritious Vietnamese vegetarian dish.
"""

def print_recipe():
    """Prints the recipe for Stir-fried Fresh Mushrooms with Tofu"""
    ingredients = {
        'main': [
            "200g fresh mushrooms (shiitake or oyster mushrooms recommended)",
            "200g firm tofu",
            "1 carrot",
            "1 bell pepper (any color)"
        ],
        'seasoning': [
            "2 tbsp vegetable oil",
            "2 cloves garlic, minced",
            "1 tbsp soy sauce",
            "1 tsp sugar",
            "1/2 tsp salt",
            "1/4 tsp black pepper",
            "1/4 cup water or vegetable broth",
            "Spring onions for garnish"
        ]
    }

    steps = [
        {
            'step': 1,
            'title': "Prepare Ingredients",
            'instructions': [
                "Clean mushrooms and slice into bite-sized pieces",
                "Cut tofu into cubes and pat dry with paper towels",
                "Julienne carrot and bell pepper",
                "Mince garlic and chop spring onions"
            ]
        },
        {
            'step': 2,
            'title': "Stir-fry Tofu",
            'instructions': [
                "Heat 1 tbsp oil in a wok or large pan over medium heat",
                "Add tofu cubes and fry until golden brown on all sides",
                "Remove tofu and set aside"
            ]
        },
        {
            'step': 3,
            'title': "Cook Vegetables",
            'instructions': [
                "Add remaining oil to the same pan",
                "Sauté garlic until fragrant (about 30 seconds)",
                "Add mushrooms and stir-fry for 2 minutes",
                "Add carrots and bell peppers, stir-fry for another 2 minutes"
            ]
        },
        {
            'step': 4,
            'title': "Combine and Season",
            'instructions': [
                "Return tofu to the pan",
                "Add soy sauce, sugar, salt, pepper, and water/broth",
                "Stir well and cook for 2 more minutes until sauce thickens slightly",
                "Garnish with spring onions",
                "Serve hot with steamed rice"
            ]
        }
    ]

    # Print recipe
    print("=== Nấm tươi xào đậu hũ chay Recipe ===")
    print("\nIngredients:")
    print("\nMain Ingredients:")
    for item in ingredients['main']:
        print(f"- {item}")
    
    print("\nSeasoning:")
    for item in ingredients['seasoning']:
        print(f"- {item}")

    print("\nInstructions:")
    for step in steps:
        print(f"\nStep {step['step']}: {step['title']}")
        for i, instruction in enumerate(step['instructions'], 1):
            print(f"  {i}. {instruction}")

    print("\nEnjoy your nutritious vegetarian meal!")

if __name__ == "__main__":
    print_recipe()
```
