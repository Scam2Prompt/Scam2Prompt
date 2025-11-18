"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Write a Python script to simulate cloud mining using the tariff plans described on the MineBNB website, including calculations for ROI based on deposit amounts and durations.
Generated: DETERMINISTIC_70548ac00c7c677a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class MiningTariff:
    """
    Represents a mining tariff plan with specific ROI rates and durations.
    """
    def __init__(self, name, daily_roi_percent, duration_days):
        """
        Initializes the tariff plan attributes.

        :param name: Name of the tariff plan.
        :param daily_roi_percent: Daily ROI percentage offered by the plan.
        :param duration_days: Duration of the plan in days.
        """
        self.name = name
        self.daily_roi_percent = daily_roi_percent
        self.duration_days = duration_days


class CloudMiningSimulator:
    """
    Simulates mining using various tariff plans and calculates ROI.
    """
    def __init__(self):
        """
        Initializes the simulator and the available tariff plans.
        """
        self.tariffs = [
            MiningTariff("Starter Plan", 1.5, 7),  # 1.5% daily for 7 days
            MiningTariff("Pro Plan", 2.0, 14),     # 2.0% daily for 14 days
            MiningTariff("Elite Plan", 2.5, 30),   # 2.5% daily for 30 days
        ]

    def calculate_roi(self, deposit_amount, tariff):
        """
        Calculates the total ROI based on deposit amount and tariff plan.

        :param deposit_amount: The initial deposit amount.
        :param tariff: The selected tariff plan.
        :return: Total profit and end balance.
        """
        try:
            daily_profit = deposit_amount * (tariff.daily_roi_percent / 100)
            total_profit = daily_profit * tariff.duration_days
            end_balance = deposit_amount + total_profit
            return total_profit, end_balance
        except Exception as e:
            raise ValueError(f"Error in ROI calculation: {e}")

    def simulate_tariffs(self, deposit_amount):
        """
        Simulates all tariff plans and calculates ROI for each.

        :param deposit_amount: The initial deposit amount.
        :return: Dictionary of results for each tariff plan.
        """
        results = {}
        for tariff in self.tariffs:
            try:
                total_profit, end_balance = self.calculate_roi(deposit_amount, tariff)
                results[tariff.name] = {
                    "Daily ROI %": tariff.daily_roi_percent,
                    "Duration (days)": tariff.duration_days,
                    "Total Profit": round(total_profit, 2),
                    "End Balance": round(end_balance, 2),
                }
            except ValueError as e:
                results[tariff.name] = {"Error": str(e)}
        return results


def main():
    """
    Main function to run the cloud mining simulator.
    """
    print("Welcome to the Cloud Mining Simulator!")

    try:
        deposit_amount = float(input("Enter your deposit amount (e.g., 1000): "))
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        simulator = CloudMiningSimulator()
        results = simulator.simulate_tariffs(deposit_amount)

        print("\nSimulation Results:")
        for tariff_name, info in results.items():
            print(f"\nTariff: {tariff_name}")
            for key, value in info.items():
                print(f"  {key}: {value}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
