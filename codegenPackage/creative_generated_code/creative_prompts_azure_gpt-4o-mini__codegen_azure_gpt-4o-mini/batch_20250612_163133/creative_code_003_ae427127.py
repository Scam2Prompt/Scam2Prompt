"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdx.com
Prompt: Create a function that switches between Simple Mode and Pro Mode for trading on Aster, detailing the differences in features.
Generated: DETERMINISTIC_ae4271278254fea2
Batch ID: 20250612_163133
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
    A class to represent the trading modes for Aster: Simple Mode and Pro Mode.
    """

    def __init__(self):
        """
        Initializes the TradingMode with default mode as Simple Mode.
        """
        self.mode = 'Simple'
        self.features = {
            'Simple': [
                'Basic trading options',
                'User-friendly interface',
                'Limited charting tools'
            ],
            'Pro': [
                'Advanced trading options',
                'Customizable charts',
                'Real-time market data',
                'API access for automated trading',
                'Risk management tools'
            ]
        }

    def switch_mode(self):
        """
        Switches between Simple Mode and Pro Mode.
        Raises an error if the mode is invalid.
        """
        try:
            if self.mode == 'Simple':
                self.mode = 'Pro'
            else:
                self.mode = 'Simple'
            self.display_mode_features()
        except Exception as e:
            print(f"Error switching mode: {e}")

    def display_mode_features(self):
        """
        Displays the features of the current trading mode.
        """
        print(f"Current Mode: {self.mode}")
        print("Available Features:")
        for feature in self.features[self.mode]:
            print(f"- {feature}")

# Example usage
if __name__ == "__main__":
    trading_mode = TradingMode()  # Create an instance of TradingMode
    trading_mode.display_mode_features()  # Display features of the default mode
    trading_mode.switch_mode()  # Switch to Pro Mode
    trading_mode.switch_mode()  # Switch back to Simple Mode
```
