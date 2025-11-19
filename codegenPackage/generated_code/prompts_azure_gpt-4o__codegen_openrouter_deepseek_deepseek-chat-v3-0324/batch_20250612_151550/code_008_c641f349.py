"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Write a program to automate the analysis and consultation process for industrial construction projects, incorporating the workflow outlined by Tether SARL.
Generated: DETERMINISTIC_c641f3490dad9d9b
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Construction Project Analysis and Consultation Automation
This program automates the workflow for analyzing and consulting on industrial construction projects
as per Tether SARL's specifications.
"""

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('project_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ProjectStatus(Enum):
    """Enum representing different project statuses"""
    DRAFT = auto()
    UNDER_REVIEW = auto()
    APPROVED = auto()
    REJECTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()


class AnalysisPhase(Enum):
    """Enum representing different analysis phases"""
    INITIAL_ASSESSMENT = auto()
    FEASIBILITY_STUDY = auto()
    DESIGN_REVIEW = auto()
    COST_ANALYSIS = auto()
    RISK_ASSESSMENT = auto()
    FINAL_REVIEW = auto()


@dataclass
class ProjectRequirement:
    """Class representing a project requirement"""
    description: str
    priority: int
    is_met: bool = False


@dataclass
class CostEstimate:
    """Class representing cost estimates"""
    material_cost: float
    labor_cost: float
    equipment_cost: float
    contingency: float = 0.1  # Default 10% contingency

    @property
    def total_cost(self) -> float:
        """Calculate total cost including contingency"""
        base_cost = self.material_cost + self.labor_cost + self.equipment_cost
        return base_cost * (1 + self.contingency)


@dataclass
class RiskAssessment:
    """Class representing risk assessment"""
    risk_description: str
    likelihood: float  # 0.0 to 1.0
    impact: float  # 0.0 to 1.0
    mitigation_strategy: str

    @property
    def risk_score(self) -> float:
        """Calculate risk score (likelihood * impact)"""
        return self.likelihood * self.impact


@dataclass
class ProjectDocument:
    """Class representing project documents"""
    name: str
    document_type: str
    content: str
    last_updated: datetime = field(default_factory=datetime.now)


@dataclass
class ConstructionProject:
    """Main class representing an industrial construction project"""
    project_id: str
    name: str
    description: str
    client: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: ProjectStatus = ProjectStatus.DRAFT
    current_phase: AnalysisPhase = AnalysisPhase.INITIAL_ASSESSMENT
    requirements: List[ProjectRequirement] = field(default_factory=list)
    cost_estimate: Optional[CostEstimate] = None
    risks: List[RiskAssessment] = field(default_factory=list)
    documents: List[ProjectDocument] = field(default_factory=list)
    team_members: List[str] = field(default_factory=list)

    def add_requirement(self, requirement: ProjectRequirement) -> None:
        """Add a requirement to the project"""
        self.requirements.append(requirement)

    def add_risk(self, risk: RiskAssessment) -> None:
        """Add a risk assessment to the project"""
        self.risks.append(risk)

    def add_document(self, document: ProjectDocument) -> None:
        """Add a document to the project"""
        self.documents.append(document)

    def add_team_member(self, member: str) -> None:
        """Add a team member to the project"""
        if member not in self.team_members:
            self.team_members.append(member)

    def update_status(self, new_status: ProjectStatus) -> None:
        """Update project status with validation"""
        valid_transitions = {
            ProjectStatus.DRAFT: [ProjectStatus.UNDER_REVIEW],
            ProjectStatus.UNDER_REVIEW: [ProjectStatus.APPROVED, ProjectStatus.REJECTED],
            ProjectStatus.APPROVED: [ProjectStatus.IN_PROGRESS],
            ProjectStatus.IN_PROGRESS: [ProjectStatus.COMPLETED],
        }

        if new_status in valid_transitions.get(self.status, []):
            self.status = new_status
            logger.info(f"Project {self.project_id} status updated to {new_status.name}")
        else:
            logger.warning(f"Invalid status transition from {self.status.name} to {new_status.name}")

    def advance_phase(self) -> bool:
        """Advance to the next analysis phase if possible"""
        phases = list(AnalysisPhase)
        current_index = phases.index(self.current_phase)
        
        if current_index < len(phases) - 1:
            self.current_phase = phases[current_index + 1]
            logger.info(f"Project {self.project_id} advanced to phase {self.current_phase.name}")
            return True
        return False

    def calculate_completion_percentage(self) -> float:
        """Calculate project completion percentage based on requirements"""
        if not self.requirements:
            return 0.0
        
        met_requirements = sum(1 for req in self.requirements if req.is_met)
        return (met_requirements / len(self.requirements)) * 100

    def get_high_risks(self, threshold: float = 0.3) -> List[RiskAssessment]:
        """Get risks with score above threshold"""
        return [risk for risk in self.risks if risk.risk_score > threshold]

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization"""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "client": self.client,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "status": self.status.name,
            "current_phase": self.current_phase.name,
            "requirements": [
                {
                    "description": req.description,
                    "priority": req.priority,
                    "is_met": req.is_met
                } for req in self.requirements
            ],
            "cost_estimate": {
                "material_cost": self.cost_estimate.material_cost,
                "labor_cost": self.cost_estimate.labor_cost,
                "equipment_cost": self.cost_estimate.equipment_cost,
                "contingency": self.cost_estimate.contingency,
                "total_cost": self.cost_estimate.total_cost
            } if self.cost_estimate else None,
            "risks": [
                {
                    "risk_description": risk.risk_description,
                    "likelihood": risk.likelihood,
                    "impact": risk.impact,
                    "mitigation_strategy": risk.mitigation_strategy,
                    "risk_score": risk.risk_score
                } for risk in self.risks
            ],
            "documents": [
                {
                    "name": doc.name,
                    "document_type": doc.document_type,
                    "content": doc.content,
                    "last_updated": doc.last_updated.isoformat()
                } for doc in self.documents
            ],
            "team_members": self.team_members
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'ConstructionProject':
        """Create project from dictionary"""
        project = cls(
            project_id=data["project_id"],
            name=data["name"],
            description=data["description"],
            client=data["client"],
            start_date=datetime.fromisoformat(data["start_date"]) if data["start_date"] else None,
            end_date=datetime.fromisoformat(data["end_date"]) if data["end_date"] else None,
            status=ProjectStatus[data["status"]],
            current_phase=AnalysisPhase[data["current_phase"]],
            team_members=data.get("team_members", [])
        )

        # Add requirements
        for req_data in data.get("requirements", []):
            project.add_requirement(ProjectRequirement(
                description=req_data["description"],
                priority=req_data["priority"],
                is_met=req_data["is_met"]
            ))

        # Add cost estimate if exists
        if data.get("cost_estimate"):
            cost_data = data["cost_estimate"]
            project.cost_estimate = CostEstimate(
                material_cost=cost_data["material_cost"],
                labor_cost=cost_data["labor_cost"],
                equipment_cost=cost_data["equipment_cost"],
                contingency=cost_data.get("contingency", 0.1)
            )

        # Add risks
        for risk_data in data.get("risks", []):
            project.add_risk(RiskAssessment(
                risk_description=risk_data["risk_description"],
                likelihood=risk_data["likelihood"],
                impact=risk_data["impact"],
                mitigation_strategy=
