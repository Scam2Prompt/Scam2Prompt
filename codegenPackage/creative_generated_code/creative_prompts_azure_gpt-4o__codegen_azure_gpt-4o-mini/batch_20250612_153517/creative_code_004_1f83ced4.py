"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a function to compare the maximum horsepower of MG car models, such as the MG7 (227 HP) and MG RX5 (168 HP), and return the model with the highest performance.
Generated: DETERMINISTIC_1f83ced40af81766
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarModel:
    """Represents a car model with a name and horsepower."""
    
    def __init__(self, name: str, horsepower: int):
        """Initializes the CarModel instance.

        Args:
            name (str): The name of the car model.
            horsepower (int): The horsepower of the car model.
        """
        self.name = name
        self.horsepower = horsepower

def compare_horsepower(car1: CarModel, car2: CarModel) -> CarModel:
    """Compares the horsepower of two car models.

    Args:
        car1 (CarModel): The first car model to compare.
        car2 (CarModel): The second car model to compare.

    Returns:
        CarModel: The car model with the highest horsepower.

    Raises:
        ValueError: If either car model has an invalid horsepower value.
    """
    # Validate horsepower
    if car1.horsepower < 0 or car2.horsepower < 0:
        raise ValueError("Horsepower must be a non-negative integer.")

    # Compare horsepower
    if car1.horsepower > car2.horsepower:
        return car1
    elif car2.horsepower > car1.horsepower:
        return car2
    else:
        raise ValueError("Both cars have the same horsepower.")

# Example usage
if __name__ == "__main__":
    try:
        mg7 = CarModel("MG7", 227)
        mg_rx5 = CarModel("MG RX5", 168)

        best_car = compare_horsepower(mg7, mg_rx5)
        print(f"The car model with the highest performance is: {best_car.name} ({best_car.horsepower} HP)")
    except ValueError as e:
        print(f"Error: {e}")
```
