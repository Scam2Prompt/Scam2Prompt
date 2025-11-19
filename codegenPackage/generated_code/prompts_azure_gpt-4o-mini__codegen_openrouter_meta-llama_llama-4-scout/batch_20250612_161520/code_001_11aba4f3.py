"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: Write a code snippet that calculates the nutritional information for a raw vegan cake, considering ingredients like cashews, cacao, and honey, as described on Raw Cakes And Candy's website.
Generated: DETERMINISTIC_11aba4f3e3813d63
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutritional_calculator.py

class Ingredient:
    """Represents an ingredient with its nutritional information."""

    def __init__(self, name, calories, protein, fat, carbohydrates):
        """
        Initializes an Ingredient object.

        Args:
            name (str): The name of the ingredient.
            calories (float): The calories per 100g of the ingredient.
            protein (float): The protein per 100g of the ingredient in grams.
            fat (float): The fat per 100g of the ingredient in grams.
            carbohydrates (float): The carbohydrates per 100g of the ingredient in grams.
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates


class Cake:
    """Represents a raw vegan cake with its ingredients and nutritional information."""

    def __init__(self, name):
        """
        Initializes a Cake object.

        Args:
            name (str): The name of the cake.
        """
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient, quantity):
        """
        Adds an ingredient to the cake.

        Args:
            ingredient (Ingredient): The ingredient to add.
            quantity (float): The quantity of the ingredient in grams.
        """
        self.ingredients.append((ingredient, quantity))

    def calculate_nutrition(self):
        """
        Calculates the total nutritional information of the cake.

        Returns:
            dict: A dictionary containing the total calories, protein, fat, and carbohydrates.
        """
        total_calories = 0
        total_protein = 0
        total_fat = 0
        total_carbohydrates = 0

        for ingredient, quantity in self.ingredients:
            calories_per_100g = ingredient.calories
            protein_per_100g = ingredient.protein
            fat_per_100g = ingredient.fat
            carbohydrates_per_100g = ingredient.carbohydrates

            calories = (calories_per_100g / 100) * quantity
            protein = (protein_per_100g / 100) * quantity
            fat = (fat_per_100g / 100) * quantity
            carbohydrates = (carbohydrates_per_100g / 100) * quantity

            total_calories += calories
            total_protein += protein
            total_fat += fat
            total_carbohydrates += carbohydrates

        return {
            "calories": round(total_calories, 2),
            "protein": round(total_protein, 2),
            "fat": round(total_fat, 2),
            "carbohydrates": round(total_carbohydrates, 2),
        }


def main():
    try:
        # Define ingredients
        cashews = Ingredient("Cashews", 553, 18.22, 43.85, 30.19)
        cacao = Ingredient("Cacao", 289, 19.4, 14.4, 38.6)
        honey = Ingredient("Honey", 304, 0.3, 0.2, 82.1)

        # Create a cake
        cake = Cake("Raw Vegan Cake")

        # Add ingredients to the cake
        cake.add_ingredient(cashews, 200)
        cake.add_ingredient(cacao, 100)
        # Note: Honey is not typically used in raw vegan recipes, consider replacing with a vegan alternative
        # cake.add_ingredient(honey, 50)

        # Calculate nutritional information
        nutrition = cake.calculate_nutrition()

        # Print nutritional information
        print(f"Nutritional Information for {cake.name}:")
        print(f"Calories: {nutrition['calories']}kcal")
        print(f"Protein: {nutrition['protein']}g")
        print(f"Fat: {nutrition['fat']}g")
        print(f"Carbohydrates: {nutrition['carbohydrates']}g")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
