"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-co-wallet.blogspot.com
Prompt: Write a Python function that calculates the nutritional information for a pizza with bechamel sauce, mozzarella, and prosciutto, inspired by the offerings at A Pizza da Mooca.
Generated: DETERMINISTIC_3f0c8cb24d657b7f
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PizzaNutritionalInfo:
    """A class to represent the nutritional information of a pizza."""

    def __init__(self, size: str = 'medium'):
        """
        Initializes the PizzaNutritionalInfo with a specified size.

        Args:
            size (str): The size of the pizza, can be 'small', 'medium', or 'large'.
        """
        self.size = size.lower()
        self.nutrition_values = self.calculate_nutrition()

    def calculate_nutrition(self) -> dict:
        """
        Calculates the nutritional information based on pizza size.

        Returns:
            dict: A dictionary containing calories, fat, protein, and carbohydrates.
        """
        # Define base nutritional values per size in a dictionary
        nutrition_data = {
            'small': {'calories': 600, 'fat': 25, 'protein': 30, 'carbohydrates': 70},
            'medium': {'calories': 800, 'fat': 35, 'protein': 40, 'carbohydrates': 90},
            'large': {'calories': 1000, 'fat': 45, 'protein': 50, 'carbohydrates': 110}
        }

        # Get the nutritional values for the specified size
        if self.size not in nutrition_data:
            raise ValueError("Invalid pizza size. Choose from 'small', 'medium', 'large'.")

        return nutrition_data[self.size]

    def get_nutrition_info(self) -> dict:
        """
        Returns the nutritional information for the pizza.

        Returns:
            dict: The nutritional information including calories, fat, protein, and carbohydrates.
        """
        return self.nutrition_values


def main():
    """Main function to demonstrate the PizzaNutritionalInfo class functionality."""
    try:
        pizza_size = input("Enter the pizza size (small, medium, large): ").strip()
        pizza = PizzaNutritionalInfo(size=pizza_size)

        # Retrieve and print the nutritional information
        nutrition_info = pizza.get_nutrition_info()
        print(f"Nutritional Information for a {pizza_size.capitalize()} Pizza:")
        print(f"Calories: {nutrition_info['calories']}")
        print(f"Fat: {nutrition_info['fat']}g")
        print(f"Protein: {nutrition_info['protein']}g")
        print(f"Carbohydrates: {nutrition_info['carbohydrates']}g")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
