"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asetrdex.com
Prompt: Create a script to automate switching between Simple Mode and Pro Mode on Aster DEX based on user preferences for trading.
Generated: DETERMINISTIC_1891010efcdc2e97
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class AsterDexModeSwitcher:
    """
    A class to handle mode switching between Simple Mode and Pro Mode on Aster DEX.
    """

    def __init__(self, config_file="user_preferences.json"):
        """
        Initialize the mode switcher with a configuration file.

        :param config_file: Path to the JSON file storing user preferences.
        """
        self.config_file = config_file
        self.supported_modes = ["Simple Mode", "Pro Mode"]

    def load_preferences(self):
        """
        Load user preferences from the configuration file.

        :return: A dictionary containing user preferences.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
        
        try:
            with open(self.config_file, "r") as file:
                preferences = json.load(file)
                return preferences
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file '{self.config_file}': {e}")

    def save_preferences(self, preferences):
        """
        Save user preferences to the configuration file.

        :param preferences: A dictionary containing user preferences to save.
        """
        try:
            with open(self.config_file, "w") as file:
                json.dump(preferences, file, indent=4)
        except Exception as e:
            raise IOError(f"Error writing to configuration file '{self.config_file}': {e}")

    def switch_mode(self, mode):
        """
        Switch the trading mode based on user preferences.

        :param mode: The mode to switch to. Must be "Simple Mode" or "Pro Mode".
        """
        if mode not in self.supported_modes:
            raise ValueError(f"Unsupported mode '{mode}'. Supported modes: {self.supported_modes}")
        
        # Simulating mode switch functionality
        print(f"Switching to {mode} on Aster DEX...")
        # Normally, here you'd interact with the Aster DEX API to apply the mode change.

    def run(self):
        """
        Main method to load preferences and switch trading mode accordingly.
        """
        try:
            preferences = self.load_preferences()
            preferred_mode = preferences.get("preferred_mode", "Simple Mode")

            if preferred_mode not in self.supported_modes:
                print(f"Invalid mode '{preferred_mode}' in preferences. Defaulting to 'Simple Mode'.")
                preferred_mode = "Simple Mode"

            self.switch_mode(preferred_mode)
            print("Mode switched successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example: Create an instance and run the mode switching automation.
    switcher = AsterDexModeSwitcher()
    switcher.run()
```

### Notes:
1. Ensure that a `user_preferences.json` file exists in the same directory as the script, with content like:
   ```json
   {
       "preferred_mode": "Pro Mode"
   }
   ```
2. Replace any simulated functionality (e.g., `print()` statements) with actual API calls to the Aster DEX platform when integrating into production.
3. Proper logging and monitoring can be added for production systems.
