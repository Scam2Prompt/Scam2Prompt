"""
Generated Code Metadata:
========================
Original URL: https://academiamedicinaestetica.cl
Prompt: Generate a Python script that demonstrates the techniques taught in the advanced Botox and dermal fillers course offered by Academia Medicina Estética.
Generated: DETERMINISTIC_7f1995234dc536f3
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Advanced Botox and Dermal Fillers Treatment Planning Tool

This script demonstrates techniques from the advanced Botox and dermal fillers course,
providing treatment planning assistance for medical professionals.

Features:
- Facial anatomy mapping
- Dosage calculation
- Injection site recommendations
- Safety checks
- Treatment simulation
"""

import math
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


class TreatmentArea(Enum):
    """Enumeration of facial treatment areas"""
    FOREHEAD = "Forehead"
    GLABELLA = "Glabella"
    CROWNS_FEET = "Crow's Feet"
    BUNNY_LINES = "Bunny Lines"
    LIP_FLIP = "Lip Flip"
    MARIONETTE = "Marionette Lines"
    NASOLABIAL = "Nasolabial Folds"
    JAWLINE = "Jawline Contouring"
    CHIN = "Chin Augmentation"
    CHEEKS = "Cheek Augmentation"
    TEMPLES = "Temple Hollowing"
    NECK_BANDS = "Neck Bands"


class ProductType(Enum):
    """Enumeration of product types"""
    BOTOX = "Botulinum Toxin Type A"
    HYALURONIC_ACID = "Hyaluronic Acid Filler"
    CALCIUM_HYDROXYLAPATITE = "Calcium Hydroxylapatite"
    POLY_L_LACTIC_ACID = "Poly-L-lactic Acid"


@dataclass
class Patient:
    """Patient data structure"""
    name: str
    age: int
    gender: str
    weight: float  # in kg
    medical_history: List[str]
    previous_treatments: Dict[TreatmentArea, str]
    allergies: List[str]


@dataclass
class TreatmentPlan:
    """Treatment plan data structure"""
    patient: Patient
    areas: List[TreatmentArea]
    products: Dict[TreatmentArea, Tuple[ProductType, float]]
    injection_sites: Dict[TreatmentArea, List[Tuple[float, float]]]
    notes: str


