"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondo-finance-migration.pages.dev
Prompt: Write a program to track weekly updates of Ondo Points for various asset holders and display the last updated date and next update date.
Generated: DETERMINISTIC_9630bb392eed8f81
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class AssetHolder:
    """
    Class to represent an asset holder with Ondo Points.
    """
    def __init__(self, name):
        """
        Initializes an AssetHolder instance.

        Args:
            name (str): The name of the asset holder.
        """
        self.name = name
        self.points = 0
        self.last_updated = None

    def update_points(self, points):
        """
        Updates the Ondo Points for the asset holder.

        Args:
            points (int): The number of points to add.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points
        self.last_updated = datetime.now()

    def get_next_update_date(self):
        """
        Calculates the next update date, which is one week from the last updated date.

        Returns:
            datetime: The next update date.
        """
        if self.last_updated is None:
            return None
        return self.last_updated + timedelta(weeks=1)

    def __repr__(self):
        return f"{self.name} - Points: {self.points}, Last Updated: {self.last_updated}, Next Update: {self.get_next_update_date()}"

class OndoPointsTracker:
    """
    Class to track Ondo Points for multiple asset holders.
    """
    def __init__(self):
        self.asset_holders = {}

    def add_asset_holder(self, name):
        """
        Adds a new asset holder to the tracker.

        Args:
            name (str): The name of the new asset holder.
        """
        if name in self.asset_holders:
            raise ValueError("Asset holder already exists.")
        self.asset_holders[name] = AssetHolder(name)

    def update_asset_holder_points(self, name, points):
        """
        Updates the points for a specific asset holder.

        Args:
            name (str): The name of the asset holder to update.
            points (int): The number of points to add.
        """
        if name not in self.asset_holders:
            raise ValueError("Asset holder does not exist.")
        self.asset_holders[name].update_points(points)

    def display_asset_holders(self):
        """
        Displays the details of all asset holders.
        """
        for holder in self.asset_holders.values():
            print(holder)

    def save_to_file(self, filename):
        """
        Saves the current state of asset holders to a JSON file.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({name: holder.__dict__ for name, holder in self.asset_holders.items()}, file, default=str)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Loads asset holders from a JSON file.

        Args:
            filename (str): The name of the file to load from.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, info in data.items():
                    holder = AssetHolder(name)
                    holder.points = info['points']
                    holder.last_updated = datetime.fromisoformat(info['last_updated'])
                    self.asset_holders[name] = holder
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    tracker = OndoPointsTracker()

    # Adding asset holders
    tracker.add_asset_holder("Alice")
    tracker.add_asset_holder("Bob")

    # Updating points
    tracker.update_asset_holder_points("Alice", 150)
    tracker.update_asset_holder_points("Bob", 200)

    # Displaying asset holders
    tracker.display_asset_holders()

    # Saving to file
    tracker.save_to_file("ondo_points.json")

    # Loading from file
    tracker.load_from_file("ondo_points.json")
    tracker.display_asset_holders()
```
