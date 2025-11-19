"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Generate a Python script to calculate the cost-effectiveness of various performance upgrades for a Cobalt SS, considering factors like the price of parts and expected performance gains.
Generated: DETERMINISTIC_0751eafd3e7b8d00
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PerformanceUpgrade:
    """
    A class to represent a performance upgrade for a Cobalt SS.
    
    Attributes:
        name (str): The name of the performance upgrade.
        price (float): The cost of the upgrade in dollars.
        performance_gain (float): The expected performance gain in horsepower.
    """

    def __init__(self, name: str, price: float, performance_gain: float):
        """
        Initializes a new PerformanceUpgrade instance.

        Args:
            name (str): The name of the performance upgrade.
            price (float): The cost of the upgrade in dollars.
            performance_gain (float): The expected performance gain in horsepower.
        """
        self.name = name
        self.price = price
        self.performance_gain = performance_gain

    def cost_effectiveness(self) -> float:
        """
        Calculates the cost-effectiveness of the performance upgrade.

        Returns:
            float: The cost per horsepower gained.
        """
        if self.performance_gain <= 0:
            raise ValueError("Performance gain must be greater than zero.")
        return self.price / self.performance_gain


def main():
    """
    Main function to calculate and display the cost-effectiveness of various performance upgrades.
    """
    # List of performance upgrades
    upgrades = [
        PerformanceUpgrade("Cold Air Intake", 300, 15),
        PerformanceUpgrade("Turbocharger", 2500, 100),
        PerformanceUpgrade("Exhaust System", 800, 25),
        PerformanceUpgrade("ECU Tune", 500, 20),
        PerformanceUpgrade("Intercooler", 1200, 40)
    ]

    # Prepare data for DataFrame
    data = {
        "Upgrade": [],
        "Price ($)": [],
        "Performance Gain (hp)": [],
        "Cost Effectiveness ($/hp)": []
    }

    # Calculate cost-effectiveness for each upgrade
    for upgrade in upgrades:
        try:
            effectiveness = upgrade.cost_effectiveness()
            data["Upgrade"].append(upgrade.name)
            data["Price ($)"].append(upgrade.price)
            data["Performance Gain (hp)"].append(upgrade.performance_gain)
            data["Cost Effectiveness ($/hp)"].append(effectiveness)
        except ValueError as e:
            print(f"Error calculating cost-effectiveness for {upgrade.name}: {e}")

    # Create a DataFrame for better visualization
    df = pd.DataFrame(data)

    # Sort by cost-effectiveness
    df.sort_values(by="Cost Effectiveness ($/hp)", inplace=True)

    # Display the results
    print(df)


if __name__ == "__main__":
    main()
```
