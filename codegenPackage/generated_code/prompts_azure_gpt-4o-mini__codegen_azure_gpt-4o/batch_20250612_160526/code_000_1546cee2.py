"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Generate a code snippet for a party planning application that includes features for organizing children's birthday parties, including customizable themes and entertainment options as described on Wonderplanet.ee.
Generated: DETERMINISTIC_1546cee2d70f63bf
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PartyPlanner:
    """
    A class to organize children's birthday parties with customizable themes and entertainment options.
    """

    def __init__(self):
        """
        Initializes the PartyPlanner with default themes and entertainment options.
        """
        self.themes = ["Pirates", "Princesses", "Superheroes", "Space Adventure", "Animal Safari"]
        self.entertainment_options = ["Magician", "Clown", "Face Painting", "Balloon Twisting", "Puppet Show"]
        self.parties = []  # Stores planned parties

    def list_themes(self):
        """
        Lists all available themes.
        """
        return self.themes

    def list_entertainment_options(self):
        """
        Lists all available entertainment options.
        """
        return self.entertainment_options

    def plan_party(self, name, age, theme, entertainment):
        """
        Plans a party with the given details.

        Args:
            name (str): Name of the child.
            age (int): Age of the child.
            theme (str): Selected theme for the party.
            entertainment (str): Selected entertainment option.

        Returns:
            dict: Details of the planned party.
        """
        # Validate theme and entertainment
        if theme not in self.themes:
            raise ValueError(f"Invalid theme selected. Available themes: {', '.join(self.themes)}")
        if entertainment not in self.entertainment_options:
            raise ValueError(f"Invalid entertainment option selected. Available options: {', '.join(self.entertainment_options)}")

        # Create party details
        party = {
            "child_name": name,
            "child_age": age,
            "theme": theme,
            "entertainment": entertainment
        }
        self.parties.append(party)
        return party

    def view_planned_parties(self):
        """
        Returns a list of all planned parties.
        """
        return self.parties

    def save_parties_to_file(self, filename="planned_parties.json"):
        """
        Saves all planned parties to a JSON file.

        Args:
            filename (str): Name of the file to save the parties. Defaults to 'planned_parties.json'.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.parties, file, indent=4)
        except IOError as e:
            print(f"Error saving parties to file: {e}")

    def load_parties_from_file(self, filename="planned_parties.json"):
        """
        Loads planned parties from a JSON file.

        Args:
            filename (str): Name of the file to load the parties from. Defaults to 'planned_parties.json'.
        """
        try:
            with open(filename, "r") as file:
                self.parties = json.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found. No parties loaded.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    planner = PartyPlanner()

    # List available themes and entertainment options
    print("Available Themes:", planner.list_themes())
    print("Available Entertainment Options:", planner.list_entertainment_options())

    # Plan a party
    try:
        party = planner.plan_party(name="Alice", age=7, theme="Princesses", entertainment="Magician")
        print("Party Planned:", party)
    except ValueError as e:
        print(e)

    # View all planned parties
    print("Planned Parties:", planner.view_planned_parties())

    # Save parties to file
    planner.save_parties_to_file()

    # Load parties from file
    planner.load_parties_from_file()
    print("Loaded Parties:", planner.view_planned_parties())
```
