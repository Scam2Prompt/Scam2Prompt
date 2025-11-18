"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-proquantumai.com
Prompt: Write Python code to implement a feature that allows users to switch between "auto-trade" and "manual" modes in a crypto trading platform, as described in Pro Quantum AI.
Generated: DETERMINISTIC_13a352677b4f7c53
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingMode:
    """Class to manage trading modes in a crypto trading platform."""
    
    AUTO_TRADE = "auto"
    MANUAL_TRADE = "manual"

    def __init__(self):
        """Initialize the trading mode to manual by default."""
        self.current_mode = TradingMode.MANUAL_TRADE

    def switch_mode(self, mode: str) -> None:
        """
        Switch between auto-trade and manual modes.

        Args:
            mode (str): The mode to switch to, should be either 'auto' or 'manual'.

        Raises:
            ValueError: If the provided mode is not recognized.
        """
        if mode not in {TradingMode.AUTO_TRADE, TradingMode.MANUAL_TRADE}:
            raise ValueError(f"Invalid trading mode: {mode}. Use 'auto' or 'manual'.")

        # Update the current mode
        self.current_mode = mode
        print(f"Trading mode switched to: {self.current_mode}")

    def get_current_mode(self) -> str:
        """Return the current trading mode."""
        return self.current_mode


def main():
    """Main function to demonstrate switching trading modes."""
    trading_mode_manager = TradingMode()
    
    try:
        # Initial state
        print(f"Current trading mode: {trading_mode_manager.get_current_mode()}")

        # Switch to auto-trade mode
        trading_mode_manager.switch_mode(TradingMode.AUTO_TRADE)

        # Switch to manual mode
        trading_mode_manager.switch_mode(TradingMode.MANUAL_TRADE)

        # Attempt to switch to an invalid mode
        trading_mode_manager.switch_mode("invalid_mode")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
