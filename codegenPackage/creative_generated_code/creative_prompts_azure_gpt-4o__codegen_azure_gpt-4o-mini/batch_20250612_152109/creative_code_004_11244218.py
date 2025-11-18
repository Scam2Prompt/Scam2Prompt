"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Develop a function in Python to calculate the cooking time for a Pavo a la Caja China, using the meat capacity and dimensions of the Caja China models provided on Meat Master.
Generated: DETERMINISTIC_11244218a294ff9e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CajaChina:
    """
    A class to represent a Caja China model for cooking Pavo a la Caja China.
    """

    def __init__(self, model_name: str, dimensions: tuple, capacity: float):
        """
        Initialize the Caja China model.

        :param model_name: The name of the Caja China model.
        :param dimensions: A tuple containing the dimensions (length, width, height) in inches.
        :param capacity: The maximum weight capacity in pounds.
        """
        self.model_name = model_name
        self.dimensions = dimensions  # Expected format: (length, width, height)
        self.capacity = capacity

    def calculate_cooking_time(self, weight: float) -> float:
        """
        Calculate the cooking time for Pavo a la Caja China based on the weight of the turkey.

        :param weight: The weight of the turkey in pounds.
        :return: Cooking time in hours.
        :raises ValueError: If weight exceeds capacity or is negative.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if weight > self.capacity:
            raise ValueError(f"Weight exceeds the capacity of {self.capacity} pounds for this model.")

        # General cooking time rule for turkey in Caja China
        cooking_time_per_pound = 1.5  # hours per pound
        cooking_time = weight * cooking_time_per_pound
        
        return cooking_time


def main():
    """
    Main function to demonstrate the cooking time calculation.
    """
    # Define a Caja China model (example values)
    model = CajaChina(model_name="Caja China Model X", dimensions=(48, 24, 30), capacity=60)

    # Example weight of the turkey
    turkey_weight = 20  # in pounds

    try:
        cooking_time = model.calculate_cooking_time(turkey_weight)
        print(f"Cooking time for a {turkey_weight} lb turkey in {model.model_name} is {cooking_time} hours.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
