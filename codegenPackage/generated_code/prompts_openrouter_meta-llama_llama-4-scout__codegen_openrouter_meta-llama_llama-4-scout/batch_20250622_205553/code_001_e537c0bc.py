"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "How to make Đậu cô ve xào tỏi with a detailed 5-step process and what makes it a popular side dish in Vietnamese cuisine?"
Generated: DETERMINISTIC_e537c0bcb25a611e
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Đậu cô ve xào tỏi Recipe

class Recipe:
    def __init__(self, name, description, steps):
        """
        Initialize a Recipe object.

        Args:
            name (str): The name of the recipe.
            description (str): A brief description of the recipe.
            steps (list): A list of steps to prepare the recipe.
        """
        self.name = name
        self.description = description
        self.steps = steps

    def display_recipe(self):
        """
        Display the recipe details.
        """
        print(f"**{self.name}**")
        print(self.description)
        for i, step in enumerate(self.steps, start=1):
            print(f"\n**Step {i}: {step['title']}**")
            print(step['description'])

def main():
    # Define the recipe steps
    steps = [
        {
            'title': 'Prepare Ingredients',
            'description': 'Gather 200g of đậu cô ve (string beans), 3-4 cloves of tỏi (garlic), 1 tablespoon of vegetable oil, salt, and pepper to taste.'
        },
        {
            'title': 'Chop and Mince',
            'description': 'Chop the đậu cô ve into 2-inch pieces and mince the tỏi.'
        },
        {
            'title': 'Heat Oil and Sauté Tỏi',
            'description': 'Heat the vegetable oil in a pan over medium heat. Sauté the minced tỏi until fragrant.'
        },
        {
            'title': 'Add Đậu Cô Ve',
            'description': 'Add the chopped đậu cô ve to the pan. Stir well to combine with the tỏi and oil.'
        },
        {
            'title': 'Season and Serve',
            'description': 'Season with salt and pepper to taste. Stir-fry for another 2-3 minutes until the đậu cô ve is cooked through. Serve hot.'
        }
    ]

    # Create a Recipe object
    recipe = Recipe(
        name="Đậu Cô Ve Xào Tỏi",
        description="A popular Vietnamese side dish made with stir-fried string beans and garlic.",
        steps=steps
    )

    try:
        # Display the recipe
        recipe.display_recipe()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
