"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: "Develop a model operating procedure for shelters and helplines in Kenya, focusing on organizational capacity and sustainability."
Generated: DETERMINISTIC_a138aac709260713
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Model Operating Procedure for Shelters and Helplines in Kenya
Focus: Organizational Capacity and Sustainability
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class ShelterHelplineProcedure:
    """
    A class representing the model operating procedure for shelters and helplines in Kenya.
    Manages organizational capacity and sustainability operations.
    """
    
    def __init__(self, organization_name: str, location: str):
        """
        Initialize the ShelterHelplineProcedure with organization details.
        
        Args:
            organization_name (str): Name of the shelter/helpline organization
            location (str): Physical location of the organization
        """
        self.organization_name = organization_name
        self.location = location
        self.established_date = datetime.now().strftime("%Y-%m-%d")
        self.staff: List[Dict] = []
        self.resources: Dict[str, int] = {}
        self.funding_sources: List[str] = []
        self.policies: List[str] = []
        self.partners: List[str] = []
        self.clients_served: int = 0
        
    def add_staff(self, name: str, role: str, qualifications: str) -> None:
        """
        Add a staff member to the organization.
        
        Args:
            name (str): Staff member's name
            role (str): Their role in the organization
            qualifications (str): Their professional qualifications
        """
        self.staff.append({
            "name": name,
            "role": role,
            "qualifications": qualifications,
            "date_added": datetime.now().strftime("%Y-%m-%d")
        })
        
    def update_resources(self, resource_name: str, quantity: int) -> None:
        """
        Update the organization's resources inventory.
        
        Args:
            resource_name (str): Name of the resource (e.g., beds, food)
            quantity (int): Available quantity
        """
        self.resources[resource_name] = quantity
        
    def add_funding_source(self, source: str) -> None:
        """
        Add a funding source to the organization.
        
        Args:
            source (str): Name of funding source
        """
        if source not in self.funding_sources:
            self.funding_sources.append(source)
            
    def add_policy(self, policy: str) -> None:
        """
        Add an operational policy to the organization.
        
        Args:
            policy (str): Description of the policy
        """
        self.policies.append(policy)
        
    def add_partner(self, partner_name: str) -> None:
        """
        Add a partner organization.
        
        Args:
            partner_name (str): Name of partner organization
        """
        if partner_name not in self.partners:
            self.partners.append(partner_name)
            
    def record_client_service(self, count: int = 1) -> None:
        """
        Record clients served by the organization.
        
        Args:
            count (int): Number of clients served (default 1)
        """
        self.clients_served += count
        
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive report of the organization's status.
        
        Returns:
            Dict: Contains all organizational data
        """
        return {
            "organization_name": self.organization_name,
            "location": self.location,
            "established_date": self.established_date,
            "staff_count": len(self.staff),
            "staff_details": self.staff,
            "resources": self.resources,
            "funding_sources": self.funding_sources,
            "policies": self.policies,
            "partners": self.partners,
            "clients_served": self.clients_served,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def save_to_file(self, filename: str) -> None:
        """
        Save the organization's data to a JSON file.
        
        Args:
            filename (str): Name of the file to save to
        """
        with open(filename, 'w') as f:
            json.dump(self.generate_report(), f, indent=4)
            
    @classmethod
    def load_from_file(cls, filename: str) -> 'ShelterHelplineProcedure':
        """
        Load organization data from a JSON file.
        
        Args:
            filename (str): Name of the file to load from
            
        Returns:
            ShelterHelplineProcedure: New instance with loaded data
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            
        instance = cls(data["organization_name"], data["location"])
        instance.established_date = data["established_date"]
        instance.staff = data["staff_details"]
        instance.resources = data["resources"]
        instance.funding_sources = data["funding_sources"]
        instance.policies = data["policies"]
        instance.partners = data["partners"]
        instance.clients_served = data["clients_served"]
        
        return instance

# Example Usage
if __name__ == "__main__":
    # Create a new shelter/helpline organization
    shelter = ShelterHelplineProcedure("Nairobi Women's Shelter", "Nairobi, Kenya")
    
    # Add staff members
    shelter.add_staff("Jane Muthoni", "Social Worker", "Degree in Social Work")
    shelter.add_staff("Peter Kamau", "Counselor", "Masters in Psychology")
    
    # Update resources
    shelter.update_resources("Beds", 20)
    shelter.update_resources("Food Packages", 100)
    
    # Add funding sources
    shelter.add_funding_source("Ministry of Gender")
    shelter.add_funding_source("UN Women")
    
    # Add policies
    shelter.add_policy("Confidentiality policy for client information")
    shelter.add_policy("Non-discrimination policy")
    
    # Add partners
    shelter.add_partner("Kenya Red Cross")
    shelter.add_partner("Child Welfare Society")
    
    # Record clients served
    shelter.record_client_service(5)
    shelter.record_client_service(3)
    
    # Generate and save report
    report = shelter.generate_report()
    shelter.save_to_file("nairobi_womens_shelter_report.json")
    
    # Load from file
    loaded_shelter = ShelterHelplineProcedure.load_from_file("nairobi_womens_shelter_report.json")
    print(f"Loaded shelter: {loaded_shelter.organization_name}")
```
