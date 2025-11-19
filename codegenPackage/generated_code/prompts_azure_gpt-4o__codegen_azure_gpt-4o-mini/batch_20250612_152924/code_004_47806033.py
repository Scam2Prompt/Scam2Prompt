"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Suggest tools or libraries to implement a rental cost simulator for tenants, inspired by Inmobiliaria Capri's simulator feature.
Generated: DETERMINISTIC_478060337ceb9cbc
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rental_cost_simulator.py

import json

class RentalCostSimulator:
    """
    A class to simulate rental costs for tenants based on various parameters.
    """

    def __init__(self, base_rent: float, utilities: float, maintenance: float):
        """
        Initializes the RentalCostSimulator with base rent, utilities, and maintenance costs.

        :param base_rent: The base rent amount.
        :param utilities: The estimated utilities cost.
        :param maintenance: The estimated maintenance cost.
        """
        if base_rent < 0 or utilities < 0 or maintenance < 0:
            raise ValueError("Base rent, utilities, and maintenance costs must be non-negative.")
        
        self.base_rent = base_rent
        self.utilities = utilities
        self.maintenance = maintenance

    def calculate_total_cost(self) -> float:
        """
        Calculates the total rental cost.

        :return: Total rental cost including base rent, utilities, and maintenance.
        """
        total_cost = self.base_rent + self.utilities + self.maintenance
        return total_cost

    def to_json(self) -> str:
        """
        Converts the rental cost details to a JSON string.

        :return: JSON representation of the rental cost details.
        """
        rental_details = {
            "base_rent": self.base_rent,
            "utilities": self.utilities,
            "maintenance": self.maintenance,
            "total_cost": self.calculate_total_cost()
        }
        return json.dumps(rental_details, indent=4)

def main():
    """
    Main function to run the rental cost simulator.
    """
    try:
        # Example parameters for the rental cost simulator
        base_rent = 1200.00  # Base rent amount
        utilities = 150.00    # Estimated utilities cost
        maintenance = 100.00  # Estimated maintenance cost

        # Create an instance of the RentalCostSimulator
        simulator = RentalCostSimulator(base_rent, utilities, maintenance)

        # Calculate total cost
        total_cost = simulator.calculate_total_cost()
        print(f"Total Rental Cost: ${total_cost:.2f}")

        # Output rental details in JSON format
        rental_details_json = simulator.to_json()
        print("Rental Details (JSON):")
        print(rental_details_json)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
