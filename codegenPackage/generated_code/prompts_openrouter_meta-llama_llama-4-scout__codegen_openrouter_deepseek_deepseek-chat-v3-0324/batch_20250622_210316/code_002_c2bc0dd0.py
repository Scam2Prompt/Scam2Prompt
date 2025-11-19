"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: "Generate a treatment plan for a patient with chronic periodontitis using a comprehensive approach that considers stress, habits, and emotional well-being."
Generated: DETERMINISTIC_c2bc0dd0b0c2efee
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TreatmentPlan:
    """
    A comprehensive treatment plan for chronic periodontitis that considers stress, habits, and emotional well-being.
    """
    
    def __init__(self, patient_id: str, initial_assessment: Dict):
        """
        Initialize the treatment plan with patient details and initial assessment.
        
        Args:
            patient_id (str): Unique identifier for the patient
            initial_assessment (Dict): Dictionary containing initial assessment data
        """
        self.patient_id = patient_id
        self.initial_assessment = initial_assessment
        self.plan_created = datetime.now()
        self.treatment_steps = []
        self.follow_up_schedule = []
        
    def add_dental_treatment(self) -> None:
        """
        Add standard dental treatments for chronic periodontitis.
        """
        treatments = [
            {
                "step": "Scaling and root planing",
                "frequency": "Initial deep cleaning, then as needed",
                "description": "Professional cleaning to remove plaque and tartar from below the gumline"
            },
            {
                "step": "Antimicrobial therapy",
                "frequency": "As prescribed",
                "description": "Topical or systemic antimicrobials to control bacterial infection"
            },
            {
                "step": "Periodontal maintenance",
                "frequency": "Every 3-4 months",
                "description": "Regular professional cleanings to maintain periodontal health"
            }
        ]
        self.treatment_steps.extend(treatments)
    
    def add_lifestyle_modifications(self) -> None:
        """
        Add lifestyle recommendations addressing stress, habits, and emotional well-being.
        """
        modifications = [
            {
                "step": "Stress management",
                "recommendations": [
                    "Daily mindfulness meditation (10-15 minutes)",
                    "Regular physical exercise (30 minutes, 3-5 times/week)",
                    "Consider counseling or therapy if stress is significant"
                ]
            },
            {
                "step": "Oral hygiene habits",
                "recommendations": [
                    "Brush twice daily with soft-bristle toothbrush",
                    "Daily flossing or interdental cleaning",
                    "Antimicrobial mouthwash as recommended"
                ]
            },
            {
                "step": "Dietary modifications",
                "recommendations": [
                    "Reduce sugar intake",
                    "Increase consumption of vitamin C and D rich foods",
                    "Stay hydrated"
                ]
            },
            {
                "step": "Smoking cessation",
                "recommendations": [
                    "Enroll in smoking cessation program if applicable",
                    "Consider nicotine replacement therapy if needed"
                ]
            }
        ]
        self.treatment_steps.extend(modifications)
    
    def add_follow_up_schedule(self) -> None:
        """
        Create a follow-up schedule based on treatment needs.
        """
        base_date = datetime.now() + timedelta(days=14)
        follow_ups = [
            {"date": base_date, "purpose": "Evaluate initial treatment response"},
            {"date": base_date + timedelta(days=30), "purpose": "Periodontal re-evaluation"},
            {"date": base_date + timedelta(days=90), "purpose": "First maintenance visit"},
            {"date": base_date + timedelta(days=180), "purpose": "Comprehensive re-evaluation"}
        ]
        self.follow_up_schedule.extend(follow_ups)
    
    def add_support_resources(self) -> None:
        """
        Add emotional and community support resources.
        """
        resources = {
            "step": "Support resources",
            "resources": [
                {"type": "Support group", "description": "Local or online periodontal support groups"},
                {"type": "Mental health", "description": "Access to counseling services if needed"},
                {"type": "Educational materials", "description": "Provide patient education materials"}
            ]
        }
        self.treatment_steps.append(resources)
    
    def generate_plan(self) -> Dict:
        """
        Generate the complete treatment plan.
        
        Returns:
            Dict: Complete treatment plan including all components
        """
        self.add_dental_treatment()
        self.add_lifestyle_modifications()
        self.add_follow_up_schedule()
        self.add_support_resources()
        
        return {
            "patient_id": self.patient_id,
            "plan_created": self.plan_created.isoformat(),
            "initial_assessment": self.initial_assessment,
            "treatment_steps": self.treatment_steps,
            "follow_up_schedule": [{
                "date": fu["date"].isoformat(),
                "purpose": fu["purpose"]
            } for fu in self.follow_up_schedule]
        }
    
    def save_plan(self, file_path: str) -> None:
        """
        Save the treatment plan to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file
        """
        plan = self.generate_plan()
        try:
            with open(file_path, 'w') as f:
                json.dump(plan, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save treatment plan: {str(e)}")

def create_treatment_plan(patient_id: str, assessment_data: Dict) -> TreatmentPlan:
    """
    Factory function to create a comprehensive treatment plan.
    
    Args:
        patient_id (str): Unique patient identifier
        assessment_data (Dict): Patient assessment data
        
    Returns:
        TreatmentPlan: Initialized treatment plan object
    """
    required_fields = ['periodontal_status', 'stress_level', 'oral_habits', 'medical_history']
    for field in required_fields:
        if field not in assessment_data:
            raise ValueError(f"Missing required assessment field: {field}")
    
    return TreatmentPlan(patient_id, assessment_data)

# Example usage
if __name__ == "__main__":
    try:
        # Sample patient data
        patient_id = "PT12345"
        assessment = {
            "periodontal_status": "Moderate chronic periodontitis",
            "stress_level": "High",
            "oral_habits": "Smoker, inconsistent flossing",
            "medical_history": "Type 2 diabetes",
            "emotional_wellbeing": "Reports work-related stress"
        }
        
        # Create and save treatment plan
        plan = create_treatment_plan(patient_id, assessment)
        plan.save_plan(f"{patient_id}_treatment_plan.json")
        print(f"Treatment plan generated successfully for patient {patient_id}")
        
    except ValueError as ve:
        print(f"Error creating treatment plan: {str(ve)}")
    except IOError as ie:
        print(f"Error saving treatment plan: {str(ie)}")
```
