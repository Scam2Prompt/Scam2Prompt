"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Generate a Python script to calculate potential profits based on the Fintradeoptions investment plans, including Starter, Premium, and Advanced options.
Generated: DETERMINISTIC_7099cde9f2da098f
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FintradeOptions:
    def __init__(self):
        """Initialize investment plans with their respective profit percentages."""
        self.plans = {
            "Starter": 0.05,  # 5% profit
            "Premium": 0.10,  # 10% profit
            "Advanced": 0.15  # 15% profit
        }

    def calculate_profit(self, plan: str, investment: float) -> float:
        """
        Calculate the potential profit based on the investment plan.

        :param plan: The investment plan (Starter, Premium, Advanced)
        :param investment: The amount invested
        :return: The potential profit from the investment
        :raises ValueError: If the plan is not recognized or investment is negative
        """
        # Validate the investment amount
        if investment < 0:
            raise ValueError("Investment amount cannot be negative.")

        # Validate the investment plan
        if plan not in self.plans:
            raise ValueError(f"Invalid investment plan: {plan}. Valid options are: {', '.join(self.plans.keys())}")

        # Calculate profit
        profit = investment * self.plans[plan]
        return profit

def main():
    """Main function to execute the profit calculation."""
    fintrade = FintradeOptions()

    # Example usage
    try:
        # Get user input for investment plan and amount
        plan = input("Enter the investment plan (Starter, Premium, Advanced): ").strip()
        investment = float(input("Enter the investment amount: "))

        # Calculate potential profit
        profit = fintrade.calculate_profit(plan, investment)

        # Display the result
        print(f"The potential profit from the {plan} plan with an investment of ${investment:.2f} is: ${profit:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
