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
class Equipment:
    """
    A class to represent equipment managed by a foundation or nonprofit.

    Attributes:
        id (int): Unique identifier for the equipment.
        name (str): Name of the equipment.
        location (str): Location where the equipment is stored.
        status (str): Current status of the equipment (e.g., available, in use, maintenance).
    """

    def __init__(self, id: int, name: str, location: str, status: str = "available"):
        self.id = id
        self.name = name
        self.location = location
        self.status = status

    def update_status(self, new_status: str):
        """
        Update the status of the equipment.

        Args:
            new_status (str): The new status to set for the equipment.
        """
        self.status = new_status


class Site:
    """
    A class to represent a site managed by a foundation or nonprofit.

    Attributes:
        name (str): Name of the site.
        equipment_list (list): List of equipment associated with the site.
    """

    def __init__(self, name: str):
        self.name = name
        self.equipment_list = []

    def add_equipment(self, equipment: Equipment):
        """
        Add equipment to the site.

        Args:
            equipment (Equipment): The equipment to add to the site.
        """
        self.equipment_list.append(equipment)

    def remove_equipment(self, equipment_id: int):
        """
        Remove equipment from the site by its ID.

        Args:
            equipment_id (int): The ID of the equipment to remove.
        """
        self.equipment_list = [eq for eq in self.equipment_list if eq.id != equipment_id]


class CRM:
    """
    A class to manage multiple sites and their equipment for foundations and nonprofits.

    Attributes:
        sites (dict): A dictionary to store sites by their name.
    """

    def __init__(self):
        self.sites = {}

    def add_site(self, site: Site):
        """
        Add a new site to the CRM.

        Args:
            site (Site): The site to add.
        """
        self.sites[site.name] = site

    def get_site(self, site_name: str) -> Site:
        """
        Retrieve a site by its name.

        Args:
            site_name (str): The name of the site to retrieve.

        Returns:
            Site: The site object if found, else raises a KeyError.
        """
        try:
            return self.sites[site_name]
        except KeyError:
            raise ValueError(f"Site '{site_name}' not found.")

    def transfer_equipment(self, equipment_id: int, from_site_name: str, to_site_name: str):
        """
        Transfer equipment from one site to another.

        Args:
            equipment_id (int): The ID of the equipment to transfer.
            from_site_name (str): The name of the site to transfer from.
            to_site_name (str): The name of the site to transfer to.

        Raises:
            ValueError: If the equipment or site is not found.
        """
        from_site = self.get_site(from_site_name)
        to_site = self.get_site(to_site_name)

        # Find the equipment in the from_site
        equipment = next((eq for eq in from_site.equipment_list if eq.id == equipment_id), None)
        if equipment is None:
            raise ValueError(f"Equipment with ID '{equipment_id}' not found in site '{from_site_name}'.")

        # Remove from the from_site and add to the to_site
        from_site.remove_equipment(equipment_id)
        to_site.add_equipment(equipment)

        # Update equipment status to reflect the transfer
        equipment.update_status("available")


# Example usage
if __name__ == "__main__":
    # Initialize CRM
    crm = CRM()

    # Create sites
    site_a = Site("Site A")
    site_b = Site("Site B")

    # Add sites to CRM
    crm.add_site(site_a)
    crm.add_site(site_b)

    # Create equipment
    equipment_1 = Equipment(id=1, name="Excavator", location="Site A")
    equipment_2 = Equipment(id=2, name="Generator", location="Site A")

    # Add equipment to Site A
    site_a.add_equipment(equipment_1)
    site_a.add_equipment(equipment_2)

    # Transfer equipment from Site A to Site B
    try:
        crm.transfer_equipment(equipment_id=1, from_site_name="Site A", to_site_name="Site B")
    except ValueError as e:
        print(e)

    # Output the status of equipment in both sites
    print(f"Site A Equipment: {[eq.name for eq in site_a.equipment_list]}")
    print(f"Site B Equipment: {[eq.name for eq in site_b.equipment_list]}")
```
