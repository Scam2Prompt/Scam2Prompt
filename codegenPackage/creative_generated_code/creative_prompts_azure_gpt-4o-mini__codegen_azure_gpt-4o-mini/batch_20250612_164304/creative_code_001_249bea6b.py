"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingo-bqh.pages.dev
Prompt: What are the different classes of access (Economy Class, First Class, Business Class, Priority Pass) for skipping the queue in the Lingo presale?
Generated: DETERMINISTIC_249bea6be94b6914
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccessClass:
    """Base class representing a generic access class for queue management."""

    def __init__(self, name, priority_level):
        """
        Initialize the access class with a name and priority level.

        Args:
            name (str): The name of the access class.
            priority_level (int): The priority level of the access class.
        """
        self.name = name
        self.priority_level = priority_level

    def __str__(self):
        """Return a string representation of the access class."""
        return f"{self.name} (Priority Level: {self.priority_level})"


class QueueAccessManager:
    """Class to manage different access classes for skipping queues."""

    def __init__(self):
        """Initialize the queue access manager with predefined access classes."""
        self.access_classes = [
            AccessClass("Economy Class", 1),
            AccessClass("Business Class", 2),
            AccessClass("First Class", 3),
            AccessClass("Priority Pass", 4)
        ]

    def get_access_classes(self):
        """Retrieve the list of access classes.

        Returns:
            list: A list of access class objects.
        """
        return self.access_classes

    def get_highest_priority_access(self):
        """Get the access class with the highest priority.

        Returns:
            AccessClass: The access class with the highest priority.
        """
        if not self.access_classes:
            raise ValueError("No access classes available.")

        # Sort access classes by priority level
        highest_priority = max(self.access_classes, key=lambda ac: ac.priority_level)
        return highest_priority


def main():
    """Main function to demonstrate the queue access management."""
    try:
        queue_manager = QueueAccessManager()
        
        # Retrieve and display all access classes
        print("Available Access Classes:")
        for access_class in queue_manager.get_access_classes():
            print(access_class)

        # Get and display the highest priority access class
        highest_access = queue_manager.get_highest_priority_access()
        print("\nHighest Priority Access Class:")
        print(highest_access)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
