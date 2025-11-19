"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a code snippet that generates a Plan de Prévention for managing Sécurité et Santé au Travail (SST) in construction projects, incorporating the principles of "Construire, Exploiter, Maintenir."
Generated: DETERMINISTIC_3dcfb21f6232b074
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plan de Prévention for Sécurité et Santé au Travail (SST) in construction projects.
Incorporates principles of "Construire, Exploiter, Maintenir".
"""

from datetime import datetime
from enum import Enum
import json
from typing import List, Dict, Optional

class ProjectPhase(Enum):
    """Phases of a construction project."""
    CONSTRUCTION = "Construire"
    OPERATION = "Exploiter"
    MAINTENANCE = "Maintenir"

class RiskLevel(Enum):
    """Risk levels for safety assessment."""
    LOW = "Faible"
    MEDIUM = "Moyen"
    HIGH = "Élevé"

class SafetyMeasure:
    """Represents a safety measure to mitigate risks."""
    def __init__(self, name: str, description: str, responsible: str):
        self.name = name
        self.description = description
        self.responsible = responsible

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "responsible": self.responsible
        }

class RiskAssessment:
    """Represents a risk assessment for a specific task."""
    def __init__(self, task: str, risk_level: RiskLevel, measures: List[SafetyMeasure]):
        self.task = task
        self.risk_level = risk_level
        self.measures = measures

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "task": self.task,
            "risk_level": self.risk_level.value,
            "measures": [measure.to_dict() for measure in self.measures]
        }

class PreventionPlan:
    """Main class representing the prevention plan."""
    def __init__(self, project_name: str, project_manager: str, start_date: datetime, end_date: datetime):
        self.project_name = project_name
        self.project_manager = project_manager
        self.start_date = start_date
        self.end_date = end_date
        self.phase_assessments: Dict[ProjectPhase, List[RiskAssessment]] = {
            phase: [] for phase in ProjectPhase
        }

    def add_risk_assessment(self, phase: ProjectPhase, assessment: RiskAssessment) -> None:
        """Add a risk assessment for a specific project phase."""
        if phase not in self.phase_assessments:
            raise ValueError(f"Invalid project phase: {phase}")
        self.phase_assessments[phase].append(assessment)

    def generate_report(self) -> Dict:
        """Generate a comprehensive report of the prevention plan."""
        report = {
            "project_name": self.project_name,
            "project_manager": self.project_manager,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "phases": {
                phase.value: [assessment.to_dict() for assessment in assessments]
                for phase, assessments in self.phase_assessments.items()
            }
        }
        return report

    def save_to_file(self, filename: str) -> None:
        """Save the prevention plan to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)

    @classmethod
    def load_from_file(cls, filename: str) -> 'PreventionPlan':
        """Load a prevention plan from a JSON file."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d")
        plan = cls(data["project_name"], data["project_manager"], start_date, end_date)
        
        for phase_name, assessments in data["phases"].items():
            phase = ProjectPhase(phase_name)
            for assessment_data in assessments:
                measures = [
                    SafetyMeasure(
                        name=measure["name"],
                        description=measure["description"],
                        responsible=measure["responsible"]
                    ) for measure in assessment_data["measures"]
                ]
                risk_level = RiskLevel(assessment_data["risk_level"])
                assessment = RiskAssessment(
                    task=assessment_data["task"],
                    risk_level=risk_level,
                    measures=measures
                )
                plan.phase_assessments[phase].append(assessment)
        
        return plan

# Example usage
if __name__ == "__main__":
    # Create a new prevention plan
    plan = PreventionPlan(
        project_name="Construction Site X",
        project_manager="Jean Dupont",
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2023, 12, 31)
    )

    # Add risk assessments for different phases
    construction_measures = [
        SafetyMeasure(
            name="EPI obligatoire",
            description="Port du casque, gants et chaussures de sécurité",
            responsible="Chef de chantier"
        ),
        SafetyMeasure(
            name="Formation SST",
            description="Formation à la sécurité pour tous les ouvriers",
            responsible="Responsable RH"
        )
    ]
    construction_assessment = RiskAssessment(
        task="Travaux en hauteur",
        risk_level=RiskLevel.HIGH,
        measures=construction_measures
    )
    plan.add_risk_assessment(ProjectPhase.CONSTRUCTION, construction_assessment)

    # Generate and save the report
    plan.save_to_file("prevention_plan.json")
```
