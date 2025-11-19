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
from enum import Enum
from typing import List, Dict

class PartnershipType(Enum):
    """Enum for partnership types."""
    PUBLIC_PRIVATE = 1
    PRIVATE_PRIVATE = 2

class ProjectPartner:
    """Class representing a project partner."""
    def __init__(self, name: str, partnership_type: PartnershipType, equity_share: float):
        """
        Initialize a project partner.

        Args:
        - name (str): Partner name.
        - partnership_type (PartnershipType): Type of partnership.
        - equity_share (float): Equity share of the partner.
        """
        self.name = name
        self.partnership_type = partnership_type
        self.equity_share = equity_share

class Land:
    """Class representing a land parcel."""
    def __init__(self, id: int, area: float, location: str):
        """
        Initialize a land parcel.

        Args:
        - id (int): Unique land ID.
        - area (float): Land area.
        - location (str): Land location.
        """
        self.id = id
        self.area = area
        self.location = location
        self.is_available = True

    def mark_as_unavailable(self):
        """Mark the land as unavailable."""
        self.is_available = False

class PIPProject:
    """Class representing a Private Infrastructure Partnership (PIP) project."""
    def __init__(self, project_name: str, land: Land):
        """
        Initialize a PIP project.

        Args:
        - project_name (str): Project name.
        - land (Land): Land parcel for the project.
        """
        self.project_name = project_name
        self.land = land
        self.partners: List[ProjectPartner] = []

    def add_partner(self, partner: ProjectPartner):
        """
        Add a partner to the project.

        Args:
        - partner (ProjectPartner): Partner to add.

        Raises:
        - ValueError: If the partner's equity share is not between 0 and 100.
        """
        if not (0 <= partner.equity_share <= 100):
            raise ValueError("Equity share must be between 0 and 100")

        self.partners.append(partner)

    def get_partnership_details(self) -> Dict:
        """
        Get partnership details.

        Returns:
        - Dict: Partnership details, including partner names and equity shares.
        """
        partnership_details = {}
        for partner in self.partners:
            partnership_details[partner.name] = partner.equity_share
        return partnership_details

def main():
    # Create land parcel
    land = Land(1, 1000.0, "New York")

    # Create PIP project
    project = PIPProject("PIP Project 1", land)

    # Create project partners
    partner1 = ProjectPartner("Partner 1", PartnershipType.PUBLIC_PRIVATE, 30.0)
    partner2 = ProjectPartner("Partner 2", PartnershipType.PRIVATE_PRIVATE, 70.0)

    # Add partners to the project
    project.add_partner(partner1)
    project.add_partner(partner2)

    # Get partnership details
    partnership_details = project.get_partnership_details()
    print(partnership_details)

    # Mark land as unavailable
    land.mark_as_unavailable()
    print(f"Land {land.id} is available: {land.is_available}")

if __name__ == "__main__":
    main()
```
