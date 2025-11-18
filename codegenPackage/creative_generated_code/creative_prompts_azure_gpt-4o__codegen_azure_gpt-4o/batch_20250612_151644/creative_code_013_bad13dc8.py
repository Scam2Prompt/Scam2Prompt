"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Develop a tool to calculate mining profitability across MinerLab's supported cryptocurrencies, factoring in plan duration and daily returns.
Generated: DETERMINISTIC_bad13dc8ec741fa8
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class MiningProfitabilityCalculator:
    """
    A class to calculate mining profitability for supported cryptocurrencies
    based on plan duration and daily returns.
    """

    def __init__(self):
        """
        Initializes the MiningProfitabilityCalculator with supported cryptocurrencies.
        """
        self.supported_cryptocurrencies = {
            "BTC": {"daily_return_usd": 15.0},
            "ETH": {"daily_return_usd": 10.0},
            "LTC": {"daily_return_usd": 5.0},
        }

    def calculate_profit(self, currency: str, plan_duration_days: int) -> dict:
        """
        Calculates the total profit for the given cryptocurrency and plan duration.

        :param currency: Cryptocurrency symbol (e.g., 'BTC', 'ETH', 'LTC').
        :param plan_duration_days: Duration of the mining plan in days.
        :return: A dictionary containing the cryptocurrency, plan duration, and total profit.
        """
        if currency not in self.supported_cryptocurrencies:
            raise ValueError(f"Unsupported cryptocurrency: {currency}")

        daily_return_usd = self.supported_cryptocurrencies[currency]["daily_return_usd"]
        total_profit_usd = daily_return_usd * plan_duration_days

        return {
            "currency": currency,
            "plan_duration_days": plan_duration_days,
            "total_profit_usd": round(total_profit_usd, 2),
        }

    def add_cryptocurrency(self, currency: str, daily_return_usd: float) -> None:
        """
        Adds a new cryptocurrency to the supported list.

        :param currency: Cryptocurrency symbol (e.g., 'BTC', 'ETH', 'LTC').
        :param daily_return_usd: Daily return in USD for the cryptocurrency.
        """
        if currency in self.supported_cryptocurrencies:
            raise ValueError(f"Cryptocurrency {currency} already supported.")

        if daily_return_usd <= 0:
            raise ValueError("Daily return must be greater than 0.")

        self.supported_cryptocurrencies[currency] = {"daily_return_usd": daily_return_usd}

    def remove_cryptocurrency(self, currency: str) -> None:
        """
        Removes an existing cryptocurrency from the supported list.

        :param currency: Cryptocurrency symbol to remove.
        """
        if currency not in self.supported_cryptocurrencies:
            raise ValueError(f"Cryptocurrency {currency} is not in the supported list.")

        del self.supported_cryptocurrencies[currency]

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the list of supported cryptocurrencies to a file in JSON format.

        :param file_path: File path to save the data.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.supported_cryptocurrencies, file, indent=4)
        except Exception as e:
            raise IOError(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Loads the list of supported cryptocurrencies from a file in JSON format.

        :param file_path: File path to load the data from.
        """
        try:
            with open(file_path, "r") as file:
                self.supported_cryptocurrencies = json.load(file)
        except Exception as e:
            raise IOError(f"Error loading from file: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        calculator = MiningProfitabilityCalculator()

        # Add a custom cryptocurrency
        calculator.add_cryptocurrency("DOGE", daily_return_usd=2.0)

        # Calculate profit for BTC for a 30-day plan
        print(calculator.calculate_profit(currency="BTC", plan_duration_days=30))

        # Save supported cryptocurrencies to a file
        calculator.save_to_file(file_path="supported_cryptocurrencies.json")

        # Load supported cryptocurrencies from a file
        calculator.load_from_file(file_path="supported_cryptocurrencies.json")

        # Calculate profit for DOGE for a 45-day plan
        print(calculator.calculate_profit(currency="DOGE", plan_duration_days=45))

    except Exception as e:
        print(f"Error: {e}")
```
