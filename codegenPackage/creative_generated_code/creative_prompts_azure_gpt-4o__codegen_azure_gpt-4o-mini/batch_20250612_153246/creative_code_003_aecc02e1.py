"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Using the Gree air conditioner specifications provided on the website, write Python code to calculate the total cost of ownership over 5 years, factoring in the initial purchase price and estimated annual energy consumption.
Generated: DETERMINISTIC_aecc02e1f6e4cec1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirConditioner:
    def __init__(self, purchase_price: float, annual_energy_consumption_kwh: float, energy_cost_per_kwh: float):
        """
        Initializes the AirConditioner instance with purchase price, annual energy consumption, and energy cost.
        
        :param purchase_price: The initial purchase price of the air conditioner
        :param annual_energy_consumption_kwh: The estimated annual energy consumption in kilowatt-hours
        :param energy_cost_per_kwh: The cost of energy per kilowatt-hour
        """
        self.purchase_price = purchase_price
        self.annual_energy_consumption_kwh = annual_energy_consumption_kwh
        self.energy_cost_per_kwh = energy_cost_per_kwh

    def calculate_total_cost_of_ownership(self, years: int) -> float:
        """
        Calculates the total cost of ownership over a specified number of years.
        
        :param years: The number of years to calculate the total cost of ownership
        :return: The total cost of ownership
        """
        if years <= 0:
            raise ValueError("Number of years must be positive.")
        
        # Calculate total energy cost over the specified number of years
        total_energy_cost = self.annual_energy_consumption_kwh * self.energy_cost_per_kwh * years
        
        # Total cost is the sum of the purchase price and the total energy cost
        total_cost = self.purchase_price + total_energy_cost
        
        return total_cost

if __name__ == "__main__":
    # Example usage:
    try:
        # Replace the values below with actual specifications from the Gree air conditioner
        purchase_price = 500.0  # Example purchase price in dollars
        annual_energy_consumption_kwh = 1500.0  # Example annual energy consumption in kWh
        energy_cost_per_kwh = 0.12  # Example cost of energy per kWh in dollars
        
        # Create an instance of AirConditioner
        ac = AirConditioner(purchase_price, annual_energy_consumption_kwh, energy_cost_per_kwh)
        
        # Calculate total cost of ownership over 5 years
        total_cost = ac.calculate_total_cost_of_ownership(5)
        
        print(f"Total cost of ownership over 5 years: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
