"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Create a visitor tracking system for a company using DemirSoft's Ziyaretçi Takip Programı, including features for recording visitor information and tracking entry/exit times.
Generated: DETERMINISTIC_5b52873c2434b3cc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Visitor:
    """
    A class to represent a visitor.
    """
    def __init__(self, name, company, purpose):
        """
        Initialize a visitor with their name, company, and purpose of visit.
        """
        self.name = name
        self.company = company
        self.purpose = purpose
        self.entry_time = None
        self.exit_time = None

    def record_entry(self):
        """
        Record the entry time of the visitor.
        """
        self.entry_time = datetime.datetime.now()

    def record_exit(self):
        """
        Record the exit time of the visitor.
        """
        self.exit_time = datetime.datetime.now()

    def __str__(self):
        """
        Return a string representation of the visitor's information.
        """
        return (f"Visitor: {self.name}, Company: {self.company}, Purpose: {self.purpose}, "
                f"Entry Time: {self.entry_time}, Exit Time: {self.exit_time}")


class VisitorTrackingSystem:
    """
    A class to manage the visitor tracking system.
    """
    def __init__(self):
        """
        Initialize the tracking system with an empty list of visitors.
        """
        self.visitors = []

    def add_visitor(self, name, company, purpose):
        """
        Add a new visitor to the system.
        """
        visitor = Visitor(name, company, purpose)
        visitor.record_entry()
        self.visitors.append(visitor)
        print(f"Visitor {name} has been added and entry time recorded.")

    def record_exit(self, name):
        """
        Record the exit time for a visitor by their name.
        """
        for visitor in self.visitors:
            if visitor.name == name and visitor.exit_time is None:
                visitor.record_exit()
                print(f"Exit time recorded for visitor {name}.")
                return
        print(f"Visitor {name} not found or exit time already recorded.")

    def list_visitors(self):
        """
        List all visitors and their information.
        """
        if not self.visitors:
            print("No visitors recorded.")
        else:
            for visitor in self.visitors:
                print(visitor)

    def find_visitor(self, name):
        """
        Find a visitor by their name and display their information.
        """
        for visitor in self.visitors:
            if visitor.name == name:
                print(visitor)
                return
        print(f"Visitor {name} not found.")


# Example usage
if __name__ == "__main__":
    try:
        system = VisitorTrackingSystem()

        # Adding visitors
        system.add_visitor("John Doe", "Acme Corp", "Business Meeting")
        system.add_visitor("Jane Smith", "Tech Solutions", "Interview")

        # Listing all visitors
        print("\nAll Visitors:")
        system.list_visitors()

        # Recording exit for a visitor
        system.record_exit("John Doe")

        # Finding a specific visitor
        print("\nFinding Visitor:")
        system.find_visitor("John Doe")

        # Listing all visitors again
        print("\nAll Visitors After Exit:")
        system.list_visitors()

    except Exception as e:
        print(f"An error occurred: {e}")
```
