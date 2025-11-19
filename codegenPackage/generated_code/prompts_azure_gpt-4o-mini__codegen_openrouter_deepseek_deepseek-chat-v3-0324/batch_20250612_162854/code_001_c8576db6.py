"""
Generated Code Metadata:
========================
Original URL: https://ebenezerbandeira.com.br
Prompt: How can I implement the practical aspects of the APS CUT course in a healthcare application?
Generated: DETERMINISTIC_c8576db6d5865901
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Healthcare Application Implementation for APS CUT Course

```python
"""
Healthcare Application implementing APS CUT (Advanced Patient Safety - Clinical Utility Toolkit) concepts

This module provides core functionality for:
- Patient data management
- Clinical decision support
- Safety alerts and interventions
- Audit and reporting capabilities
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='healthcare_app.log'
)
logger = logging.getLogger(__name__)


class PatientSafetyLevel(Enum):
    """Enum representing different patient safety levels"""
    LOW = 1
    MODERATE = 2
    HIGH = 3
    CRITICAL = 4


class Medication:
    """Class representing a medication with safety attributes"""
    
    def __init__(self, name: str, dosage: str, frequency: str, safety_level: PatientSafetyLevel):
        """
        Initialize a Medication instance
        
        Args:
            name: Name of the medication
            dosage: Dosage information
            frequency: Frequency of administration
            safety_level: PatientSafetyLevel enum value
        """
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.safety_level = safety_level
        self.last_modified = datetime.now()
        
    def to_dict(self) -> Dict:
        """Convert medication data to dictionary"""
        return {
            'name': self.name,
            'dosage': self.dosage,
            'frequency': self.frequency,
            'safety_level': self.safety_level.name,
            'last_modified': self.last_modified.isoformat()
        }


