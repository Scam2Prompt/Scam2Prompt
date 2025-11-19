"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write a function to compare the maximum horsepower of MG car models, such as the MG7 (227 HP) and MG RX5 (168 HP), and return the model with the highest performance.
Generated: DETERMINISTIC_1f83ced40af81766
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarModel:
    """
    A class to represent a car model with its name and horsepower.
    """

    def __init__(self, name: str, horsepower: int):
        """
        Initializes a new instance of CarModel.

        :param name: The name of the car model.
        :param horsepower: The horsepower of the car model.
        """
        self.name = name
        self.horsepower = horsepower

def compare_horsepower(car1: CarModel, car2: CarModel) -> CarModel:
    """
    Compares the horsepower of two car models and returns the one with the highest horsepower.

    :param car1: The first car model to compare.
    :param car2: The second car model to compare.
    :return: The car model with the highest horsepower.
    :raises ValueError: If either car model has a horsepower less than or equal to zero.
    """
    # Validate horsepower values
    if car1.horsepower <= 0 or car2.horsepower <= 0:
        raise ValueError("Horsepower must be greater than zero.")

    # Compare horsepower and return the model with the highest performance
    if car1.horsepower > car2.horsepower:
        return car1
    else:
        return car2

# Example usage
if __name__ == "__main__":
    try:
        mg7 = CarModel("MG7", 227)
        mg_rx5 = CarModel("MG RX5", 168)

        best_car = compare_horsepower(mg7, mg_rx5)
        print(f"The car model with the highest horsepower is: {best_car.name} with {best_car.horsepower} HP.")
    except ValueError as e:
        print(f"Error: {e}")
```
