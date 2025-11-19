"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Using the Gree air conditioner specifications provided on the website, write Python code to calculate the total cost of ownership over 5 years, factoring in the initial purchase price and estimated annual energy consumption.
Generated: DETERMINISTIC_aecc02e1f6e4cec1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditioner:
    """
    A class to represent an air conditioner and calculate its total cost of ownership.
    """

    def __init__(self, purchase_price: float, annual_energy_consumption: float, energy_cost_per_kwh: float):
        """
        Initializes the AirConditioner with purchase price, annual energy consumption, and energy cost per kWh.

        :param purchase_price: Initial purchase price of the air conditioner
        :param annual_energy_consumption: Estimated annual energy consumption in kWh
        :param energy_cost_per_kwh: Cost of energy per kWh
        """
        self.purchase_price = purchase_price
        self.annual_energy_consumption = annual_energy_consumption
        self.energy_cost_per_kwh = energy_cost_per_kwh

    def calculate_annual_energy_cost(self) -> float:
        """
        Calculates the annual energy cost based on energy consumption and cost per kWh.

        :return: Annual energy cost
        """
        return self.annual_energy_consumption * self.energy_cost_per_kwh

    def calculate_total_cost_of_ownership(self, years: int) -> float:
        """
        Calculates the total cost of ownership over a specified number of years.

        :param years: Number of years to calculate the total cost of ownership
        :return: Total cost of ownership
        """
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")
        
        annual_cost = self.calculate_annual_energy_cost()
        total_energy_cost = annual_cost * years
        total_cost = self.purchase_price + total_energy_cost
        
        return total_cost


def main():
    """
    Main function to execute the cost of ownership calculation.
    """
    try:
        # Example values for the air conditioner
        purchase_price = 500.0  # Initial purchase price in dollars
        annual_energy_consumption = 1500.0  # Annual energy consumption in kWh
        energy_cost_per_kwh = 0.12  # Cost of energy per kWh in dollars

        # Create an instance of AirConditioner
        ac = AirConditioner(purchase_price, annual_energy_consumption, energy_cost_per_kwh)

        # Calculate total cost of ownership over 5 years
        total_cost = ac.calculate_total_cost_of_ownership(5)

        print(f"Total cost of ownership over 5 years: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
