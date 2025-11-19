"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo2-162.pages.dev
Prompt: Explain the process for updating skin tones for S1 and S2 citizens in Neo Tokyo.
Generated: DETERMINISTIC_32cab197a56b741d
Batch ID: 20250612_140250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NeoTokyoSkinToneUpdater:
    """
    A class to manage updates to the skin tones of citizens S1 and S2 in Neo Tokyo.
    """

    def __init__(self, citizens_data):
        """
        Initializes the updater with the provided citizens data.
        
        Parameters:
            citizens_data (dict): A dictionary containing citizen identifiers and their data.
        """
        self.citizens_data = citizens_data

    def update_skin_tone(self, citizen_id, new_skin_tone):
        """
        Updates the skin tone of a specified citizen.

        Parameters:
            citizen_id (str): The unique identifier of the citizen.
            new_skin_tone (str): The new skin tone to assign to the citizen.

        Raises:
            ValueError: If the citizen ID does not exist or if the new skin tone is invalid.
        """
        if citizen_id not in self.citizens_data:
            raise ValueError(f"Citizen ID {citizen_id} does not exist.")

        if new_skin_tone not in ["light", "medium", "dark"]:
            raise ValueError(f"Invalid skin tone '{new_skin_tone}'. Must be one of: ['light', 'medium', 'dark'].")

        # Update the skin tone
        self.citizens_data[citizen_id]["skin_tone"] = new_skin_tone
        print(f"Updated citizen {citizen_id} skin tone to '{new_skin_tone}'.")

    def update_multiple_skin_tones(self, updates):
        """
        Updates the skin tones of multiple citizens.

        Parameters:
            updates (dict): A dictionary where keys are citizen IDs and values are the new skin tones.

        Raises:
            Exception: If any errors occur during the update process.
        """
        for citizen_id, new_skin_tone in updates.items():
            try:
                self.update_skin_tone(citizen_id, new_skin_tone)
            except ValueError as e:
                # Log the error (could be printed, logged to a file, etc.)
                print(f"Error updating citizen {citizen_id}: {e}")

if __name__ == "__main__":
    # Example citizen data structure
    citizens_data = {
        "S1": {"name": "Alice", "skin_tone": "light"},
        "S2": {"name": "Bob", "skin_tone": "medium"}
    }

    # Create an instance of the updater
    updater = NeoTokyoSkinToneUpdater(citizens_data)

    # Update skin tones for multiple citizens
    skin_tone_updates = {
        "S1": "dark",
        "S2": "light"
    }
    
    updater.update_multiple_skin_tones(skin_tone_updates)
```
