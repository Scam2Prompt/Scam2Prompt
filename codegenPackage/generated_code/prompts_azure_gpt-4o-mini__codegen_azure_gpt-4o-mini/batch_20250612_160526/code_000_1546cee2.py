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
# party_planner.py

class Party:
    """
    A class to represent a children's birthday party.
    """

    def __init__(self, child_name, age, theme, entertainment_options):
        """
        Initializes a new Party instance.

        :param child_name: Name of the child
        :param age: Age of the child
        :param theme: Theme of the party
        :param entertainment_options: List of entertainment options
        """
        self.child_name = child_name
        self.age = age
        self.theme = theme
        self.entertainment_options = entertainment_options

    def customize_theme(self, new_theme):
        """
        Customize the party theme.

        :param new_theme: New theme for the party
        """
        self.theme = new_theme
        print(f"Theme updated to: {self.theme}")

    def add_entertainment(self, entertainment):
        """
        Add an entertainment option to the party.

        :param entertainment: Entertainment option to add
        """
        if entertainment not in self.entertainment_options:
            self.entertainment_options.append(entertainment)
            print(f"Added entertainment: {entertainment}")
        else:
            print(f"Entertainment option '{entertainment}' already exists.")

    def remove_entertainment(self, entertainment):
        """
        Remove an entertainment option from the party.

        :param entertainment: Entertainment option to remove
        """
        try:
            self.entertainment_options.remove(entertainment)
            print(f"Removed entertainment: {entertainment}")
        except ValueError:
            print(f"Entertainment option '{entertainment}' not found.")

    def display_party_details(self):
        """
        Display the details of the party.
        """
        print(f"Party Details for {self.child_name}'s {self.age}th Birthday:")
        print(f"Theme: {self.theme}")
        print("Entertainment Options:")
        for option in self.entertainment_options:
            print(f"- {option}")


def main():
    """
    Main function to run the party planning application.
    """
    # Example usage
    try:
        party = Party("Alice", 7, "Unicorn", ["Clown", "Magic Show"])
        party.display_party_details()

        # Customizing theme
        party.customize_theme("Fairy Tale")

        # Adding entertainment
        party.add_entertainment("Face Painting")
        party.add_entertainment("Clown")  # Should notify that it already exists

        # Removing entertainment
        party.remove_entertainment("Magic Show")
        party.remove_entertainment("Balloons")  # Should notify that it doesn't exist

        # Display updated party details
        party.display_party_details()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
