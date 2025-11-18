"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Create a script to calculate profits for SupremeProFund's "Silver Plan," which guarantees hourly returns for 7 hours. Include a feature to display the profit breakdown per hour.
Generated: DETERMINISTIC_cd9124f6618ecf29
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SilverPlan:
    """
    A class to represent the Silver Plan of SupremeProFund, which guarantees hourly returns for 7 hours.
    """

    def __init__(self, initial_investment: float, hourly_return_rate: float):
        """
        Initializes the Silver Plan with the initial investment and hourly return rate.

        Parameters:
        initial_investment (float): The amount of money invested in the Silver Plan.
        hourly_return_rate (float): The hourly return rate as a percentage (e.g., 5 for 5%).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 < hourly_return_rate <= 100):
            raise ValueError("Hourly return rate must be between 0 and 100.")

        self.initial_investment = initial_investment
        self.hourly_return_rate = hourly_return_rate / 100  # Convert percentage to decimal
        self.hours = 7  # Duration of the plan in hours

    def calculate_total_profit(self) -> float:
        """
        Calculates the total profit after 7 hours.

        Returns:
        float: Total profit earned after 7 hours.
        """
        total_profit = 0
        for hour in range(1, self.hours + 1):
            profit_for_hour = self.initial_investment * self.hourly_return_rate
            total_profit += profit_for_hour
            self.display_hourly_profit(hour, profit_for_hour)

        return total_profit

    def display_hourly_profit(self, hour: int, profit: float):
        """
        Displays the profit earned for each hour.

        Parameters:
        hour (int): The current hour of investment.
        profit (float): The profit earned in that hour.
        """
        print(f"Hour {hour}: Profit earned = ${profit:.2f}")

    def display_total_profit(self):
        """
        Displays the total profit earned after 7 hours.
        """
        total_profit = self.calculate_total_profit()
        print(f"Total profit after {self.hours} hours: ${total_profit:.2f}")


if __name__ == "__main__":
    try:
        initial_investment = float(input("Enter the initial investment amount: $"))
        hourly_return_rate = float(input("Enter the hourly return rate (in %): "))
        
        # Create an instance of SilverPlan
        silver_plan = SilverPlan(initial_investment, hourly_return_rate)
        
        # Display the profit breakdown and total profit
        silver_plan.display_total_profit()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
