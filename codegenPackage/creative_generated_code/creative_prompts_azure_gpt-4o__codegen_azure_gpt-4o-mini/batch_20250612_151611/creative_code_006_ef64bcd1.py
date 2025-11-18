"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aave.net
Prompt: Develop a script to toggle between testnet mode and mainnet mode for interacting with Aave V3 markets.
Generated: DETERMINISTIC_ef64bcd116aaff0e
Batch ID: 20250612_151611
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.aave.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://app.aave.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os

class AaveModeSwitcher:
    """
    A class to switch between Aave V3 testnet and mainnet modes.
    """

    def __init__(self):
        self.current_mode = self.get_current_mode()

    def get_current_mode(self):
        """
        Retrieves the current mode from environment variables.
        Defaults to 'mainnet' if not set.
        """
        return os.getenv('AAVE_MODE', 'mainnet')

    def set_mode(self, mode):
        """
        Sets the mode for Aave interaction.

        Parameters:
        mode (str): The mode to set ('testnet' or 'mainnet').

        Raises:
        ValueError: If an invalid mode is provided.
        """
        if mode not in ['testnet', 'mainnet']:
            raise ValueError("Mode must be either 'testnet' or 'mainnet'.")

        os.environ['AAVE_MODE'] = mode
        self.current_mode = mode
        print(f"Switched to {self.current_mode} mode.")

    def toggle_mode(self):
        """
        Toggles between testnet and mainnet modes.
        """
        new_mode = 'testnet' if self.current_mode == 'mainnet' else 'mainnet'
        self.set_mode(new_mode)

    def get_aave_market_url(self):
        """
        Returns the Aave market URL based on the current mode.

        Returns:
        str: The Aave market URL.
        """
        if self.current_mode == 'mainnet':
            return "https://app.aave.com"
        return "https://testnet.aave.com"

def main():
    """
    Main function to demonstrate the toggling of Aave modes.
    """
    switcher = AaveModeSwitcher()

    try:
        print(f"Current Aave mode: {switcher.current_mode}")
        print(f"Aave market URL: {switcher.get_aave_market_url()}")

        # Toggle the mode
        switcher.toggle_mode()
        print(f"Toggled Aave mode: {switcher.current_mode}")
        print(f"Aave market URL: {switcher.get_aave_market_url()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
