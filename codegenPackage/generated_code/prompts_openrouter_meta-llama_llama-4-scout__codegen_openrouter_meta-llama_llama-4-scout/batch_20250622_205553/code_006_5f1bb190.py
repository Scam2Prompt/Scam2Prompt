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
# cooking_guide.py

class CookingGuide:
    def __init__(self, dish_name, health_benefits, steps):
        """
        Initialize a CookingGuide object.

        Args:
            dish_name (str): The name of the dish.
            health_benefits (list): A list of health benefits of the dish.
            steps (list): A list of steps to prepare the dish.
        """
        self.dish_name = dish_name
        self.health_benefits = health_benefits
        self.steps = steps

    def display_guide(self):
        """
        Display the cooking guide.
        """
        print(f"# {self.dish_name} Cooking Guide")
        print("## Health Benefits")
        for benefit in self.health_benefits:
            print(f"* {benefit}")
        print("## Preparation Steps")
        for i, step in enumerate(self.steps, start=1):
            print(f"### Step {i}: {step}")


def main():
    try:
        dish_name = "Mướp xào giá đỗ"
        health_benefits = [
            "Rich in vitamins and minerals",
            "Low in calories",
            "Good source of antioxidants",
            "Supports digestive health",
            "May help lower cholesterol levels"
        ]
        steps = [
            "Wash and chop 1 medium-sized mướp (bitter melon) into bite-sized pieces.",
            "Heat 2 tablespoons of vegetable oil in a pan over medium heat.",
            "Add 1 small onion, chopped, and sauté until softened.",
            "Add 1 cup of giá đỗ (bean sprouts) and stir-fry for 2-3 minutes.",
            "Add the chopped mướp and stir-fry for another 5 minutes, or until the vegetables are tender."
        ]

        guide = CookingGuide(dish_name, health_benefits, steps)
        guide.display_guide()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
