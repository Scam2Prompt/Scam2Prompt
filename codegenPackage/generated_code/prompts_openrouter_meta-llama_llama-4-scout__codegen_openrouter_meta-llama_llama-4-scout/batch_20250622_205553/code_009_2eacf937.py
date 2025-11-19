"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "Provide a simple recipe for Tôm chay kho, highlighting its preparation in 5 steps and why it's a preferred choice for those looking for vegetarian and quick meal options."
Generated: DETERMINISTIC_2eacf93784dd2e8b
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Recipe class for Tôm chay kho
class Recipe:
    def __init__(self, name, description, prep_time, cook_time):
        """
        Initialize a Recipe object.

        Args:
            name (str): Name of the recipe.
            description (str): Brief description of the recipe.
            prep_time (int): Preparation time in minutes.
            cook_time (int): Cooking time in minutes.
        """
        self.name = name
        self.description = description
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.steps = []

    def add_step(self, step):
        """
        Add a preparation step to the recipe.

        Args:
            step (str): A preparation step.
        """
        self.steps.append(step)

    def display_recipe(self):
        """
        Display the recipe details and preparation steps.
        """
        print(f"**{self.name}**")
        print(self.description)
        print(f"Prep Time: {self.prep_time} minutes | Cook Time: {self.cook_time} minutes")
        print("**Preparation Steps:**")
        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step}")


# Tôm chay kho recipe
def main():
    try:
        # Create a new recipe
        tom_chay_kho = Recipe(
            "Tôm chay kho",
            "A simple and delicious vegetarian dish made with tofu, perfect for a quick meal.",
            10,
            20
        )

        # Add preparation steps
        tom_chay_kho.add_step("Prepare the ingredients: tofu, vegetable oil, garlic, and soy sauce.")
        tom_chay_kho.add_step("Heat oil in a pan and sauté garlic until fragrant.")
        tom_chay_kho.add_step("Add tofu and stir well.")
        tom_chay_kho.add_step("Add soy sauce and water, then bring to a boil.")
        tom_chay_kho.add_step("Simmer until the sauce thickens.")

        # Display the recipe
        tom_chay_kho.display_recipe()

        # Why Tôm chay kho is preferred
        print("\n**Why Tôm chay kho is a preferred choice:**")
        print("* It's a vegetarian dish, suitable for those looking for meat-free options.")
        print("* It's quick and easy to prepare, perfect for busy days.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
