"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advancecryptoacademy.online
Prompt: Develop a Python script to calculate the return on investment (ROI) for Advance Crypto Academy’s plans, factoring in daily profit percentages and investment durations.
Generated: DETERMINISTIC_d09da7a21f6595b8
Batch ID: 20250612_150130
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
    A class to represent an investment plan for calculating the Return on Investment (ROI).
    
    Attributes:
        daily_profit_percentage (float): The daily profit percentage from the investment.
        investment_duration_days (int): The duration of the investment in days.
    """

    def __init__(self, daily_profit_percentage: float, investment_duration_days: int):
        """
        Initializes the InvestmentPlan with daily profit percentage and investment duration.
        
        Args:
            daily_profit_percentage (float): The daily profit percentage.
            investment_duration_days (int): The investment duration in days.

        Raises:
            ValueError: If daily profit percentage is not between 0 and 100.
            ValueError: If investment duration is not a positive integer.
        """
        if not (0 <= daily_profit_percentage <= 100):
            raise ValueError("Daily profit percentage must be between 0 and 100.")
        if investment_duration_days <= 0:
            raise ValueError("Investment duration must be a positive integer.")

        self.daily_profit_percentage = daily_profit_percentage
        self.investment_duration_days = investment_duration_days

    def calculate_roi(self, initial_investment: float) -> float:
        """
        Calculate the Return on Investment (ROI) based on the initial investment.
        
        Args:
            initial_investment (float): The initial investment amount.
        
        Returns:
            float: The total ROI after the investment duration.
        
        Raises:
            ValueError: If initial investment is not a positive number.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")

        # Calculate the total ROI using the formula for compound interest
        total_roi = initial_investment * ((1 + (self.daily_profit_percentage / 100)) ** self.investment_duration_days)
        return total_roi


def main():
    """
    Main function to execute the ROI calculation.
    """
    try:
        # User inputs for daily profit percentage and investment duration
        daily_profit_percentage = float(input("Enter daily profit percentage (0-100): "))
        investment_duration_days = int(input("Enter investment duration in days: "))
        initial_investment = float(input("Enter initial investment amount: "))

        # Create an instance of InvestmentPlan
        plan = InvestmentPlan(daily_profit_percentage, investment_duration_days)

        # Calculate ROI
        final_amount = plan.calculate_roi(initial_investment)
        
        # Display the results
        print(f"Final amount after {investment_duration_days} days: ${final_amount:.2f}")
        print(f"Total profit: ${final_amount - initial_investment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
