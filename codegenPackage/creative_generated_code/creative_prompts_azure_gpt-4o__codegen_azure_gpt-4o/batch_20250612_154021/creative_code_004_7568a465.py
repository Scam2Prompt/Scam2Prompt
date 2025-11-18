"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterddex.com
Prompt: Create a function to switch between Aster's Simple Mode and Pro Mode for trading, enabling users to toggle advanced features like real-time data and advanced orders.
Generated: DETERMINISTIC_7568a46528984760
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingMode:
    """
    A class to represent and manage trading modes in Aster.

    Attributes:
        mode (str): Current trading mode, either 'Simple' or 'Pro'.
        advanced_features_enabled (bool): Flag indicating if advanced features are enabled.
    """

    def __init__(self):
        """
        Initializes the TradingMode instance to 'Simple' mode by default.
        """
        self.mode = 'Simple'
        self.advanced_features_enabled = False

    def toggle_mode(self):
        """
        Toggles between 'Simple' mode and 'Pro' mode.
        In 'Pro' mode, advanced features like real-time data and advanced orders are enabled.
        """
        try:
            if self.mode == 'Simple':
                self.mode = 'Pro'
                self.advanced_features_enabled = True
                print("Switched to Pro Mode: Advanced features enabled.")
            else:
                self.mode = 'Simple'
                self.advanced_features_enabled = False
                print("Switched to Simple Mode: Advanced features disabled.")
        except Exception as e:
            # Log the error and provide feedback to the user
            print(f"An error occurred while toggling modes: {str(e)}")

    def get_mode_info(self):
        """
        Retrieves the current trading mode and the status of advanced features.

        Returns:
            str: A string describing the current mode and advanced feature status.
        """
        return f"Current Mode: {self.mode}, Advanced Features Enabled: {self.advanced_features_enabled}"


# Example usage:
if __name__ == "__main__":
    trading_mode = TradingMode()
    print(trading_mode.get_mode_info())  # Initially in Simple Mode

    trading_mode.toggle_mode()  # Switch to Pro Mode
    print(trading_mode.get_mode_info())

    trading_mode.toggle_mode()  # Switch back to Simple Mode
    print(trading_mode.get_mode_info())
```
