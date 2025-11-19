"""
Generated Code Metadata:
========================
Original URL: https://frame.money
Prompt: "Write a Python script to handle user privacy preferences for a website with a privacy policy similar to frame.money's."
Generated: DETERMINISTIC_4b0b02051511efe7
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, Optional, Any

class PrivacyPreferencesManager:
    """
    Manages user privacy preferences for a website.
    Handles storage, retrieval, and updating of preferences.
    """

    def __init__(self, storage_file: str = "privacy_preferences.json"):
        """
        Initialize the PrivacyPreferencesManager.
        
        Args:
            storage_file: Path to JSON file where preferences will be stored.
        """
        self.storage_file = storage_file
        self.default_preferences = {
            "essential": True,  # Essential cookies cannot be disabled
            "analytics": False,
            "marketing": False,
            "performance": False,
            "functional": False,
            "last_updated": None
        }

    def load_preferences(self, user_id: str) -> Dict[str, Any]:
        """
        Load user's privacy preferences from storage.
        
        Args:
            user_id: Unique identifier for the user.
            
        Returns:
            Dictionary containing user's privacy preferences.
            
        Raises:
            IOError: If there's an issue reading the storage file.
            ValueError: If the stored data is malformed.
        """
        try:
            with open(self.storage_file, 'r') as f:
                all_preferences = json.load(f)
                return all_preferences.get(user_id, self.default_preferences.copy())
        except FileNotFoundError:
            return self.default_preferences.copy()
        except json.JSONDecodeError:
            raise ValueError("Corrupted preferences storage file")
        except Exception as e:
            raise IOError(f"Failed to load preferences: {str(e)}")

    def save_preferences(self, user_id: str, preferences: Dict[str, Any]) -> None:
        """
        Save user's privacy preferences to storage.
        
        Args:
            user_id: Unique identifier for the user.
            preferences: Dictionary containing privacy preferences to save.
            
        Raises:
            IOError: If there's an issue writing to the storage file.
            ValueError: If preferences data is invalid.
        """
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary")
            
        # Validate preferences against defaults
        for key in self.default_preferences:
            if key not in preferences:
                raise ValueError(f"Missing required preference: {key}")
                
        # Set last updated timestamp
        preferences["last_updated"] = datetime.utcnow().isoformat()

        try:
            # Try to load existing data first
            try:
                with open(self.storage_file, 'r') as f:
                    all_preferences = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                all_preferences = {}

            # Update the specific user's preferences
            all_preferences[user_id] = preferences

            # Write back to file
            with open(self.storage_file, 'w') as f:
                json.dump(all_preferences, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save preferences: {str(e)}")

    def update_preferences(self, user_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update user's privacy preferences with new values.
        
        Args:
            user_id: Unique identifier for the user.
            updates: Dictionary containing preference updates.
            
        Returns:
            Updated preferences dictionary.
            
        Raises:
            ValueError: If updates contain invalid preferences.
        """
        # Load current preferences
        current_prefs = self.load_preferences(user_id)
        
        # Validate updates
        for key, value in updates.items():
            if key not in self.default_preferences:
                raise ValueError(f"Invalid preference key: {key}")
            if key == "essential" and not value:
                raise ValueError("Essential cookies cannot be disabled")
            if not isinstance(value, bool):
                raise ValueError(f"Preference {key} must be a boolean")
                
        # Apply updates
        current_prefs.update(updates)
        
        # Save updated preferences
        self.save_preferences(user_id, current_prefs)
        
        return current_prefs

    def get_preference(self, user_id: str, preference_key: str) -> Any:
        """
        Get a specific privacy preference for a user.
        
        Args:
            user_id: Unique identifier for the user.
            preference_key: Key of the preference to retrieve.
            
        Returns:
            Value of the requested preference.
            
        Raises:
            ValueError: If preference_key is invalid.
        """
        if preference_key not in self.default_preferences:
            raise ValueError(f"Invalid preference key: {preference_key}")
            
        preferences = self.load_preferences(user_id)
        return preferences[preference_key]

    def reset_to_defaults(self, user_id: str) -> Dict[str, Any]:
        """
        Reset user's privacy preferences to defaults.
        
        Args:
            user_id: Unique identifier for the user.
            
        Returns:
            Dictionary containing default preferences.
        """
        default_prefs = self.default_preferences.copy()
        self.save_preferences(user_id, default_prefs)
        return default_prefs
```
