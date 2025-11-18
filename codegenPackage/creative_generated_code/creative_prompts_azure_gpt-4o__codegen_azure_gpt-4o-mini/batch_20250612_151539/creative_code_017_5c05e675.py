"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Generate a script to calculate the expiration dates for unused bonus funds and free spins, adhering to the rules outlined on Santa Claus Casino.
Generated: DETERMINISTIC_5c05e675fea3c0d3
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class BonusFund:
    def __init__(self, amount, issued_date, expiration_days):
        """
        Initialize the BonusFund instance.

        :param amount: Amount of the bonus fund.
        :param issued_date: Date when the bonus fund was issued (YYYY-MM-DD).
        :param expiration_days: Number of days until the bonus expires.
        """
        self.amount = amount
        self.issued_date = datetime.strptime(issued_date, "%Y-%m-%d")
        self.expiration_days = expiration_days

    def calculate_expiration_date(self):
        """
        Calculate the expiration date of the bonus fund.

        :return: Expiration date as a datetime object.
        """
        return self.issued_date + timedelta(days=self.expiration_days)


class FreeSpin:
    def __init__(self, quantity, issued_date, expiration_days):
        """
        Initialize the FreeSpin instance.

        :param quantity: Number of free spins.
        :param issued_date: Date when the free spins were issued (YYYY-MM-DD).
        :param expiration_days: Number of days until the spins expire.
        """
        self.quantity = quantity
        self.issued_date = datetime.strptime(issued_date, "%Y-%m-%d")
        self.expiration_days = expiration_days

    def calculate_expiration_date(self):
        """
        Calculate the expiration date of the free spins.

        :return: Expiration date as a datetime object.
        """
        return self.issued_date + timedelta(days=self.expiration_days)


def load_bonus_data(file_path):
    """
    Load bonus fund and free spin data from a JSON file.

    :param file_path: Path to the JSON file containing bonus data.
    :return: List of BonusFund and FreeSpin instances.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            bonuses = []
            for item in data.get("bonuses", []):
                bonuses.append(BonusFund(**item))
            for item in data.get("free_spins", []):
                bonuses.append(FreeSpin(**item))
            return bonuses
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file at {file_path}.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """
    Main function to load bonus data and calculate expiration dates.
    """
    # Load bonuses and free spins from a JSON file
    file_path = 'bonus_data.json'
    bonuses = load_bonus_data(file_path)

    for bonus in bonuses:
        expiration_date = bonus.calculate_expiration_date()
        if isinstance(bonus, BonusFund):
            print(f"Bonus Fund: {bonus.amount}, Issued on: {bonus.issued_date.date()}, "
                  f"Expires on: {expiration_date.date()}")
        elif isinstance(bonus, FreeSpin):
            print(f"Free Spins: {bonus.quantity}, Issued on: {bonus.issued_date.date()}, "
                  f"Expires on: {expiration_date.date()}")


if __name__ == "__main__":
    main()
```

```json
{
    "bonuses": [
        {
            "amount": 100,
            "issued_date": "2023-10-01",
            "expiration_days": 30
        },
        {
            "amount": 50,
            "issued_date": "2023-10-15",
            "expiration_days": 15
        }
    ],
    "free_spins": [
        {
            "quantity": 10,
            "issued_date": "2023-10-05",
            "expiration_days": 7
        },
        {
            "quantity": 5,
            "issued_date": "2023-10-10",
            "expiration_days": 10
        }
    ]
}
```
