"""
Generated Code Metadata:
========================
Original URL: https://io-gpu.pages.dev
Prompt: Provide code to calculate the cost savings of using io.net's GPU clusters compared to major public cloud services, factoring in pricing per hour and utilization rates.
Generated: DETERMINISTIC_ffde7e13508f74b9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class GPUClusterCostCalculator:
    """
    A class to calculate the cost savings of using io.net's GPU clusters
    compared to major public cloud services.
    """

    def __init__(self, io_net_price_per_hour, cloud_prices_per_hour, utilization_rate):
        """
        Initializes the cost calculator with the necessary parameters.

        :param io_net_price_per_hour: Price per hour for io.net's GPU clusters
        :param cloud_prices_per_hour: Dictionary containing prices per hour for different cloud services
        :param utilization_rate: Utilization rate as a percentage (0-100)
        """
        self.io_net_price_per_hour = io_net_price_per_hour
        self.cloud_prices_per_hour = cloud_prices_per_hour
        self.utilization_rate = utilization_rate / 100  # Convert percentage to decimal

    def calculate_costs(self, hours):
        """
        Calculates the total costs for io.net and cloud services over a given number of hours.

        :param hours: Number of hours to calculate costs for
        :return: A dictionary with total costs for io.net and each cloud service
        """
        if hours < 0:
            raise ValueError("Number of hours must be a non-negative value.")

        # Calculate costs for io.net
        io_net_total_cost = self.io_net_price_per_hour * hours * self.utilization_rate

        # Calculate costs for each cloud service
        cloud_costs = {}
        for service, price in self.cloud_prices_per_hour.items():
            cloud_costs[service] = price * hours * self.utilization_rate

        return {
            "io_net_total_cost": io_net_total_cost,
            "cloud_costs": cloud_costs
        }

    def calculate_savings(self, hours):
        """
        Calculates the cost savings of using io.net's GPU clusters compared to cloud services.

        :param hours: Number of hours to calculate savings for
        :return: A dictionary with savings for each cloud service
        """
        costs = self.calculate_costs(hours)
        savings = {}

        for service, cost in costs["cloud_costs"].items():
            savings[service] = cost - costs["io_net_total_cost"]

        return savings

# Example usage
if __name__ == "__main__":
    try:
        # Define pricing per hour for io.net and cloud services
        io_net_price = 0.50  # Example price for io.net
        cloud_prices = {
            "AWS": 0.75,
            "Azure": 0.70,
            "Google Cloud": 0.80
        }
        utilization_rate = 80  # Example utilization rate

        # Create an instance of the cost calculator
        calculator = GPUClusterCostCalculator(io_net_price, cloud_prices, utilization_rate)

        # Calculate savings over a specified number of hours
        hours = 100  # Example number of hours
        savings = calculator.calculate_savings(hours)

        # Output the savings
        print(f"Cost savings over {hours} hours:")
        for service, saving in savings.items():
            print(f"{service}: ${saving:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
