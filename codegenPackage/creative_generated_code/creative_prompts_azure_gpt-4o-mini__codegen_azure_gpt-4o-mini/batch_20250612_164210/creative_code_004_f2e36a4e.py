"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokentransact.net
Prompt: Develop a code example for a project investment tracker that includes features for crypto mining and energy investments as highlighted on Token Transact.
Generated: DETERMINISTIC_f2e36a4ebcabcdeb
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Investment:
    def __init__(self, name: str, amount: float, investment_type: str):
        """
        Initializes a new investment instance.

        :param name: The name of the investment (e.g., 'Bitcoin Mining').
        :param amount: The amount invested.
        :param investment_type: The type of investment (e.g., 'Crypto', 'Energy').
        """
        self.name = name
        self.amount = amount
        self.investment_type = investment_type

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the investment object to a dictionary representation.

        :return: A dictionary containing the investment details.
        """
        return {
            'name': self.name,
            'amount': self.amount,
            'investment_type': self.investment_type
        }


class InvestmentTracker:
    def __init__(self):
        """
        Initializes the investment tracker with an empty list of investments.
        """
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment) -> None:
        """
        Adds an investment to the tracker.

        :param investment: The investment object to add.
        """
        if investment.amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.investments.append(investment)

    def total_investment(self) -> float:
        """
        Calculates the total amount of investments tracked.

        :return: The total investment amount.
        """
        return sum(investment.amount for investment in self.investments)

    def investments_summary(self) -> List[Dict[str, Any]]:
        """
        Provides a summary of all investments.

        :return: A list of dictionaries summarizing each investment.
        """
        return [investment.to_dict() for investment in self.investments]

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the investment data to a JSON file.

        :param file_path: The path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.investments_summary(), file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Loads investment data from a JSON file.

        :param file_path: The path to the file from which data will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                investments_data = json.load(file)
                for item in investments_data:
                    investment = Investment(item['name'], item['amount'], item['investment_type'])
                    self.add_investment(investment)
        except IOError as e:
            raise Exception(f"An error occurred while loading from file: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = InvestmentTracker()
    tracker.add_investment(Investment("Bitcoin Mining", 5000, "Crypto"))
    tracker.add_investment(Investment("Solar Panel Installation", 2000, "Energy"))

    print(f"Total Investment: ${tracker.total_investment():.2f}")
    print("Investments Summary:")
    for investment in tracker.investments_summary():
        print(investment)

    # Save investments to file
    tracker.save_to_file("investments.json")

    # Load investments from file
    new_tracker = InvestmentTracker()
    new_tracker.load_from_file("investments.json")
    print("Loaded Investments:")
    for investment in new_tracker.investments_summary():
        print(investment)
```
