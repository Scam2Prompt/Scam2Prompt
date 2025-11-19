"""
Generated Code Metadata:
========================
Original URL: https://theprofit-rex-ervaring.com
Prompt: Write code to personalize a cryptocurrency trading interface based on user preferences, similar to the customization options provided by the Profit Rex Ervaring app.
Generated: DETERMINISTIC_7c0a7a4ac6c9c66f
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
import os

@dataclass
class UserPreferences:
    theme: str = "dark"
    layout: str = "compact"
    default_crypto: str = "BTC"
    alert_threshold: float = 5.0
    show_advanced_charts: bool = False
    favorite_pairs: list = None
    notification_sound: bool = True
    auto_refresh: bool = True
    refresh_interval: int = 30

    def __post_init__(self):
        if self.favorite_pairs is None:
            self.favorite_pairs = ["BTC/USDT", "ETH/USDT"]

class TradingInterfaceCustomizer:
    def __init__(self, user_id: str, storage_dir: str = "user_preferences"):
        self.user_id = user_id
        self.storage_dir = storage_dir
        self.preferences = UserPreferences()
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_preferences_path(self) -> str:
        return os.path.join(self.storage_dir, f"{self.user_id}_preferences.json")

    def load_preferences(self) -> Optional[UserPreferences]:
        try:
            path = self._get_preferences_path()
            if os.path.exists(path):
                with open(path, 'r') as f:
                    data = json.load(f)
                    self.preferences = UserPreferences(**data)
                    return self.preferences
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading preferences: {e}")
        return None

    def save_preferences(self) -> bool:
        try:
            path = self._get_preferences_path()
            with open(path, 'w') as f:
                json.dump(asdict(self.preferences), f, indent=4)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving preferences: {e}")
            return False

    def update_preference(self, key: str, value: Any) -> bool:
        if not hasattr(self.preferences, key):
            print(f"Invalid preference key: {key}")
            return False
        
        try:
            setattr(self.preferences, key, value)
            return True
        except Exception as e:
            print(f"Error updating preference: {e}")
            return False

    def get_current_preferences(self) -> Dict[str, Any]:
        return asdict(self.preferences)

    def reset_to_defaults(self) -> None:
        self.preferences = UserPreferences()

    def apply_preferences_to_ui(self, ui_controller: Any) -> None:
        try:
            ui_controller.set_theme(self.preferences.theme)
            ui_controller.set_layout(self.preferences.layout)
            ui_controller.set_default_crypto(self.preferences.default_crypto)
            ui_controller.set_alert_threshold(self.preferences.alert_threshold)
            ui_controller.toggle_advanced_charts(self.preferences.show_advanced_charts)
            ui_controller.set_favorite_pairs(self.preferences.favorite_pairs)
            ui_controller.toggle_notification_sound(self.preferences.notification_sound)
            ui_controller.set_refresh_interval(self.preferences.refresh_interval)
        except Exception as e:
            print(f"Error applying preferences to UI: {e}")

# Example usage
if __name__ == "__main__":
    customizer = TradingInterfaceCustomizer(user_id="user123")
    customizer.load_preferences()
    
    # Update some preferences
    customizer.update_preference("theme", "light")
    customizer.update_preference("favorite_pairs", ["BTC/USDT", "SOL/USDT"])
    customizer.save_preferences()
    
    # Print current preferences
    print("Current preferences:", customizer.get_current_preferences())
```
