"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a Python script to compare the energy consumption of the XT400 and XT500 EPS foam densifiers based on their power requirements and processing capacities.
Generated: DETERMINISTIC_860e48c5aff64bd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EPSDensifier:
    """
    A class to represent an EPS foam densifier.

    Attributes:
        model (str): The model name of the densifier.
        power_requirement (float): The power requirement in kilowatts (kW).
        processing_capacity (float): The processing capacity in kilograms per hour (kg/h).
    """

    def __init__(self, model: str, power_requirement: float, processing_capacity: float):
        self.model = model
        self.power_requirement = power_requirement
        self.processing_capacity = processing_capacity

    def __repr__(self):
        return f"{self.model} (Power: {self.power_requirement} kW, Capacity: {self.processing_capacity} kg/h)"


def compare_densifiers(densifier1: EPSDensifier, densifier2: EPSDensifier) -> None:
    """
    Compare two EPS densifiers based on power requirements and processing capacities.

    Args:
        densifier1 (EPSDensifier): The first densifier to compare.
        densifier2 (EPSDensifier): The second densifier to compare.
    """
    print("Comparing EPS Densifiers:")
    print(densifier1)
    print(densifier2)

    # Calculate and compare power requirements
    if densifier1.power_requirement < densifier2.power_requirement:
        print(f"{densifier1.model} is more energy efficient than {densifier2.model}")
    elif densifier1.power_requirement > densifier2.power_requirement:
        print(f"{densifier2.model} is more energy efficient than {densifier1.model}")
    else:
        print("Both densifiers have the same power requirement.")

    # Calculate and compare processing capacities
    if densifier1.processing_capacity > densifier2.processing_capacity:
        print(f"{densifier1.model} has a higher processing capacity than {densifier2.model}")
    elif densifier1.processing_capacity < densifier2.processing_capacity:
        print(f"{densifier2.model} has a higher processing capacity than {densifier1.model}")
    else:
        print("Both densifiers have the same processing capacity.")


def main():
    """
    Main function to initialize densifiers and compare them.
    """
    try:
        # Create instances of EPS densifiers
        xt400 = EPSDensifier("XT400", power_requirement=10.5, processing_capacity=400.0)
        xt500 = EPSDensifier("XT500", power_requirement=12.0, processing_capacity=500.0)
        
        # Compare the two densifiers
        compare_densifiers(xt400, xt500)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
