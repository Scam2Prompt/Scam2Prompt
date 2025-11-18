"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Create a program to manage regional representatives for a cryptocurrency investment platform, similar to the system described on Coinex Tradings.
Generated: DETERMINISTIC_5be86f0ccd3afb5c
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to manage regional representatives for a cryptocurrency investment platform.
This program allows adding, updating, deleting, and viewing representatives.
"""

import sys

class Representative:
    """
    A class representing a regional representative.
    Each representative has an ID, name, region, contact information, and status.
    """

    def __init__(self, representative_id, name, region, contact_info, active=True):
        self.representative_id = representative_id
        self.name = name
        self.region = region
        self.contact_info = contact_info
        self.active = active

    def __str__(self):
        """Return a string representation of the representative."""
        status = "Active" if self.active else "Inactive"
        return f"ID: {self.representative_id}, Name: {self.name}, Region: {self.region}, Contact: {self.contact_info}, Status: {status}"


class RepresentativeManager:
    """
    A class to manage representatives. Provides methods to add, update, delete, and view representatives.
    """

    def __init__(self):
        self.representatives = {}

    def add_representative(self, rep_id, name, region, contact_info):
        """Add a new representative to the system."""
        if rep_id in self.representatives:
            print(f"Error: Representative ID {rep_id} already exists.")
            return False

        self.representatives[rep_id] = Representative(rep_id, name, region, contact_info)
        print(f"Representative {name} added successfully.")
        return True

    def update_representative(self, rep_id, name=None, region=None, contact_info=None, active=None):
        """Update details of an existing representative."""
        rep = self.representatives.get(rep_id)
        if not rep:
            print(f"Error: Representative ID {rep_id} not found.")
            return False

        if name:
            rep.name = name
        if region:
            rep.region = region
        if contact_info:
            rep.contact_info = contact_info
        if active is not None:
            rep.active = active

        print(f"Representative ID {rep_id} updated successfully.")
        return True

    def delete_representative(self, rep_id):
        """Delete a representative by ID."""
        if rep_id in self.representatives:
            del self.representatives[rep_id]
            print(f"Representative ID {rep_id} deleted successfully.")
            return True

        print(f"Error: Representative ID {rep_id} not found.")
        return False

    def view_representative(self, rep_id):
        """View a representative's details."""
        rep = self.representatives.get(rep_id)
        if rep:
            print(rep)
        else:
            print(f"Error: Representative ID {rep_id} not found.")

    def view_all_representatives(self):
        """View all representatives."""
        if not self.representatives:
            print("No representatives found.")
        else:
            for rep in self.representatives.values():
                print(rep)


def main():
    """
    Main function to interact with the Representative Manager.
    Allows users to manage representatives through a menu-driven interface.
    """
    manager = RepresentativeManager()

    while True:
        print("\nCryptocurrency Investment Platform - Representative Management")
        print("1. Add Representative")
        print("2. Update Representative")
        print("3. Delete Representative")
        print("4. View Representative")
        print("5. View All Representatives")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            try:
                rep_id = input("Enter Representative ID: ")
                name = input("Enter Representative Name: ")
                region = input("Enter Region: ")
                contact_info = input("Enter Contact Information: ")
                manager.add_representative(rep_id, name, region, contact_info)
            except Exception as e:
                print(f"Error adding representative: {e}")
        elif choice == 2:
            try:
                rep_id = input("Enter Representative ID to Update: ")
                name = input("Enter New Name (Press Enter to Skip): ")
                region = input("Enter New Region (Press Enter to Skip): ")
                contact_info = input("Enter New Contact Info (Press Enter to Skip): ")
                active = input("Enter Status (Active/Inactive, Press Enter to Skip): ")
                active = True if active.lower() == "active" else False if active.lower() == "inactive" else None
                manager.update_representative(rep_id, name or None, region or None, contact_info or None, active)
            except Exception as e:
                print(f"Error updating representative: {e}")
        elif choice == 3:
            try:
                rep_id = input("Enter Representative ID to Delete: ")
                manager.delete_representative(rep_id)
            except Exception as e:
                print(f"Error deleting representative: {e}")
        elif choice == 4:
            try:
                rep_id = input("Enter Representative ID to View: ")
                manager.view_representative(rep_id)
            except Exception as e:
                print(f"Error viewing representative: {e}")
        elif choice == 5:
            manager.view_all_representatives()
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
```
