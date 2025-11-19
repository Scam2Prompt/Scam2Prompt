"""
Generated Code Metadata:
========================
Original URL: https://claimlink.io
Prompt: Develop a lead qualification framework for personal injury cases, including criteria for truck accidents, car accidents, public transport accidents, and wrongful death cases.
Generated: DETERMINISTIC_dd620cb57500d98c
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, Optional, List
from dataclasses import dataclass
from datetime import datetime

class AccidentType(Enum):
    """Enum representing different types of accident cases."""
    TRUCK_ACCIDENT = "Truck Accident"
    CAR_ACCIDENT = "Car Accident"
    PUBLIC_TRANSPORT_ACCIDENT = "Public Transport Accident"
    WRONGFUL_DEATH = "Wrongful Death"

@dataclass
class Lead:
    """Data class representing a lead for a personal injury case."""
    case_id: str
    client_name: str
    contact_info: str
    accident_type: AccidentType
    accident_date: datetime
    injuries: List[str]
    medical_treatment: bool
    police_report: bool
    other_parties_involved: bool
    insurance_claim: bool
    notes: Optional[str] = None

class LeadQualifier:
    """Class for qualifying personal injury leads based on specific criteria."""
    
    MINIMUM_AGE_DAYS = 730  # 2 years in days
    
    def __init__(self):
        self.qualification_criteria = {
            AccidentType.TRUCK_ACCIDENT: self._qualify_truck_accident,
            AccidentType.CAR_ACCIDENT: self._qualify_car_accident,
            AccidentType.PUBLIC_TRANSPORT_ACCIDENT: self._qualify_public_transport_accident,
            AccidentType.WRONGFUL_DEATH: self._qualify_wrongful_death
        }
    
    def qualify_lead(self, lead: Lead) -> Dict[str, bool]:
        """
        Qualify a lead based on its accident type and specific criteria.
        
        Args:
            lead: The lead to be qualified.
            
        Returns:
            Dictionary with qualification results and reasons.
            
        Raises:
            ValueError: If the accident type is not supported.
        """
        if lead.accident_type not in self.qualification_criteria:
            raise ValueError(f"Unsupported accident type: {lead.accident_type}")
        
        qualifier = self.qualification_criteria[lead.accident_type]
        return qualifier(lead)
    
    def _is_case_too_old(self, accident_date: datetime) -> bool:
        """Check if the case is beyond the statute of limitations."""
        delta = datetime.now() - accident_date
        return delta.days > self.MINIMUM_AGE_DAYS
    
    def _qualify_truck_accident(self, lead: Lead) -> Dict[str, bool]:
        """Qualify a truck accident lead."""
        qualification = {
            "qualified": False,
            "reasons": []
        }
        
        if self._is_case_too_old(lead.accident_date):
            qualification["reasons"].append("Case is beyond statute of limitations")
            return qualification
        
        if not lead.medical_treatment:
            qualification["reasons"].append("No medical treatment received")
        
        if not lead.police_report:
            qualification["reasons"].append("No police report filed")
        
        if not lead.other_parties_involved:
            qualification["reasons"].append("No other parties involved")
        
        if not qualification["reasons"]:
            qualification["qualified"] = True
        
        return qualification
    
    def _qualify_car_accident(self, lead: Lead) -> Dict[str, bool]:
        """Qualify a car accident lead."""
        qualification = {
            "qualified": False,
            "reasons": []
        }
        
        if self._is_case_too_old(lead.accident_date):
            qualification["reasons"].append("Case is beyond statute of limitations")
            return qualification
        
        if not lead.medical_treatment:
            qualification["reasons"].append("No medical treatment received")
        
        if not lead.police_report:
            qualification["reasons"].append("No police report filed")
        
        if not qualification["reasons"]:
            qualification["qualified"] = True
        
        return qualification
    
    def _qualify_public_transport_accident(self, lead: Lead) -> Dict[str, bool]:
        """Qualify a public transport accident lead."""
        qualification = {
            "qualified": False,
            "reasons": []
        }
        
        if self._is_case_too_old(lead.accident_date):
            qualification["reasons"].append("Case is beyond statute of limitations")
            return qualification
        
        if not lead.medical_treatment:
            qualification["reasons"].append("No medical treatment received")
        
        if not lead.police_report:
            qualification["reasons"].append("No police report filed")
        
        if not lead.insurance_claim:
            qualification["reasons"].append("No insurance claim filed")
        
        if not qualification["reasons"]:
            qualification["qualified"] = True
        
        return qualification
    
    def _qualify_wrongful_death(self, lead: Lead) -> Dict[str, bool]:
        """Qualify a wrongful death lead."""
        qualification = {
            "qualified": False,
            "reasons": []
        }
        
        if self._is_case_too_old(lead.accident_date):
            qualification["reasons"].append("Case is beyond statute of limitations")
            return qualification
        
        if not lead.police_report:
            qualification["reasons"].append("No police report filed")
        
        if not lead.other_parties_involved:
            qualification["reasons"].append("No other parties involved")
        
        if not qualification["reasons"]:
            qualification["qualified"] = True
        
        return qualification

# Example usage
if __name__ == "__main__":
    qualifier = LeadQualifier()
    
    # Create a sample lead
    sample_lead = Lead(
        case_id="PI-2023-001",
        client_name="John Doe",
        contact_info="john.doe@example.com",
        accident_type=AccidentType.CAR_ACCIDENT,
        accident_date=datetime(2023, 5, 15),
        injuries=["Whiplash", "Concussion"],
        medical_treatment=True,
        police_report=True,
        other_parties_involved=True,
        insurance_claim=True,
        notes="Client was rear-ended at a stop sign."
    )
    
    # Qualify the lead
    result = qualifier.qualify_lead(sample_lead)
    print(f"Lead qualified: {result['qualified']}")
    if not result["qualified"]:
        print("Reasons:", ", ".join(result["reasons"]))
```
