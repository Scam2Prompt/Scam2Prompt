"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: What are the key factors that determine the price of a hair transplantation procedure at Clínica Harmonie, and how can a patient get a personalized quote?
Generated: DETERMINISTIC_a3f9a164fe73cdc0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List
import json

# Define enums for different factors affecting price
class HairLossStage(Enum):
    """Stages of hair loss according to Norwood scale"""
    STAGE_I = auto()
    STAGE_II = auto()
    STAGE_III = auto()
    STAGE_IV = auto()
    STAGE_V = auto()
    STAGE_VI = auto()
    STAGE_VII = auto()

class Technique(Enum):
    """Available transplantation techniques"""
    FUE = auto()
    FUT = auto()
    DHI = auto()

class ClinicLocation(Enum):
    """Available clinic locations"""
    MADRID = auto()
    BARCELONA = auto()
    VALENCIA = auto()

@dataclass
class PatientDetails:
    """Data class to store patient information"""
    name: str
    age: int
    hair_loss_stage: HairLossStage
    desired_technique: Technique
    grafts_estimate: int
    location: ClinicLocation
    previous_treatments: Optional[List[str]] = None
    special_requests: Optional[str] = None

class PriceCalculator:
    """Class to calculate hair transplant price based on various factors"""
    
    BASE_PRICES = {
        Technique.FUE: 2.5,
        Technique.FUT: 2.0,
        Technique.DHI: 3.0
    }
    
    LOCATION_MULTIPLIERS = {
        ClinicLocation.MADRID: 1.0,
        ClinicLocation.BARCELONA: 1.1,
        ClinicLocation.VALENCIA: 0.9
    }
    
    STAGE_MULTIPLIERS = {
        HairLossStage.STAGE_I: 0.8,
        HairLossStage.STAGE_II: 0.9,
        HairLossStage.STAGE_III: 1.0,
        HairLossStage.STAGE_IV: 1.1,
        HairLossStage.STAGE_V: 1.2,
        HairLossStage.STAGE_VI: 1.3,
        HairLossStage.STAGE_VII: 1.4
    }
    
    def calculate_price(self, patient: PatientDetails) -> float:
        """Calculate the total price based on patient details"""
        try:
            base_price = self.BASE_PRICES[patient.desired_technique]
            location_multiplier = self.LOCATION_MULTIPLIERS[patient.location]
            stage_multiplier = self.STAGE_MULTIPLIERS[patient.hair_loss_stage]
            
            total = base_price * patient.grafts_estimate * location_multiplier * stage_multiplier
            
            # Apply discounts for previous treatments if any
            if patient.previous_treatments and len(patient.previous_treatments) > 0:
                total *= 0.95  # 5% discount
            
            return round(total, 2)
        except KeyError as e:
            raise ValueError(f"Invalid input data: {str(e)}") from e

class QuoteRequestHandler:
    """Handles quote requests and generates personalized quotes"""
    
    def __init__(self):
        self.calculator = PriceCalculator()
    
    def generate_quote(self, patient_data: dict) -> dict:
        """Generate a personalized quote based on patient data"""
        try:
            # Validate and parse input data
            patient = self._parse_patient_data(patient_data)
            
            # Calculate price
            total_price = self.calculator.calculate_price(patient)
            
            # Prepare quote response
            return {
                "patient_name": patient.name,
                "technique": patient.desired_technique.name,
                "grafts_estimate": patient.grafts_estimate,
                "location": patient.location.name,
                "total_price": total_price,
                "currency": "EUR"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def _parse_patient_data(self, data: dict) -> PatientDetails:
        """Parse and validate raw patient data"""
        required_fields = ['name', 'age', 'hair_loss_stage', 'desired_technique', 'grafts_estimate', 'location']
        
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        return PatientDetails(
            name=data['name'],
            age=data['age'],
            hair_loss_stage=HairLossStage[data['hair_loss_stage']],
            desired_technique=Technique[data['desired_technique']],
            grafts_estimate=data['grafts_estimate'],
            location=ClinicLocation[data['location']],
            previous_treatments=data.get('previous_treatments'),
            special_requests=data.get('special_requests')
        )

# Example usage
if __name__ == "__main__":
    handler = QuoteRequestHandler()
    
    # Sample patient data
    patient_data = {
        "name": "John Doe",
        "age": 35,
        "hair_loss_stage": "STAGE_III",
        "desired_technique": "FUE",
        "grafts_estimate": 2000,
        "location": "MADRID",
        "previous_treatments": ["Minoxidil"],
        "special_requests": "None"
    }
    
    # Get quote
    quote = handler.generate_quote(patient_data)
    print(json.dumps(quote, indent=2))
```
