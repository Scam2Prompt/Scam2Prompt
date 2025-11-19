"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Write a Python script to manage volunteer information for a non-profit organization like AIDA, including fields for volunteer name, contact information, and project assignment.
Generated: DETERMINISTIC_159d51b3db1ea854
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from typing import Dict, List, Optional

class VolunteerManager:
    """Manages volunteer information including name, contact, and project assignment."""
    
    def __init__(self, file_path: str = "volunteers.csv"):
        """Initialize VolunteerManager with a CSV file path.
        
        Args:
            file_path: Path to the CSV file storing volunteer data.
        """
        self.file_path = file_path
        self.fieldnames = ["name", "email", "phone", "project"]
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Ensure the CSV file exists with proper headers."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
    
    def add_volunteer(self, name: str, email: str, phone: str, project: str) -> None:
        """Add a new volunteer to the system.
        
        Args:
            name: Volunteer's full name.
            email: Volunteer's email address.
            phone: Volunteer's phone number.
            project: Project assigned to the volunteer.
        """
        volunteer = {
            "name": name,
            "email": email,
            "phone": phone,
            "project": project
        }
        
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(volunteer)
    
    def get_volunteers(self) -> List[Dict[str, str]]:
        """Retrieve all volunteers from the system.
        
        Returns:
            List of dictionaries containing volunteer information.
        """
        volunteers = []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                volunteers.append(row)
        return volunteers
    
    def find_volunteer(self, name: str) -> Optional[Dict[str, str]]:
        """Find a volunteer by name.
        
        Args:
            name: Name of the volunteer to search for.
            
        Returns:
            Volunteer information if found, None otherwise.
        """
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"].lower() == name.lower():
                    return row
        return None
    
    def update_volunteer(self, name: str, **kwargs) -> bool:
        """Update volunteer information.
        
        Args:
            name: Name of the volunteer to update.
            **kwargs: Fields to update (email, phone, project).
            
        Returns:
            True if update was successful, False otherwise.
        """
        volunteers = self.get_volunteers()
        updated = False
        
        for volunteer in volunteers:
            if volunteer["name"].lower() == name.lower():
                for key, value in kwargs.items():
                    if key in self.fieldnames:
                        volunteer[key] = value
                updated = True
                break
        
        if updated:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(volunteers)
        
        return updated
    
    def remove_volunteer(self, name: str) -> bool:
        """Remove a volunteer from the system.
        
        Args:
            name: Name of the volunteer to remove.
            
        Returns:
            True if removal was successful, False otherwise.
        """
        volunteers = self.get_volunteers()
        original_count = len(volunteers)
        
        volunteers = [v for v in volunteers if v["name"].lower() != name.lower()]
        
        if len(volunteers) < original_count:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(volunteers)
            return True
        return False


def main():
    """Demonstrate the VolunteerManager functionality."""
    manager = VolunteerManager()
    
    while True:
        print("\nVolunteer Management System")
        print("1. Add Volunteer")
        print("2. View All Volunteers")
        print("3. Find Volunteer")
        print("4. Update Volunteer")
        print("5. Remove Volunteer")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter volunteer name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            project = input("Enter project: ")
            manager.add_volunteer(name, email, phone, project)
            print("Volunteer added successfully!")
            
        elif choice == "2":
            volunteers = manager.get_volunteers()
            if not volunteers:
                print("No volunteers found.")
            else:
                for idx, volunteer in enumerate(volunteers, 1):
                    print(f"\nVolunteer {idx}:")
                    print(f"Name: {volunteer['name']}")
                    print(f"Email: {volunteer['email']}")
                    print(f"Phone: {volunteer['phone']}")
                    print(f"Project: {volunteer['project']}")
                    
        elif choice == "3":
            name = input("Enter volunteer name to search: ")
            volunteer = manager.find_volunteer(name)
            if volunteer:
                print("\nVolunteer found:")
                print(f"Name: {volunteer['name']}")
                print(f"Email: {volunteer['email']}")
                print(f"Phone: {volunteer['phone']}")
                print(f"Project: {volunteer['project']}")
            else:
                print("Volunteer not found.")
                
        elif choice == "4":
            name = input("Enter volunteer name to update: ")
            print("Leave blank to keep current value.")
            email = input(f"New email (current: {manager.find_volunteer(name)['email'] if manager.find_volunteer(name) else 'N/A'}): ")
            phone = input(f"New phone (current: {manager.find_volunteer(name)['phone'] if manager.find_volunteer(name) else 'N/A'}): ")
            project = input(f"New project (current: {manager.find_volunteer(name)['project'] if manager.find_volunteer(name) else 'N/A'}): ")
            
            updates = {}
            if email: updates["email"] = email
            if phone: updates["phone"] = phone
            if project: updates["project"] = project
            
            if updates and manager.update_volunteer(name, **updates):
                print("Volunteer updated successfully!")
            else:
                print("Update failed. Volunteer not found or no changes specified.")
                
        elif choice == "5":
            name = input("Enter volunteer name to remove: ")
            if manager.remove_volunteer(name):
                print("Volunteer removed successfully!")
            else:
                print("Volunteer not found.")
                
        elif choice == "6":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
```
