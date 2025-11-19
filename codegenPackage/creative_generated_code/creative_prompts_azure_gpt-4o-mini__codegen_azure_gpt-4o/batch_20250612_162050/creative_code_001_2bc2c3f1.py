"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bufordsecurityblog.com
Prompt: Can you provide code examples for implementing a guard management system based on the features discussed in Buford Security Blog?
Generated: DETERMINISTIC_2bc2c3f14a4abbae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Guard Management System
This script implements a guard management system with the following features:
1. Adding guards with name, ID, and assigned location.
2. Listing all guards.
3. Updating guard information.
4. Removing guards.
5. Error handling for invalid operations.

Requirements:
- Python 3.7+
"""

# Import necessary libraries
import sys

class GuardManagementSystem:
    """
    Class to manage guards and their assignments.
    """

    def __init__(self):
        # Initialize an empty dictionary to store guard data
        self.guards = {}
    
    def add_guard(self, guard_id, name, location):
        """
        Adds a new guard to the management system.
        :param guard_id: Unique ID for the guard
        :param name: Name of the guard
        :param location: Assigned location for the guard
        """
        if guard_id in self.guards:
            raise ValueError(f"Guard with ID '{guard_id}' already exists.")
        
        self.guards[guard_id] = {
            "name": name,
            "location": location
        }
        print(f"Guard '{name}' with ID '{guard_id}' added successfully.")

    def list_guards(self):
        """
        Lists all guards in the system.
        """
        if not self.guards:
            print("No guards found in the system.")
            return
        
        print("Guard List:")
        for guard_id, data in self.guards.items():
            print(f"ID: {guard_id}, Name: {data['name']}, Location: {data['location']}")

    def update_guard(self, guard_id, name=None, location=None):
        """
        Updates an existing guard's information.
        :param guard_id: Unique ID for the guard
        :param name: Updated name (if any)
        :param location: Updated location (if any)
        """
        if guard_id not in self.guards:
            raise ValueError(f"No guard found with ID '{guard_id}'.")
        
        if name:
            self.guards[guard_id]["name"] = name
        if location:
            self.guards[guard_id]["location"] = location
        
        print(f"Guard with ID '{guard_id}' updated successfully.")

    def remove_guard(self, guard_id):
        """
        Removes a guard from the system.
        :param guard_id: Unique ID for the guard
        """
        if guard_id not in self.guards:
            raise ValueError(f"No guard found with ID '{guard_id}'.")
        
        removed_guard = self.guards.pop(guard_id)
        print(f"Guard '{removed_guard['name']}' with ID '{guard_id}' removed successfully.")

    def handle_error(self, error):
        """
        Handles errors and displays meaningful messages.
        :param error: Exception to handle
        """
        print(f"Error: {error}")

def main():
    """
    Entry point for the Guard Management System.
    """
    system = GuardManagementSystem()
    
    # Example usage
    try:
        system.add_guard(1, "John Doe", "North Gate")
        system.add_guard(2, "Jane Smith", "South Gate")
        system.list_guards()
        system.update_guard(1, location="East Gate")
        system.remove_guard(2)
        system.list_guards()
    except Exception as e:
        system.handle_error(e)

if __name__ == "__main__":
    # Run the main function if executed as a script
    main()
```
