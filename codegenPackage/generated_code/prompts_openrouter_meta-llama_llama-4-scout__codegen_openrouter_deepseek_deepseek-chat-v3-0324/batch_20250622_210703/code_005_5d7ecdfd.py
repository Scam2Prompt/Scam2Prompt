"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Suggest a set of safety measures and emergency protocols for a trekking company like Visit Abroad Travels, including travel insurance options and compliance with local regulations."
Generated: DETERMINISTIC_5d7ecdfd93dd31ef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Safety Measures and Emergency Protocols for Trekking Company
This module implements safety protocols, insurance options, and compliance checks
for a trekking company like Visit Abroad Travels.
"""

import json
from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime

class EmergencyContact:
    """Class representing emergency contact information"""
    def __init__(self, name: str, phone: str, relationship: str):
        self.name = name
        self.phone = phone
        self.relationship = relationship

class Trekker:
    """Class representing a trekker with safety information"""
    def __init__(self, name: str, age: int, medical_conditions: str, emergency_contacts: List[EmergencyContact]):
        self.name = name
        self.age = age
        self.medical_conditions = medical_conditions
        self.emergency_contacts = emergency_contacts
        self.insurance_details = None

class InsuranceProvider(Enum):
    """Enumeration of supported insurance providers"""
    WORLD_NOMADS = "World Nomads"
    TRAVEL_GUARD = "Travel Guard"
    ALLIANZ = "Allianz Global Assistance"
    IMG = "IMG Global"

class InsurancePlan:
    """Class representing an insurance plan option"""
    def __init__(self, provider: InsuranceProvider, plan_name: str, coverage_amount: float, adventure_sports: bool):
        self.provider = provider
        self.plan_name = plan_name
        self.coverage_amount = coverage_amount
        self.adventure_sports = adventure_sports

class TrekkingCompany:
    """Main class implementing safety protocols for the trekking company"""
    def __init__(self):
        self.insurance_options = self._load_insurance_options()
        self.safety_protocols = self._load_safety_protocols()
        self.compliance_checklist = self._load_compliance_checklist()

    def _load_insurance_options(self) -> List[InsurancePlan]:
        """Load available insurance options"""
        return [
            InsurancePlan(InsuranceProvider.WORLD_NOMADS, "Explorer Plan", 100000, True),
            InsurancePlan(InsuranceProvider.TRAVEL_GUARD, "Adventure Plan", 75000, True),
            InsurancePlan(InsuranceProvider.ALLIANZ, "Standard Plan", 50000, False),
            InsurancePlan(InsuranceProvider.IMG, "Global Trekker", 125000, True)
        ]

    def _load_safety_protocols(self) -> Dict[str, str]:
        """Load standard safety protocols"""
        return {
            "medical_check": "All trekkers must complete medical check before departure",
            "equipment_check": "All equipment must be inspected before trek",
            "guide_ratio": "Maximum 1 guide per 8 trekkers",
            "emergency_plan": "Detailed emergency evacuation plan must be in place",
            "weather_monitoring": "Daily weather monitoring and route adjustments",
            "communication": "Satellite phones for all guides in remote areas"
        }

    def _load_compliance_checklist(self) -> Dict[str, bool]:
        """Load compliance checklist for different regions"""
        return {
            "nepal": {
                "trekking_permit": True,
                "tim_card": True,
                "guide_requirement": True
            },
            "peru": {
                "inca_trail_permit": True,
                "guide_requirement": True
            },
            "tanzania": {
                "park_fees": True,
                "guide_requirement": True
            }
        }

    def recommend_insurance(self, trekker: Trekker, destination: str) -> Optional[InsurancePlan]:
        """Recommend appropriate insurance plan based on trekker details"""
        if trekker.age > 65:
            return None  # Some plans have age restrictions
        
        for plan in self.insurance_options:
            if plan.adventure_sports and (trekker.medical_conditions.lower() == "none" or "minor" in trekker.medical_conditions.lower()):
                return plan
        return None

    def verify_compliance(self, destination: str) -> Dict[str, bool]:
        """Verify compliance with local regulations for destination"""
        return self.compliance_checklist.get(destination.lower(), {})

    def generate_emergency_plan(self, trekker: Trekker, destination: str) -> Dict:
        """Generate emergency plan document for trekker"""
        return {
            "trekker_name": trekker.name,
            "destination": destination,
            "emergency_contacts": [{"name": ec.name, "phone": ec.phone} for ec in trekker.emergency_contacts],
            "insurance_provider": trekker.insurance_details.provider.value if trekker.insurance_details else "None",
            "local_emergency_numbers": self._get_local_emergency_numbers(destination),
            "protocols": self.safety_protocols,
            "generated_on": datetime.now().isoformat()
        }

    def _get_local_emergency_numbers(self, destination: str) -> Dict[str, str]:
        """Get emergency numbers for destination country"""
        # In a real implementation, this would be a database lookup
        numbers = {
            "nepal": {
                "police": "100",
                "ambulance": "102",
                "tourist_police": "1144"
            },
            "peru": {
                "police": "105",
                "ambulance": "117",
                "tourist_police": "0800-22221"
            },
            "tanzania": {
                "police": "112",
                "ambulance": "112",
                "tourist_police": "0754-783324"
            }
        }
        return numbers.get(destination.lower(), {})

    def register_trekker(self, trekker: Trekker, destination: str) -> bool:
        """Complete registration process including safety checks"""
        if not self.verify_compliance(destination):
            return False
        
        recommended_insurance = self.recommend_insurance(trekker, destination)
        if recommended_insurance:
            trekker.insurance_details = recommended_insurance
        
        return True

# Example usage
if __name__ == "__main__":
    company = TrekkingCompany()
    
    # Create a trekker
    contacts = [
        EmergencyContact("Jane Doe", "+1234567890", "Spouse"),
        EmergencyContact("John Smith", "+1987654321", "Parent")
    ]
    trekker = Trekker("Alex Johnson", 32, "None", contacts)
    
    # Register trekker for Nepal trek
    if company.register_trekker(trekker, "nepal"):
        print("Trekker registered successfully")
        emergency_plan = company.generate_emergency_plan(trekker, "nepal")
        print(json.dumps(emergency_plan, indent=2))
    else:
        print("Registration failed - compliance issues")
```
