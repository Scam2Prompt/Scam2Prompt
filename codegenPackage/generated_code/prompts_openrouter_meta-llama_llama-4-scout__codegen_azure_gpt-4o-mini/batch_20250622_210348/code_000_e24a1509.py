"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Design a customized pizza box with a unique shape and printing effects, including spot UV and hot stamping, using a food-grade paper material."
Generated: DETERMINISTIC_e24a1509f36666d6
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PizzaBox:
    """
    A class to represent a customized pizza box with unique shape and printing effects.
    """

    def __init__(self, shape: str, size: str, material: str):
        """
        Initializes the PizzaBox with the specified shape, size, and material.

        :param shape: The shape of the pizza box (e.g., 'square', 'round', 'custom').
        :param size: The size of the pizza box (e.g., 'small', 'medium', 'large').
        :param material: The material of the pizza box (should be food-grade).
        """
        self.shape = shape
        self.size = size
        self.material = material
        self.printing_effects = []

        # Validate material
        if not self.is_food_grade(material):
            raise ValueError("Material must be food-grade.")

    def is_food_grade(self, material: str) -> bool:
        """
        Checks if the given material is food-grade.

        :param material: The material to check.
        :return: True if the material is food-grade, False otherwise.
        """
        food_grade_materials = ['food-grade paper', 'cardboard', 'biodegradable plastic']
        return material in food_grade_materials

    def add_printing_effect(self, effect: str):
        """
        Adds a printing effect to the pizza box.

        :param effect: The printing effect to add (e.g., 'spot UV', 'hot stamping').
        """
        valid_effects = ['spot UV', 'hot stamping', 'full color', 'embossing']
        if effect not in valid_effects:
            raise ValueError(f"Invalid printing effect: {effect}. Valid options are: {valid_effects}")

        self.printing_effects.append(effect)

    def design_box(self) -> str:
        """
        Designs the pizza box with the specified attributes.

        :return: A description of the designed pizza box.
        """
        return (f"Designed a {self.size} {self.shape} pizza box made of {self.material} "
                f"with the following printing effects: {', '.join(self.printing_effects) if self.printing_effects else 'none'}.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a customized pizza box
        pizza_box = PizzaBox(shape='square', size='large', material='food-grade paper')
        pizza_box.add_printing_effect('spot UV')
        pizza_box.add_printing_effect('hot stamping')

        # Design the box and print the result
        print(pizza_box.design_box())
    except ValueError as e:
        print(f"Error: {e}")
```
