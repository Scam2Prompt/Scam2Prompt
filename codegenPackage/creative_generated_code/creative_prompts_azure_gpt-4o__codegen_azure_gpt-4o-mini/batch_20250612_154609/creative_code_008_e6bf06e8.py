"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Write code to simulate the investment growth over time for ZenixGlobaltrade's plans, including Starter, Classic, Professional, and Premium, with user-defined deposit amounts.
Generated: DETERMINISTIC_e6bf06e8a3da51e0
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan with its growth properties.
    """
    def __init__(self, name, interest_rate, duration_years):
        """
        Initializes the investment plan with a name, interest rate, and duration.

        :param name: str - The name of the investment plan
        :param interest_rate: float - Annual interest rate (as a percentage)
        :param duration_years: int - Duration of the investment in years
        """
        self.name = name
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_growth(self, deposit_amount):
        """
        Calculates the future value of the investment based on deposit amount.

        :param deposit_amount: float - The initial deposit amount
        :return: float - The future value of the investment after the specified duration
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount must be a non-negative value.")
        
        future_value = deposit_amount * (1 + self.interest_rate) ** self.duration_years
        return future_value


def main():
    """
    Main function to simulate investment growth for different plans.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Starter", 5.0, 5),
        InvestmentPlan("Classic", 7.0, 10),
        InvestmentPlan("Professional", 10.0, 15),
        InvestmentPlan("Premium", 12.0, 20)
    ]

    try:
        # User input for deposit amount
        deposit_amount = float(input("Enter the deposit amount: "))

        # Calculate and display investment growth for each plan
        for plan in plans:
            future_value = plan.calculate_growth(deposit_amount)
            print(f"Investment growth in the {plan.name} plan over {plan.duration_years} years: ${future_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
