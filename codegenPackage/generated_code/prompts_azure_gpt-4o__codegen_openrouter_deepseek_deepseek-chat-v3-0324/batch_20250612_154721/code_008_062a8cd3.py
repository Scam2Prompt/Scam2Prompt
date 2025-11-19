"""
Generated Code Metadata:
========================
Original URL: https://w7.com.au
Prompt: Create a program that maps the relationship between Kundalini symptoms and self-healing practices, using transpersonal therapy principles.
Generated: DETERMINISTIC_062a8cd3d2888966
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Kundalini Symptoms and Self-Healing Practices Mapper

This program maps Kundalini awakening symptoms to recommended self-healing practices
based on transpersonal therapy principles. It provides a structured way to explore
and address various symptoms through appropriate therapeutic practices.

Features:
- Database of Kundalini symptoms and corresponding practices
- Search functionality by symptom or practice
- Personalized recommendations
- Symptom tracking over time
"""

import json
from typing import Dict, List, Optional
from enum import Enum
import datetime
from dataclasses import dataclass, asdict
import os

class SymptomSeverity(Enum):
    """Enum for symptom severity levels"""
    MILD = 1
    MODERATE = 2
    SEVERE = 3

@dataclass
class HealingPractice:
    """Data class representing a healing practice"""
    name: str
    description: str
    duration_minutes: int
    frequency: str  # e.g., "daily", "weekly", "as needed"
    contraindications: List[str]

@dataclass
class KundaliniSymptom:
    """Data class representing a Kundalini symptom"""
    name: str
    description: str
    common_triggers: List[str]
    related_practices: List[str]  # Names of related practices

@dataclass
class UserSymptomRecord:
    """Data class for tracking user symptoms"""
    symptom_name: str
    severity: SymptomSeverity
    date_recorded: datetime.date
    notes: str = ""

