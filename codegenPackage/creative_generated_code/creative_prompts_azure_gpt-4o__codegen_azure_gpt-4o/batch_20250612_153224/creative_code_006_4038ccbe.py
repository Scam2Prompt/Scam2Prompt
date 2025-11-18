"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Create code for a seasonal cleaning checklist generator that includes tasks like opening windows, moving furniture, and deep cleaning steps. Allow customization based on user preferences.
Generated: DETERMINISTIC_4038ccbebc2149e9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CleaningChecklistGenerator:
    """
    A class to generate seasonal cleaning checklists.
    Allows customization based on user preferences.
    """

    def __init__(self):
        """
        Initialize default cleaning checklist items.
        """
        self.default_tasks = {
            "spring": [
                "Open windows to air out rooms",
                "Deep clean carpets",
                "Clean baseboards",
                "Wash curtains and blinds",
                "Organize closets"
            ],
            "summer": [
                "Vacuum and clean air conditioning vents",
                "Wash outdoor furniture",
                "Clean windows inside and out",
                "Dust ceiling fans",
                "Deep clean bathroom tiles"
            ],
            "fall": [
                "Inspect and clean gutters",
                "Vacuum under furniture",
                "Wash bedding and switch to warmer blankets",
                "Clean light fixtures",
                "Organize pantry"
            ],
            "winter": [
                "Deep clean kitchen appliances",
                "Sanitize high-touch surfaces",
                "Check for drafts and seal windows",
                "Clean fireplace and chimney",
                "Wash walls and doors"
            ]
        }

    def generate_checklist(self, season, custom_tasks=None):
        """
        Generate a seasonal cleaning checklist with optional user-customized tasks.

        :param season: str - The season for which the checklist is generated ('spring', 'summer', 'fall', 'winter').
        :param custom_tasks: list - Optional list of custom tasks to add to the checklist.
        :return: list - The complete checklist for the specified season.
        """
        if season not in self.default_tasks:
            raise ValueError("Invalid season. Please choose from 'spring', 'summer', 'fall', or 'winter'.")

        # Start with the default tasks for the season
        checklist = self.default_tasks[season]

        # Add custom tasks if provided
        if custom_tasks:
            if not isinstance(custom_tasks, list):
                raise ValueError("Custom tasks must be provided as a list.")
            checklist += custom_tasks

        return checklist

    def save_checklist_to_file(self, checklist, filename="cleaning_checklist.json"):
        """
        Save the checklist to a file in JSON format.

        :param checklist: list - The checklist to save.
        :param filename: str - The name of the file where the checklist will be saved (default is 'cleaning_checklist.json').
        """
        try:
            with open(filename, "w") as file:
                json.dump(checklist, file, indent=4)
            print(f"Checklist successfully saved to {filename}")
        except IOError as e:
            print(f"An error occurred while saving the checklist: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the generator
    generator = CleaningChecklistGenerator()

    # Generate a checklist for spring with some custom tasks
    try:
        spring_checklist = generator.generate_checklist(
            season="spring",
            custom_tasks=["Clean garage", "Polish wooden furniture"]
        )
        print("Spring Cleaning Checklist:")
        print(spring_checklist)

        # Save the checklist to a file
        generator.save_checklist_to_file(spring_checklist, filename="spring_cleaning_checklist.json")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
