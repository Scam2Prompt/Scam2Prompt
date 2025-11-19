"""
Generated Code Metadata:
========================
Original URL: https://pancakesrus.net
Prompt: Write a code snippet to calculate the nutritional information of a meal, considering factors like lean protein, good fats, and complex carbohydrates, as discussed in the Iron Man Healthy Choices section of PancakesRus.
Generated: DETERMINISTIC_5e6b8e2bd124ee0d
Batch ID: 20250622_212115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutritional_calculator.py

class NutritionalInfo:
    """Calculates nutritional information of a meal."""

    def __init__(self, lean_protein, good_fats, complex_carbohydrates):
        """
        Initializes a NutritionalInfo object.

        Args:
            lean_protein (float): Lean protein in grams.
            good_fats (float): Good fats in grams.
            complex_carbohydrates (float): Complex carbohydrates in grams.
        """
        self.lean_protein = lean_protein
        self.good_fats = good_fats
        self.complex_carbohydrates = complex_carbohydrates

    def calculate_calories(self):
        """
        Calculates total calories based on macronutrients.

        Returns:
            float: Total calories.
        """
        # Approximate calorie values per gram
        protein_calories = 4.0
        fat_calories = 9.0
        carb_calories = 4.0

        total_calories = (self.lean_protein * protein_calories) + \
                         (self.good_fats * fat_calories) + \
                         (self.complex_carbohydrates * carb_calories)
        return total_calories

    def calculate_macronutrient_ratio(self):
        """
        Calculates macronutrient ratio.

        Returns:
            dict: Macronutrient ratio.
        """
        total_macronutrients = self.lean_protein + self.good_fats + self.complex_carbohydrates

        protein_ratio = (self.lean_protein / total_macronutrients) * 100
        fat_ratio = (self.good_fats / total_macronutrients) * 100
        carb_ratio = (self.complex_carbohydrates / total_macronutrients) * 100

        return {
            "protein": f"{protein_ratio:.2f}%",
            "fat": f"{fat_ratio:.2f}%",
            "carbohydrates": f"{carb_ratio:.2f}%",
        }

    def validate_input(self):
        """
        Validates input values.

        Raises:
            ValueError: If any input value is non-positive.
        """
        if self.lean_protein <= 0 or self.good_fats <= 0 or self.complex_carbohydrates <= 0:
            raise ValueError("Input values must be positive.")


def main():
    try:
        lean_protein = float(input("Enter lean protein in grams: "))
        good_fats = float(input("Enter good fats in grams: "))
        complex_carbohydrates = float(input("Enter complex carbohydrates in grams: "))

        nutritional_info = NutritionalInfo(lean_protein, good_fats, complex_carbohydrates)
        nutritional_info.validate_input()

        total_calories = nutritional_info.calculate_calories()
        macronutrient_ratio = nutritional_info.calculate_macronutrient_ratio()

        print(f"Total Calories: {total_calories:.2f} kcal")
        print("Macronutrient Ratio:")
        for nutrient, ratio in macronutrient_ratio.items():
            print(f"{nutrient.capitalize()}: {ratio}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
