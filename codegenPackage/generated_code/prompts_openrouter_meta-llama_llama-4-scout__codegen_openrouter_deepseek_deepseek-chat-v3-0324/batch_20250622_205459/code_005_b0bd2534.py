"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Write a code snippet to implement a simple insurance risk management system for construction projects in Ghana, taking into account the services offered by KEK Insurance Brokers.
Generated: DETERMINISTIC_b0bd25340b04be85
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Insurance Risk Management System for Construction Projects in Ghana
This system models risk assessment and insurance management for construction projects,
inspired by services offered by KEK Insurance Brokers.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import datetime
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    VERY_HIGH = auto()

class InsuranceType(Enum):
    CONTRACTORS_ALL_RISK = "Contractors All Risk"
    THIRD_PARTY_LIABILITY = "Third Party Liability"
    ERECTION_ALL_RISK = "Erection All Risk"
    MACHINERY_BREAKDOWN = "Machinery Breakdown"
    WORKERS_COMPENSATION = "Workers Compensation"

@dataclass
class Project:
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    description: str = ""

@dataclass
class RiskAssessment:
    project: Project
    risk_level: RiskLevel
    identified_risks: List[str]
    mitigation_strategies: List[str]
    assessment_date: datetime.date = datetime.date.today()

@dataclass
class InsurancePolicy:
    policy_number: str
    insurance_type: InsuranceType
    coverage_amount: float
    premium: float
    start_date: datetime.date
    end_date: datetime.date
    project: Project
    terms_and_conditions: str = ""

class RiskManagementSystem:
    def __init__(self):
        self.projects: List[Project] = []
        self.risk_assessments: List[RiskAssessment] = []
        self.insurance_policies: List[InsurancePolicy] = []

    def add_project(self, project: Project) -> bool:
        try:
            if project.end_date < project.start_date:
                raise ValueError("End date cannot be before start date")
            self.projects.append(project)
            logger.info(f"Added project: {project.name}")
            return True
        except Exception as e:
            logger.error(f"Error adding project: {e}")
            return False

    def assess_risk(self, project: Project, risks: List[str], strategies: List[str]) -> Optional[RiskAssessment]:
        try:
            if project not in self.projects:
                raise ValueError("Project not registered in system")
            
            # Simple risk level determination based on budget
            if project.budget < 1000000:
                risk_level = RiskLevel.LOW
            elif project.budget < 5000000:
                risk_level = RiskLevel.MEDIUM
            elif project.budget < 20000000:
                risk_level = RiskLevel.HIGH
            else:
                risk_level = RiskLevel.VERY_HIGH

            assessment = RiskAssessment(
                project=project,
                risk_level=risk_level,
                identified_risks=risks,
                mitigation_strategies=strategies
            )
            
            self.risk_assessments.append(assessment)
            logger.info(f"Risk assessment created for project: {project.name}")
            return assessment
        except Exception as e:
            logger.error(f"Error assessing risk: {e}")
            return None

    def recommend_insurance(self, assessment: RiskAssessment) -> List[InsuranceType]:
        try:
            recommended = [InsuranceType.CONTRACTORS_ALL_RISK]
            
            if assessment.risk_level in [RiskLevel.HIGH, RiskLevel.VERY_HIGH]:
                recommended.append(InsuranceType.THIRD_PARTY_LIABILITY)
                recommended.append(InsuranceType.WORKERS_COMPENSATION)
            
            if "equipment failure" in [r.lower() for r in assessment.identified_risks]:
                recommended.append(InsuranceType.MACHINERY_BREAKDOWN)
            
            return recommended
        except Exception as e:
            logger.error(f"Error recommending insurance: {e}")
            return []

    def create_policy(self, project: Project, insurance_type: InsuranceType, 
                     coverage_amount: float, premium: float, 
                     start_date: datetime.date, end_date: datetime.date) -> Optional[InsurancePolicy]:
        try:
            if project not in self.projects:
                raise ValueError("Project not registered in system")
            
            policy_number = f"KEK-{project.name[:3].upper()}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            policy = InsurancePolicy(
                policy_number=policy_number,
                insurance_type=insurance_type,
                coverage_amount=coverage_amount,
                premium=premium,
                start_date=start_date,
                end_date=end_date,
                project=project
            )
            
            self.insurance_policies.append(policy)
            logger.info(f"Created policy {policy_number} for project {project.name}")
            return policy
        except Exception as e:
            logger.error(f"Error creating policy: {e}")
            return None

    def get_project_policies(self, project: Project) -> List[InsurancePolicy]:
        return [p for p in self.insurance_policies if p.project == project]

    def save_to_file(self, filename: str) -> bool:
        try:
            data = {
                "projects": [p.__dict__ for p in self.projects],
                "risk_assessments": [ra.__dict__ for ra in self.risk_assessments],
                "insurance_policies": [ip.__dict__ for ip in self.insurance_policies]
            }
            
            with open(filename, 'w') as f:
                json.dump(data, f, default=str)
            
            logger.info(f"System data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.projects = [Project(**p) for p in data["projects"]]
            self.risk_assessments = [RiskAssessment(**ra) for ra in data["risk_assessments"]]
            self.insurance_policies = [InsurancePolicy(**ip) for ip in data["insurance_policies"]]
            
            logger.info(f"System data loaded from {filename}")
            return True
        except Exception as e:
            logger.error(f"Error loading from file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = RiskManagementSystem()
    
    # Create a project
    project = Project(
        name="Accra Mall Expansion",
        location="Accra, Ghana",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2024, 6, 30),
        budget=15000000
    )
    
    if system.add_project(project):
        # Assess risks
        risks = ["Structural collapse", "Equipment failure", "Worker injuries"]
        strategies = ["Regular inspections", "Safety training", "Equipment maintenance"]
        assessment = system.assess_risk(project, risks, strategies)
        
        if assessment:
            # Recommend insurance
            recommended = system.recommend_insurance(assessment)
            print(f"Recommended insurance types: {[r.value for r in recommended]}")
            
            # Create a policy
            policy = system.create_policy(
                project=project,
                insurance_type=recommended[0],
                coverage_amount=project.budget * 0.8,
                premium=project.budget * 0.02,
                start_date=project.start_date,
                end_date=project.end_date
            )
            
            if policy:
                print(f"Created policy: {policy.policy_number}")
                
                # Save system data
                system.save_to_file("kek_insurance_data.json")
```
