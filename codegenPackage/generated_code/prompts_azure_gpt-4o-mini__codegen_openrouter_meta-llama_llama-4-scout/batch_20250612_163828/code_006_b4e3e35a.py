"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Explain how CRM.f facilitates multi-site equipment management for foundations and nonprofits.
Generated: DETERMINISTIC_b4e3e35a6c779560
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# CRM.f Equipment Management Module

class Equipment:
    """Represents a piece of equipment."""

    def __init__(self, id, name, description, location, status):
        """
        Initializes an Equipment object.

        Args:
            id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            description (str): Description of the equipment.
            location (str): Location of the equipment.
            status (str): Status of the equipment (e.g., "active", "inactive").
        """
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.status = status

class Site:
    """Represents a site with equipment."""

    def __init__(self, id, name, location):
        """
        Initializes a Site object.

        Args:
            id (int): Unique identifier for the site.
            name (str): Name of the site.
            location (str): Location of the site.
        """
        self.id = id
        self.name = name
        self.location = location
        self.equipment = []

    def add_equipment(self, equipment):
        """
        Adds equipment to the site.

        Args:
            equipment (Equipment): Equipment to add.
        """
        self.equipment.append(equipment)

    def remove_equipment(self, equipment_id):
        """
        Removes equipment from the site.

        Args:
            equipment_id (int): ID of the equipment to remove.

        Raises:
            ValueError: If equipment not found.
        """
        for equipment in self.equipment:
            if equipment.id == equipment_id:
                self.equipment.remove(equipment)
                return
        raise ValueError("Equipment not found")

class CRM:
    """Represents a CRM system for multi-site equipment management."""

    def __init__(self):
        """
        Initializes a CRM object.
        """
        self.sites = []
        self.equipment = []

    def add_site(self, site):
        """
        Adds a site to the CRM.

        Args:
            site (Site): Site to add.
        """
        self.sites.append(site)

    def add_equipment(self, equipment, site_id):
        """
        Adds equipment to a site.

        Args:
            equipment (Equipment): Equipment to add.
            site_id (int): ID of the site to add equipment to.

        Raises:
            ValueError: If site not found.
        """
        for site in self.sites:
            if site.id == site_id:
                site.add_equipment(equipment)
                self.equipment.append(equipment)
                return
        raise ValueError("Site not found")

    def get_equipment(self, site_id):
        """
        Gets equipment for a site.

        Args:
            site_id (int): ID of the site to get equipment for.

        Returns:
            list[Equipment]: Equipment for the site.

        Raises:
            ValueError: If site not found.
        """
        for site in self.sites:
            if site.id == site_id:
                return site.equipment
        raise ValueError("Site not found")

def main():
    crm = CRM()

    # Create sites
    site1 = Site(1, "Site 1", "Location 1")
    site2 = Site(2, "Site 2", "Location 2")

    # Add sites to CRM
    crm.add_site(site1)
    crm.add_site(site2)

    # Create equipment
    equipment1 = Equipment(1, "Equipment 1", "Description 1", "Location 1", "active")
    equipment2 = Equipment(2, "Equipment 2", "Description 2", "Location 2", "inactive")

    # Add equipment to sites
    crm.add_equipment(equipment1, 1)
    crm.add_equipment(equipment2, 2)

    # Get equipment for a site
    site1_equipment = crm.get_equipment(1)
    print("Site 1 Equipment:")
    for equipment in site1_equipment:
        print(f"ID: {equipment.id}, Name: {equipment.name}, Description: {equipment.description}")

if __name__ == "__main__":
    main()
```
