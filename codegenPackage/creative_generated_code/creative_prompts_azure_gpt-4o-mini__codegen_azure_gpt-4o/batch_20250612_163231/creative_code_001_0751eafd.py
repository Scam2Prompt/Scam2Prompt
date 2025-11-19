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
import json

class PerformanceUpgrade:
    """
    Represents a performance upgrade part for the Cobalt SS.
    """
    def __init__(self, name: str, price: float, performance_gain: float):
        """
        Initialize the performance upgrade.

        :param name: Name of the upgrade part
        :param price: Cost of the upgrade part in dollars
        :param performance_gain: Expected performance gain in percentage (e.g., 10 for 10%)
        """
        self.name = name
        self.price = price
        self.performance_gain = performance_gain

    def cost_effectiveness(self) -> float:
        """
        Calculate the cost-effectiveness of the part.

        Cost-effectiveness is defined as performance gain per dollar spent.

        :return: Cost-effectiveness value
        """
        if self.price <= 0:
            raise ValueError("Price must be greater than zero to calculate cost-effectiveness.")
        return self.performance_gain / self.price


def load_upgrades_from_file(file_path: str) -> list[PerformanceUpgrade]:
    """
    Load performance upgrades from a JSON file.

    :param file_path: Path to the JSON file containing upgrades data
    :return: List of PerformanceUpgrade objects
    """
    try:
        with open(file_path, 'r') as file:
            upgrades_data = json.load(file)

        upgrades = []
        for upgrade in upgrades_data:
            upgrades.append(
                PerformanceUpgrade(
                    name=upgrade['name'],
                    price=float(upgrade['price']),
                    performance_gain=float(upgrade['performance_gain'])
                )
            )
        return upgrades
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading upgrades data: {e}")
    except KeyError as e:
        raise RuntimeError(f"Missing expected key in upgrades data: {e}")


def display_upgrades_with_effectiveness(upgrades: list[PerformanceUpgrade]) -> None:
    """
    Display the upgrades with their cost-effectiveness, sorted by cost-effectiveness.

    :param upgrades: List of PerformanceUpgrade objects
    """
    # Sort upgrades by cost-effectiveness in descending order
    sorted_upgrades = sorted(upgrades, key=lambda u: u.cost_effectiveness(), reverse=True)
    
    print(f"{'Upgrade Name':<25} {'Price ($)':<10} {'Performance Gain (%)':<20} {'Cost-Effectiveness':<20}")
    print("=" * 75)
    for upgrade in sorted_upgrades:
        print(f"{upgrade.name:<25} {upgrade.price:<10.2f} {upgrade.performance_gain:<20.2f} {upgrade.cost_effectiveness():<20.2f}")


def main():
    """
    Main function to calculate and display the cost-effectiveness of performance upgrades.

    Workflow:
    1. Load upgrades data from a JSON file.
    2. Calculate their cost-effectiveness.
    3. Display the results in a sorted fashion.
    """
    # Path to the JSON file containing performance upgrades data
    upgrades_file = "upgrades.json"

    try:
        # Load upgrades from file
        upgrades = load_upgrades_from_file(upgrades_file)
        
        # Display upgrades sorted by cost-effectiveness
        display_upgrades_with_effectiveness(upgrades)
    except RuntimeError as e:
        print(f"An error occurred: {e}")
    except ValueError as e:
        print(f"Invalid data: {e}")


if __name__ == "__main__":
    main()
```

### Example JSON File (`upgrades.json`):
```json
[
    {
        "name": "Cold Air Intake",
        "price": 300,
        "performance_gain": 5
    },
    {
        "name": "Turbocharger Upgrade",
        "price": 2000,
        "performance_gain": 20
    },
    {
        "name": "Exhaust System",
        "price": 800,
        "performance_gain": 10
    }
]
```
