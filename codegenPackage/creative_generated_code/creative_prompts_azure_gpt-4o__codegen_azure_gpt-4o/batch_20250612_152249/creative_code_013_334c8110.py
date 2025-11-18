"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Write a Python program to calculate profits from cryptocurrency farming and staking, inspired by Ark Capital Markets' services.
Generated: DETERMINISTIC_334c8110d78e4ca3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CryptoProfitCalculator:
    """
    A class to calculate profits from cryptocurrency farming and staking.
    Inspired by Ark Capital Markets' services.
    """
    def __init__(self):
        # Initialize profit data for farming and staking
        self.profits = {
            "farming": [],
            "staking": []
        }

    def add_farming_income(self, date, amount, expenses):
        """
        Records income and expenses for farming on a specific date.
        :param date: str - Date of the income in YYYY-MM-DD format.
        :param amount: float - Income generated from farming.
        :param expenses: float - Expenses incurred for farming.
        """
        if amount < 0 or expenses < 0:
            raise ValueError("Income and expenses must be non-negative.")
        profit = amount - expenses
        self.profits["farming"].append({
            "date": date,
            "amount": amount,
            "expenses": expenses,
            "profit": profit
        })

    def add_staking_income(self, date, rewards, staking_fee):
        """
        Records rewards and fees for staking on a specific date.
        :param date: str - Date of the income in YYYY-MM-DD format.
        :param rewards: float - Rewards earned through staking.
        :param staking_fee: float - Fee for staking services.
        """
        if rewards < 0 or staking_fee < 0:
            raise ValueError("Rewards and staking fees must be non-negative.")
        profit = rewards - staking_fee
        self.profits["staking"].append({
            "date": date,
            "rewards": rewards,
            "staking_fee": staking_fee,
            "profit": profit
        })

    def calculate_total_profit(self):
        """
        Calculates the total profits from farming and staking.
        :return: dict - Total profits categorized under 'farming' and 'staking'.
        """
        total_farming_profit = sum(entry["profit"] for entry in self.profits["farming"])
        total_staking_profit = sum(entry["profit"] for entry in self.profits["staking"])
        return {
            "total_farming_profit": total_farming_profit,
            "total_staking_profit": total_staking_profit,
            "grand_total_profit": total_farming_profit + total_staking_profit
        }

    def export_to_json(self, file_name="profits.json"):
        """
        Exports the profit data to a JSON file.
        :param file_name: str - Name of the file to export the data.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.profits, file, indent=4)
            print(f"Profit data successfully exported to {file_name}")
        except Exception as e:
            print(f"Error while exporting data to file: {e}")

if __name__ == "__main__":
    try:
        # Instantiate the CryptoProfitCalculator
        calculator = CryptoProfitCalculator()

        # Add farming income (example data)
        calculator.add_farming_income(date="2023-10-01", amount=1000.0, expenses=200.0)
        calculator.add_farming_income(date="2023-10-05", amount=1500.0, expenses=300.0)

        # Add staking income (example data)
        calculator.add_staking_income(date="2023-10-02", rewards=500.0, staking_fee=50.0)
        calculator.add_staking_income(date="2023-10-06", rewards=800.0, staking_fee=80.0)

        # Calculate total profit
        total_profit = calculator.calculate_total_profit()
        print("Total Profits:", total_profit)

        # Export profit data to JSON file
        calculator.export_to_json()
    except Exception as e:
        print(f"An error occurred: {e}")
```
