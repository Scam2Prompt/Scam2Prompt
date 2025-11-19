"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: Can you provide code examples for implementing a guard management system based on the features discussed in Buford Security Blog?
Generated: DETERMINISTIC_2bc2c3f14a4abbae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guard_management_system.py

class Guard:
    """Class representing a security guard."""
    
    def __init__(self, id, name, shift):
        """
        Initialize a new guard instance.

        :param id: Unique identifier for the guard
        :param name: Name of the guard
        :param shift: Shift assigned to the guard
        """
        self.id = id
        self.name = name
        self.shift = shift

    def __str__(self):
        """Return a string representation of the guard."""
        return f"Guard(ID: {self.id}, Name: {self.name}, Shift: {self.shift})"


class GuardManagementSystem:
    """Class to manage guards in the security system."""
    
    def __init__(self):
        """Initialize the guard management system with an empty list of guards."""
        self.guards = []

    def add_guard(self, guard):
        """
        Add a new guard to the system.

        :param guard: Guard instance to be added
        :raises ValueError: If the guard already exists
        """
        if any(g.id == guard.id for g in self.guards):
            raise ValueError(f"Guard with ID {guard.id} already exists.")
        self.guards.append(guard)

    def remove_guard(self, guard_id):
        """
        Remove a guard from the system by ID.

        :param guard_id: Unique identifier of the guard to be removed
        :raises ValueError: If the guard does not exist
        """
        for guard in self.guards:
            if guard.id == guard_id:
                self.guards.remove(guard)
                return
        raise ValueError(f"Guard with ID {guard_id} not found.")

    def list_guards(self):
        """Return a list of all guards in the system."""
        return self.guards

    def find_guard(self, guard_id):
        """
        Find a guard by ID.

        :param guard_id: Unique identifier of the guard to find
        :return: Guard instance if found, else None
        """
        for guard in self.guards:
            if guard.id == guard_id:
                return guard
        return None


def main():
    """Main function to demonstrate the guard management system."""
    gms = GuardManagementSystem()

    # Adding guards
    try:
        gms.add_guard(Guard(1, "Alice", "Night"))
        gms.add_guard(Guard(2, "Bob", "Day"))
        print("Guards added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing guards
    print("Current Guards:")
    for guard in gms.list_guards():
        print(guard)

    # Finding a guard
    guard = gms.find_guard(1)
    if guard:
        print(f"Found Guard: {guard}")
    else:
        print("Guard not found.")

    # Removing a guard
    try:
        gms.remove_guard(1)
        print("Guard removed successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing guards after removal
    print("Guards after removal:")
    for guard in gms.list_guards():
        print(guard)


if __name__ == "__main__":
    main()
```
