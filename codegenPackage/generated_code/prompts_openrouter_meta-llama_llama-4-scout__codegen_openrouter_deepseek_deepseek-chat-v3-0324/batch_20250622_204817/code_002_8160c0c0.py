"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: How does Polkadot Africa facilitate blockchain adoption and development across the continent?
Generated: DETERMINISTIC_8160c0c0460a858a
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates a Polkadot Africa initiative to facilitate blockchain adoption
# and development across Africa through education, grants, and community building.

import json
from typing import Dict, List, Optional
from enum import Enum

class InitiativeType(Enum):
    EDUCATION = "Education"
    GRANTS = "Grants"
    COMMUNITY = "Community Building"
    HACKATHONS = "Hackathons"
    INFRASTRUCTURE = "Infrastructure Development"

class PolkadotAfricaInitiative:
    """
    Represents an initiative by Polkadot Africa to promote blockchain adoption.
    """
    
    def __init__(self, name: str, initiative_type: InitiativeType, countries: List[str], description: str):
        self.name = name
        self.initiative_type = initiative_type
        self.countries = countries
        self.description = description
        self.participants = 0
        self.success_stories = []
    
    def add_participant(self, count: int = 1) -> None:
        """Increment participant count for this initiative."""
        if count < 0:
            raise ValueError("Participant count cannot be negative")
        self.participants += count
    
    def add_success_story(self, story: str) -> None:
        """Add a success story to this initiative."""
        if not story.strip():
            raise ValueError("Success story cannot be empty")
        self.success_stories.append(story)
    
    def to_dict(self) -> Dict:
        """Convert initiative data to dictionary for serialization."""
        return {
            "name": self.name,
            "type": self.initiative_type.value,
            "countries": self.countries,
            "description": self.description,
            "participants": self.participants,
            "success_stories": self.success_stories
        }

class PolkadotAfrica:
    """
    Main class representing Polkadot Africa's efforts to facilitate blockchain adoption.
    """
    
    def __init__(self):
        self.initiatives: List[PolkadotAfricaInitiative] = []
        self.country_coverage = set()
    
    def launch_initiative(self, initiative: PolkadotAfricaInitiative) -> None:
        """Register a new initiative and update country coverage."""
        if not isinstance(initiative, PolkadotAfricaInitiative):
            raise TypeError("Must provide a PolkadotAfricaInitiative object")
        
        self.initiatives.append(initiative)
        self.country_coverage.update(initiative.countries)
    
    def get_initiatives_by_type(self, initiative_type: InitiativeType) -> List[PolkadotAfricaInitiative]:
        """Get all initiatives of a specific type."""
        return [init for init in self.initiatives if init.initiative_type == initiative_type]
    
    def get_country_initiatives(self, country: str) -> List[PolkadotAfricaInitiative]:
        """Get all initiatives in a specific country."""
        if not country.strip():
            raise ValueError("Country name cannot be empty")
        return [init for init in self.initiatives if country in init.countries]
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report of all initiatives."""
        return {
            "total_initiatives": len(self.initiatives),
            "countries_covered": list(self.country_coverage),
            "initiatives_by_type": {
                itype.value: len(self.get_initiatives_by_type(itype)) 
                for itype in InitiativeType
            },
            "success_stories": sum(len(init.success_stories) for init in self.initiatives),
            "total_participants": sum(init.participants for init in self.initiatives)
        }
    
    def save_to_json(self, filename: str) -> None:
        """Save all initiatives data to a JSON file."""
        data = {
            "initiatives": [init.to_dict() for init in self.initiatives],
            "report": self.generate_report()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    polkadot_africa = PolkadotAfrica()
    
    # Create initiatives
    education_init = PolkadotAfricaInitiative(
        "Blockchain 101 Workshops",
        InitiativeType.EDUCATION,
        ["Nigeria", "Kenya", "South Africa"],
        "Introductory workshops on blockchain technology"
    )
    
    grant_init = PolkadotAfricaInitiative(
        "Developer Grants Program",
        InitiativeType.GRANTS,
        ["Ghana", "Egypt", "Senegal"],
        "Funding for promising blockchain projects"
    )
    
    # Add participants and success stories
    education_init.add_participant(150)
    education_init.add_success_story("Trained 50 developers in Lagos who built their first dApps")
    
    grant_init.add_participant(25)
    grant_init.add_success_story("Funded a decentralized identity solution in Accra")
    
    # Launch initiatives
    polkadot_africa.launch_initiative(education_init)
    polkadot_africa.launch_initiative(grant_init)
    
    # Generate report and save
    print(json.dumps(polkadot_africa.generate_report(), indent=2))
    polkadot_africa.save_to_json("polkadot_africa_initiatives.json")
```
