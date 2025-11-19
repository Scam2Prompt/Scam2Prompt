"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate the optimal cooler size for a camping trip based on the Engel Coolers product line.
Generated: DETERMINISTIC_cc921f6640a3becf
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cooler_calculator.py

class EngelCooler:
    def __init__(self, model, capacity_liters, weight_kg, length_cm, width_cm, height_cm):
        """
        Initialize an Engel Cooler object.

        Args:
            model (str): Cooler model name.
            capacity_liters (float): Cooler capacity in liters.
            weight_kg (float): Cooler weight in kilograms.
            length_cm (float): Cooler length in centimeters.
            width_cm (float): Cooler width in centimeters.
            height_cm (float): Cooler height in centimeters.
        """
        self.model = model
        self.capacity_liters = capacity_liters
        self.weight_kg = weight_kg
        self.length_cm = length_cm
        self.width_cm = width_cm
        self.height_cm = height_cm

    def __str__(self):
        return f"{self.model}: {self.capacity_liters}L, {self.weight_kg}kg, {self.length_cm}cm x {self.width_cm}cm x {self.height_cm}cm"


class CoolerCalculator:
    def __init__(self):
        """
        Initialize a CoolerCalculator object with Engel Coolers product line.
        """
        self.coolers = [
            EngelCooler("MR40F-U1", 40, 12.7, 55.5, 28.5, 28.5),
            EngelCooler("MR45F-U1", 45, 14.3, 57.5, 30.5, 30.5),
            EngelCooler("MR60F-U1", 60, 18.2, 65.5, 34.5, 34.5),
            EngelCooler("MR80F-U1", 80, 22.7, 73.5, 38.5, 38.5),
            EngelCooler("MR100F-U1", 100, 27.2, 81.5, 42.5, 42.5),
        ]

    def calculate_optimal_cooler_size(self, required_capacity_liters, max_weight_kg, max_length_cm, max_width_cm, max_height_cm):
        """
        Calculate the optimal cooler size based on the given constraints.

        Args:
            required_capacity_liters (float): Required cooler capacity in liters.
            max_weight_kg (float): Maximum cooler weight in kilograms.
            max_length_cm (float): Maximum cooler length in centimeters.
            max_width_cm (float): Maximum cooler width in centimeters.
            max_height_cm (float): Maximum cooler height in centimeters.

        Returns:
            EngelCooler: Optimal cooler object or None if no suitable cooler is found.
        """
        suitable_coolers = [
            cooler
            for cooler in self.coolers
            if cooler.capacity_liters >= required_capacity_liters
            and cooler.weight_kg <= max_weight_kg
            and cooler.length_cm <= max_length_cm
            and cooler.width_cm <= max_width_cm
            and cooler.height_cm <= max_height_cm
        ]

        if not suitable_coolers:
            return None

        # Find the smallest cooler that meets the requirements
        optimal_cooler = min(suitable_coolers, key=lambda cooler: cooler.capacity_liters)
        return optimal_cooler


def main():
    calculator = CoolerCalculator()

    required_capacity_liters = float(input("Enter the required cooler capacity in liters: "))
    max_weight_kg = float(input("Enter the maximum cooler weight in kilograms: "))
    max_length_cm = float(input("Enter the maximum cooler length in centimeters: "))
    max_width_cm = float(input("Enter the maximum cooler width in centimeters: "))
    max_height_cm = float(input("Enter the maximum cooler height in centimeters: "))

    optimal_cooler = calculator.calculate_optimal_cooler_size(
        required_capacity_liters, max_weight_kg, max_length_cm, max_width_cm, max_height_cm
    )

    if optimal_cooler:
        print("Optimal cooler size:")
        print(optimal_cooler)
    else:
        print("No suitable cooler found.")


if __name__ == "__main__":
    main()
```
