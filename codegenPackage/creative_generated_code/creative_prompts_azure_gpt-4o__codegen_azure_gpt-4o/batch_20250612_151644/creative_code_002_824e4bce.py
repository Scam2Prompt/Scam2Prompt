"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Create a script to simulate MinerLab's mining plan profitability over time, factoring in plan costs, daily returns, and maintenance fees.
Generated: DETERMINISTIC_824e4bce83ef8b4e
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class MiningPlan:
    """
    Class to represent a mining plan and calculate profitability over time.
    """

    def __init__(self, plan_name, plan_cost, daily_return, maintenance_fee):
        """
        Initialize the MiningPlan object.

        :param plan_name: Name of the mining plan (string)
        :param plan_cost: Upfront cost for the mining plan (float)
        :param daily_return: Expected daily return in profit (float)
        :param maintenance_fee: Daily maintenance fee (float)
        """
        self.plan_name = plan_name
        self.plan_cost = plan_cost
        self.daily_return = daily_return
        self.maintenance_fee = maintenance_fee

    def simulate_profitability(self, duration_days):
        """
        Simulate the profitability of the mining plan over a given duration.

        :param duration_days: Number of days to simulate (integer)
        :return: List of profitability data over the duration
        """
        if duration_days <= 0:
            raise ValueError("Duration must be greater than 0 days")

        profitability_data = []
        net_profit = -self.plan_cost  # Upfront cost is subtracted initially

        for day in range(1, duration_days + 1):
            # Daily profit calculation: daily return - maintenance fee
            daily_profit = self.daily_return - self.maintenance_fee
            net_profit += daily_profit

            # Record the current day's data
            profitability_data.append({
                'day': day,
                'date': (datetime.date.today() + datetime.timedelta(days=day)).isoformat(),
                'daily_profit': daily_profit,
                'net_profit': net_profit
            })

        return profitability_data

def main():
    """
    Main function to simulate and display mining plan profitability.
    """
    try:
        # Configuration for the mining plan
        plan_name = "Premium Mining Plan"
        plan_cost = 5000.0  # $5000 upfront cost
        daily_return = 200.0  # $200 daily return
        maintenance_fee = 50.0  # $50 daily maintenance fee
        duration_days = 30  # Simulate for 30 days

        # Initialize the mining plan
        mining_plan = MiningPlan(plan_name, plan_cost, daily_return, maintenance_fee)

        # Simulate profitability
        profitability_data = mining_plan.simulate_profitability(duration_days)

        # Display results
        print(f"Profitability Simulation for: {plan_name}")
        print(f"Duration: {duration_days} days\n")
        for entry in profitability_data:
            print(f"Day {entry['day']} ({entry['date']}): Daily Profit = ${entry['daily_profit']:.2f}, "
                  f"Net Profit = ${entry['net_profit']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
