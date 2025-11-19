"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Generate a Python script that calculates the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels, considering the 40% lighter specification mentioned on the website.
Generated: DETERMINISTIC_d56e0d245bcfb85f
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Brixton Forged Wheels Weight Savings Calculator

class Wheel:
    """
    Class representing a wheel with a specific weight.
    """

    def __init__(self, name: str, weight: float):
        """
        Initialize a Wheel instance.

        :param name: Name of the wheel.
        :param weight: Weight of the wheel in pounds.
        """
        self.name = name
        self.weight = weight

    def __str__(self):
        """Return a string representation of the wheel."""
        return f"{self.name} Wheel - Weight: {self.weight} lbs"


def calculate_weight_savings(oem_wheel: Wheel, forged_wheel: Wheel) -> float:
    """
    Calculate the weight savings between two wheels.

    :param oem_wheel: Wheel object representing the OEM wheel.
    :param forged_wheel: Wheel object representing the Brixton Forged wheel.
    :return: Weight savings in pounds.
    """
    # Validate that both weights are positive
    if oem_wheel.weight <= 0 or forged_wheel.weight <= 0:
        raise ValueError("Weights must be positive values.")

    # Calculate weight savings
    weight_savings = oem_wheel.weight - forged_wheel.weight
    return weight_savings


def main():
    """
    Main function to execute the weight savings calculation.
    """
    # Example weights (in pounds)
    try:
        oem_wheel_weight = 20.0  # Example OEM wheel weight
        forged_wheel_weight = oem_wheel_weight * 0.6  # 40% lighter

        # Create Wheel instances
        oem_wheel = Wheel("High-Performance OEM", oem_wheel_weight)
        forged_wheel = Wheel("Brixton Forged", forged_wheel_weight)

        # Print wheel details
        print(oem_wheel)
        print(forged_wheel)

        # Calculate and print weight savings
        savings = calculate_weight_savings(oem_wheel, forged_wheel)
        print(f"Weight Savings: {savings:.2f} lbs")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
