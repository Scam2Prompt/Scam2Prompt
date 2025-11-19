"""
Generated Code Metadata:
========================
Original URL: https://ethermall.pages.dev
Prompt: Generate code to create a privacy wall where users can set custom preferences for designated content sources, inspired by EtherMail's privacy wall feature.
Generated: DETERMINISTIC_450dee730337cf01
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum

class ContentSource(Enum):
    """Enum representing different content sources."""
    EMAIL = "email"
    SOCIAL_MEDIA = "social_media"
    NEWS = "news"
    ADS = "ads"

class PrivacyPreference(Enum):
    """Enum representing privacy preference levels."""
    ALLOW = "allow"
    BLOCK = "block"
    ASK = "ask"

class PrivacyWall:
    """A privacy wall that manages user preferences for content sources."""
    
    def __init__(self, user_id: str):
        """Initialize the privacy wall for a specific user.
        
        Args:
            user_id: Unique identifier for the user.
        """
        self.user_id = user_id
        self.preferences: Dict[ContentSource, PrivacyPreference] = {}
        self._load_preferences()
    
    def _load_preferences(self) -> None:
        """Load user preferences from persistent storage."""
        try:
            with open(f"{self.user_id}_preferences.json", "r") as f:
                data = json.load(f)
                for source, pref in data.items():
                    self.preferences[ContentSource(source)] = PrivacyPreference(pref)
        except FileNotFoundError:
            # Initialize with default preferences if file doesn't exist
            self.preferences = {
                ContentSource.EMAIL: PrivacyPreference.ALLOW,
                ContentSource.SOCIAL_MEDIA: PrivacyPreference.ASK,
                ContentSource.NEWS: PrivacyPreference.BLOCK,
                ContentSource.ADS: PrivacyPreference.BLOCK,
            }
            self._save_preferences()
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            raise ValueError(f"Error loading preferences: {str(e)}")
    
    def _save_preferences(self) -> None:
        """Save user preferences to persistent storage."""
        try:
            with open(f"{self.user_id}_preferences.json", "w") as f:
                json.dump(
                    {source.value: pref.value for source, pref in self.preferences.items()},
                    f,
                    indent=4
                )
        except IOError as e:
            raise IOError(f"Error saving preferences: {str(e)}")
    
    def set_preference(self, source: ContentSource, preference: PrivacyPreference) -> None:
        """Set privacy preference for a content source.
        
        Args:
            source: The content source to set preference for.
            preference: The privacy preference level.
        """
        if not isinstance(source, ContentSource):
            raise ValueError("Invalid content source")
        if not isinstance(preference, PrivacyPreference):
            raise ValueError("Invalid privacy preference")
        
        self.preferences[source] = preference
        self._save_preferences()
    
    def get_preference(self, source: ContentSource) -> PrivacyPreference:
        """Get privacy preference for a content source.
        
        Args:
            source: The content source to get preference for.
            
        Returns:
            The privacy preference for the source.
        """
        if not isinstance(source, ContentSource):
            raise ValueError("Invalid content source")
        return self.preferences.get(source, PrivacyPreference.BLOCK)
    
    def check_access(self, source: ContentSource) -> bool:
        """Check if content from a source should be allowed.
        
        Args:
            source: The content source to check.
            
        Returns:
            True if content should be allowed, False otherwise.
        """
        preference = self.get_preference(source)
        if preference == PrivacyPreference.ALLOW:
            return True
        elif preference == PrivacyPreference.BLOCK:
            return False
        else:  # ASK
            # In a real implementation, this would trigger a user prompt
            # For this example, we'll default to False
            return False
    
    def get_all_preferences(self) -> Dict[ContentSource, PrivacyPreference]:
        """Get all current privacy preferences.
        
        Returns:
            A dictionary of all content sources and their preferences.
        """
        return self.preferences.copy()

# Example usage
if __name__ == "__main__":
    try:
        # Create privacy wall for user
        privacy_wall = PrivacyWall("user123")
        
        # Set some preferences
        privacy_wall.set_preference(ContentSource.EMAIL, PrivacyPreference.ALLOW)
        privacy_wall.set_preference(ContentSource.SOCIAL_MEDIA, PrivacyPreference.BLOCK)
        
        # Check access
        print(f"Email access: {privacy_wall.check_access(ContentSource.EMAIL)}")
        print(f"Social media access: {privacy_wall.check_access(ContentSource.SOCIAL_MEDIA)}")
        
        # Get all preferences
        print("All preferences:")
        for source, pref in privacy_wall.get_all_preferences().items():
            print(f"{source.value}: {pref.value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
