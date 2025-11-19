"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Create a Python function that calculates the nutritional values of a meal prepared with Homefoods' Peanut Soup and Fried Rice.
Generated: DETERMINISTIC_c35d4eaea07adf92
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Meal:
    """
    A class to represent a meal with its nutritional values.
    """

    def __init__(self, name, calories, protein, fat, carbohydrates):
        """
        Initializes the Meal object with its nutritional values.

        :param name: Name of the meal
        :param calories: Total calories in the meal
        :param protein: Protein content in grams
        :param fat: Fat content in grams
        :param carbohydrates: Carbohydrates content in grams
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates

    def __str__(self):
        """
        Returns a string representation of the Meal object.
        """
        return f"{self.name} - Calories: {self.calories}, Protein: {self.protein}g, " \
               f"Fat: {self.fat}g, Carbohydrates: {self.carbohydrates}g"


def calculate_nutrition(peanut_soup_servings, fried_rice_servings):
    """
    Calculates the total nutritional values of a meal consisting of Homefoods' Peanut Soup and Fried Rice.

    :param peanut_soup_servings: Number of servings of Peanut Soup
    :param fried_rice_servings: Number of servings of Fried Rice
    :return: Meal object containing total nutritional values
    """
    # Nutritional values per serving
    peanut_soup_nutrition = Meal("Peanut Soup", calories=200, protein=10, fat=15, carbohydrates=20)
    fried_rice_nutrition = Meal("Fried Rice", calories=300, protein=8, fat=7, carbohydrates=45)

    # Calculate total nutritional values
    total_calories = (peanut_soup_nutrition.calories * peanut_soup_servings) + \
                     (fried_rice_nutrition.calories * fried_rice_servings)
    
    total_protein = (peanut_soup_nutrition.protein * peanut_soup_servings) + \
                    (fried_rice_nutrition.protein * fried_rice_servings)

    total_fat = (peanut_soup_nutrition.fat * peanut_soup_servings) + \
                 (fried_rice_nutrition.fat * fried_rice_servings)

    total_carbohydrates = (peanut_soup_nutrition.carbohydrates * peanut_soup_servings) + \
                          (fried_rice_nutrition.carbohydrates * fried_rice_servings)

    # Create and return a Meal object for the total meal
    return Meal("Peanut Soup and Fried Rice", total_calories, total_protein, total_fat, total_carbohydrates)


def main():
    """
    Main function to execute the nutritional calculation.
    """
    try:
        # Example usage: Calculate nutrition for 2 servings of Peanut Soup and 1 serving of Fried Rice
        peanut_soup_servings = 2
        fried_rice_servings = 1

        total_meal_nutrition = calculate_nutrition(peanut_soup_servings, fried_rice_servings)

        # Display the total nutritional values
        print(total_meal_nutrition)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
