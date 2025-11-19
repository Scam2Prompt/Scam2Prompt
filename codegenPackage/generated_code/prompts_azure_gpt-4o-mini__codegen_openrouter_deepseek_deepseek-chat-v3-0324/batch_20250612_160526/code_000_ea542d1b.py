"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: Generate a code snippet that implements a risk management framework for a construction project, considering the unique challenges outlined by Carte Noir Consulting.
Generated: DETERMINISTIC_ea542d1b547cff30
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Risk Management Framework for Construction Projects
Developed based on Carte Noir Consulting's unique challenges
"""

import json
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RiskCategory(Enum):
    """Enumeration of risk categories in construction projects"""
    SAFETY = "Safety"
    ENVIRONMENTAL = "Environmental"
    SCHEDULE = "Schedule"
    COST = "Cost"
    QUALITY = "Quality"
    LEGAL = "Legal"
    SUPPLY_CHAIN = "Supply Chain"
    TECHNOLOGY = "Technology"

class RiskLevel(Enum):
    """Enumeration of risk severity levels"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class RiskStatus(Enum):
    """Enumeration of risk statuses"""
    IDENTIFIED = "Identified"
    ASSESSED = "Assessed"
    MITIGATED = "Mitigated"
    MONITORED = "Monitored"
    CLOSED = "Closed"

class ConstructionRisk:
    """Class representing a construction project risk"""
    
    def __init__(
        self,
        risk_id: str,
        description: str,
        category: RiskCategory,
        probability: float,
        impact: float,
        level: RiskLevel,
        mitigation_plan: str,
        owner: str,
        status: RiskStatus = RiskStatus.IDENTIFIED,
        date_identified: Optional[datetime] = None
    ):
        """
        Initialize a construction risk
        
        Args:
            risk_id: Unique identifier for the risk
            description: Description of the risk
            category: Risk category
            probability: Probability of occurrence (0-1)
            impact: Impact severity (0-1)
            level: Risk level
            mitigation_plan: Plan to mitigate the risk
            owner: Person responsible for managing the risk
            status: Current status of the risk
            date_identified: Date when risk was identified
        """
        self.risk_id = risk_id
        self.description = description
        self.category = category
        self.probability = probability
        self.impact = impact
        self.level = level
        self.mitigation_plan = mitigation_plan
        self.owner = owner
        self.status = status
        self.date_identified = date_identified or datetime.now()
        self.last_updated = datetime.now()
        
        # Validate probability and impact
        if not 0 <= probability <= 1:
            raise ValueError("Probability must be between 0 and 1")
        if not 0 <= impact <= 1:
            raise ValueError("Impact must be between 0 and 1")
    
    def calculate_risk_score(self) -> float:
        """Calculate the risk score (probability * impact)"""
        return self.probability * self.impact
    
    def update_status(self, new_status: RiskStatus) -> None:
        """Update the status of the risk"""
        self.status = new_status
        self.last_updated = datetime.now()
        logger.info(f"Risk {self.risk_id} status updated to {new_status.value}")
    
    def to_dict(self) -> Dict:
        """Convert risk object to dictionary"""
        return {
            "risk_id": self.risk_id,
            "description": self.description,
            "category": self.category.value,
            "probability": self.probability,
            "impact": self.impact,
            "level": self.level.value,
            "mitigation_plan": self.mitigation_plan,
            "owner": self.owner,
            "status": self.status.value,
            "date_identified": self.date_identified.isoformat(),
            "last_updated": self.last_updated.isoformat(),
            "risk_score": self.calculate_risk_score()
        }

