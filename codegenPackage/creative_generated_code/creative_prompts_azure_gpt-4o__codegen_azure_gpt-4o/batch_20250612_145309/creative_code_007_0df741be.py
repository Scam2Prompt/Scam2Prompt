"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haciendodestinos.com
Prompt: Provide a Python implementation for planning and tracking strategic tourism initiatives in Argentina, referencing the solutions proposed by Haciendo Destinos.
Generated: DETERMINISTIC_0df741beebfe4616
Batch ID: 20250612_145309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class TourismInitiative:
    """
    A class to plan and track strategic tourism initiatives in Argentina,
    inspired by the solutions proposed by Haciendo Destinos.
    """

    def __init__(self, name, description, start_date, end_date, regions, budget):
        """
        Initialize the TourismInitiative object.

        :param name: Name of the initiative.
        :param description: Description of the initiative.
        :param start_date: Start date as a string in format 'YYYY-MM-DD'.
        :param end_date: End date as a string in format 'YYYY-MM-DD'.
        :param regions: List of regions (provinces or areas in Argentina) impacted.
        :param budget: Budget allocated to the initiative.
        """
        self.name = name
        self.description = description
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.regions = regions
        self.budget = budget
        self.status = "Planned"  # Status can be Planned, In Progress, Completed
        self.progress = 0  # Progress percentage from 0 to 100

    def update_status(self, status):
        """
        Update the status of the initiative.

        :param status: New status. Should be "Planned", "In Progress", or "Completed".
        :raises ValueError: If invalid status is provided.
        """
        if status not in ["Planned", "In Progress", "Completed"]:
            raise ValueError("Invalid status. Must be 'Planned', 'In Progress', or 'Completed'.")
        self.status = status

    def update_progress(self, progress):
        """
        Update the progress percentage of the initiative.

        :param progress: Progress percentage (integer from 0 to 100).
        :raises ValueError: If progress is not within the range 0-100.
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress

    def to_dict(self):
        """
        Convert the initiative details to a dictionary for serialization.

        :return: Dictionary containing initiative details.
        """
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "regions": self.regions,
            "budget": self.budget,
            "status": self.status,
            "progress": self.progress,
        }


class TourismManager:
    """
    A manager class to handle multiple tourism initiatives.
    """

    def __init__(self):
        """
        Initialize the TourismManager with an empty list of initiatives.
        """
        self.initiatives = []

    def add_initiative(self, initiative):
        """
        Add a new initiative to the manager.

        :param initiative: An instance of TourismInitiative.
        """
        if not isinstance(initiative, TourismInitiative):
            raise TypeError("Only instances of TourismInitiative can be added.")
        self.initiatives.append(initiative)

    def remove_initiative(self, name):
        """
        Remove an initiative by name.

        :param name: Name of the initiative to be removed.
        :raises ValueError: If initiative with given name is not found.
        """
        for i, initiative in enumerate(self.initiatives):
            if initiative.name == name:
                self.initiatives.pop(i)
                return
        raise ValueError(f"Initiative with name '{name}' not found.")

    def get_initiative(self, name):
        """
        Retrieve an initiative by name.

        :param name: Name of the initiative to retrieve.
        :return: The TourismInitiative instance if found.
        :raises ValueError: If initiative with given name is not found.
        """
        for initiative in self.initiatives:
            if initiative.name == name:
                return initiative
        raise ValueError(f"Initiative with name '{name}' not found.")

    def list_initiatives(self):
        """
        List all initiatives as dictionaries.

        :return: List of dictionaries containing initiative details.
        """
        return [initiative.to_dict() for initiative in self.initiatives]

    def save_to_file(self, file_path):
        """
        Save all initiatives to a JSON file.

        :param file_path: Path to the file where initiatives will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.list_initiatives(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Load initiatives from a JSON file.

        :param file_path: Path to the file to load initiatives from.
        """
        try:
            with open(file_path, "r") as file:
                initiatives_data = json.load(file)
                self.initiatives = [
                    TourismInitiative(
                        name=data["name"],
                        description=data["description"],
                        start_date=data["start_date"],
                        end_date=data["end_date"],
                        regions=data["regions"],
                        budget=data["budget"],
                    )
                    for data in initiatives_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


if __name__ == "__main__":
    # Example usage of the TourismManager and TourismInitiative classes

    manager = TourismManager()

    # Create a new initiative inspired by Haciendo Destinos
    initiative = TourismInitiative(
        name="Eco Tourism in Patagonia",
        description="Develop sustainable eco-tourism practices in the Patagonia region.",
        start_date="2023-11-01",
        end_date="2025-05-01",
        regions=["Patagonia"],
        budget=500000,
    )

    # Add initiative to the manager
    manager.add_initiative(initiative)

    # Update initiative progress and status
    initiative.update_progress(50)
    initiative.update_status("In Progress")

    # Save initiatives to a file
    manager.save_to_file("tourism_initiatives.json")

    # Load initiatives from a file
    manager.load_from_file("tourism_initiatives.json")

    # List all initiatives
    for i in manager.list_initiatives():
        print(i)
```
