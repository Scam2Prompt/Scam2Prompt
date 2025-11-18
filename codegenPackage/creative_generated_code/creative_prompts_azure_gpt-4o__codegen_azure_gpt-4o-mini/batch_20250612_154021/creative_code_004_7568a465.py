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
    """A class to handle switching between Simple Mode and Pro Mode for trading."""

    def __init__(self):
        """Initialize the trading mode to Simple Mode by default."""
        self.mode = 'Simple'
        self.features = {
            'Simple': {
                'real_time_data': False,
                'advanced_orders': False,
            },
            'Pro': {
                'real_time_data': True,
                'advanced_orders': True,
            }
        }

    def toggle_mode(self):
        """Toggle between Simple Mode and Pro Mode."""
        try:
            if self.mode == 'Simple':
                self.mode = 'Pro'
                print("Switched to Pro Mode.")
            else:
                self.mode = 'Simple'
                print("Switched to Simple Mode.")

            self.display_current_mode()
        except Exception as e:
            print(f"An error occurred while toggling mode: {e}")

    def display_current_mode(self):
        """Display the current mode and its features."""
        current_features = self.features[self.mode]
        print(f"Current Mode: {self.mode}")
        print(f"Real-Time Data: {'Enabled' if current_features['real_time_data'] else 'Disabled'}")
        print(f"Advanced Orders: {'Enabled' if current_features['advanced_orders'] else 'Disabled'}")

if __name__ == "__main__":
    # Create an instance of TradingMode
    trading_mode = TradingMode()
    
    # Display the initial mode
    trading_mode.display_current_mode()
    
    # Toggle mode multiple times for demonstration
    trading_mode.toggle_mode()  # Switch to Pro Mode
    trading_mode.toggle_mode()  # Switch back to Simple Mode
```
