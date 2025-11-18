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

class InvestmentPlan:
    def __init__(self, name, cost, hash_rate, duration, return_rate):
        """
        Initializes an investment plan with the specified parameters.

        :param name: str - The name of the investment plan.
        :param cost: float - The cost of the investment plan.
        :param hash_rate: float - The hash rate associated with the plan (in TH/s).
        :param duration: int - The duration of the plan in days.
        :param return_rate: float - The expected return rate (as a percentage).
        """
        self.name = name
        self.cost = cost
        self.hash_rate = hash_rate
        self.duration = duration
        self.return_rate = return_rate

    def calculate_returns(self, investment):
        """
        Calculates the potential returns based on the investment amount.

        :param investment: float - The amount of investment.
        :return: float - The potential returns.
        """
        if investment < self.cost:
            raise ValueError("Investment must be greater than or equal to the plan cost.")
        
        return (investment * self.return_rate / 100) * (self.duration / 365)

class CloudMiningSimulator:
    def __init__(self):
        """
        Initializes the cloud mining simulator with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("Basic Plan", 500, 10, 30, 5),
            InvestmentPlan("Standard Plan", 1000, 20, 60, 7),
            InvestmentPlan("Premium Plan", 2000, 50, 90, 10)
        ]

    def display_plans(self):
        """
        Displays the available investment plans.
        """
        print("Available Investment Plans:")
        for idx, plan in enumerate(self.plans):
            print(f"{idx + 1}. {plan.name} - Cost: ${plan.cost}, Hash Rate: {plan.hash_rate} TH/s, "
                  f"Duration: {plan.duration} days, Return Rate: {plan.return_rate}%")

    def select_plan(self, choice):
        """
        Selects an investment plan based on user input.

        :param choice: int - The user's choice of investment plan.
        :return: InvestmentPlan - The selected investment plan.
        """
        if choice < 1 or choice > len(self.plans):
            raise IndexError("Invalid plan selection.")
        return self.plans[choice - 1]

    def run(self):
        """
        Starts the cloud mining simulation program.
        """
        try:
            self.display_plans()
            choice = int(input("Select an investment plan (1-3): "))
            selected_plan = self.select_plan(choice)

            investment = float(input(f"Enter amount to invest for {selected_plan.name} (minimum ${selected_plan.cost}): "))
            returns = selected_plan.calculate_returns(investment)

            print(f"\nInvestment Details:")
            print(f"Plan: {selected_plan.name}")
            print(f"Investment Amount: ${investment}")
            print(f"Potential Returns after {selected_plan.duration} days: ${returns:.2f}")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except IndexError as ie:
            print(f"Error: {ie}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    simulator = CloudMiningSimulator()
    simulator.run()
```
