"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: Provide Python code to model a private infrastructure partnership (PIP) project, utilizing unused land and integrating project-level partnerships as described by VfM Advisory.
Generated: DETERMINISTIC_b11132336b1cacd3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Land:
    """
    Represents a parcel of unused land for a Private Infrastructure Partnership (PIP) project.
    """

    def __init__(self, area: float, location: str):
        """
        Initializes a Land object.

        :param area: Area of the land in square meters.
        :param location: Location description of the land.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        self.area = area
        self.location = location


class Partnership:
    """
    Represents a partnership in a PIP project.
    """

    def __init__(self, name: str, contribution: float):
        """
        Initializes a Partnership object.

        :param name: Name of the partner.
        :param contribution: Financial contribution of the partner.
        """
        if contribution < 0:
            raise ValueError("Contribution must be a non-negative number.")
        self.name = name
        self.contribution = contribution


class PIPProject:
    """
    Represents a Private Infrastructure Partnership (PIP) project.
    """

    def __init__(self, project_name: str, land: Land):
        """
        Initializes a PIPProject object.

        :param project_name: Name of the PIP project.
        :param land: Land object associated with the project.
        """
        self.project_name = project_name
        self.land = land
        self.partners = []
        self.total_contribution = 0.0

    def add_partner(self, partner: Partnership):
        """
        Adds a partner to the PIP project.

        :param partner: Partnership object to be added.
        """
        self.partners.append(partner)
        self.total_contribution += partner.contribution

    def get_project_details(self):
        """
        Returns the details of the PIP project including partners and total contributions.

        :return: A dictionary containing project details.
        """
        return {
            "project_name": self.project_name,
            "land_area": self.land.area,
            "land_location": self.land.location,
            "partners": [(partner.name, partner.contribution) for partner in self.partners],
            "total_contribution": self.total_contribution
        }


def main():
    """
    Main function to demonstrate the PIP project model.
    """
    try:
        # Create a land object
        unused_land = Land(area=5000, location="Downtown")

        # Create a PIP project
        pip_project = PIPProject(project_name="Urban Development", land=unused_land)

        # Add partners to the project
        partner1 = Partnership(name="Partner A", contribution=100000)
        partner2 = Partnership(name="Partner B", contribution=150000)

        pip_project.add_partner(partner1)
        pip_project.add_partner(partner2)

        # Get and print project details
        project_details = pip_project.get_project_details()
        print(project_details)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
