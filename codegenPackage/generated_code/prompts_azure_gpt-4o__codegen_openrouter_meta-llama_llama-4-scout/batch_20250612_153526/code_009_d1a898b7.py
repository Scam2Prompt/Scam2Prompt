"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Generate code for a vocational education partnership management system that facilitates collaboration between schools and international organizations, inspired by AVEA's joint education programs.
Generated: DETERMINISTIC_d1a898b7ab869762
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vocational_education_partnership_management_system.py

from typing import List, Dict
from enum import Enum
from datetime import datetime

class PartnershipStatus(str, Enum):
    """Partnership status"""
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

class OrganizationType(str, Enum):
    """Organization type"""
    SCHOOL = "school"
    INTERNATIONAL_ORGANIZATION = "international_organization"

class Partnership:
    """Partnership between a school and an international organization"""
    def __init__(self, 
                 id: int, 
                 school_id: int, 
                 organization_id: int, 
                 organization_type: OrganizationType, 
                 start_date: datetime, 
                 end_date: datetime, 
                 status: PartnershipStatus):
        self.id = id
        self.school_id = school_id
        self.organization_id = organization_id
        self.organization_type = organization_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

class School:
    """School entity"""
    def __init__(self, id: int, name: str, country: str):
        self.id = id
        self.name = name
        self.country = country

class InternationalOrganization:
    """International organization entity"""
    def __init__(self, id: int, name: str, country: str):
        self.id = id
        self.name = name
        self.country = country

class VocationalEducationPartnershipManagementSystem:
    """Vocational education partnership management system"""
    def __init__(self):
        self.partnerships: Dict[int, Partnership] = {}
        self.schools: Dict[int, School] = {}
        self.international_organizations: Dict[int, InternationalOrganization] = {}

    def create_partnership(self, 
                          school_id: int, 
                          organization_id: int, 
                          organization_type: OrganizationType, 
                          start_date: datetime, 
                          end_date: datetime) -> Partnership:
        """Create a new partnership"""
        if organization_type == OrganizationType.SCHOOL and school_id == organization_id:
            raise ValueError("School and organization cannot be the same")

        partnership_id = len(self.partnerships) + 1
        partnership = Partnership(partnership_id, 
                                  school_id, 
                                  organization_id, 
                                  organization_type, 
                                  start_date, 
                                  end_date, 
                                  PartnershipStatus.PENDING)
        self.partnerships[partnership_id] = partnership
        return partnership

    def activate_partnership(self, partnership_id: int) -> Partnership:
        """Activate a partnership"""
        if partnership_id not in self.partnerships:
            raise ValueError("Partnership not found")

        partnership = self.partnerships[partnership_id]
        partnership.status = PartnershipStatus.ACTIVE
        return partnership

    def deactivate_partnership(self, partnership_id: int) -> Partnership:
        """Deactivate a partnership"""
        if partnership_id not in self.partnerships:
            raise ValueError("Partnership not found")

        partnership = self.partnerships[partnership_id]
        partnership.status = PartnershipStatus.INACTIVE
        return partnership

    def add_school(self, school: School) -> School:
        """Add a school"""
        self.schools[school.id] = school
        return school

    def add_international_organization(self, organization: InternationalOrganization) -> InternationalOrganization:
        """Add an international organization"""
        self.international_organizations[organization.id] = organization
        return organization

def main():
    # Create a vocational education partnership management system
    system = VocationalEducationPartnershipManagementSystem()

    # Create schools
    school1 = School(1, "School 1", "USA")
    school2 = School(2, "School 2", "Canada")

    # Create international organizations
    organization1 = InternationalOrganization(1, "Organization 1", "France")
    organization2 = InternationalOrganization(2, "Organization 2", "Germany")

    # Add schools and international organizations to the system
    system.add_school(school1)
    system.add_school(school2)
    system.add_international_organization(organization1)
    system.add_international_organization(organization2)

    # Create partnerships
    partnership1 = system.create_partnership(school1.id, organization1.id, OrganizationType.INTERNATIONAL_ORGANIZATION, datetime(2024, 1, 1), datetime(2025, 12, 31))
    partnership2 = system.create_partnership(school2.id, organization2.id, OrganizationType.INTERNATIONAL_ORGANIZATION, datetime(2024, 6, 1), datetime(2026, 5, 31))

    # Activate partnerships
    system.activate_partnership(partnership1.id)
    system.activate_partnership(partnership2.id)

    # Print partnerships
    for partnership in system.partnerships.values():
        print(f"Partnership {partnership.id}: School {partnership.school_id} - Organization {partnership.organization_id} ({partnership.organization_type}) - Status: {partnership.status}")

if __name__ == "__main__":
    main()
```
