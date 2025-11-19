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
class TradingModeSwitcher:
    """
    A class to manage trading modes (Simple Mode and Pro Mode) for the Aster platform.
    """

    def __init__(self):
        """
        Initialize the trading mode switcher with default mode set to 'Simple Mode'.
        """
        self.mode = 'Simple Mode'

    def switch_mode(self, mode):
        """
        Switch between Simple Mode and Pro Mode.

        Parameters:
        mode (str): The mode to switch to. Accepted values are 'Simple Mode' or 'Pro Mode'.

        Returns:
        str: Confirmation message indicating the current mode.

        Raises:
        ValueError: If an invalid mode is provided.
        """
        if mode not in ['Simple Mode', 'Pro Mode']:
            raise ValueError("Invalid mode. Please choose 'Simple Mode' or 'Pro Mode'.")
        
        self.mode = mode
        return f"Trading mode switched to {self.mode}."

    def get_features(self):
        """
        Retrieve features available in the current trading mode.

        Returns:
        list: List of features available in the current mode.
        """
        features = {
            'Simple Mode': [
                "Basic trading interface",
                "Pre-set trading strategies",
                "Limited customization",
                "Beginner-friendly guidance"
            ],
            'Pro Mode': [
                "Advanced trading interface",
                "Customizable trading strategies",
                "Access to detailed analytics",
                "Integration with external trading tools"
            ]
        }
        return features[self.mode]

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the trading mode switcher
        switcher = TradingModeSwitcher()

        # Switch to Pro Mode
        print(switcher.switch_mode('Pro Mode'))

        # Retrieve and display features for Pro Mode
        print("Features in Pro Mode:")
        for feature in switcher.get_features():
            print(f"- {feature}")

        # Switch back to Simple Mode
        print(switcher.switch_mode('Simple Mode'))

        # Retrieve and display features for Simple Mode
        print("Features in Simple Mode:")
        for feature in switcher.get_features():
            print(f"- {feature}")

    except ValueError as e:
        print(f"Error: {e}")
```
