"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Generate code to simulate the effect of river diversion on local ecosystems, inspired by the campaigns against river exploitation discussed by "Čuvari Šare."
Generated: DETERMINISTIC_b253ce56ea4adb72
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class River:
    """Class to represent the river and its characteristics."""
    def __init__(self, name, flow_rate, biodiversity_level):
        """
        Initialize the river object.

        :param name: Name of the river
        :param flow_rate: Water flow rate in cubic meters per second
        :param biodiversity_level: Biodiversity level of the river ecosystem (scale of 1 to 100)
        """
        self.name = name
        self.flow_rate = flow_rate
        self.biodiversity_level = biodiversity_level

    def divert_water(self, diversion_amount):
        """
        Simulates water diversion and its impact on flow rate.

        :param diversion_amount: Amount of water diverted (in cubic meters per second)
        :return: None
        """
        if diversion_amount < 0:
            raise ValueError("Diversion amount must be non-negative.")
        if diversion_amount > self.flow_rate:
            raise ValueError("Diversion amount cannot exceed current flow rate.")
        self.flow_rate -= diversion_amount

    def simulate_ecosystem_impact(self):
        """
        Simulates the impact of reduced flow rate on biodiversity.

        :return: New biodiversity level
        """
        if self.flow_rate <= 0:
            # Severe impact: river has dried up, biodiversity collapses
            self.biodiversity_level = 0
        else:
            # Gradual impact: lower flow reduces biodiversity proportionally
            impact_factor = random.uniform(0.5, 0.8)  # Randomized impact multiplier
            self.biodiversity_level *= impact_factor
            self.biodiversity_level = max(0, self.biodiversity_level)
        return self.biodiversity_level


def simulate_river_diversion():
    """
    Main function to simulate river diversion effects on ecosystems.
    """
    try:
        # Initialize a river
        river = River(name="Šara River", flow_rate=500, biodiversity_level=80)
        print(f"Initial state of {river.name}:")
        print(f"Flow Rate: {river.flow_rate} m³/s, Biodiversity Level: {river.biodiversity_level}/100")

        # Simulate water diversion
        diversion_amount = random.randint(50, 300)  # Random diversion amount
        print(f"\nDiverting {diversion_amount} m³/s of water...")
        river.divert_water(diversion_amount)

        # Simulate ecosystem impact
        new_biodiversity_level = river.simulate_ecosystem_impact()
        print(f"\nAfter water diversion:")
        print(f"Flow Rate: {river.flow_rate} m³/s, Biodiversity Level: {new_biodiversity_level:.2f}/100")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the simulation
if __name__ == "__main__":
    simulate_river_diversion()
```
