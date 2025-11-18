"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easyfxtrades-invest.com
Prompt: Write Python code to simulate daily returns for an investment plan based on the "Basic Plan" described on easyfxtrades-invest.com, which offers 5% returns for 7 days on investments between $300 and $4999.
Generated: DETERMINISTIC_0591ab8d88312ed9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class InvestmentPlan:
    """
    A class to simulate daily returns for an investment plan.
    """

    def __init__(self, principal: float):
        """
        Initialize the investment plan.

        :param principal: The initial amount of investment.
                          Must be between $300 and $4999 for the Basic Plan.
        """
        if principal < 300 or principal > 4999:
            raise ValueError("Principal amount must be between $300 and $4999 for the Basic Plan.")
        self.principal = principal
        self.daily_return_rate = 0.05  # 5% daily return
        self.duration = 7  # 7 days duration
        self.start_date = datetime.date.today()

    def simulate_daily_returns(self):
        """
        Simulates daily returns for the Basic Plan.

        :return: A list of dictionaries containing daily return details.
        """
        daily_returns = []
        current_date = self.start_date

        for day in range(1, self.duration + 1):
            # Calculate daily return as 5% of the principal
            daily_return = round(self.principal * self.daily_return_rate, 2)
            
            # Append the result to the list
            daily_returns.append({
                "Day": day,
                "Date": current_date.strftime("%Y-%m-%d"),
                "Daily Return": daily_return
            })
            
            # Move to the next day
            current_date += datetime.timedelta(days=1)

        return daily_returns

    def generate_summary(self):
        """
        Generates a summary of the investment after 7 days.

        :return: A dictionary containing the total return and ending balance.
        """
        total_return = round(self.principal * self.daily_return_rate * self.duration, 2)
        ending_balance = round(self.principal + total_return, 2)
        return {
            "Total Return": total_return,
            "Ending Balance": ending_balance
        }


def main():
    """
    Main function to execute the simulation.
    """
    try:
        # Input the principal investment amount
        principal = float(input("Enter your investment amount (between $300 and $4999): "))

        # Create an instance of InvestmentPlan
        plan = InvestmentPlan(principal)

        # Simulate daily returns
        print("\nDaily Returns:")
        daily_returns = plan.simulate_daily_returns()
        for entry in daily_returns:
            print(f"Day {entry['Day']}: {entry['Date']} - Daily Return: ${entry['Daily Return']}")

        # Generate and display summary
        summary = plan.generate_summary()
        print("\nInvestment Summary:")
        print(f"Total Return: ${summary['Total Return']}")
        print(f"Ending Balance: ${summary['Ending Balance']}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
