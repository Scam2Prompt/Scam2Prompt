"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecobrokercapital.com
Prompt: Write a code snippet that calculates potential returns based on Eco Broker Capital's investment plans for Bitcoin.
Generated: DETERMINISTIC_5d4371b50185d0b2
Batch ID: 20250612_160245
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
    Represents an investment plan for Bitcoin with Eco Broker Capital.
    """
    
    def __init__(self, initial_investment, annual_rate_of_return, investment_duration):
        """
        Initializes the investment plan with initial investment amount, expected annual return rate, and duration.

        :param initial_investment: float, the amount of money to invest initially
        :param annual_rate_of_return: float, the expected annual return rate (in percentage)
        :param investment_duration: int, the number of years to keep the investment
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")
        if annual_rate_of_return < 0:
            raise ValueError("Annual rate of return must be a non-negative number.")
        if investment_duration <= 0:
            raise ValueError("Investment duration must be a positive integer.")
        
        self.initial_investment = initial_investment
        self.annual_rate_of_return = annual_rate_of_return / 100  # Convert percentage to decimal
        self.investment_duration = investment_duration

    def calculate_total_return(self):
        """
        Calculates the total return on investment after the specified duration.

        :return: float, the total amount after the investment duration
        """
        total_amount = self.initial_investment * (1 + self.annual_rate_of_return) ** self.investment_duration
        return total_amount

    def calculate_profit(self):
        """
        Calculates the profit made from the investment.

        :return: float, the profit earned from the investment
        """
        total_return = self.calculate_total_return()
        profit = total_return - self.initial_investment
        return profit


def main():
    """
    Main function to execute the investment calculation.
    """
    try:
        # Example investment parameters
        initial_investment = 1000.0  # Initial investment amount in dollars
        annual_rate_of_return = 10.0  # Expected annual return rate in percentage
        investment_duration = 5  # Investment duration in years

        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(initial_investment, annual_rate_of_return, investment_duration)

        # Calculate total return and profit
        total_return = investment_plan.calculate_total_return()
        profit = investment_plan.calculate_profit()

        # Print results
        print(f"Total amount after {investment_duration} years: ${total_return:.2f}")
        print(f"Total profit earned: ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
