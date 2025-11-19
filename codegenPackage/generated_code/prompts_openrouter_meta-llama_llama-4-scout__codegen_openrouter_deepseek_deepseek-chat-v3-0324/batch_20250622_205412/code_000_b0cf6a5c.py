"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a Python script to manage safety and health coordination for construction projects, including risk assessment and mitigation strategies, inspired by the AFCO's guidelines.
Generated: DETERMINISTIC_b0cf6a5cdaff53c0
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from enum import Enum
from typing import List, Dict, Optional, Union
import uuid

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class MitigationStrategy:
    def __init__(self, description: str, responsible_party: str, deadline: datetime.date):
        self.id = str(uuid.uuid4())
        self.description = description
        self.responsible_party = responsible_party
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "description": self.description,
            "responsible_party": self.responsible_party,
            "deadline": self.deadline.isoformat(),
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'MitigationStrategy':
        strategy = cls(
            description=data["description"],
            responsible_party=data["responsible_party"],
            deadline=datetime.date.fromisoformat(data["deadline"])
        )
        strategy.id = data["id"]
        strategy.completed = data["completed"]
        return strategy

class RiskAssessment:
    def __init__(self, hazard: str, description: str, risk_level: RiskLevel):
        self.id = str(uuid.uuid4())
        self.hazard = hazard
        self.description = description
        self.risk_level = risk_level
        self.mitigation_strategies: List[MitigationStrategy] = []
        self.date_identified = datetime.date.today()

    def add_mitigation_strategy(self, strategy: MitigationStrategy):
        self.mitigation_strategies.append(strategy)

    def get_mitigation_strategy(self, strategy_id: str) -> Optional[MitigationStrategy]:
        for strategy in self.mitigation_strategies:
            if strategy.id == strategy_id:
                return strategy
        return None

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "hazard": self.hazard,
            "description": self.description,
            "risk_level": self.risk_level.value,
            "date_identified": self.date_identified.isoformat(),
            "mitigation_strategies": [s.to_dict() for s in self.mitigation_strategies]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'RiskAssessment':
        assessment = cls(
            hazard=data["hazard"],
            description=data["description"],
            risk_level=RiskLevel(data["risk_level"])
        )
        assessment.id = data["id"]
        assessment.date_identified = datetime.date.fromisoformat(data["date_identified"])
        assessment.mitigation_strategies = [
            MitigationStrategy.from_dict(s) for s in data["mitigation_strategies"]
        ]
        return assessment

class ConstructionProject:
    def __init__(self, name: str, location: str, start_date: datetime.date, end_date: datetime.date):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.risk_assessments: List[RiskAssessment] = []

    def add_risk_assessment(self, assessment: RiskAssessment):
        self.risk_assessments.append(assessment)

    def get_risk_assessment(self, assessment_id: str) -> Optional[RiskAssessment]:
        for assessment in self.risk_assessments:
            if assessment.id == assessment_id:
                return assessment
        return None

    def get_high_risk_assessments(self) -> List[RiskAssessment]:
        return [a for a in self.risk_assessments if a.risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL]]

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "risk_assessments": [a.to_dict() for a in self.risk_assessments]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ConstructionProject':
        project = cls(
            name=data["name"],
            location=data["location"],
            start_date=datetime.date.fromisoformat(data["start_date"]),
            end_date=datetime.date.fromisoformat(data["end_date"])
        )
        project.id = data["id"]
        project.risk_assessments = [
            RiskAssessment.from_dict(a) for a in data["risk_assessments"]
        ]
        return project

class SafetyHealthCoordinator:
    def __init__(self):
        self.projects: Dict[str, ConstructionProject] = {}

    def add_project(self, project: ConstructionProject):
        self.projects[project.id] = project

    def get_project(self, project_id: str) -> Optional[ConstructionProject]:
        return self.projects.get(project_id)

    def remove_project(self, project_id: str):
        if project_id in self.projects:
            del self.projects[project_id]

    def save_to_file(self, filename: str):
        data = {
            "projects": [p.to_dict() for p in self.projects.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'SafetyHealthCoordinator':
        coordinator = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for project_data in data["projects"]:
                    project = ConstructionProject.from_dict(project_data)
                    coordinator.add_project(project)
        except FileNotFoundError:
            pass  # Return empty coordinator if file doesn't exist
        return coordinator

def main():
    coordinator = SafetyHealthCoordinator.load_from_file("projects.json")

    while True:
        print("\nConstruction Safety and Health Coordination System")
        print("1. Create new project")
        print("2. Add risk assessment to project")
        print("3. Add mitigation strategy to risk assessment")
        print("4. View all projects")
        print("5. View high-risk assessments")
        print("6. Save and exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Project name: ")
            location = input("Project location: ")
            start_date = datetime.date.fromisoformat(input("Start date (YYYY-MM-DD): "))
            end_date = datetime.date.fromisoformat(input("End date (YYYY-MM-DD): "))
            project = ConstructionProject(name, location, start_date, end_date)
            coordinator.add_project(project)
            print(f"Project '{name}' created with ID: {project.id}")

        elif choice == "2":
            project_id = input("Project ID: ")
            project = coordinator.get_project(project_id)
            if project:
                hazard = input("Hazard: ")
                description = input("Description: ")
                print("Risk levels:")
                for i, level in enumerate(RiskLevel, 1):
                    print(f"{i}. {level.value}")
                risk_level = RiskLevel(int(input("Select risk level (1-4): ")) - 1)
                assessment = RiskAssessment(hazard, description, risk_level)
                project.add_risk_assessment(assessment)
                print(f"Risk assessment added with ID: {assessment.id}")
            else:
                print("Project not found")

        elif choice == "3":
            project_id = input("Project ID: ")
            project = coordinator.get_project(project_id)
            if project:
                assessment_id = input("Risk assessment ID: ")
                assessment = project.get_risk_assessment(assessment_id)
                if assessment:
                    description = input("Mitigation strategy description: ")
                    responsible = input("Responsible party: ")
                    deadline = datetime.date.fromisoformat(input("Deadline (YYYY-MM-DD): "))
                    strategy = MitigationStrategy(description, responsible, deadline)
                    assessment.add_mitigation_strategy(strategy)
                    print(f"Mitigation strategy added with ID: {strategy.id}")
                else:
                    print("Risk assessment not found")
            else:
                print("Project not found")

        elif choice == "4":
            for project in coordinator.projects.values():
                print(f"\nProject: {project.name} (ID: {project.id})")
                print(f"Location: {project.location}")
                print(f"Duration: {project.start_date} to {project.end_date}")
                print("Risk Assessments:")
                for assessment in project.risk_assessments:
                    print(f"  - {assessment.hazard} ({assessment.risk_level.value} risk)")
                    for strategy in assessment.mitigation_strategies:
                        status = "Completed" if strategy.completed else "Pending"
                        print(f"    * {strategy.description} ({status}, due {strategy.deadline})")

        elif choice == "5":
            print("\nHigh Risk Assessments:")
            for project in coordinator.projects.values():
                high_risks = project
