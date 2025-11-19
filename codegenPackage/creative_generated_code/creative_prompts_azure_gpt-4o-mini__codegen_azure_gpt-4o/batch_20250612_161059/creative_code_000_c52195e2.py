"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Generate a Python script that implements a tree planting initiative, inspired by the afforestation goals of Indological India.
Generated: DETERMINISTIC_c52195e274316311
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tree Planting Initiative Script
Inspired by the afforestation goals of Indological India.

This script tracks the progress of a tree planting initiative, allowing users to add tree planting events,
view statistics, and generate reports.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Union

# Constants
DATA_FILE = "tree_planting_data.json"

# Error messages
ERROR_INVALID_EVENT = "Invalid tree planting event. Please provide a valid number of trees planted."


class TreePlantingInitiative:
    """Class to manage the tree planting initiative."""

    def __init__(self, data_file: str = DATA_FILE):
        """
        Initializes the initiative with a data file.

        :param data_file: Path to the JSON file used for storing data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """
        Loads existing data from the JSON file.

        :return: Dictionary containing tree planting data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load existing data ({e}). Starting fresh.")
        return {"events": [], "total_trees_planted": 0}

    def _save_data(self) -> None:
        """
        Saves current data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error: Failed to save data ({e}).")

    def add_tree_planting_event(self, trees_planted: int, location: str) -> None:
        """
        Adds a tree planting event to the initiative.

        :param trees_planted: Number of trees planted.
        :param location: Location where the trees were planted.
        """
        if trees_planted <= 0:
            raise ValueError(ERROR_INVALID_EVENT)

        event = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "trees_planted": trees_planted,
            "location": location
        }
        self.data["events"].append(event)
        self.data["total_trees_planted"] += trees_planted

        # Save data after adding the event
        self._save_data()

    def generate_report(self) -> str:
        """
        Generates a text report of the initiative's progress.

        :return: A formatted string report.
        """
        report = [
            "Tree Planting Initiative Report",
            "=" * 40,
            f"Total Trees Planted: {self.data['total_trees_planted']}",
            "",
            "Events:"
        ]
        for event in self.data["events"]:
            report.append(
                f" - {event['date']} | {event['trees_planted']} trees | Location: {event['location']}"
            )
        return "\n".join(report)

    def get_statistics(self) -> Dict[str, Union[int, List]]:
        """
        Retrieves statistics about the initiative.

        :return: Dictionary containing statistics.
        """
        return {
            "total_trees_planted": self.data["total_trees_planted"],
            "event_count": len(self.data["events"]),
            "events": self.data["events"]
        }


def main():
    """Main function to handle user interaction."""
    initiative = TreePlantingInitiative()

    while True:
        print("\nTree Planting Initiative")
        print("1. Add Tree Planting Event")
        print("2. View Statistics")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                trees = int(input("Number of trees planted: ").strip())
                location = input("Location of tree planting: ").strip()
                initiative.add_tree_planting_event(trees, location)
                print("Tree planting event added successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            stats = initiative.get_statistics()
            print("\nStatistics:")
            print(f"Total Trees Planted: {stats['total_trees_planted']}")
            print(f"Number of Events: {stats['event_count']}")
        elif choice == "3":
            print("\nReport:")
            print(initiative.generate_report())
        elif choice == "4":
            print("Exiting the initiative. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
