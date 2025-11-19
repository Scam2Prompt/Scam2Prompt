"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Compare the costs of ductless mini-splits and traditional air conditioning systems for a commercial building in Fayetteville, AR, using RJW Mechanical's pricing and services as a reference.
Generated: DETERMINISTIC_f9bf50ec051095bd
Batch ID: 20250622_211659
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

class HVACSystem:
    """Base class for HVAC systems"""
    def __init__(self, name, cost_per_ton):
        """
        Initialize an HVAC system

        Args:
            name (str): Name of the HVAC system
            cost_per_ton (float): Cost per ton of the HVAC system
        """
        self.name = name
        self.cost_per_ton = cost_per_ton

    def calculate_cost(self, tons):
        """
        Calculate the total cost of the HVAC system

        Args:
            tons (float): Tons of cooling required

        Returns:
            float: Total cost of the HVAC system
        """
        return self.cost_per_ton * tons


class DuctlessMiniSplit(HVACSystem):
    """Class for ductless mini-split systems"""
    def __init__(self, cost_per_ton=1.50):
        """
        Initialize a ductless mini-split system

        Args:
            cost_per_ton (float, optional): Cost per ton of the ductless mini-split system. Defaults to 1.50.
        """
        super().__init__("Ductless Mini-Split", cost_per_ton)


class TraditionalAirConditioning(HVACSystem):
    """Class for traditional air conditioning systems"""
    def __init__(self, cost_per_ton=1.00):
        """
        Initialize a traditional air conditioning system

        Args:
            cost_per_ton (float, optional): Cost per ton of the traditional air conditioning system. Defaults to 1.00.
        """
        super().__init__("Traditional Air Conditioning", cost_per_ton)


class RJWMechanical:
    """Class for RJW Mechanical's pricing and services"""
    def __init__(self):
        """
        Initialize RJW Mechanical's pricing and services
        """
        self.ductless_mini_split_cost_per_ton = 1.40
        self.traditional_air_conditioning_cost_per_ton = 0.90

    def get_ductless_mini_split_cost(self, tons):
        """
        Get the cost of a ductless mini-split system from RJW Mechanical

        Args:
            tons (float): Tons of cooling required

        Returns:
            float: Cost of the ductless mini-split system
        """
        return self.ductless_mini_split_cost_per_ton * tons

    def get_traditional_air_conditioning_cost(self, tons):
        """
        Get the cost of a traditional air conditioning system from RJW Mechanical

        Args:
            tons (float): Tons of cooling required

        Returns:
            float: Cost of the traditional air conditioning system
        """
        return self.traditional_air_conditioning_cost_per_ton * tons


def compare_hvac_costs(tons, rjw_mechanical):
    """
    Compare the costs of ductless mini-splits and traditional air conditioning systems

    Args:
        tons (float): Tons of cooling required
        rjw_mechanical (RJWMechanical): RJW Mechanical's pricing and services

    Returns:
        dict: Comparison of the costs of ductless mini-splits and traditional air conditioning systems
    """
    ductless_mini_split = DuctlessMiniSplit(rjw_mechanical.ductless_mini_split_cost_per_ton)
    traditional_air_conditioning = TraditionalAirConditioning(rjw_mechanical.traditional_air_conditioning_cost_per_ton)

    ductless_mini_split_cost = ductless_mini_split.calculate_cost(tons)
    traditional_air_conditioning_cost = traditional_air_conditioning.calculate_cost(tons)

    rjw_ductless_mini_split_cost = rjw_mechanical.get_ductless_mini_split_cost(tons)
    rjw_traditional_air_conditioning_cost = rjw_mechanical.get_traditional_air_conditioning_cost(tons)

    return {
        "Ductless Mini-Split": ductless_mini_split_cost,
        "Traditional Air Conditioning": traditional_air_conditioning_cost,
        "RJW Ductless Mini-Split": rjw_ductless_mini_split_cost,
        "RJW Traditional Air Conditioning": rjw_traditional_air_conditioning_cost,
    }


def main():
    try:
        tons = float(input("Enter the tons of cooling required: "))
        rjw_mechanical = RJWMechanical()
        costs = compare_hvac_costs(tons, rjw_mechanical)

        print("Comparison of HVAC Costs:")
        for system, cost in costs.items():
            print(f"{system}: ${cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for tons of cooling required.")


if __name__ == "__main__":
    main()
```
