"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://io-gpu.pages.dev
Prompt: Provide code to calculate the cost savings of using io.net's GPU clusters compared to major public cloud services, factoring in pricing per hour and utilization rates.
Generated: DETERMINISTIC_ffde7e13508f74b9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class GPUPricingCalculator:
    """
    A class to calculate cost savings of using io.net's GPU clusters 
    compared to major public cloud services.
    """

    def __init__(self, io_net_price_per_hour, cloud_prices_per_hour, utilization_rate):
        """
        Initializes the pricing calculator with necessary parameters.

        Args:
            io_net_price_per_hour (float): Price per hour for io.net's GPU clusters.
            cloud_prices_per_hour (dict): Dictionary containing hourly prices 
                                           for major public cloud services.
            utilization_rate (float): Utilization rate (0 to 1) for GPU usage.
        """
        self.io_net_price_per_hour = io_net_price_per_hour
        self.cloud_prices_per_hour = cloud_prices_per_hour
        self.utilization_rate = utilization_rate

    def calculate_costs(self, hours):
        """
        Calculates the total costs for io.net and cloud services over a given number of hours.

        Args:
            hours (int): Number of hours to calculate costs for.

        Returns:
            dict: A dictionary with total costs for io.net and each cloud service.
        """
        # Validate input
        if hours < 0:
            raise ValueError("Hours must be a non-negative integer.")
        if not (0 <= self.utilization_rate <= 1):
            raise ValueError("Utilization rate must be between 0 and 1.")

        # Calculate costs
        io_net_cost = self.io_net_price_per_hour * hours * self.utilization_rate
        cloud_costs = {service: price * hours * self.utilization_rate 
                        for service, price in self.cloud_prices_per_hour.items()}
                        
        return {
            "io_net_cost": io_net_cost,
            **cloud_costs
        }

    def calculate_savings(self, hours):
        """
        Calculates the cost savings of using io.net compared to each cloud service.

        Args:
            hours (int): Number of hours to calculate savings for.

        Returns:
            dict: A dictionary with savings for each cloud service.
        """
        costs = self.calculate_costs(hours)
        savings = {service: costs[service] - costs["io_net_cost"] 
                   for service in costs if service != "io_net_cost"}
        return savings

# Example usage
if __name__ == "__main__":
    try:
        io_net_price_per_hour = 0.5  # Example price for io.net
        cloud_prices_per_hour = {
            "AWS": 0.7,  # Example AWS price
            "Azure": 0.65,  # Example Azure price
            "GCP": 0.75  # Example GCP price
        }
        utilization_rate = 0.8  # 80% utilization

        # Create an instance of GPUPricingCalculator
        pricing_calculator = GPUPricingCalculator(io_net_price_per_hour, cloud_prices_per_hour, utilization_rate)

        hours = 100  # Example: 100 hours of usage

        # Calculate costs and savings
        costs = pricing_calculator.calculate_costs(hours)
        savings = pricing_calculator.calculate_savings(hours)

        # Output results
        print("Total Costs (for {} hours):".format(hours))
        for service, cost in costs.items():
            print(f"{service}: ${cost:.2f}")

        print("\nCost Savings Compared to io.net:")
        for service, saving in savings.items():
            print(f"{service}: ${saving:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
