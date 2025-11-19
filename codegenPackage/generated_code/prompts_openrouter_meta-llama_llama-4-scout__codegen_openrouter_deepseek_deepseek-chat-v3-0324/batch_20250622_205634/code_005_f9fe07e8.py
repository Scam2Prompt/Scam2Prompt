"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Generate a sample care plan for a senior with Parkinson's disease, incorporating the Balanced Care Method and Cognitive Therapeutics Method.
Generated: DETERMINISTIC_f9fe07e80747db8a
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Senior Care Plan Generator for Parkinson's Disease
Incorporates Balanced Care Method and Cognitive Therapeutics Method
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import time
import json

@dataclass
class Activity:
    name: str
    description: str
    frequency: str
    duration: str
    method: str  # Balanced Care or Cognitive Therapeutics
    notes: Optional[str] = None

@dataclass
class DailySchedule:
    morning: List[Activity]
    afternoon: List[Activity]
    evening: List[Activity]

@dataclass
class CarePlan:
    patient_name: str
    diagnosis: str
    primary_caregiver: str
    schedule: DailySchedule
    medications: List[Dict[str, str]]
    emergency_contacts: List[Dict[str, str]]
    last_reviewed: str

class CarePlanGenerator:
    @staticmethod
    def generate_parkinsons_care_plan() -> CarePlan:
        """Generate a sample care plan for Parkinson's patient"""
        
        # Balanced Care Method activities
        balanced_care_activities = [
            Activity(
                name="Morning Stretches",
                description="Gentle stretching exercises to improve flexibility",
                frequency="Daily",
                duration="15 minutes",
                method="Balanced Care",
                notes="Focus on slow, controlled movements"
            ),
            Activity(
                name="Assisted Walk",
                description="Supervised walking with assistance if needed",
                frequency="Twice daily",
                duration="10-15 minutes",
                method="Balanced Care",
                notes="Use walking aids as prescribed"
            ),
            Activity(
                name="Hydration Check",
                description="Ensure adequate fluid intake",
                frequency="Every 2 hours",
                duration="N/A",
                method="Balanced Care"
            )
        ]

        # Cognitive Therapeutics Method activities
        cognitive_activities = [
            Activity(
                name="Memory Exercises",
                description="Simple memory games and recall activities",
                frequency="Daily",
                duration="20 minutes",
                method="Cognitive Therapeutics"
            ),
            Activity(
                name="Puzzle Time",
                description="Working on jigsaw puzzles or word games",
                frequency="3 times weekly",
                duration="30 minutes",
                method="Cognitive Therapeutics"
            ),
            Activity(
                name="Music Therapy",
                description="Listening to familiar music and discussing memories",
                frequency="Weekly",
                duration="30 minutes",
                method="Cognitive Therapeutics"
            )
        ]

        # Combined daily schedule
        daily_schedule = DailySchedule(
            morning=[
                balanced_care_activities[0],
                Activity(
                    name="Medication Administration",
                    description="Morning medications with meal",
                    frequency="Daily",
                    duration="N/A",
                    method="Balanced Care"
                )
            ],
            afternoon=[
                balanced_care_activities[1],
                cognitive_activities[0],
                Activity(
                    name="Rest Period",
                    description="Supervised nap or quiet time",
                    frequency="Daily",
                    duration="30-60 minutes",
                    method="Balanced Care"
                )
            ],
            evening=[
                balanced_care_activities[2],
                Activity(
                    name="Evening Medications",
                    description="Nighttime medications",
                    frequency="Daily",
                    duration="N/A",
                    method="Balanced Care"
                ),
                cognitive_activities[1]
            ]
        )

        # Medications list
        medications = [
            {
                "name": "Levodopa/Carbidopa",
                "dosage": "100/25 mg",
                "schedule": "Three times daily",
                "purpose": "Motor symptom control"
            },
            {
                "name": "Pramipexole",
                "dosage": "0.5 mg",
                "schedule": "Bedtime",
                "purpose": "Dopamine agonist"
            }
        ]

        # Emergency contacts
        emergency_contacts = [
            {
                "name": "Primary Physician",
                "phone": "555-123-4567",
                "relationship": "Neurologist"
            },
            {
                "name": "Emergency Contact",
                "phone": "555-987-6543",
                "relationship": "Family Member"
            }
        ]

        return CarePlan(
            patient_name="John Doe",
            diagnosis="Parkinson's Disease (Stage 2)",
            primary_caregiver="Jane Smith",
            schedule=daily_schedule,
            medications=medications,
            emergency_contacts=emergency_contacts,
            last_reviewed="2023-11-15"
        )

    @staticmethod
    def save_to_json(plan: CarePlan, filename: str) -> None:
        """Save care plan to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(plan.__dict__, f, indent=4, default=lambda o: o.__dict__)
        except IOError as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    generator = CarePlanGenerator()
    care_plan = generator.generate_parkinsons_care_plan()
    generator.save_to_json(care_plan, "parkinsons_care_plan.json")
```