class TreatmentPlanner:
    """Main class for treatment planning"""
    
    # Standard dosage guidelines (units)
    STANDARD_DOSAGES = {
        TreatmentArea.FOREHEAD: (10, 20),
        TreatmentArea.GLABELLA: (15, 25),
        TreatmentArea.CROWNS_FEET: (10, 15),
        TreatmentArea.BUNNY_LINES: (5, 10),
        TreatmentArea.LIP_FLIP: (2, 4),
        TreatmentArea.MARIONETTE: (2, 5),
        TreatmentArea.NASOLABIAL: (0.5, 1.0),  # ml for fillers
        TreatmentArea.JAWLINE: (1.0, 2.0),
        TreatmentArea.CHIN: (0.5, 1.5),
        TreatmentArea.CHEEKS: (1.0, 3.0),
        TreatmentArea.TEMPLES: (0.5, 1.5),
        TreatmentArea.NECK_BANDS: (20, 30)
    }
    
    # Standard injection coordinates (relative to facial landmarks)
    INJECTION_SITES = {
        TreatmentArea.FOREHEAD: [(0.3, 0.7), (0.5, 0.7), (0.7, 0.7)],
        TreatmentArea.GLABELLA: [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)],
        TreatmentArea.CROWNS_FEET: [(0.2, 0.3), (0.8, 0.3)],
        TreatmentArea.BUNNY_LINES: [(0.5, 0.4)],
        TreatmentArea.LIP_FLIP: [(0.5, 0.2)],
        TreatmentArea.MARIONETTE: [(0.4, 0.1), (0.6, 0.1)],
        TreatmentArea.NASOLABIAL: [(0.3, 0.3), (0.7, 0.3)],
        TreatmentArea.JAWLINE: [(0.2, 0.0), (0.4, 0.0), (0.6, 0.0), (0.8, 0.0)],
        TreatmentArea.CHIN: [(0.5, 0.0)],
        TreatmentArea.CHEEKS: [(0.3, 0.4), (0.7, 0.4)],
        TreatmentArea.TEMPLES: [(0.2, 0.6), (0.8, 0.6)],
        TreatmentArea.NECK_BANDS: [(0.3, -0.1), (0.5, -0.1), (0.7, -0.1)]
    }
    
    def __init__(self, patient: Patient):
        self.patient = patient
        self.plan = TreatmentPlan(
            patient=patient,
            areas=[],
            products={},
            injection_sites={},
            notes=""
        )
    
    def check_contraindications(self) -> List[str]:
        """Check for any contraindications based on patient data"""
        contraindications = []
        
        if "pregnancy" in self.patient.medical_history:
            contraindications.append("Pregnancy is a contraindication for Botox and fillers")
        
        if "neuromuscular disorder" in self.patient.medical_history:
            contraindications.append("Neuromuscular disorders may contraindicate Botox")
            
        if "bleeding disorder" in self.patient.medical_history:
            contraindications.append("Bleeding disorders may require special precautions")
            
        for allergy in self.patient.allergies:
            if "botulinum" in allergy.lower():
                contraindications.append(f"Allergy to botulinum toxin: {allergy}")
            if "hyaluronic" in allergy.lower():
                contraindications.append(f"Allergy to hyaluronic acid: {allergy}")
                
        return contraindications
    
    def calculate_dosage(self, area: TreatmentArea, product: ProductType) -> float:
        """Calculate appropriate dosage for a treatment area"""
        min_dose, max_dose = self.STANDARD_DOSAGES[area]
        
        # Adjust for patient factors
        if product == ProductType.BOTOX:
            # Higher doses may be needed for men due to stronger muscles
            if self.patient.gender.lower() == "male":
                min_dose *= 1.2
                max_dose *= 1.2
                
            # Consider previous treatments
            if area in self.patient.previous_treatments:
                if "resistant" in self.patient.previous_treatments[area].lower():
                    min_dose *= 1.3
                    max_dose *= 1.3
        
        # Return midpoint of adjusted range
        return (min_dose + max_dose) / 2
    
    def recommend_product(self, area: TreatmentArea) -> ProductType:
        """Recommend appropriate product for treatment area"""
        if area in [
            TreatmentArea.FOREHEAD, 
            TreatmentArea.GLABELLA, 
            TreatmentArea.CROWNS_FEET,
            TreatmentArea.BUNNY_LINES,
            TreatmentArea.LIP_FLIP,
            TreatmentArea.NECK_BANDS
        ]:
            return ProductType.BOTOX
        else:
            return ProductType.HYALURONIC_ACID
    
    def add_treatment_area(self, area: TreatmentArea) -> None:
        """Add a treatment area to the plan with recommended product and dosage"""
        if area not in self.plan.areas:
            self.plan.areas.append(area)
            product = self.recommend_product(area)
            dosage = self.calculate_dosage(area, product)
            self.plan.products[area] = (product, dosage)
            self.plan.injection_sites[area] = self.INJECTION_SITES[area]
    
    def generate_plan(self, areas: List[TreatmentArea]) -> TreatmentPlan:
        """Generate complete treatment plan for requested areas"""
        contraindications = self.check_contraindications()
        if contraindications:
            self.plan.notes = "CONTRAINDICATIONS:\n" + "\n".join(contraindications)
            return self.plan
        
        for area in areas:
            self.add_treatment_area(area)
        
        self.plan.notes = self._generate_notes()
        return self.plan
    
    def _generate_notes(self) -> str:
        """Generate clinical notes for the treatment plan"""
        notes = []
        notes.append(f"Treatment Plan for {self.patient.name} (Age: {self.patient.age}, Gender: {self.patient.gender})")
        notes.append("\nAreas to be treated:")
        
        for area in self.plan.areas:
            product, dosage = self.plan.products[area]
            notes.append(f"- {area.value}: {dosage:.1f} {'units' if product == ProductType.BOTOX else 'ml'} of {product.value}")
