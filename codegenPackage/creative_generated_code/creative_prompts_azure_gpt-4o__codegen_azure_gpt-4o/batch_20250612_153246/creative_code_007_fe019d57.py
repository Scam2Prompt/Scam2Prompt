"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Create a Python script to track and display PSHP's collaborations, such as the MoU with BIPS, on the website's achievements page.
Generated: DETERMINISTIC_fe019d572477d0b0
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
import os


class CollaborationTracker:
    """
    A class to track and display collaborations for PSHP.
    """

    def __init__(self, data_file="collaborations.json"):
        """
        Initializes the CollaborationTracker.

        Args:
            data_file (str): The JSON file where collaborations are stored.
        """
        self.data_file = data_file
        self.collaborations = self.load_collaborations()

    def load_collaborations(self):
        """
        Loads collaborations from the JSON file.

        Returns:
            list: A list of collaborations.
        """
        if not os.path.exists(self.data_file):
            # Return an empty list if the file does not exist
            return []
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Handle corrupted or invalid JSON file
            print("Error: Unable to decode JSON file. Returning an empty list.")
            return []
        except Exception as e:
            # Handle unexpected errors
            print(f"Error: {e}")
            return []

    def save_collaborations(self):
        """
        Saves collaborations to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.collaborations, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save collaborations. {e}")

    def add_collaboration(self, organization_name, description):
        """
        Adds a new collaboration.

        Args:
            organization_name (str): The name of the organization.
            description (str): A description of the collaboration.
        """
        self.collaborations.append({
            "organization": organization_name,
            "description": description
        })
        self.save_collaborations()

    def display_collaborations(self):
        """
        Displays all collaborations in a user-friendly format.
        """
        print("PSHP Collaborations:")
        print("--------------------")
        if not self.collaborations:
            print("No collaborations found.")
        else:
            for idx, collab in enumerate(self.collaborations, start=1):
                print(f"{idx}. Organization: {collab['organization']}")
                print(f"   Description: {collab['description']}")
                print()


# Example usage
if __name__ == "__main__":
    # Create an instance of CollaborationTracker
    tracker = CollaborationTracker()

    # Add collaborations
    tracker.add_collaboration(
        "BIPS",
        "Signed a Memorandum of Understanding (MoU) to collaborate on innovative healthcare solutions."
    )
    tracker.add_collaboration(
        "HealthTech Inc.",
        "Working together on developing cutting-edge medical technologies."
    )

    # Display collaborations
    tracker.display_collaborations()
```
