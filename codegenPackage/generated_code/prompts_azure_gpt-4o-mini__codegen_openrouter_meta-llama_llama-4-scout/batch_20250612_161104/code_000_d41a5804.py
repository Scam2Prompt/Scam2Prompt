"""
Generated Code Metadata:
========================
Original URL: https://krajkovac.rs
Prompt: Generate a code snippet for a travel app that highlights Krajkovac's unique features, including Krajkovačko Lake and its historical significance.
Generated: DETERMINISTIC_d41a5804552b20a8
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_app.py

class Destination:
    def __init__(self, name, description, features=None):
        """
        Initialize a Destination object.

        Args:
            name (str): Name of the destination.
            description (str): Brief description of the destination.
            features (list, optional): List of unique features. Defaults to None.
        """
        self.name = name
        self.description = description
        self.features = features if features else []

    def add_feature(self, feature):
        """
        Add a unique feature to the destination.

        Args:
            feature (str): Unique feature to add.
        """
        self.features.append(feature)

    def __str__(self):
        return f"{self.name}: {self.description}"


class TravelApp:
    def __init__(self):
        """
        Initialize a TravelApp object.
        """
        self.destinations = {}

    def add_destination(self, destination):
        """
        Add a destination to the travel app.

        Args:
            destination (Destination): Destination object to add.
        """
        self.destinations[destination.name] = destination

    def get_destination(self, name):
        """
        Get a destination by name.

        Args:
            name (str): Name of the destination.

        Returns:
            Destination: Destination object if found, None otherwise.
        """
        return self.destinations.get(name)

    def display_destination_info(self, name):
        """
        Display information about a destination.

        Args:
            name (str): Name of the destination.

        Raises:
            ValueError: If the destination is not found.
        """
        destination = self.get_destination(name)
        if not destination:
            raise ValueError(f"Destination '{name}' not found.")

        print(destination)
        print("Unique Features:")
        for feature in destination.features:
            print(f"- {feature}")


def main():
    try:
        app = TravelApp()

        krajkovac = Destination(
            "Krajkovac",
            "A village in Serbia with a rich history and natural beauty.",
        )
        krajkovac.add_feature("Krajkovačko Lake")
        krajkovac.add_feature("Historical Monastery")
        krajkovac.add_feature("Scenic Hiking Trails")

        app.add_destination(krajkovac)

        print("Travel App")
        print("-----------")
        app.display_destination_info("Krajkovac")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
