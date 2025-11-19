"""
Generated Code Metadata:
========================
Original URL: https://the-proquantumai.com
Prompt: Explain how Pro Quantum AI's automated trading software can be used for risk management, including setting stop-loss and take-profit levels.
Generated: DETERMINISTIC_50c812a384597271
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AutomatedTradingSoftware:
    """
    A class to represent an automated trading software for risk management.
    This software allows users to set stop-loss and take-profit levels for their trades.
    """

    def __init__(self, initial_balance):
        """
        Initializes the trading software with a given initial balance.

        :param initial_balance: float, the initial balance for trading
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        self.balance = initial_balance
        self.open_positions = []

    def set_stop_loss(self, entry_price, stop_loss_percentage):
        """
        Calculates the stop-loss price based on the entry price and stop-loss percentage.

        :param entry_price: float, the price at which the position was entered
        :param stop_loss_percentage: float, the percentage to set the stop-loss
        :return: float, the stop-loss price
        """
        if stop_loss_percentage < 0 or stop_loss_percentage > 100:
            raise ValueError("Stop-loss percentage must be between 0 and 100.")
        stop_loss_price = entry_price * (1 - stop_loss_percentage / 100)
        return stop_loss_price

    def set_take_profit(self, entry_price, take_profit_percentage):
        """
        Calculates the take-profit price based on the entry price and take-profit percentage.

        :param entry_price: float, the price at which the position was entered
        :param take_profit_percentage: float, the percentage to set the take-profit
        :return: float, the take-profit price
        """
        if take_profit_percentage < 0 or take_profit_percentage > 100:
            raise ValueError("Take-profit percentage must be between 0 and 100.")
        take_profit_price = entry_price * (1 + take_profit_percentage / 100)
        return take_profit_price

    def open_position(self, entry_price, stop_loss_percentage, take_profit_percentage):
        """
        Opens a new trading position with specified stop-loss and take-profit levels.

        :param entry_price: float, the price at which to enter the position
        :param stop_loss_percentage: float, the percentage for stop-loss
        :param take_profit_percentage: float, the percentage for take-profit
        """
        stop_loss_price = self.set_stop_loss(entry_price, stop_loss_percentage)
        take_profit_price = self.set_take_profit(entry_price, take_profit_percentage)

        position = {
            'entry_price': entry_price,
            'stop_loss': stop_loss_price,
            'take_profit': take_profit_price
        }
        self.open_positions.append(position)
        print(f"Opened position: {position}")

    def check_positions(self, current_price):
        """
        Checks the current price against open positions to determine if stop-loss or take-profit
        conditions have been met.

        :param current_price: float, the current market price
        """
        for position in self.open_positions:
            if current_price <= position['stop_loss']:
                self.close_position(position, "stop-loss")
            elif current_price >= position['take_profit']:
                self.close_position(position, "take-profit")

    def close_position(self, position, reason):
        """
        Closes a trading position and removes it from open positions.

        :param position: dict, the position to close
        :param reason: str, the reason for closing the position
        """
        self.open_positions.remove(position)
        print(f"Closed position: {position} due to {reason}")

# Example usage
if __name__ == "__main__":
    try:
        trading_software = AutomatedTradingSoftware(initial_balance=10000)
        trading_software.open_position(entry_price=100, stop_loss_percentage=5, take_profit_percentage=10)
        trading_software.check_positions(current_price=95)  # Simulate a price drop
        trading_software.check_positions(current_price=110)  # Simulate a price rise
    except ValueError as e:
        print(f"Error: {e}")
```
