"""
Generated Code Metadata:
========================
Original URL: https://thebitx3eprex.com
Prompt: Create a function that automates the process of switching between auto-trade and manual modes in the Bit X3 Eprex platform.
Generated: DETERMINISTIC_4e1c466330c960f5
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BitX3Eprex:
    def __init__(self):
        # Initialize the trading mode to manual by default
        self.mode = 'manual'

    def switch_mode(self, mode: str) -> None:
        """
        Switches between auto-trade and manual modes.

        Args:
            mode (str): The mode to switch to. Should be either 'auto' or 'manual'.

        Raises:
            ValueError: If the provided mode is not 'auto' or 'manual'.
        """
        # Validate the input mode
        if mode not in ['auto', 'manual']:
            raise ValueError("Invalid mode. Please choose 'auto' or 'manual'.")

        # Log the current mode before switching
        print(f"Switching from {self.mode} mode to {mode} mode.")

        # Switch the mode
        self.mode = mode

        # Log the new mode
        print(f"Successfully switched to {self.mode} mode.")

    def get_current_mode(self) -> str:
        """
        Returns the current trading mode.

        Returns:
            str: The current trading mode ('auto' or 'manual').
        """
        return self.mode


# Example usage
if __name__ == "__main__":
    try:
        trading_platform = BitX3Eprex()
        print(f"Current mode: {trading_platform.get_current_mode()}")

        # Switch to auto mode
        trading_platform.switch_mode('auto')
        print(f"Current mode: {trading_platform.get_current_mode()}")

        # Switch back to manual mode
        trading_platform.switch_mode('manual')
        print(f"Current mode: {trading_platform.get_current_mode()}")

        # Attempt to switch to an invalid mode
        trading_platform.switch_mode('invalid_mode')

    except ValueError as e:
        print(f"Error: {e}")
```
