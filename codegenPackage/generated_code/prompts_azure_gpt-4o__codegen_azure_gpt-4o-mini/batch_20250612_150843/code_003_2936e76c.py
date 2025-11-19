"""
Generated Code Metadata:
========================
Original URL: https://tradegpt360-evix.com
Prompt: Create a script to simulate trading autonomy and support settings, allowing users to adjust their trading preferences as described in the TradeGPT 360 Evix application.
Generated: DETERMINISTIC_2936e76cb1b2b714
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TradingSettings:
    """
    A class to represent trading settings for a user.
    """

    def __init__(self, risk_tolerance='medium', trade_frequency='daily', max_investment=1000):
        """
        Initializes the trading settings with user-defined preferences.

        :param risk_tolerance: The user's risk tolerance level (low, medium, high).
        :param trade_frequency: The frequency of trading (daily, weekly, monthly).
        :param max_investment: The maximum amount to invest per trade.
        """
        self.risk_tolerance = risk_tolerance
        self.trade_frequency = trade_frequency
        self.max_investment = max_investment

    def update_settings(self, risk_tolerance=None, trade_frequency=None, max_investment=None):
        """
        Updates the trading settings based on user input.

        :param risk_tolerance: New risk tolerance level.
        :param trade_frequency: New trade frequency.
        :param max_investment: New maximum investment amount.
        """
        if risk_tolerance:
            self.risk_tolerance = risk_tolerance
        if trade_frequency:
            self.trade_frequency = trade_frequency
        if max_investment is not None:
            if max_investment < 0:
                raise ValueError("Maximum investment must be a non-negative value.")
            self.max_investment = max_investment

    def to_dict(self):
        """
        Converts the trading settings to a dictionary.

        :return: A dictionary representation of the trading settings.
        """
        return {
            'risk_tolerance': self.risk_tolerance,
            'trade_frequency': self.trade_frequency,
            'max_investment': self.max_investment
        }

    def save_settings(self, filename='trading_settings.json'):
        """
        Saves the trading settings to a JSON file.

        :param filename: The name of the file to save the settings to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            print(f"Error saving settings to {filename}: {e}")

    @classmethod
    def load_settings(cls, filename='trading_settings.json'):
        """
        Loads trading settings from a JSON file.

        :param filename: The name of the file to load the settings from.
        :return: An instance of TradingSettings with loaded settings.
        """
        try:
            with open(filename, 'r') as file:
                settings = json.load(file)
                return cls(**settings)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading settings from {filename}: {e}")
            return cls()  # Return default settings on error


def main():
    """
    Main function to simulate trading autonomy and support settings.
    """
    # Load existing settings or create new ones
    trading_settings = TradingSettings.load_settings()

    # Display current settings
    print("Current Trading Settings:")
    print(trading_settings.to_dict())

    # Example of updating settings
    try:
        trading_settings.update_settings(risk_tolerance='high', max_investment=2000)
        print("Updated Trading Settings:")
        print(trading_settings.to_dict())
    except ValueError as e:
        print(f"Error updating settings: {e}")

    # Save updated settings
    trading_settings.save_settings()


if __name__ == "__main__":
    main()
```
