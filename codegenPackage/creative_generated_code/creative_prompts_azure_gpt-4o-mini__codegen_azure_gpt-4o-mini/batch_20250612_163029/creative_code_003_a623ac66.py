"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-3x-maxair.com
Prompt: Create a function that customizes trading parameters for the Immediate 3X Maxair software, allowing users to set their risk management strategies.
Generated: DETERMINISTIC_a623ac66a72a43cf
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingParameters:
    """
    A class to define and manage trading parameters for the Immediate 3X Maxair software.
    This class allows users to customize their risk management strategies.
    """
    def __init__(self, max_loss: float = 0.02, take_profit: float = 0.05, stop_loss: float = 0.03):
        """
        Initializes the TradingParameters with default values or user-defined values.
        
        Args:
            max_loss (float): Maximum acceptable loss per trade (as a percentage).
            take_profit (float): Target profit level per trade (as a percentage).
            stop_loss (float): Stop loss level per trade (as a percentage).
        """
        self.set_max_loss(max_loss)
        self.set_take_profit(take_profit)
        self.set_stop_loss(stop_loss)

    def set_max_loss(self, max_loss: float):
        """
        Sets the maximum loss limit for a trade.
        
        Args:
            max_loss (float): Maximum acceptable loss per trade (as a percentage).

        Raises:
            ValueError: If max_loss is not between 0 and 1.
        """
        if not (0 <= max_loss <= 1):
            raise ValueError("max_loss must be between 0 and 1.")
        self.max_loss = max_loss

    def set_take_profit(self, take_profit: float):
        """
        Sets the take profit level for a trade.
        
        Args:
            take_profit (float): Target profit level per trade (as a percentage).

        Raises:
            ValueError: If take_profit is not between 0 and 1.
        """
        if not (0 <= take_profit <= 1):
            raise ValueError("take_profit must be between 0 and 1.")
        self.take_profit = take_profit

    def set_stop_loss(self, stop_loss: float):
        """
        Sets the stop loss level for a trade.
        
        Args:
            stop_loss (float): Stop loss level per trade (as a percentage).

        Raises:
            ValueError: If stop_loss is not between 0 and 1.
        """
        if not (0 <= stop_loss <= 1):
            raise ValueError("stop_loss must be between 0 and 1.")
        self.stop_loss = stop_loss

    def get_parameters(self):
        """
        Returns the current trading parameters as a dictionary.
        
        Returns:
            dict: A dictionary containing the trading parameters.
        """
        return {
            'max_loss': self.max_loss,
            'take_profit': self.take_profit,
            'stop_loss': self.stop_loss
        }

# Example of usage
if __name__ == "__main__":
    try:
        trading_params = TradingParameters(max_loss=0.02, take_profit=0.05, stop_loss=0.03)
        print("Trading Parameters:", trading_params.get_parameters())
    except ValueError as e:
        print(f"Error: {e}")
```
