"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerspluslimited.com
Prompt: Write Python code to simulate the daily profit calculation for the "Basic Plan" offered by minerspluslimited.com, which provides 5% daily profit for 2 days with a minimum deposit of $100.
Generated: DETERMINISTIC_dc1bc4575d462384
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BasicPlan:
    def __init__(self, deposit_amount):
        """
        Initializes the BasicPlan with the deposit amount.
        
        :param deposit_amount: The amount to be deposited (minimum $100).
        :raises ValueError: If deposit amount is less than $100.
        """
        if deposit_amount < 100:
            raise ValueError("Minimum deposit amount is $100.")
        
        self.deposit_amount = deposit_amount
        self.daily_profit_rate = 0.05  # 5% daily profit
        self.total_days = 2  # Duration of the plan in days
    
    def calculate_daily_profit(self):
        """
        Calculates the daily profit for the duration of the plan.
        
        :return: A list containing the profit for each day.
        """
        daily_profits = []
        for day in range(1, self.total_days + 1):
            profit = self.deposit_amount * self.daily_profit_rate
            daily_profits.append(profit)
            print(f"Day {day}: Profit = ${profit:.2f}")

        return daily_profits

    def calculate_total_profit(self):
        """
        Calculates the total profit accumulated over the duration of the plan.
        
        :return: Total profit amount.
        """
        total_profit = sum(self.calculate_daily_profit())
        print(f"Total Profit over {self.total_days} days: ${total_profit:.2f}")
        return total_profit


# Example usage:
if __name__ == "__main__":
    try:
        deposit = float(input("Enter your deposit amount (minimum $100): "))
        plan = BasicPlan(deposit)
        plan.calculate_total_profit()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
