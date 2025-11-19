"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Generate code to automate the calculation of installation costs for air conditioning systems based on the BTU range (e.g., 7000-16000 BTU) and the pricing details listed on Frigoterm.ro.
Generated: DETERMINISTIC_5f04fb16f6304e64
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# air_conditioning_cost_calculator.py

class AirConditioningSystem:
    def __init__(self, btu_range, price):
        """
        Initialize an AirConditioningSystem object.

        Args:
            btu_range (str): The BTU range of the air conditioning system (e.g., "7000-16000").
            price (float): The price of the air conditioning system.
        """
        self.btu_range = btu_range
        self.price = price

    def __str__(self):
        return f"Air Conditioning System - BTU Range: {self.btu_range}, Price: {self.price}"


class InstallationCostCalculator:
    def __init__(self, systems):
        """
        Initialize an InstallationCostCalculator object.

        Args:
            systems (list[AirConditioningSystem]): A list of AirConditioningSystem objects.
        """
        self.systems = systems
        self.installation_costs = {
            "7000-10000": 200,
            "10001-14000": 300,
            "14001-16000": 400,
            "16001-20000": 500,
            "20001-25000": 600,
        }

    def calculate_installation_cost(self, btu):
        """
        Calculate the installation cost based on the BTU range.

        Args:
            btu (int): The BTU of the air conditioning system.

        Returns:
            float: The installation cost.

        Raises:
            ValueError: If the BTU is not within a known range.
        """
        for btu_range, cost in self.installation_costs.items():
            min_btu, max_btu = map(int, btu_range.split("-"))
            if min_btu <= btu <= max_btu:
                return cost
        raise ValueError("BTU is not within a known range")

    def get_system_price(self, btu_range):
        """
        Get the price of an air conditioning system based on its BTU range.

        Args:
            btu_range (str): The BTU range of the air conditioning system.

        Returns:
            float: The price of the air conditioning system.

        Raises:
            ValueError: If the BTU range is not found.
        """
        for system in self.systems:
            if system.btu_range == btu_range:
                return system.price
        raise ValueError("BTU range not found")

    def calculate_total_cost(self, btu_range, btu):
        """
        Calculate the total cost of an air conditioning system, including installation.

        Args:
            btu_range (str): The BTU range of the air conditioning system.
            btu (int): The BTU of the air conditioning system.

        Returns:
            float: The total cost.

        Raises:
            ValueError: If the BTU range or BTU is not valid.
        """
        system_price = self.get_system_price(btu_range)
        installation_cost = self.calculate_installation_cost(btu)
        return system_price + installation_cost


def main():
    # Pricing details from Frigoterm.ro (example data)
    systems = [
        AirConditioningSystem("7000-10000", 1000),
        AirConditioningSystem("10001-14000", 1200),
        AirConditioningSystem("14001-16000", 1500),
        AirConditioningSystem("16001-20000", 1800),
        AirConditioningSystem("20001-25000", 2000),
    ]

    calculator = InstallationCostCalculator(systems)

    # Example usage
    btu_range = "7000-10000"
    btu = 9000
    try:
        total_cost = calculator.calculate_total_cost(btu_range, btu)
        print(f"Total cost for {btu_range} BTU range and {btu} BTU: {total_cost}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
