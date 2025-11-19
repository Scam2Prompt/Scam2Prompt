"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Develop a function in Python to calculate the cooking time for a Pavo a la Caja China, using the meat capacity and dimensions of the Caja China models provided on Meat Master.
Generated: DETERMINISTIC_11244218a294ff9e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pavo a la Caja China Cooking Time Calculator

This module provides a function to calculate the cooking time for a Pavo a la Caja China
based on the meat capacity and dimensions of the Caja China models.

Author: [Your Name]
Date: [Today's Date]
"""

class CajaChinaModel:
    """Represents a Caja China model with its dimensions and meat capacity."""

    def __init__(self, name, length, width, height, meat_capacity):
        """
        Initializes a CajaChinaModel instance.

        Args:
            name (str): The name of the Caja China model.
            length (float): The length of the Caja China model in inches.
            width (float): The width of the Caja China model in inches.
            height (float): The height of the Caja China model in inches.
            meat_capacity (float): The meat capacity of the Caja China model in pounds.
        """
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.meat_capacity = meat_capacity


class CookingTimeCalculator:
    """Provides a method to calculate the cooking time for a Pavo a la Caja China."""

    def __init__(self, caja_china_models):
        """
        Initializes a CookingTimeCalculator instance.

        Args:
            caja_china_models (list[CajaChinaModel]): A list of CajaChinaModel instances.
        """
        self.caja_china_models = caja_china_models

    def calculate_cooking_time(self, meat_weight, caja_china_model_name):
        """
        Calculates the cooking time for a Pavo a la Caja China.

        Args:
            meat_weight (float): The weight of the meat in pounds.
            caja_china_model_name (str): The name of the Caja China model.

        Returns:
            float: The cooking time in minutes.

        Raises:
            ValueError: If the Caja China model is not found or if the meat weight is invalid.
        """
        # Find the Caja China model by name
        caja_china_model = next((model for model in self.caja_china_models if model.name == caja_china_model_name), None)
        if caja_china_model is None:
            raise ValueError(f"Caja China model '{caja_china_model_name}' not found")

        # Validate meat weight
        if meat_weight <= 0:
            raise ValueError("Meat weight must be greater than zero")

        # Calculate cooking time based on meat weight and Caja China model capacity
        # Assuming a base cooking time of 20 minutes per 5 pounds of meat
        base_cooking_time = 20  # minutes
        cooking_time_per_5_pounds = base_cooking_time
        cooking_time = (meat_weight / 5) * cooking_time_per_5_pounds

        # Adjust cooking time based on Caja China model dimensions (assuming a larger model cooks faster)
        volume = caja_china_model.length * caja_china_model.width * caja_china_model.height
        cooking_time *= 1 / (volume / 1000)  # adjust cooking time based on volume

        return cooking_time


def main():
    # Define Caja China models
    caja_china_models = [
        CajaChinaModel("Small", 24, 12, 6, 20),
        CajaChinaModel("Medium", 30, 15, 7, 30),
        CajaChinaModel("Large", 36, 18, 8, 40),
    ]

    # Create a CookingTimeCalculator instance
    calculator = CookingTimeCalculator(caja_china_models)

    # Example usage
    meat_weight = 25  # pounds
    caja_china_model_name = "Medium"
    try:
        cooking_time = calculator.calculate_cooking_time(meat_weight, caja_china_model_name)
        print(f"Cooking time for {meat_weight} pounds of meat in a {caja_china_model_name} Caja China: {cooking_time:.2f} minutes")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
