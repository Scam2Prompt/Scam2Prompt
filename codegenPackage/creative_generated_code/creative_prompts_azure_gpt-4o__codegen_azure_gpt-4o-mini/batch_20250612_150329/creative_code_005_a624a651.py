"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Write a script to automate the calculation of total returns for Renzo Cash's investment packages, including conditions for daily or monthly withdrawals.
Generated: DETERMINISTIC_a624a6510aeebfe3
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPackage:
    """
    Class to represent an investment package.
    Attributes:
        principal (float): The initial amount invested.
        daily_interest_rate (float): Daily interest rate as a decimal (e.g., 0.01 for 1%).
        monthly_interest_rate (float): Monthly interest rate as a decimal (e.g., 0.03 for 3%).
        duration_days (int): Duration of the investment in days.
        withdrawal_frequency (str): Frequency of withdrawals ('daily' or 'monthly').
    """

    def __init__(self, principal, daily_interest_rate, monthly_interest_rate, duration_days, withdrawal_frequency):
        """
        Initialize the investment package with provided parameters.
        
        Args:
            principal (float): Initial investment amount.
            daily_interest_rate (float): Daily interest rate.
            monthly_interest_rate (float): Monthly interest rate.
            duration_days (int): Duration of the investment in days.
            withdrawal_frequency (str): Frequency of withdrawals ('daily' or 'monthly').
        """
        self.principal = principal
        self.daily_interest_rate = daily_interest_rate
        self.monthly_interest_rate = monthly_interest_rate
        self.duration_days = duration_days
        self.withdrawal_frequency = withdrawal_frequency.lower()

        if self.withdrawal_frequency not in ['daily', 'monthly']:
            raise ValueError("withdrawal_frequency must be either 'daily' or 'monthly'.")

    def calculate_returns(self):
        """
        Calculate the total returns based on the investment package's parameters.
        
        Returns:
            float: The total returns after the specified duration.
        """
        total_returns = self.principal

        # Calculate returns based on withdrawal frequency
        if self.withdrawal_frequency == 'daily':
            for day in range(self.duration_days):
                total_returns += total_returns * self.daily_interest_rate
        elif self.withdrawal_frequency == 'monthly':
            # Monthly interest is applied at the end of each month
            total_months = self.duration_days // 30
            for month in range(total_months):
                total_returns += total_returns * self.monthly_interest_rate

        return total_returns

def main():
    """
    Main function to execute the investment return calculation.
    """
    try:
        # Example investment parameters
        principal = 10000.0  # Initial investment amount
        daily_interest_rate = 0.01  # Daily interest rate
        monthly_interest_rate = 0.03  # Monthly interest rate
        duration_days = 90  # Duration of the investment in days
        withdrawal_frequency = 'monthly'  # Frequency of withdrawals

        # Create an InvestmentPackage instance
        investment_package = InvestmentPackage(principal, daily_interest_rate, monthly_interest_rate, duration_days, withdrawal_frequency)
        
        # Calculate total returns
        total_returns = investment_package.calculate_returns()
        print(f"Total returns after {duration_days} days with {withdrawal_frequency} withdrawals: ${total_returns:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