class RiskRegister:
    """Class representing a risk register for a construction project"""
    
    def __init__(self, project_name: str):
        """
        Initialize a risk register
        
        Args:
            project_name: Name of the construction project
        """
        self.project_name = project_name
        self.risks: Dict[str, ConstructionRisk] = {}
        self.created_at = datetime.now()
        logger.info(f"Created new risk register for project: {project_name}")
    
    def add_risk(self, risk: ConstructionRisk) -> None:
        """Add a risk to the register"""
        if risk.risk_id in self.risks:
            raise ValueError(f"Risk with ID {risk.risk_id} already exists")
        self.risks[risk.risk_id] = risk
        logger.info(f"Added new risk to register: {risk.risk_id}")
    
    def remove_risk(self, risk_id: str) -> None:
        """Remove a risk from the register"""
        if risk_id not in self.risks:
            raise ValueError(f"Risk with ID {risk_id} not found")
        del self.risks[risk_id]
        logger.info(f"Removed risk from register: {risk_id}")
    
    def get_risk(self, risk_id: str) -> ConstructionRisk:
        """Get a risk by its ID"""
        if risk_id not in self.risks:
            raise ValueError(f"Risk with ID {risk_id} not found")
        return self.risks[risk_id]
    
    def get_risks_by_category(self, category: RiskCategory) -> List[ConstructionRisk]:
        """Get all risks in a specific category"""
        return [risk for risk in self.risks.values() if risk.category == category]
    
    def get_risks_by_level(self, level: RiskLevel) -> List[ConstructionRisk]:
        """Get all risks with a specific level"""
        return [risk for risk in self.risks.values() if risk.level == level]
    
    def get_risks_by_status(self, status: RiskStatus) -> List[ConstructionRisk]:
        """Get all risks with a specific status"""
        return [risk for risk in self.risks.values() if risk.status == status]
    
    def get_top_risks(self, limit: int = 5) -> List[ConstructionRisk]:
        """Get the top risks by risk score"""
        sorted_risks = sorted(
            self.risks.values(),
            key=lambda x: x.calculate_risk_score(),
            reverse=True
        )
        return sorted_risks[:limit]
    
    def to_json(self) -> str:
        """Convert the risk register to JSON format"""
        register_data = {
            "project_name": self.project_name,
            "created_at": self.created_at.isoformat(),
            "risks": [risk.to_dict() for risk in self.risks.values()]
        }
        return json.dumps(register_data, indent=2)
    
    def save_to_file(self, file_path: str) -> None:
        """Save the risk register to a file"""
        try:
            with open(file_path, 'w') as f:
                f.write(self.to_json())
            logger.info(f"Risk register saved to {file_path}")
        except IOError as e:
            logger.error(f"Failed to save risk register: {str(e)}")
            raise
    
    @classmethod
    def load_from_file(cls, file_path: str) -> 'RiskRegister':
        """Load a risk register from a file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            register = cls(data["project_name"])
            register.created_at = datetime.fromisoformat(data["created_at"])
            
            for risk_data in data["risks"]:
                risk = ConstructionRisk(
                    risk_id=risk_data["risk_id"],
                    description=risk_data["description"],
                    category=RiskCategory(risk_data["category"]),
                    probability=risk_data["probability"],
                    impact=risk_data["impact"],
                    level=RiskLevel(risk_data["level"]),
                    mitigation_plan=risk_data["mitigation_plan"],
                    owner=risk_data["owner"],
                    status=RiskStatus(risk_data["status"]),
                    date_identified=datetime.fromisoformat(risk_data["date_identified"])
                )
                register.risks[risk.risk_id] = risk
            
            logger.info(f"Risk register loaded from {file_path}")
            return register
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to load risk register: {str(e)}")
            raise

class RiskMitigationStrategy:
    """Class representing risk mitigation strategies"""
    
    @staticmethod
    def apply_standard_mitigation(risk: ConstructionRisk) -> None:
        """Apply standard mitigation based on risk level"""
        if risk.level == RiskLevel.LOW:
            risk.mitigation_plan = "Monitor periodically"
        elif risk.level == RiskLevel.MEDIUM:
            risk.mitigation_plan = "Implement control measures and monitor"
        elif risk.level == RiskLevel.HIGH:
            risk.mitigation_plan = "Immediate action required with contingency plans"
        elif risk.level == RiskLevel.CRITICAL:
            risk.mitigation_plan = "Stop work until resolved with executive
