"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinvest-financial.com
Prompt: Generate code for managing both spot and futures positions in one interface, as described in GlobalInvest's trading efficiency features.
Generated: DETERMINISTIC_76ff32aa4f22f55a
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingPositionManager:
    """
    A class to manage both spot and futures trading positions in one interface.
    It provides methods to add, remove, and display positions for both spot and futures.
    """

    class Position:
        """
        A class to represent a trading position.
        """

        def __init__(self, symbol, quantity, price, position_type):
            """
            Initializes a trading position.

            :param symbol: The trading symbol (e.g., 'AAPL', 'BTC-USD').
            :param quantity: The quantity of the asset.
            :param price: The price at which the position was opened.
            :param position_type: The type of position ('spot' or 'futures').
            """
            self.symbol = symbol
            self.quantity = quantity
            self.price = price
            self.position_type = position_type

        def __repr__(self):
            return f"{self.position_type.capitalize()} Position: {self.symbol}, Quantity: {self.quantity}, Price: {self.price}"

    def __init__(self):
        """
        Initializes the TradingPositionManager with empty position lists for spot and futures.
        """
        self.spot_positions = []
        self.futures_positions = []

    def add_position(self, symbol, quantity, price, position_type):
        """
        Adds a new trading position to the appropriate list.

        :param symbol: The trading symbol.
        :param quantity: The quantity of the asset.
        :param price: The price of the asset.
        :param position_type: The type of position ('spot' or 'futures').
        :raises ValueError: If the position type is not recognized.
        """
        if position_type not in ['spot', 'futures']:
            raise ValueError("Position type must be 'spot' or 'futures'.")

        position = self.Position(symbol, quantity, price, position_type)

        if position_type == 'spot':
            self.spot_positions.append(position)
        else:  # position_type == 'futures'
            self.futures_positions.append(position)

    def remove_position(self, symbol, position_type):
        """
        Removes a trading position from the appropriate list.

        :param symbol: The trading symbol of the position to be removed.
        :param position_type: The type of position ('spot' or 'futures').
        :raises ValueError: If the position type is not recognized.
        :raises LookupError: If the position is not found.
        """
        if position_type not in ['spot', 'futures']:
            raise ValueError("Position type must be 'spot' or 'futures'.")

        positions = self.spot_positions if position_type == 'spot' else self.futures_positions
        for position in positions:
            if position.symbol == symbol:
                positions.remove(position)
                return

        raise LookupError(f"{position_type.capitalize()} position for symbol {symbol} not found.")

    def display_positions(self):
        """
        Displays all trading positions for both spot and futures.
        """
        print("Spot Positions:")
        for position in self.spot_positions:
            print(position)

        print("\nFutures Positions:")
        for position in self.futures_positions:
            print(position)

# Example usage:
if __name__ == "__main__":
    try:
        manager = TradingPositionManager()
        manager.add_position('AAPL', 10, 150.00, 'spot')
        manager.add_position('BTC-USD', 1, 30000.00, 'futures')
        manager.display_positions()
        manager.remove_position('AAPL', 'spot')
        manager.display_positions()
    except Exception as e:
        print(f"An error occurred: {e}")
```
