"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Provide a Python implementation for managing a portfolio that combines cryptoassets and hedge funds, similar to Welstrade's diversified investment offerings.
Generated: DETERMINISTIC_0a514e025349a13d
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class PortfolioManager:
    """
    A class to manage a portfolio with cryptoassets and hedge funds.
    """

    def __init__(self):
        """
        Initializes the portfolio with empty holdings for cryptoassets and hedge funds.
        """
        self.portfolio = {
            "cryptoassets": {},
            "hedge_funds": {}
        }

    def add_asset(self, asset_type, name, value):
        """
        Adds an asset to the portfolio.

        :param asset_type: Type of asset ('cryptoassets' or 'hedge_funds').
        :param name: Name of the asset.
        :param value: Value of the asset in USD.
        :raises ValueError: If the asset type is invalid or value is negative.
        """
        if asset_type not in self.portfolio:
            raise ValueError("Invalid asset type. Use 'cryptoassets' or 'hedge_funds'.")
        if value < 0:
            raise ValueError("Value cannot be negative.")

        if name in self.portfolio[asset_type]:
            self.portfolio[asset_type][name] += value  # Update existing asset value
        else:
            self.portfolio[asset_type][name] = value  # Add new asset

    def remove_asset(self, asset_type, name):
        """
        Removes an asset from the portfolio.

        :param asset_type: Type of asset ('cryptoassets' or 'hedge_funds').
        :param name: Name of the asset.
        :raises ValueError: If the asset type is invalid or the asset does not exist.
        """
        if asset_type not in self.portfolio:
            raise ValueError("Invalid asset type. Use 'cryptoassets' or 'hedge_funds'.")

        if name not in self.portfolio[asset_type]:
            raise ValueError(f"Asset '{name}' does not exist in {asset_type}.")

        del self.portfolio[asset_type][name]

    def get_total_value(self):
        """
        Calculates the total value of the portfolio.

        :return: Total value of the portfolio in USD.
        """
        total_value = 0
        for asset_type in self.portfolio:
            total_value += sum(self.portfolio[asset_type].values())
        return total_value

    def get_portfolio_summary(self):
        """
        Generates a summary of the portfolio.

        :return: A JSON string containing the portfolio summary.
        """
        return json.dumps(self.portfolio, indent=4)

    def save_to_file(self, file_path):
        """
        Saves the portfolio to a JSON file.

        :param file_path: Path to the file where the portfolio should be saved.
        :raises IOError: If there is an error during file operations.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.portfolio, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving portfolio to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads the portfolio from a JSON file.

        :param file_path: Path to the file containing the portfolio data.
        :raises IOError: If there is an error during file operations.
        :raises ValueError: If the file content is not a valid portfolio.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict) or \
                        "cryptoassets" not in data or \
                        "hedge_funds" not in data:
                    raise ValueError("Invalid portfolio data in file.")
                self.portfolio = data
        except IOError as e:
            raise IOError(f"Error loading portfolio from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")


# Example usage:
if __name__ == "__main__":
    pm = PortfolioManager()

    # Adding assets
    pm.add_asset("cryptoassets", "Bitcoin", 50000)
    pm.add_asset("cryptoassets", "Ethereum", 30000)
    pm.add_asset("hedge_funds", "Fund A", 100000)

    # Removing an asset
    pm.remove_asset("cryptoassets", "Ethereum")

    # Getting portfolio summary
    print("Portfolio Summary:")
    print(pm.get_portfolio_summary())

    # Saving to file
    pm.save_to_file("portfolio.json")

    # Loading from file
    pm.load_from_file("portfolio.json")
    print("Portfolio loaded from file:")
    print(pm.get_portfolio_summary())
```
