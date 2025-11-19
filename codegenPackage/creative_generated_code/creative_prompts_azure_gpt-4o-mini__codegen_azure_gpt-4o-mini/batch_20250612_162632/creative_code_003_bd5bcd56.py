"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buzo-lola.pages.dev
Prompt: Generate a Python script that calculates potential savings from participating in the Tesla Reward Programme for electric car owners.
Generated: DETERMINISTIC_bd5bcd56f46e4a6d
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TeslaRewardCalculator:
    """
    A class to calculate potential savings from participating in the Tesla Reward Programme.
    """

    def __init__(self, points_per_kwh, reward_value, monthly_usage_kwh):
        """
        Initializes the TeslaRewardCalculator with the required parameters.

        :param points_per_kwh: The number of reward points earned per kWh used.
        :param reward_value: The monetary value of each reward point.
        :param monthly_usage_kwh: The average monthly usage in kWh.
        """
        self.points_per_kwh = points_per_kwh
        self.reward_value = reward_value
        self.monthly_usage_kwh = monthly_usage_kwh

    def calculate_monthly_savings(self):
        """
        Calculates the monthly savings based on the Tesla Reward Programme.

        :return: The calculated monthly savings in currency.
        """
        total_points = self.points_per_kwh * self.monthly_usage_kwh
        monthly_savings = total_points * self.reward_value
        return monthly_savings

    def calculate_annual_savings(self):
        """
        Calculates the annual savings based on the Tesla Reward Programme.

        :return: The calculated annual savings in currency.
        """
        monthly_savings = self.calculate_monthly_savings()
        annual_savings = monthly_savings * 12
        return annual_savings

def main():
    """
    Main function to execute the savings calculation.
    """
    # Configuration for the Tesla Reward Programme
    config = {
        "points_per_kwh": 0.1,      # Example: 0.1 points per kWh
        "reward_value": 0.05,        # Example: Each point is worth $0.05
        "monthly_usage_kwh": 500     # Example: Average monthly usage of 500 kWh
    }

    try:
        # Create an instance of the calculator
        calculator = TeslaRewardCalculator(
            points_per_kwh=config["points_per_kwh"],
            reward_value=config["reward_value"],
            monthly_usage_kwh=config["monthly_usage_kwh"]
        )
        
        # Calculate savings
        monthly_savings = calculator.calculate_monthly_savings()
        annual_savings = calculator.calculate_annual_savings()

        # Output savings
        print(f"Monthly Savings: ${monthly_savings:.2f}")
        print(f"Annual Savings: ${annual_savings:.2f}")
    
    except KeyError as e:
        print(f"Configuration error: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
