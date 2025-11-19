"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Compare and contrast the benefits of using sea freight versus land transport for shipping goods within Pakistan, referencing the services provided by Portline Shipping & Logistic.
Generated: DETERMINISTIC_b694cfc135bea249
Batch ID: 20250622_205306
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

class TransportMode:
    """Base class for transport modes."""

    def __init__(self, name, cost_per_km, cost_per_ton):
        """
        Initialize transport mode.

        Args:
            name (str): Name of transport mode.
            cost_per_km (float): Cost per kilometer.
            cost_per_ton (float): Cost per ton.
        """
        self.name = name
        self.cost_per_km = cost_per_km
        self.cost_per_ton = cost_per_ton

    def calculate_cost(self, distance, weight):
        """
        Calculate transport cost.

        Args:
            distance (float): Distance in kilometers.
            weight (float): Weight in tons.

        Returns:
            float: Total transport cost.
        """
        return distance * self.cost_per_km + weight * self.cost_per_ton


class SeaFreight(TransportMode):
    """Sea freight transport mode."""

    def __init__(self, cost_per_km=0.05, cost_per_ton=50):
        """
        Initialize sea freight.

        Args:
            cost_per_km (float, optional): Cost per kilometer. Defaults to 0.05.
            cost_per_ton (float, optional): Cost per ton. Defaults to 50.
        """
        super().__init__("Sea Freight", cost_per_km, cost_per_ton)


class LandTransport(TransportMode):
    """Land transport mode."""

    def __init__(self, cost_per_km=0.10, cost_per_ton=100):
        """
        Initialize land transport.

        Args:
            cost_per_km (float, optional): Cost per kilometer. Defaults to 0.10.
            cost_per_ton (float, optional): Cost per ton. Defaults to 100.
        """
        super().__init__("Land Transport", cost_per_km, cost_per_ton)


class PortlineShipping:
    """Portline Shipping & Logistic services."""

    def __init__(self):
        self.services = {
            "sea_freight": SeaFreight(),
            "land_transport": LandTransport(),
        }

    def compare_transport_modes(self, distance, weight):
        """
        Compare transport modes.

        Args:
            distance (float): Distance in kilometers.
            weight (float): Weight in tons.

        Returns:
            dict: Comparison of transport modes.
        """
        results = {}
        for mode, transport in self.services.items():
            cost = transport.calculate_cost(distance, weight)
            results[mode] = {
                "name": transport.name,
                "cost": cost,
            }
        return results


def main():
    try:
        # Initialize Portline Shipping & Logistic services
        portline = PortlineShipping()

        # Define shipping parameters
        distance = 1000  # kilometers
        weight = 10  # tons

        # Compare transport modes
        results = portline.compare_transport_modes(distance, weight)

        # Print comparison results
        print("Comparison of Transport Modes:")
        for mode, result in results.items():
            print(f"Mode: {result['name']}, Cost: PKR {result['cost']:.2f}")

        # Determine the most cost-effective mode
        most_cost_effective_mode = min(results, key=lambda x: results[x]['cost'])
        print(f"\nMost Cost-Effective Mode: {results[most_cost_effective_mode]['name']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
