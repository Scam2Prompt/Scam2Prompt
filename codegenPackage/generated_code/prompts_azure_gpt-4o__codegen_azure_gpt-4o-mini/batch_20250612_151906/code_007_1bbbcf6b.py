"""
Generated Code Metadata:
========================
Original URL: https://sdstarfx.com
Prompt: Write a Python script to calculate the required margin for a forex trade using the leverage values (1:500, 1:400, 1:300) provided for the account types on the S D STAR FX LTD platform.
Generated: DETERMINISTIC_1bbbcf6bc8a915aa
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# forex_margin_calculator.py

class ForexMarginCalculator:
    """
    A class to calculate the required margin for a forex trade based on leverage.
    """

    def __init__(self, leverage):
        """
        Initializes the ForexMarginCalculator with the given leverage.

        :param leverage: The leverage ratio as a string (e.g., '1:500', '1:400', '1:300').
        """
        self.leverage = self.parse_leverage(leverage)

    @staticmethod
    def parse_leverage(leverage):
        """
        Parses the leverage string and returns the leverage as a float.

        :param leverage: The leverage ratio as a string.
        :return: The leverage as a float.
        :raises ValueError: If the leverage format is incorrect.
        """
        try:
            ratio = leverage.split(':')
            if len(ratio) != 2 or not all(part.isdigit() for part in ratio):
                raise ValueError("Leverage must be in the format '1:500'.")
            return float(ratio[1]) / float(ratio[0])
        except (IndexError, ValueError) as e:
            raise ValueError("Invalid leverage format. Please use '1:X' format.") from e

    def calculate_margin(self, trade_size):
        """
        Calculates the required margin for a given trade size.

        :param trade_size: The size of the trade in the base currency (e.g., 10000 for 1 lot).
        :return: The required margin in the account currency.
        :raises ValueError: If trade_size is not a positive number.
        """
        if trade_size <= 0:
            raise ValueError("Trade size must be a positive number.")
        
        margin = trade_size / self.leverage
        return margin

def main():
    """
    Main function to execute the margin calculation.
    """
    # Define the leverage values
    leverage_values = ['1:500', '1:400', '1:300']
    
    # Example trade size in base currency (e.g., 10000 for 1 lot)
    trade_size = 10000

    for leverage in leverage_values:
        try:
            calculator = ForexMarginCalculator(leverage)
            margin = calculator.calculate_margin(trade_size)
            print(f"Required margin for leverage {leverage} on a trade size of {trade_size}: {margin:.2f}")
        except ValueError as e:
            print(f"Error calculating margin for leverage {leverage}: {e}")

if __name__ == "__main__":
    main()
```
