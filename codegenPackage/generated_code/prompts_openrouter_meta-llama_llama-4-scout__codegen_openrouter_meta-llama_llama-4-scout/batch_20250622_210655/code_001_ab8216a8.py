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
# Define a class for mini excavators
class MiniExcavator:
    def __init__(self, name, engine_power, weight, digging_depth):
        """
        Initialize a mini excavator object.

        Args:
            name (str): Name of the excavator model.
            engine_power (float): Engine power in horsepower (hp).
            weight (float): Operating weight in kilograms (kg).
            digging_depth (float): Maximum digging depth in millimeters (mm).
        """
        self.name = name
        self.engine_power = engine_power
        self.weight = weight
        self.digging_depth = digging_depth

# Define a function to compare excavator specifications
def compare_excavators(excavators):
    """
    Compare the specifications of multiple mini excavators.

    Args:
        excavators (list[MiniExcavator]): List of mini excavator objects.

    Returns:
        None
    """
    # Print header
    print(f"{'Name':^15} | {'Engine Power (hp)':^15} | {'Weight (kg)':^15} | {'Digging Depth (mm)':^15}")
    print("-" * 65)

    # Print specifications for each excavator
    for excavator in excavators:
        print(f"{excavator.name:^15} | {excavator.engine_power:^15.2f} | {excavator.weight:^15.2f} | {excavator.digging_depth:^15.2f}")

# Define main function with example usage
def main():
    try:
        # Create mini excavator objects
        vio12 = MiniExcavator("Yanmar ViO12", 9.5, 1220, 2830)
        vio17 = MiniExcavator("Yanmar ViO17", 14.5, 1630, 3050)
        vio25 = MiniExcavator("Yanmar ViO25", 22.5, 2480, 3620)
        vio35 = MiniExcavator("Yanmar ViO35", 33.5, 3530, 4050)

        # Compare excavator specifications
        excavators = [vio12, vio17, vio25, vio35]
        compare_excavators(excavators)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