class KundaliniHealingMapper:
    """Main class for mapping symptoms to healing practices"""
    
    def __init__(self, data_file: str = "kundalini_data.json"):
        """
        Initialize the mapper with data from JSON file
        
        Args:
            data_file: Path to JSON file containing symptom and practice data
        """
        self.symptoms: Dict[str, KundaliniSymptom] = {}
        self.practices: Dict[str, HealingPractice] = {}
        self.user_records: List[UserSymptomRecord] = []
        self.data_file = data_file
        
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from JSON file or create default data if file doesn't exist"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self._deserialize_data(data)
        else:
            self._create_default_data()
            self._save_data()
    
    def _save_data(self) -> None:
        """Save current data to JSON file"""
        data = {
            'symptoms': [asdict(s) for s in self.symptoms.values()],
            'practices': [asdict(p) for p in self.practices.values()],
            'user_records': [asdict(r) for r in self.user_records]
        }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    def _deserialize_data(self, data: Dict) -> None:
        """Convert JSON data back into objects"""
        self.symptoms = {
            s['name']: KundaliniSymptom(**s) for s in data.get('symptoms', [])
        }
        
        self.practices = {
            p['name']: HealingPractice(**p) for p in data.get('practices', [])
        }
        
        self.user_records = [
            UserSymptomRecord(
                symptom_name=r['symptom_name'],
                severity=SymptomSeverity[r['severity']],
                date_recorded=datetime.datetime.strptime(r['date_recorded'], '%Y-%m-%d').date(),
                notes=r.get('notes', '')
            ) for r in data.get('user_records', [])
        ]
    
    def _create_default_data(self) -> None:
        """Create default dataset if no data file exists"""
        # Default healing practices
        self.practices = {
            "Grounding Meditation": HealingPractice(
                name="Grounding Meditation",
                description="Meditation focusing on connecting with the earth",
                duration_minutes=15,
                frequency="daily",
                contraindications=[]
            ),
            "Breathwork": HealingPractice(
                name="Breathwork",
                description="Conscious control of breathing patterns",
                duration_minutes=10,
                frequency="daily",
                contraindications=["heart conditions", "pregnancy"]
            ),
            "Yoga Nidra": HealingPractice(
                name="Yoga Nidra",
                description="Guided yogic sleep for deep relaxation",
                duration_minutes=30,
                frequency="as needed",
                contraindications=[]
            )
        }
        
        # Default symptoms and their mappings
        self.symptoms = {
            "Energy Surges": KundaliniSymptom(
                name="Energy Surges",
                description="Sudden rushes of energy through the body",
                common_triggers=["meditation", "stress"],
                related_practices=["Grounding Meditation", "Breathwork"]
            ),
            "Spontaneous Movements": KundaliniSymptom(
                name="Spontaneous Movements",
                description="Involuntary body movements or tremors",
                common_triggers=["energy activation"],
                related_practices=["Grounding Meditation", "Yoga Nidra"]
            ),
            "Emotional Releases": KundaliniSymptom(
                name="Emotional Releases",
                description="Sudden emotional outbursts or catharsis",
                common_triggers=["past trauma", "energy movement"],
                related_practices=["Breathwork", "Yoga Nidra"]
            )
        }
    
    def get_practices_for_symptom(self, symptom_name: str) -> List[HealingPractice]:
        """
        Get recommended practices for a given symptom
        
        Args:
            symptom_name: Name of the symptom to look up
            
        Returns:
            List of recommended HealingPractice objects
            
        Raises:
            ValueError: If symptom name is not found
        """
        if symptom_name not in self.symptoms:
            raise ValueError(f"Symptom '{symptom_name}' not found")
            
        symptom = self.symptoms[symptom_name]
        practices = []
        
        for practice_name in symptom.related_practices:
            if practice_name in self.practices:
                practices.append(self.practices[practice_name])
        
        return practices
    
    def search_practices(self, keyword: str) -> List[HealingPractice]:
        """
        Search practices by keyword in name or description
        
        Args:
            keyword: Search term to look for
            
        Returns:
            List of matching HealingPractice objects
        """
        keyword = keyword.lower()
        results = []
        
        for practice in self.practices.values():
            if (keyword in practice.name.lower() or 
                keyword in practice.description.lower()):
                results.append(practice)
        
        return results
    
    def record_symptom(self, symptom_name: str, severity: SymptomSeverity, 
                       notes: str = "") -> None:
        """
        Record a user symptom with severity and optional notes
        
        Args:
            symptom_name: Name of the symptom
            severity: Severity level (SymptomSeverity enum)
            notes: Additional notes about the symptom
            
        Raises:
            ValueError: If symptom name is not found
        """
        if symptom_name not in self.symptoms:
            raise ValueError(f"Symptom '{symptom_name}' not found")
            
        record = UserSymptomRecord(
            symptom_name=symptom_name,
            severity=severity,
            date_recorded=datetime.date.today(),
            notes=notes
        )
        
        self.user_records.append(record)
        self._save_data()
    
    def get_symptom_history(self) -> List[UserSymptomRecord]:
        """Get all recorded user symptoms sorted by date"""
        return sorted(self.user_records, key=lambda x: x.date_recorded, reverse=True)
    
    def get_personalized_recommendations(self) -> Dict[str, List[HealingPractice]]:
        """
        Get personalized recommendations based on recent symptoms
        
        Returns:
            Dictionary mapping symptom names to recommended practices,
            sorted by most recent and severe symptoms first
        """
        if not self.user_records:
            return {}
            
        # Get recent symptoms (last 30 days)
        cutoff_date = datetime.date.today() - datetime.timedelta(days=30)
        recent_records = [
            r for r in self.user_records 
            if r.date_recorded >= cutoff_date
        ]
        
        if not recent_records:
            return {}
        
        # Sort by severity and recency
        recent_records.sort(key=lambda x: (-x.severity.value, x.date_recorded))
        
        recommendations = {}
        seen_symptoms = set()
        
        for record in recent_records:
            if record.symptom_name in seen_symptoms:
                continue
                
            practices = self.get_practices_for_symptom(record.symptom_name)
            if practices:
                recommendations[record.symptom_name] = practices
                seen_symptoms.add(record.symptom_name)
        
        return recommendations

def main():
    """Command-line interface for the Kundalini Healing Mapper"""
