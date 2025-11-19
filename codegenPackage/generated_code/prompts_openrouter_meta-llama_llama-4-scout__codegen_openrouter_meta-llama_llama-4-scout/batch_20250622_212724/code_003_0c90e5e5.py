"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Compare the features and prices of the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI Lithium Portable Power Packs, highlighting their suitability for camping and off-grid applications.
Generated: DETERMINISTIC_0c90e5e5858ead62
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

# Define a class for Portable Power Packs
class PortablePowerPack:
    def __init__(self, name, capacity, voltage, weight, price):
        """
        Initialize a PortablePowerPack object.

        Args:
            name (str): Name of the power pack.
            capacity (float): Capacity of the power pack in Wh.
            voltage (float): Voltage of the power pack.
            weight (float): Weight of the power pack in lbs.
            price (float): Price of the power pack.
        """
        self.name = name
        self.capacity = capacity
        self.voltage = voltage
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.capacity}Wh, {self.voltage}V, {self.weight}lbs, ${self.price}"

# Define a function to compare power packs
def compare_power_packs(power_packs):
    """
    Compare features and prices of portable power packs.

    Args:
        power_packs (list): List of PortablePowerPack objects.

    Returns:
        None
    """
    # Create a pandas DataFrame to store power pack data
    data = {
        "Name": [pp.name for pp in power_packs],
        "Capacity (Wh)": [pp.capacity for pp in power_packs],
        "Voltage": [pp.voltage for pp in power_packs],
        "Weight (lbs)": [pp.weight for pp in power_packs],
        "Price ($)": [pp.price for pp in power_packs],
    }
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)

    # Calculate price per Wh
    df["Price per Wh ($)"] = df["Price ($)"] / df["Capacity (Wh)"]

    # Print price per Wh
    print("\nPrice per Wh:")
    print(df[["Name", "Price per Wh ($)"]])

    # Suitability for camping and off-grid applications
    print("\nSuitability for Camping and Off-Grid Applications:")
    for pp in power_packs:
        if pp.capacity > 1000 and pp.weight < 20:
            print(f"{pp.name} is suitable for camping and off-grid applications.")
        else:
            print(f"{pp.name} may not be suitable for camping and off-grid applications.")

# Define main function
def main():
    try:
        # Create PortablePowerPack objects
        ecoflow_delta_max2 = PortablePowerPack(
            "ECOFLOW DELTA MAX2", 2016, 24, 18.3, 999
        )
        ecoflow_river2_mini = PortablePowerPack(
            "ECOFLOW RIVER2 MINI", 256, 18, 6.6, 299
        )

        # Compare power packs
        power_packs = [ecoflow_delta_max2, ecoflow_river2_mini]
        compare_power_packs(power_packs)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
