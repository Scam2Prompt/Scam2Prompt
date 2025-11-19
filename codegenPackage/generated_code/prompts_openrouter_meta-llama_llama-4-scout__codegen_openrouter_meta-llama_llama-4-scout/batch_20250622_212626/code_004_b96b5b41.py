"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Create a basic Python script to track and manage successful real estate ventures, similar to Alghanim Capital's experience in identifying and executing high-potential opportunities."
Generated: DETERMINISTIC_b96b5b41e4ba85e9
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# real_estate_ventures.py

class RealEstateVenture:
    """Represents a real estate venture with its attributes and methods."""

    def __init__(self, name, location, investment, potential_return):
        """
        Initializes a RealEstateVenture object.

        Args:
            name (str): Name of the venture.
            location (str): Location of the venture.
            investment (float): Initial investment in the venture.
            potential_return (float): Potential return on investment.
        """
        self.name = name
        self.location = location
        self.investment = investment
        self.potential_return = potential_return
        self.status = "Prospect"

    def __str__(self):
        return f"{self.name} - {self.location}"

    def execute_venture(self):
        """Marks the venture as executed and calculates the return on investment."""
        self.status = "Executed"
        return self.potential_return - self.investment

    def abandon_venture(self):
        """Marks the venture as abandoned."""
        self.status = "Abandoned"


class RealEstateTracker:
    """Tracks and manages real estate ventures."""

    def __init__(self):
        self.ventures = {}

    def add_venture(self, venture):
        """
        Adds a real estate venture to the tracker.

        Args:
            venture (RealEstateVenture): Venture to add.
        """
        self.ventures[venture.name] = venture

    def remove_venture(self, name):
        """
        Removes a real estate venture from the tracker.

        Args:
            name (str): Name of the venture to remove.

        Raises:
            KeyError: If the venture does not exist.
        """
        if name not in self.ventures:
            raise KeyError(f"Venture '{name}' does not exist.")
        del self.ventures[name]

    def get_venture(self, name):
        """
        Retrieves a real estate venture from the tracker.

        Args:
            name (str): Name of the venture to retrieve.

        Returns:
            RealEstateVenture: The venture object.

        Raises:
            KeyError: If the venture does not exist.
        """
        try:
            return self.ventures[name]
        except KeyError:
            raise KeyError(f"Venture '{name}' does not exist.")

    def list_ventures(self):
        """Lists all real estate ventures in the tracker."""
        return list(self.ventures.values())


def main():
    tracker = RealEstateTracker()

    while True:
        print("\nReal Estate Venture Tracker")
        print("1. Add Venture")
        print("2. Remove Venture")
        print("3. Get Venture")
        print("4. List Ventures")
        print("5. Execute Venture")
        print("6. Abandon Venture")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter venture name: ")
            location = input("Enter venture location: ")
            investment = float(input("Enter initial investment: "))
            potential_return = float(input("Enter potential return: "))
            venture = RealEstateVenture(name, location, investment, potential_return)
            tracker.add_venture(venture)
            print(f"Venture '{name}' added successfully.")

        elif choice == "2":
            name = input("Enter venture name: ")
            try:
                tracker.remove_venture(name)
                print(f"Venture '{name}' removed successfully.")
            except KeyError as e:
                print(e)

        elif choice == "3":
            name = input("Enter venture name: ")
            try:
                venture = tracker.get_venture(name)
                print(f"Name: {venture.name}")
                print(f"Location: {venture.location}")
                print(f"Investment: {venture.investment}")
                print(f"Potential Return: {venture.potential_return}")
                print(f"Status: {venture.status}")
            except KeyError as e:
                print(e)

        elif choice == "4":
            ventures = tracker.list_ventures()
            for venture in ventures:
                print(venture)

        elif choice == "5":
            name = input("Enter venture name: ")
            try:
                venture = tracker.get_venture(name)
                roi = venture.execute_venture()
                print(f"Venture '{name}' executed successfully. ROI: {roi}")
            except KeyError as e:
                print(e)

        elif choice == "6":
            name = input("Enter venture name: ")
            try:
                venture = tracker.get_venture(name)
                venture.abandon_venture()
                print(f"Venture '{name}' abandoned successfully.")
            except KeyError as e:
                print(e)

        elif choice == "7":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
