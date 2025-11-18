"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Develop a cloud mining simulation program that mimics the advanced mining technology described on Capitalhandelssystem. Include options for selecting different investment plans and calculating potential returns.
Generated: DETERMINISTIC_e1946922a0f8785c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import time
import logging

# Set up logging for the program
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CloudMiningSimulation:
    def __init__(self):
        """
        Initialize investment plans with their respective ROI percentages.
        """
        self.investment_plans = {
            "Basic": {"rate": 0.05, "description": "5% ROI per day"},
            "Standard": {"rate": 0.10, "description": "10% ROI per day"},
            "Premium": {"rate": 0.15, "description": "15% ROI per day"},
        }

    def display_investment_plans(self):
        """
        Display available investment plans to the user.
        """
        print("\nAvailable Investment Plans:")
        for plan, details in self.investment_plans.items():
            print(f"{plan}: {details['description']}")
        print("\n")

    def calculate_returns(self, plan, investment, days):
        """
        Calculate potential returns for the selected plan.

        :param plan: Investment plan chosen by the user
        :param investment: Amount invested by the user
        :param days: Number of days the investment will run
        :return: Total return after the specified number of days
        """
        try:
            roi_rate = self.investment_plans[plan]["rate"]
            total_return = investment * ((1 + roi_rate) ** days)
            return round(total_return, 2)
        except KeyError:
            raise ValueError("Invalid plan selected. Please choose a valid plan.")

    def run_simulation(self):
        """
        Main method to run the cloud mining simulation.
        """
        print("Welcome to Cloud Mining Simulation!")
        self.display_investment_plans()

        try:
            # Get user input for investment plan
            plan = input("Enter the investment plan (Basic, Standard, Premium): ").strip()
            if plan not in self.investment_plans:
                raise ValueError("Invalid investment plan selected.")

            # Get user input for investment amount
            investment = float(input("Enter the investment amount in USD: "))
            if investment <= 0:
                raise ValueError("Investment amount must be greater than zero.")

            # Get user input for duration
            days = int(input("Enter the number of days to run the investment: "))
            if days <= 0:
                raise ValueError("Number of days must be greater than zero.")

            # Calculate and display the total return
            total_return = self.calculate_returns(plan, investment, days)
            print(f"\nInvestment Plan: {plan}")
            print(f"Investment Amount: ${investment}")
            print(f"Duration: {days} days")
            print(f"Total Return: ${total_return}")

        except ValueError as e:
            logging.error(f"Input error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

        print("\nThank you for using Cloud Mining Simulation!")
        time.sleep(2)  # Simulate program closing

# Entry point for the program
if __name__ == "__main__":
    simulator = CloudMiningSimulation()
    simulator.run_simulation()
```
