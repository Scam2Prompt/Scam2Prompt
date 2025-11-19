"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Compare the specifications of Yanmar ViO12, ViO17, ViO25, and ViO35 mini excavators, focusing on their engine power, weight, and digging depth.
Generated: DETERMINISTIC_ab8216a8a499fda5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define a class to represent a mini excavator
class MiniExcavator:
    def __init__(self, model, engine_power, weight, digging_depth):
        """
        Initialize a MiniExcavator instance.

        :param model: str - The model name of the excavator
        :param engine_power: float - The engine power in horsepower (HP)
        :param weight: float - The weight of the excavator in kilograms (kg)
        :param digging_depth: float - The maximum digging depth in meters (m)
        """
        self.model = model
        self.engine_power = engine_power
        self.weight = weight
        self.digging_depth = digging_depth

    def __repr__(self):
        return f"{self.model}: Engine Power: {self.engine_power} HP, Weight: {self.weight} kg, Digging Depth: {self.digging_depth} m"


def compare_excavators(excavators):
    """
    Compare the specifications of a list of mini excavators.

    :param excavators: list - A list of MiniExcavator instances
    :return: pd.DataFrame - A DataFrame containing the specifications of the excavators
    """
    # Create a DataFrame from the excavator data
    data = {
        "Model": [excavator.model for excavator in excavators],
        "Engine Power (HP)": [excavator.engine_power for excavator in excavators],
        "Weight (kg)": [excavator.weight for excavator in excavators],
        "Digging Depth (m)": [excavator.digging_depth for excavator in excavators],
    }
    
    return pd.DataFrame(data)


def main():
    # Define the specifications for each Yanmar mini excavator
    excavators = [
        MiniExcavator("Yanmar ViO12", engine_power=12.5, weight=1200, digging_depth=2.3),
        MiniExcavator("Yanmar ViO17", engine_power=17.5, weight=1700, digging_depth=2.8),
        MiniExcavator("Yanmar ViO25", engine_power=24.8, weight=2500, digging_depth=3.2),
        MiniExcavator("Yanmar ViO35", engine_power=34.4, weight=3500, digging_depth=3.6),
    ]

    # Compare the excavators and display the results
    try:
        comparison_df = compare_excavators(excavators)
        print(comparison_df)
    except Exception as e:
        print(f"An error occurred while comparing excavators: {e}")


if __name__ == "__main__":
    main()
```
