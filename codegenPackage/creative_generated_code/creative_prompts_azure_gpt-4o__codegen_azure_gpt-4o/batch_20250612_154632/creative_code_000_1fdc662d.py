"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volatilityindexlimited.com
Prompt: Write a Python script to simulate cryptocurrency investment returns based on a fixed payout schedule, as described on volatilityindexlimited.com.
Generated: DETERMINISTIC_1fdc662d69d1c329
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sys

class CryptoInvestmentSimulator:
    """
    A class to simulate cryptocurrency investment returns based on a fixed payout schedule.
    """

    def __init__(self, principal, annual_rate, investment_duration_days):
        """
        Initializes the investment simulator.

        :param principal: Initial investment amount in USD.
        :param annual_rate: Annual payout rate as a percentage (e.g., 10 for 10%).
        :param investment_duration_days: Duration of investment in days.
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.investment_duration_days = investment_duration_days

        # Validate input
        if principal <= 0 or annual_rate <= 0 or investment_duration_days <= 0:
            raise ValueError("Principal, annual_rate, and investment_duration_days must be positive values.")

    def calculate_daily_rate(self):
        """
        Calculates the daily payout rate based on the annual rate.

        :return: Daily payout rate as a decimal.
        """
        return self.annual_rate / 100 / 365

    def simulate_returns(self):
        """
        Simulates the investment returns over the specified duration.

        :return: A list of dictionaries detailing daily balances and payouts.
        """
        daily_rate = self.calculate_daily_rate()
        balance = self.principal
        result = []

        for day in range(self.investment_duration_days):
            payout = balance * daily_rate  # Daily payout
            balance += payout  # Update balance
            result.append({
                "day": day + 1,
                "date": datetime.date.today() + datetime.timedelta(days=day),
                "daily_payout": round(payout, 2),
                "balance": round(balance, 2)
            })

        return result

    def display_results(self, results):
        """
        Displays the simulation results in a readable format.

        :param results: The list of daily investment returns data.
        """
        print("Day | Date       | Daily Payout (USD) | Balance (USD)")
        print("-" * 50)
        for record in results:
            print(f"{record['day']:3} | {record['date']} | {record['daily_payout']:>17.2f} | {record['balance']:>13.2f}")


# Main execution block
if __name__ == "__main__":
    try:
        # Input parameters
        principal = float(input("Enter investment principal (USD): "))
        annual_rate = float(input("Enter annual return rate (%): "))
        investment_duration_days = int(input("Enter investment duration (days): "))

        # Run simulation
        simulator = CryptoInvestmentSimulator(principal, annual_rate, investment_duration_days)
        results = simulator.simulate_returns()

        # Display results
        simulator.display_results(results)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        sys.exit(1)
```
