"""
Generated Code Metadata:
========================
Original URL: https://lowcarblife.shop
Prompt: "Write a Python script to calculate the macronutrient breakdown of a keto diet, given a list of ingredients and their quantities."
Generated: DETERMINISTIC_c08c47f126bc2a1b
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# keto_calculator.py

class Ingredient:
    """Represents a food ingredient with its macronutrient breakdown."""

    def __init__(self, name, quantity, protein, fat, carbohydrates):
        """
        Initializes an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient in grams.
            protein (float): The protein content of the ingredient per 100g.
            fat (float): The fat content of the ingredient per 100g.
            carbohydrates (float): The carbohydrate content of the ingredient per 100g.
        """
        self.name = name
        self.quantity = quantity
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates

    def calculate_macronutrients(self):
        """
        Calculates the macronutrient breakdown of the ingredient.

        Returns:
            dict: A dictionary containing the protein, fat, and carbohydrate content of the ingredient.
        """
        protein_content = (self.quantity / 100) * self.protein
        fat_content = (self.quantity / 100) * self.fat
        carbohydrate_content = (self.quantity / 100) * self.carbohydrates

        return {
            "protein": protein_content,
            "fat": fat_content,
            "carbohydrates": carbohydrate_content,
        }


class KetoCalculator:
    """Calculates the macronutrient breakdown of a keto diet."""

    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the keto calculator.

        Args:
            ingredient (Ingredient): The ingredient to add.
        """
        self.ingredients.append(ingredient)

    def calculate_total_macronutrients(self):
        """
        Calculates the total macronutrient breakdown of all ingredients.

        Returns:
            dict: A dictionary containing the total protein, fat, and carbohydrate content.
        """
        total_protein = 0
        total_fat = 0
        total_carbohydrates = 0

        for ingredient in self.ingredients:
            macronutrients = ingredient.calculate_macronutrients()
            total_protein += macronutrients["protein"]
            total_fat += macronutrients["fat"]
            total_carbohydrates += macronutrients["carbohydrates"]

        return {
            "protein": total_protein,
            "fat": total_fat,
            "carbohydrates": total_carbohydrates,
        }

    def calculate_keto_ratio(self):
        """
        Calculates the keto ratio of the total macronutrient breakdown.

        Returns:
            dict: A dictionary containing the keto ratio.
        """
        total_macronutrients = self.calculate_total_macronutrients()
        keto_ratio = {
            "protein": total_macronutrients["protein"],
            "fat": total_macronutrients["fat"],
            "carbohydrates": total_macronutrients["carbohydrates"],
        }

        try:
            keto_ratio["protein_to_fat"] = keto_ratio["protein"] / keto_ratio["fat"]
            keto_ratio["carbohydrates_to_fat"] = keto_ratio["carbohydrates"] / keto_ratio["fat"]
        except ZeroDivisionError:
            print("Error: Fat content is zero.")

        return keto_ratio


def main():
    calculator = KetoCalculator()

    # Example usage:
    ingredients = [
        Ingredient("Egg", 100, 12.6, 9.5, 0.7),
        Ingredient("Bacon", 50, 25.5, 71.2, 0.3),
        Ingredient("Avocado", 100, 1.4, 14.7, 2.2),
    ]

    for ingredient in ingredients:
        calculator.add_ingredient(ingredient)

    total_macronutrients = calculator.calculate_total_macronutrients()
    keto_ratio = calculator.calculate_keto_ratio()

    print("Total Macronutrients:")
    print(f"Protein: {total_macronutrients['protein']:.2f}g")
    print(f"Fat: {total_macronutrients['fat']:.2f}g")
    print(f"Carbohydrates: {total_macronutrients['carbohydrates']:.2f}g")

    print("\nKeto Ratio:")
    print(f"Protein: {keto_ratio['protein']:.2f}g")
    print(f"Fat: {keto_ratio['fat']:.2f}g")
    print(f"Carbohydrates: {keto_ratio['carbohydrates']:.2f}g")
    try:
        print(f"Protein to Fat Ratio: {keto_ratio['protein_to_fat']:.2f}")
        print(f"Carbohydrates to Fat Ratio: {keto_ratio['carbohydrates_to_fat']:.2f}")
    except KeyError:
        pass


if __name__ == "__main__":
    main()
```
