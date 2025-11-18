"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermall.pages.dev
Prompt: Generate code to create a privacy wall where users can set custom preferences for designated content sources, inspired by EtherMail's privacy wall feature.
Generated: DETERMINISTIC_450dee730337cf01
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# privacy_wall.py

import json

class PrivacyWall:
    """
    PrivacyWall class to manage user preferences for designated content sources.
    Inspired by EtherMail's privacy wall feature.
    """
    def __init__(self):
        """
        Initializes an empty privacy wall with no preferences set.
        """
        self.preferences = {}

    def add_preference(self, source, preferences):
        """
        Adds or updates preferences for a specific content source.
        
        Args:
            source (str): The name of the content source.
            preferences (dict): A dictionary of preferences for the source.
        
        Raises:
            ValueError: If preferences is not a dictionary.
        """
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary.")
        
        self.preferences[source] = preferences

    def remove_preference(self, source):
        """
        Removes preferences for a specific content source.
        
        Args:
            source (str): The name of the content source.
        
        Raises:
            KeyError: If the content source does not exist in preferences.
        """
        if source not in self.preferences:
            raise KeyError(f"Content source '{source}' not found.")
        
        del self.preferences[source]

    def get_preference(self, source):
        """
        Retrieves preferences for a specific content source.
        
        Args:
            source (str): The name of the content source.
        
        Returns:
            dict: The preferences for the content source.
        
        Raises:
            KeyError: If the content source does not exist in preferences.
        """
        if source not in self.preferences:
            raise KeyError(f"Content source '{source}' not found.")
        
        return self.preferences[source]

    def list_sources(self):
        """
        Lists all content sources with preferences set.
        
        Returns:
            list: A list of content source names.
        """
        return list(self.preferences.keys())

    def save_to_file(self, file_path):
        """
        Saves preferences to a JSON file.
        
        Args:
            file_path (str): The path of the file to save preferences.
        
        Raises:
            IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.preferences, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save preferences to file: {str(e)}")

    def load_from_file(self, file_path):
        """
        Loads preferences from a JSON file.
        
        Args:
            file_path (str): The path of the file to load preferences.
        
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.preferences = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load preferences from file: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON in the file: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        privacy_wall = PrivacyWall()
        
        # Set preferences for a content source
        privacy_wall.add_preference("News Source A", {"email_notifications": False, "sms_notifications": True})
        
        # Retrieve preferences for a content source
        print("Preferences for 'News Source A':", privacy_wall.get_preference("News Source A"))
        
        # List all sources
        print("Content sources:", privacy_wall.list_sources())
        
        # Save preferences to a file
        privacy_wall.save_to_file("preferences.json")
        print("Preferences saved to preferences.json")
        
        # Load preferences from a file
        privacy_wall.load_from_file("preferences.json")
        print("Preferences loaded from preferences.json:", privacy_wall.preferences)
        
        # Remove preferences for a content source
        privacy_wall.remove_preference("News Source A")
        print("Content sources after removal:", privacy_wall.list_sources())
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
