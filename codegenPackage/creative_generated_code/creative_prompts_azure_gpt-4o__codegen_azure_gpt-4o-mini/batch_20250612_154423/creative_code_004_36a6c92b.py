"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wilsonelectronics.co
Prompt: Create a program to calculate the cost comparison between owning and renting a cellular DAS system, using the pricing models described by CellAntenna Wireless.
Generated: DETERMINISTIC_36a6c92b4a17befe
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DASSCostCalculator:
    """
    A class to calculate the cost comparison between owning and renting a cellular Distributed Antenna System (DAS).
    """

    def __init__(self, rent_price, purchase_price, installation_cost, maintenance_cost, lifespan_years):
        """
        Initializes the cost calculator with the given parameters.

        :param rent_price: Monthly rent price for the DAS system
        :param purchase_price: One-time purchase price for the DAS system
        :param installation_cost: One-time installation cost for the DAS system
        :param maintenance_cost: Annual maintenance cost for the DAS system
        :param lifespan_years: Expected lifespan of the purchased DAS system in years
        """
        self.rent_price = rent_price
        self.purchase_price = purchase_price
        self.installation_cost = installation_cost
        self.maintenance_cost = maintenance_cost
        self.lifespan_years = lifespan_years

    def calculate_rent_cost(self):
        """
        Calculate the total cost of renting the DAS system over the lifespan.

        :return: Total rent cost over the lifespan
        """
        total_rent_cost = self.rent_price * 12 * self.lifespan_years
        return total_rent_cost

    def calculate_own_cost(self):
        """
        Calculate the total cost of owning the DAS system over its lifespan.

        :return: Total ownership cost over the lifespan
        """
        total_own_cost = (self.purchase_price + self.installation_cost +
                          (self.maintenance_cost * self.lifespan_years))
        return total_own_cost

    def compare_costs(self):
        """
        Compare the total costs of renting and owning the DAS system.

        :return: A string indicating which option is cheaper
        """
        rent_cost = self.calculate_rent_cost()
        own_cost = self.calculate_own_cost()

        if rent_cost < own_cost:
            return f"Renting is cheaper over {self.lifespan_years} years. Total Rental Cost: ${rent_cost:.2f}, Total Ownership Cost: ${own_cost:.2f}."
        elif rent_cost > own_cost:
            return f"Owning is cheaper over {self.lifespan_years} years. Total Rental Cost: ${rent_cost:.2f}, Total Ownership Cost: ${own_cost:.2f}."
        else:
            return f"Both options cost the same over {self.lifespan_years} years. Total Cost: ${rent_cost:.2f}."


def main():
    """
    Main function to run the DAS cost comparison.
    """
    try:
        # Sample input values (could be replaced with user input or external data)
        rent_price = 1000  # Monthly rent cost
        purchase_price = 20000  # One-time purchase price
        installation_cost = 5000  # Installation cost
        maintenance_cost = 1200  # Annual maintenance cost
        lifespan_years = 5  # Lifespan in years

        # Create an instance of the cost calculator
        cost_calculator = DASSCostCalculator(rent_price, purchase_price, installation_cost, maintenance_cost, lifespan_years)

        # Perform cost comparison
        result = cost_calculator.compare_costs()

        # Print the result
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
