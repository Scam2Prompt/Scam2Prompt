"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Generate a Python script to calculate the cost-effectiveness of various performance upgrades for a Cobalt SS, considering factors like the price of parts and expected performance gains.
Generated: DETERMINISTIC_0751eafd3e7b8d00
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class PerformanceUpgrade:
    """
    A class to represent a performance upgrade for a Cobalt SS.
    
    Attributes:
        name (str): The name of the performance upgrade.
        cost (float): The cost of the upgrade in dollars.
        performance_gain (float): The expected performance gain in horsepower.
    """

    def __init__(self, name: str, cost: float, performance_gain: float):
        """
        Initializes the PerformanceUpgrade instance.

        Args:
            name (str): The name of the performance upgrade.
            cost (float): The cost of the upgrade in dollars.
            performance_gain (float): The expected performance gain in horsepower.
        """
        self.name = name
        self.cost = cost
        self.performance_gain = performance_gain

    def cost_effectiveness(self) -> float:
        """
        Calculates the cost-effectiveness of the upgrade.

        Returns:
            float: The cost per horsepower gained.
        """
        if self.performance_gain <= 0:
            raise ValueError(f"Performance gain must be greater than zero. Current: {self.performance_gain}")
        
        return self.cost / self.performance_gain


def main():
    # Define a list of upgrades with their respective costs and performance gains
    upgrades_data = [
        {"name": "Cold Air Intake", "cost": 300, "performance_gain": 10},
        {"name": "Turbo Upgrade", "cost": 1500, "performance_gain": 50},
        {"name": "Exhaust System", "cost": 800, "performance_gain": 20},
        {"name": "ECU Tune", "cost": 400, "performance_gain": 25},
        {"name": "Intercooler", "cost": 600, "performance_gain": 30},
    ]

    # List to hold PerformanceUpgrade objects
    upgrades = []

    # Create PerformanceUpgrade objects and populate the list
    for upgrade in upgrades_data:
        try:
            upgrades.append(PerformanceUpgrade(upgrade["name"], upgrade["cost"], upgrade["performance_gain"]))
        except Exception as e:
            print(f"Error creating upgrade {upgrade['name']}: {e}")

    # Calculate cost-effectiveness for each upgrade and store results in a DataFrame
    results = []
    for upgrade in upgrades:
        try:
            effectiveness = upgrade.cost_effectiveness()
            results.append({"Upgrade": upgrade.name, "Cost": upgrade.cost, "Performance Gain": upgrade.performance_gain, "Cost per HP": effectiveness})
        except ValueError as e:
            print(f"Error calculating cost-effectiveness for {upgrade.name}: {e}")

    # Create a DataFrame to display results
    df_results = pd.DataFrame(results)

    # Sort the DataFrame by cost per horsepower gained
    df_results.sort_values(by="Cost per HP", ascending=True, inplace=True)

    # Display the results
    print(df_results)

if __name__ == "__main__":
    main()
```
