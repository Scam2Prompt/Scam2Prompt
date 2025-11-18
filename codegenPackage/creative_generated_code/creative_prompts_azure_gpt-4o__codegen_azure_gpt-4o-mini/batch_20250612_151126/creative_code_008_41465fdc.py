"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Write a program to compare battery storage options for solar energy systems, inspired by Chico Electric's solar energy solutions.
Generated: DETERMINISTIC_41465fdcef029124
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class BatteryStorageOption:
    """
    A class to represent a battery storage option for solar energy systems.
    """
    
    def __init__(self, name, capacity_kWh, efficiency, cost_usd, lifespan_years):
        """
        Initializes a BatteryStorageOption instance.

        :param name: Name of the battery storage option.
        :param capacity_kWh: Energy capacity of the battery in kilowatt-hours.
        :param efficiency: Efficiency of the battery (0 to 1).
        :param cost_usd: Cost of the battery in USD.
        :param lifespan_years: Lifespan of the battery in years.
        """
        self.name = name
        self.capacity_kWh = capacity_kWh
        self.efficiency = efficiency
        self.cost_usd = cost_usd
        self.lifespan_years = lifespan_years

    def cost_per_kWh(self):
        """
        Calculates the cost per usable kilowatt-hour of the battery.

        :return: Cost per usable kWh.
        """
        usable_capacity = self.capacity_kWh * self.efficiency
        return self.cost_usd / usable_capacity

    def total_cost_over_lifespan(self):
        """
        Calculates the total cost of the battery over its lifespan.

        :return: Total cost in USD over the lifespan.
        """
        return self.cost_usd / self.lifespan_years


def compare_battery_options(battery_options):
    """
    Compares a list of battery storage options and returns the best one based on cost per usable kWh.

    :param battery_options: List of BatteryStorageOption instances.
    :return: The BatteryStorageOption with the lowest cost per usable kWh.
    """
    if not battery_options:
        raise ValueError("No battery options provided for comparison.")

    best_option = min(battery_options, key=lambda option: option.cost_per_kWh())
    return best_option


def main():
    """
    Main function to execute battery storage comparison.
    """
    try:
        # Create a list of battery storage options
        battery_options = [
            BatteryStorageOption("Battery A", 10, 0.9, 8000, 10),
            BatteryStorageOption("Battery B", 15, 0.85, 12000, 15),
            BatteryStorageOption("Battery C", 8, 0.95, 6000, 8),
        ]

        # Compare battery options
        best_battery = compare_battery_options(battery_options)

        # Output the best battery option
        print(f"The best battery option is: {best_battery.name}")
        print(f"Cost per usable kWh: ${best_battery.cost_per_kWh():.2f}")
        print(f"Total cost over lifespan: ${best_battery.total_cost_over_lifespan():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