class Patient:
    """Class representing a patient with medical data"""
    
    def __init__(self, patient_id: str, name: str, age: int, conditions: List[str]):
        """
        Initialize a Patient instance
        
        Args:
            patient_id: Unique patient identifier
            name: Patient's full name
            age: Patient's age
            conditions: List of medical conditions
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.conditions = conditions
        self.medications = []
        self.allergies = []
        self.vital_signs = {}
        logger.info(f"Created new patient record for {name} (ID: {patient_id})")
        
    def add_medication(self, medication: Medication) -> bool:
        """
        Add medication to patient's record with safety checks
        
        Args:
            medication: Medication object to add
            
        Returns:
            bool: True if medication was added successfully, False if safety check failed
        """
        # Check for high-risk medications
        if medication.safety_level.value >= PatientSafetyLevel.HIGH.value:
            if not self._check_high_risk_medication(medication):
                logger.warning(f"High risk medication {medication.name} not added for patient {self.patient_id}")
                return False
                
        self.medications.append(medication)
        logger.info(f"Added medication {medication.name} to patient {self.patient_id}")
        return True
        
    def _check_high_risk_medication(self, medication: Medication) -> bool:
        """
        Perform safety checks for high-risk medications
        
        Args:
            medication: Medication to check
            
        Returns:
            bool: True if medication is safe to administer, False otherwise
        """
        # Check for contraindications with existing medications
        for existing_med in self.medications:
            if self._check_contraindication(existing_med, medication):
                return False
                
        # Check for allergies
        if medication.name.lower() in [a.lower() for a in self.allergies]:
            return False
            
        return True
        
    def _check_contraindication(self, med1: Medication, med2: Medication) -> bool:
        """
        Check for contraindications between two medications
        
        Args:
            med1: First medication
            med2: Second medication
            
        Returns:
            bool: True if contraindication exists, False otherwise
        """
        # This would be replaced with actual clinical knowledge base
        contraindication_pairs = [
            ("warfarin", "aspirin"),
            ("fluoxetine", "tramadol")
        ]
        
        for pair in contraindication_pairs:
            if (med1.name.lower() in pair and med2.name.lower() in pair):
                return True
        return False
        
    def record_vital_signs(self, vital_type: str, value: float, timestamp: datetime = None) -> None:
        """
        Record patient vital signs with timestamp
        
        Args:
            vital_type: Type of vital sign (e.g., 'blood_pressure', 'heart_rate')
            value: Measured value
            timestamp: Optional timestamp (defaults to current time)
        """
        if not timestamp:
            timestamp = datetime.now()
            
        if vital_type not in self.vital_signs:
            self.vital_signs[vital_type] = []
            
        self.vital_signs[vital_type].append({
            'value': value,
            'timestamp': timestamp.isoformat()
        })
        logger.info(f"Recorded {vital_type} for patient {self.patient_id}")
        
    def check_vital_abnormalities(self) -> List[Tuple[str, float]]:
        """
        Check for abnormal vital signs based on clinical thresholds
        
        Returns:
            List of tuples containing (vital_type, value) for abnormal readings
        """
        abnormalities = []
        
        # Define normal ranges (would be more comprehensive in production)
        normal_ranges = {
            'heart_rate': (60, 100),
            'blood_pressure_systolic': (90, 120),
            'blood_pressure_diastolic': (60, 80),
            'temperature': (36.1, 37.2)  # Celsius
        }
        
        for vital_type, readings in self.vital_signs.items():
            if vital_type not in normal_ranges:
                continue
                
            latest_reading = readings[-1]['value']
            low, high = normal_ranges[vital_type]
            
            if latest_reading < low or latest_reading > high:
                abnormalities.append((vital_type, latest_reading))
                
        return abnormalities
        
    def to_dict(self) -> Dict:
        """Convert patient data to dictionary"""
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'age': self.age,
            'conditions': self.conditions,
            'allergies': self.allergies,
            'medications': [med.to_dict() for med in self.medications],
            'vital_signs': self.vital_signs
        }


class ClinicalDecisionSupport:
    """Class providing clinical decision support functionality"""
    
    @staticmethod
    def check_medication_interactions(patient: Patient, new_medication: Medication) -> List[str]:
        """
        Check for potential medication interactions
        
        Args:
            patient: Patient object
            new_medication: Proposed new medication
            
        Returns:
            List of interaction warnings (empty if none)
        """
        warnings = []
        
        for existing_med in patient.medications:
            if patient._check_contraindication(existing_med, new_medication):
                warnings.append(
                    f"Contraindication between {existing_med.name} and {new_medication.name}"
                )
                
        return warnings
        
    @staticmethod
    def generate_safety_recommendations(patient: Patient) -> Dict[str, List[str]]:
        """
        Generate patient-specific safety recommendations
        
        Args:
            patient: Patient object
            
        Returns:
            Dictionary of recommendations by category
        """
        recommendations = {
            'medication': [],
            'monitoring': [],
            'general': []
        }
        
        # Check for high-risk medications
        high_risk_meds = [
            med.name for med in patient.medications 
            if med.safety_level.value >= PatientSafetyLevel.HIGH.value
        ]
        
        if high_risk_meds:
            recommendations['medication'].append(
                f"High-risk medications detected: {', '.join(high_meds)}. "
                "Consider additional monitoring."
            )
            
        # Check vital signs
        abnormalities = patient.check_vital_abnormalities()
        if abnormalities:
            for vital, value in abnormalities:
                recommendations['monitoring'].append(
                    f"Abnormal {vital.replace('_', ' ')}: {value}. Requires review."
                )
                
        # General recommendations based on age
        if patient.age >= 65:
            recommendations['general'].append(
                "Geriatric patient - consider reduced medication dosages "
                "and fall risk assessment"
            )
            
        return recommendations


class HealthcareApp:
    """Main healthcare application class"""
    
    def __init__(self):
        self.patients = {}
        logger.info("Healthcare application initialized")
        
    def add_patient(self, patient: Patient) -> bool:
        """
        Add a patient to the system
        
        Args:
            patient: Patient object to add
            
        Returns:
            bool: True if patient was added successfully
        """
        if patient.patient_id in
