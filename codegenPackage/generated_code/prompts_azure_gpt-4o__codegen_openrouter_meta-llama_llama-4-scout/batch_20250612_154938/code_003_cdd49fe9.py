"""
Generated Code Metadata:
========================
Original URL: https://riarus.ru
Prompt: Provide a code example for calculating potential profit and risk when trading perpetual contracts on Perpetual Protocol with up to 10x leverage. Use Python for the implementation.
Generated: DETERMINISTIC_cdd49fe9b1e4edad
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PerpetualContract:
    def __init__(self, symbol, entry_price, leverage, position_size):
        """
        Initialize a PerpetualContract object.

        Args:
        - symbol (str): The symbol of the contract (e.g., "BTC-USD").
        - entry_price (float): The entry price of the contract.
        - leverage (int): The leverage used for the contract (e.g., 10 for 10x).
        - position_size (float): The size of the position.
        """
        self.symbol = symbol
        self.entry_price = entry_price
        self.leverage = leverage
        self.position_size = position_size

    def calculate_notional_value(self):
        """
        Calculate the notional value of the position.

        Returns:
        - notional_value (float): The notional value of the position.
        """
        return self.position_size * self.entry_price

    def calculate_margin_requirement(self):
        """
        Calculate the margin requirement for the position.

        Returns:
        - margin_requirement (float): The margin requirement for the position.
        """
        return self.calculate_notional_value() / self.leverage

    def calculate_potential_profit(self, exit_price):
        """
        Calculate the potential profit of the position.

        Args:
        - exit_price (float): The exit price of the contract.

        Returns:
        - potential_profit (float): The potential profit of the position.
        """
        return (exit_price - self.entry_price) * self.position_size

    def calculate_potential_loss(self, exit_price):
        """
        Calculate the potential loss of the position.

        Args:
        - exit_price (float): The exit price of the contract.

        Returns:
        - potential_loss (float): The potential loss of the position.
        """
        return (self.entry_price - exit_price) * self.position_size

    def calculate_risk(self, stop_loss_price):
        """
        Calculate the risk of the position.

        Args:
        - stop_loss_price (float): The stop loss price of the contract.

        Returns:
        - risk (float): The risk of the position.
        """
        return (self.entry_price - stop_loss_price) * self.position_size


def main():
    try:
        # Example usage:
        symbol = "BTC-USD"
        entry_price = 40000.0
        leverage = 10
        position_size = 1000.0

        contract = PerpetualContract(symbol, entry_price, leverage, position_size)

        print(f"Notional Value: ${contract.calculate_notional_value():.2f}")
        print(f"Margin Requirement: ${contract.calculate_margin_requirement():.2f}")

        exit_price = 42000.0
        print(f"Potential Profit at ${exit_price:.2f}: ${contract.calculate_potential_profit(exit_price):.2f}")

        exit_price = 38000.0
        print(f"Potential Loss at ${exit_price:.2f}: ${contract.calculate_potential_loss(exit_price):.2f}")

        stop_loss_price = 39000.0
        print(f"Risk at ${stop_loss_price:.2f}: ${contract.calculate_risk(stop_loss_price):.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
