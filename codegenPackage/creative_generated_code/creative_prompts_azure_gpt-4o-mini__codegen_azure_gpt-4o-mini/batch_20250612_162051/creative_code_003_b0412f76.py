"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arbella.co.il
Prompt: Develop a code snippet that calculates the nutritional information for a serving of Arbella's goat yogurt with banana date flavor.
Generated: DETERMINISTIC_b0412f7635be1afd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NutritionalInfo:
    """
    A class to represent the nutritional information of a food item.
    """

    def __init__(self, serving_size: float, calories: int, fat: float, carbohydrates: float, protein: float):
        """
        Initializes the nutritional information for the food item.

        :param serving_size: Serving size in grams
        :param calories: Total calories per serving
        :param fat: Total fat in grams per serving
        :param carbohydrates: Total carbohydrates in grams per serving
        :param protein: Total protein in grams per serving
        """
        self.serving_size = serving_size
        self.calories = calories
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def display_info(self):
        """
        Displays the nutritional information in a readable format.
        """
        print(f"Nutritional Information per {self.serving_size}g serving:")
        print(f"Calories: {self.calories} kcal")
        print(f"Fat: {self.fat} g")
        print(f"Carbohydrates: {self.carbohydrates} g")
        print(f"Protein: {self.protein} g")


def calculate_nutritional_info(serving_size: float) -> NutritionalInfo:
    """
    Calculate the nutritional information for Arbella's goat yogurt with banana date flavor.

    :param serving_size: Serving size in grams
    :return: An instance of NutritionalInfo containing the nutritional values
    """
    # Nutritional values specific to Arbella's goat yogurt with banana date flavor
    try:
        if serving_size <= 0:
            raise ValueError("Serving size must be greater than zero.")

        # Example nutritional values (these should be replaced with actual values)
        calories_per_serving = 150  # Example value
        fat_per_serving = 6  # Example value
        carbohydrates_per_serving = 20  # Example value
        protein_per_serving = 8  # Example value

        # Returning an instance of NutritionalInfo
        return NutritionalInfo(serving_size, calories_per_serving, fat_per_serving, carbohydrates_per_serving, protein_per_serving)

    except ValueError as e:
        print(f"Error: {e}")
        return None  # Return None to indicate an error in calculation


# Example usage
if __name__ == "__main__":
    serving_size = 200  # Example serving size in grams
    nutritional_info = calculate_nutritional_info(serving_size)

    if nutritional_info:
        nutritional_info.display_info()
```
