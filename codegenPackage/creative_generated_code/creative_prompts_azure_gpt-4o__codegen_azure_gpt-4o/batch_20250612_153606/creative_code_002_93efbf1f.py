"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octaviaone.pages.dev
Prompt: How can Octavia's AI memory be leveraged to customize trading preferences for a user? Write code to demonstrate how Octavia learns and adapts to a user's trading history.
Generated: DETERMINISTIC_93efbf1f1ee3b82b
Batch ID: 20250612_153606
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

class OctaviaAI:
    """
    OctaviaAI class learns and adapts trading preferences based on user trading history.
    """
    def __init__(self, user_id):
        """
        Initialize OctaviaAI instance with user ID and load user preferences if they exist.
        """
        self.user_id = user_id
        self.preferences_file = f"user_{self.user_id}_preferences.json"
        self.preferences = self.load_preferences()

    def load_preferences(self):
        """
        Load user preferences from a JSON file. Create default preferences if the file doesn't exist.
        Returns:
            dict: User preferences.
        """
        if os.path.exists(self.preferences_file):
            try:
                with open(self.preferences_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # Handle corrupted or malformed JSON file
                print("Preferences file is corrupted. Resetting to default preferences.")
                return self.default_preferences()
        else:
            return self.default_preferences()

    @staticmethod
    def default_preferences():
        """
        Default user preferences if no history exists.
        Returns:
            dict: Default preferences dictionary.
        """
        return {
            "risk_tolerance": "medium",  # Options: low, medium, high
            "preferred_assets": ["stocks", "ETFs"],  # User's preferred trading assets
            "trade_frequency": "moderate",  # Options: low, moderate, high
        }

    def update_preferences(self, trading_history):
        """
        Update user preferences based on their trading history.
        Args:
            trading_history (list): List of user's past trades.
        """
        try:
            # Example logic to update preferences based on trading history
            if not trading_history:
                print("No trading history provided. Preferences will remain unchanged.")
                return

            risk_count = {"low": 0, "medium": 0, "high": 0}
            asset_count = {}
            trade_count = len(trading_history)

            for trade in trading_history:
                risk_count[trade["risk_level"]] += 1
                asset_count[trade["asset"]] = asset_count.get(trade["asset"], 0) + 1

            # Update risk tolerance based on majority risk level from history
            self.preferences["risk_tolerance"] = max(risk_count, key=risk_count.get)

            # Update preferred assets based on the most frequently traded assets
            self.preferences["preferred_assets"] = sorted(asset_count, key=asset_count.get, reverse=True)[:3]

            # Update trade frequency
            if trade_count < 10:
                self.preferences["trade_frequency"] = "low"
            elif 10 <= trade_count < 50:
                self.preferences["trade_frequency"] = "moderate"
            else:
                self.preferences["trade_frequency"] = "high"

            self.save_preferences()
        except Exception as e:
            print(f"Error while updating preferences: {e}")

    def save_preferences(self):
        """
        Save the updated preferences to a JSON file.
        """
        try:
            with open(self.preferences_file, 'w') as file:
                json.dump(self.preferences, file, indent=4)
        except Exception as e:
            print(f"Error while saving preferences: {e}")

    def get_preferences(self):
        """
        Get the current trading preferences of the user.
        Returns:
            dict: Current preferences.
        """
        return self.preferences


# Example usage
if __name__ == "__main__":
    # Example trading history
    trading_history = [
        {"asset": "stocks", "risk_level": "medium"},
        {"asset": "ETFs", "risk_level": "low"},
        {"asset": "crypto", "risk_level": "high"},
        {"asset": "stocks", "risk_level": "medium"},
        {"asset": "stocks", "risk_level": "medium"},
    ]

    # Initialize OctaviaAI for a user
    user_id = 12345
    octavia_ai = OctaviaAI(user_id)

    print("Initial Preferences:")
    print(octavia_ai.get_preferences())

    # Update preferences based on trading history
    octavia_ai.update_preferences(trading_history)

    print("Updated Preferences:")
    print(octavia_ai.get_preferences())
```
