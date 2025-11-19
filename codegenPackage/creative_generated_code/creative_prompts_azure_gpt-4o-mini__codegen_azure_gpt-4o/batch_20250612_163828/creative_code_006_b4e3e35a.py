"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Explain how CRM.f facilitates multi-site equipment management for foundations and nonprofits.
Generated: DETERMINISTIC_b4e3e35a6c779560
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CRM.f Multi-Site Equipment Management System

This script demonstrates a simplified implementation of a system
that facilitates multi-site equipment management for foundations
and nonprofits.

Key Features:
- Equipment tracking across multiple sites
- Ability to add/update/remove equipment
- Generate reports of equipment status
- Error handling for invalid operations

Note: This is a conceptual implementation. Integration into an actual CRM like CRM.f would require specific APIs.
"""

import json

class EquipmentManagementSystem:
    def __init__(self):
        """
        Initializes the Equipment Management System with a dictionary to store data.
        Each site will have a list of equipment and their statuses.
        """
        self.sites = {}  # Dictionary to store equipment data for each site

    def add_site(self, site_name):
        """
        Adds a new site to the system.

        Args:
            site_name (str): Name of the site to be added.
        """
        if site_name in self.sites:
            raise ValueError(f"Site '{site_name}' already exists.")
        
        self.sites[site_name] = []  # Initialize an empty list for equipment at the site
        print(f"Site '{site_name}' added successfully.")

    def add_equipment(self, site_name, equipment_name, status):
        """
        Adds a new equipment to a site.

        Args:
            site_name (str): Name of the site where the equipment is to be added.
            equipment_name (str): Name of the equipment to be added.
            status (str): Current status of the equipment (e.g., "Available", "In Use", "Under Maintenance").
        """
        if site_name not in self.sites:
            raise ValueError(f"Site '{site_name}' does not exist.")
        
        equipment = {
            "name": equipment_name,
            "status": status
        }
        self.sites[site_name].append(equipment)
        print(f"Equipment '{equipment_name}' added to site '{site_name}'.")

    def update_equipment_status(self, site_name, equipment_name, new_status):
        """
        Updates the status of an existing equipment.

        Args:
            site_name (str): Name of the site where the equipment is located.
            equipment_name (str): Name of the equipment whose status is to be updated.
            new_status (str): New status of the equipment.
        """
        if site_name not in self.sites:
            raise ValueError(f"Site '{site_name}' does not exist.")
        
        for equipment in self.sites[site_name]:
            if equipment["name"] == equipment_name:
                equipment["status"] = new_status
                print(f"Status of equipment '{equipment_name}' updated to '{new_status}'.")
                return
        
        raise ValueError(f"Equipment '{equipment_name}' not found at site '{site_name}'.")

    def remove_equipment(self, site_name, equipment_name):
        """
        Removes an equipment from a site.

        Args:
            site_name (str): Name of the site where the equipment is located.
            equipment_name (str): Name of the equipment to be removed.
        """
        if site_name not in self.sites:
            raise ValueError(f"Site '{site_name}' does not exist.")
        
        for equipment in self.sites[site_name]:
            if equipment["name"] == equipment_name:
                self.sites[site_name].remove(equipment)
                print(f"Equipment '{equipment_name}' removed from site '{site_name}'.")
                return
        
        raise ValueError(f"Equipment '{equipment_name}' not found at site '{site_name}'.")

    def generate_report(self, site_name):
        """
        Generates a report of all equipment at a site.

        Args:
            site_name (str): Name of the site for which the report is to be generated.

        Returns:
            str: A JSON-formatted string containing all equipment data for the site.
        """
        if site_name not in self.sites:
            raise ValueError(f"Site '{site_name}' does not exist.")
        
        return json.dumps(self.sites[site_name], indent=4)

# Example Usage
if __name__ == "__main__":
    try:
        system = EquipmentManagementSystem()

        # Adding sites
        system.add_site("Site A")
        system.add_site("Site B")

        # Adding equipment
        system.add_equipment("Site A", "Laptop", "Available")
        system.add_equipment("Site A", "Projector", "In Use")
        system.add_equipment("Site B", "Tablet", "Under Maintenance")

        # Updating equipment status
        system.update_equipment_status("Site A", "Laptop", "In Use")

        # Removing equipment
        system.remove_equipment("Site A", "Projector")

        # Generating report
        print("Report for Site A:")
        print(system.generate_report("Site A"))

        print("Report for Site B:")
        print(system.generate_report("Site B"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
