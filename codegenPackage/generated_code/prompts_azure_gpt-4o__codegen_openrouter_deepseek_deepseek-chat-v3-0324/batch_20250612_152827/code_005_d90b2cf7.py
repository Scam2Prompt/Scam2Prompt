"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Write a script to generate insurance quotes for habitation, auto, or health, using the criteria outlined in Crédit Agricole's "Devis Assurance" tools.
Generated: DETERMINISTIC_d90b2cf761694028
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union
import random
from datetime import date, datetime

class InsuranceType(Enum):
    HABITATION = "habitation"
    AUTO = "auto"
    HEALTH = "health"

@dataclass
class Address:
    street: str
    city: str
    postal_code: str
    country: str = "France"

@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: date
    address: Address
    email: str
    phone: str

@dataclass
class Vehicle:
    make: str
    model: str
    year: int
    license_plate: str
    value: float  # in euros
    annual_mileage: int  # in km

@dataclass
class Property:
    address: Address
    surface_area: float  # in m²
    rooms: int
    property_type: str  # "house", "apartment", etc.
    construction_year: int
    value: float  # in euros

@dataclass
class HealthDetails:
    has_chronic_condition: bool
    smoker: bool
    family_members: int

class InsuranceQuote:
    def __init__(self):
        self.quote_id = self._generate_quote_id()
        self.created_at = datetime.now()
        self.valid_until = datetime.now().replace(day=self.created_at.day + 30)
        self.price = 0.0
        self.coverage_details = {}
        self.discounts = []
        self.total_discount = 0.0
        self.final_price = 0.0

    def _generate_quote_id(self) -> str:
        timestamp = int(datetime.now().timestamp())
        random_part = random.randint(1000, 9999)
        return f"CAQ-{timestamp}-{random_part}"

    def calculate_price(self, base_price: float, discounts: List[float]) -> None:
        self.price = base_price
        self.discounts = discounts
        self.total_discount = sum(discounts)
        self.final_price = max(0, self.price - self.total_discount)

    def to_dict(self) -> Dict:
        return {
            "quote_id": self.quote_id,
            "created_at": self.created_at.isoformat(),
            "valid_until": self.valid_until.isoformat(),
            "price": self.price,
            "coverage_details": self.coverage_details,
            "discounts": self.discounts,
            "total_discount": self.total_discount,
            "final_price": self.final_price
        }

class InsuranceQuoteGenerator:
    BASE_PRICES = {
        InsuranceType.HABITATION: 300.0,
        InsuranceType.AUTO: 500.0,
        InsuranceType.HEALTH: 200.0
    }

    def __init__(self):
        self.risk_factors = {
            InsuranceType.HABITATION: self._calculate_habitation_risk,
            InsuranceType.AUTO: self._calculate_auto_risk,
            InsuranceType.HEALTH: self._calculate_health_risk
        }

    def generate_quote(self, insurance_type: InsuranceType, person: Person, 
                      details: Union[Vehicle, Property, HealthDetails]) -> InsuranceQuote:
        quote = InsuranceQuote()
        base_price = self.BASE_PRICES[insurance_type]
        risk_factor = self.risk_factors[insurance_type](person, details)
        
        # Apply risk factor to base price
        adjusted_price = base_price * risk_factor
        
        # Calculate discounts
        discounts = self._calculate_discounts(insurance_type, person)
        
        quote.calculate_price(adjusted_price, discounts)
        quote.coverage_details = self._get_coverage_details(insurance_type)
        
        return quote

    def _calculate_habitation_risk(self, person: Person, property: Property) -> float:
        # Risk factors: property value, construction year, location
        risk = 1.0
        
        # Property value adjustment
        if property.value > 500000:
            risk *= 1.3
        elif property.value < 100000:
            risk *= 0.9
            
        # Age of property adjustment
        current_year = date.today().year
        age = current_year - property.construction_year
        if age > 50:
            risk *= 1.4
        elif age < 10:
            risk *= 0.8
            
        # Location adjustment (simplified)
        if property.address.postal_code.startswith(("75", "13", "69")):  # Paris, Marseille, Lyon
            risk *= 1.2
            
        return max(0.5, min(2.0, risk))  # Cap risk between 0.5 and 2.0

    def _calculate_auto_risk(self, person: Person, vehicle: Vehicle) -> float:
        # Risk factors: driver age, vehicle value, annual mileage
        risk = 1.0
        
        # Driver age adjustment
        today = date.today()
        age = today.year - person.birth_date.year - ((today.month, today.day) < (person.birth_date.month, person.birth_date.day))
        
        if age < 25:
            risk *= 1.8
        elif age > 65:
            risk *= 1.3
        else:
            risk *= 0.9
            
        # Vehicle value adjustment
        if vehicle.value > 40000:
            risk *= 1.4
        elif vehicle.value < 10000:
            risk *= 0.8
            
        # Mileage adjustment
        if vehicle.annual_mileage > 25000:
            risk *= 1.5
        elif vehicle.annual_mileage < 10000:
            risk *= 0.7
            
        return max(0.5, min(2.5, risk))  # Cap risk between 0.5 and 2.5

    def _calculate_health_risk(self, person: Person, health_details: HealthDetails) -> float:
        # Risk factors: age, health conditions, smoker status
        risk = 1.0
        
        # Age adjustment
        today = date.today()
        age = today.year - person.birth_date.year - ((today.month, today.day) < (person.birth_date.month, person.birth_date.day))
        
        if age < 30:
            risk *= 0.7
        elif age > 50:
            risk *= 1.5
            
        # Health conditions
        if health_details.has_chronic_condition:
            risk *= 1.8
            
        # Smoker status
        if health_details.smoker:
            risk *= 1.5
            
        # Family members
        if health_details.family_members > 2:
            risk *= 1.2
            
        return max(0.5, min(3.0, risk))  # Cap risk between 0.5 and 3.0

    def _calculate_discounts(self, insurance_type: InsuranceType, person: Person) -> List[float]:
        discounts = []
        
        # Loyalty discount (simulated)
        discounts.append(random.uniform(0, 50))
        
        # Multi-policy discount
        if insurance_type != InsuranceType.HEALTH:
            discounts.append(20.0)
            
        # No claims discount (simulated)
        if insurance_type == InsuranceType.AUTO:
            discounts.append(random.uniform(0, 100))
            
        return discounts

    def _get_coverage_details(self, insurance_type: InsuranceType) -> Dict:
        if insurance_type == InsuranceType.HABITATION:
            return {
                "coverage": ["Fire", "Theft", "Water damage", "Natural disasters"],
                "liability": "Included",
                "deductible": "500€"
            }
        elif insurance_type == InsuranceType.AUTO:
            return {
                "coverage": ["Collision", "Theft", "Third-party liability", "Roadside assistance"],
                "liability": "Unlimited",
                "deductible": "300€"
            }
        elif insurance_type == InsuranceType.HEALTH:
            return {
                "coverage": ["Hospitalization", "Consultations", "Medications", "Dental"],
                "reimbursement_rate": "70-100%",
                "annual_cap": "Unlimited"
            }

def main():
    # Example usage
    generator = InsuranceQuoteGenerator()
    
    # Create a sample person
    address = Address(
        street="123 Main St",
        city="Paris",
        postal_code="75001"
    )
    person = Person(
        first_name="Jean",
        last_name="Dupont",
        birth_date=date(1980, 5, 15),
        address=address,
        email="jean.dupont@example.com",
        phone="+33123456789"
    )
    
    # Generate a habitation quote
    property = Property(
        address=address,
        surface_area=80.0,
        rooms=3,
        property_type="apartment",
        construction
