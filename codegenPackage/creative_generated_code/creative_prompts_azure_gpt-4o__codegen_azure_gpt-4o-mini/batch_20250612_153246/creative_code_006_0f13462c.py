"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Develop a script to automate the selection of redőny (blinds) types, such as külsőtokos redőny (external box blinds), based on user preferences and building specifications.
Generated: DETERMINISTIC_0f13462cadd96090
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BlindSelector:
    """A class to automate the selection of blind types based on user preferences and building specifications."""

    def __init__(self, building_specifications, user_preferences):
        """
        Initializes the BlindSelector with specified building specifications and user preferences.

        Args:
            building_specifications (dict): Specifications of the building including dimensions and features.
            user_preferences (dict): User preferences regarding the blind selection.
        """
        self.building_specifications = building_specifications
        self.user_preferences = user_preferences
        self.blind_types = self.load_blind_types()

    def load_blind_types(self):
        """Loads available blind types from a JSON file."""
        try:
            with open('blind_types.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise RuntimeError("Blind types configuration file not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Error decoding blind types configuration file.")

    def filter_blinds(self):
        """Filters blind types based on user preferences and building specifications."""
        filtered_blinds = []

        for blind in self.blind_types:
            if self.is_valid_blind(blind):
                filtered_blinds.append(blind)

        return filtered_blinds

    def is_valid_blind(self, blind):
        """Checks if a blind type meets the user's preferences and building specifications.

        Args:
            blind (dict): A blind type with its specifications.

        Returns:
            bool: True if the blind type is valid, False otherwise.
        """
        # Validate dimensions
        if (blind['width'] > self.building_specifications['max_width'] or
                blind['height'] > self.building_specifications['max_height']):
            return False
        
        # Validate user preferences
        if blind['type'] != self.user_preferences['preferred_type']:
            return False
        
        # Additional conditions can be added here

        return True

    def select_blind(self):
        """Selects the best blind option based on filtered results and user preferences."""
        filtered_blinds = self.filter_blinds()

        if not filtered_blinds:
            raise RuntimeError("No suitable blinds found based on the provided specifications and preferences.")

        # For simplicity, return the first suitable blind
        return filtered_blinds[0]

# Example usage
if __name__ == "__main__":
    # Sample building specifications
    building_specifications = {
        'max_width': 120,
        'max_height': 150
    }

    # Sample user preferences
    user_preferences = {
        'preferred_type': 'külsőtokos redőny'
    }

    try:
        blind_selector = BlindSelector(building_specifications, user_preferences)
        selected_blind = blind_selector.select_blind()
        print("Selected blind:", selected_blind)
    except RuntimeError as e:
        print("Error:", e)
```

**Note:** Ensure that the `blind_types.json` file is present in the same directory with appropriate data structure for the code to run successfully. The JSON structure should look similar to this:

```json
[
    {
        "type": "külsőtokos redőny",
        "width": 100,
        "height": 120
    },
    {
        "type": "belsőtokos redőny",
        "width": 80,
        "height": 140
    }
]
```
