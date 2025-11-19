"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Generate a code snippet for a party planning application that includes features for organizing children's birthday parties, including customizable themes and entertainment options as described on Wonderplanet.ee.
Generated: DETERMINISTIC_1546cee2d70f63bf
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define custom exceptions for the application
class PartyPlanningError(Exception):
    """Base class for party planning errors."""
    pass

class InvalidInputError(PartyPlanningError):
    """Raised when invalid input is provided."""
    pass

# Define a class for the party planning application
class PartyPlanner:
    def __init__(self):
        """Initialize the PartyPlanner with default options."""
        self.themes = ["Superheroes", "Princess Castle", "Jungle Adventure", "Space Odyssey"]
        self.entertainment_options = ["Clown Show", "Magic Performance", "Face Painting", "Balloon Twisting"]
        self.booked_parties = []

    def view_options(self):
        """View available themes and entertainment options."""
        return {
            "Themes": self.themes,
            "Entertainment Options": self.entertainment_options
        }

    def customize_party(self, theme, entertainment, number_of_guests):
        """
        Customize a party by specifying theme, entertainment, and number of guests.
        
        Args:
            theme (str): The theme of the party.
            entertainment (str): The entertainment option for the party.
            number_of_guests (int): Number of guests attending the party.

        Returns:
            dict: Details of the customized party.
        """
        # Validate input
        if theme not in self.themes:
            raise InvalidInputError(f"Invalid theme selected. Available themes: {self.themes}")
        if entertainment not in self.entertainment_options:
            raise InvalidInputError(f"Invalid entertainment option selected. Available options: {self.entertainment_options}")
        if not isinstance(number_of_guests, int) or number_of_guests <= 0:
            raise InvalidInputError("Number of guests must be a positive integer.")

        # Create party details
        party_details = {
            "Theme": theme,
            "Entertainment": entertainment,
            "Number of Guests": number_of_guests
        }
        self.booked_parties.append(party_details)
        return party_details

    def view_booked_parties(self):
        """View all booked parties."""
        return self.booked_parties

    def save_booked_parties_to_file(self, file_path):
        """
        Save booked parties to a JSON file.
        
        Args:
            file_path (str): The file path to save the party details.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.booked_parties, file, indent=4)
        except Exception as e:
            raise PartyPlanningError(f"An error occurred while saving to file: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        planner = PartyPlanner()
        print("Available options:", planner.view_options())

        # Customize and book a party
        party = planner.customize_party(
            theme="Superheroes",
            entertainment="Magic Performance",
            number_of_guests=15
        )
        print("Party booked:", party)

        # View booked parties
        print("Booked parties:", planner.view_booked_parties())

        # Save booked parties to a file
        planner.save_booked_parties_to_file("booked_parties.json")
        print("Booked parties saved to booked_parties.json")

    except PartyPlanningError as e:
        print(f"Error: {e}")
```
