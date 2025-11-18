"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Write code to simulate the payout schedule for Smarts-invests' investment plans, including daily payments and principal return after a specified duration.
Generated: DETERMINISTIC_e82b85657d47de13
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    Class to represent an investment plan with daily payouts and principal return.
    """
    def __init__(self, principal, daily_payout_rate, duration_days):
        """
        Initialize an InvestmentPlan instance.

        :param principal: The initial investment amount.
        :param daily_payout_rate: The rate of daily payout (percentage of principal).
        :param duration_days: Duration of the investment in days.
        """
        if principal <= 0 or daily_payout_rate <= 0 or duration_days <= 0:
            raise ValueError("Principal, daily payout rate, and duration days must be greater than zero.")
        self.principal = principal
        self.daily_payout_rate = daily_payout_rate
        self.duration_days = duration_days
        self.start_date = datetime.date.today()

    def simulate_payout_schedule(self):
        """
        Simulate the payout schedule over the investment duration.

        :return: A list of dictionaries containing daily payout information.
        """
        payout_schedule = []
        daily_payout = self.principal * (self.daily_payout_rate / 100)

        for day in range(1, self.duration_days + 1):
            payout_date = self.start_date + datetime.timedelta(days=day)
            payout_schedule.append({
                "Day": day,
                "Date": payout_date.strftime('%Y-%m-%d'),
                "Daily Payout": daily_payout
            })

        # Append principal return at the end of the duration
        payout_schedule.append({
            "Day": self.duration_days + 1,
            "Date": (self.start_date + datetime.timedelta(days=self.duration_days + 1)).strftime('%Y-%m-%d'),
            "Principal Return": self.principal
        })

        return payout_schedule


def main():
    """
    Main function to demonstrate the simulation of an investment plan.
    """
    try:
        # Example investment plan
        principal = float(input("Enter the principal amount: "))
        daily_payout_rate = float(input("Enter the daily payout rate (percentage): "))
        duration_days = int(input("Enter the investment duration (in days): "))

        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(principal, daily_payout_rate, duration_days)

        # Simulate the payout schedule
        print("\nSimulating payout schedule...")
        payout_schedule = investment_plan.simulate_payout_schedule()

        # Display the schedule
        for entry in payout_schedule:
            if "Daily Payout" in entry:
                print(f"Day {entry['Day']}: Date: {entry['Date']}, Daily Payout: ${entry['Daily Payout']:.2f}")
            elif "Principal Return" in entry:
                print(f"Day {entry['Day']}: Date: {entry['Date']}, Principal Returned: ${entry['Principal Return']:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
```
