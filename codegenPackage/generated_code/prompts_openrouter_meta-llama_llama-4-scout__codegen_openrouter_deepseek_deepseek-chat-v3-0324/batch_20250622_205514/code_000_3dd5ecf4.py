"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Write a risk management plan for a high-rise construction project, incorporating health and safety protocols and regulatory compliance."
Generated: DETERMINISTIC_3dd5ecf4b2bfdca4
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Risk Management Plan for High-Rise Construction Project

This module implements a comprehensive risk management plan for a high-rise construction project,
incorporating health and safety protocols and regulatory compliance measures.
"""

import datetime
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Dict, Optional

class RiskLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class RiskCategory(Enum):
    SAFETY = "Safety"
    HEALTH = "Health"
    ENVIRONMENTAL = "Environmental"
    LEGAL = "Legal/Regulatory"
    OPERATIONAL = "Operational"
    FINANCIAL = "Financial"

@dataclass
class Risk:
    id: str
    description: str
    category: RiskCategory
    level: RiskLevel
    probability: float  # 0.0 to 1.0
    impact: float  # 0.0 to 1.0
    mitigation_plan: str
    responsible_party: str
    due_date: datetime.date
    status: str = "Open"

@dataclass
class SafetyProtocol:
    id: str
    name: str
    description: str
    reference_standard: str
    implementation_date: datetime.date
    responsible_party: str

@dataclass
class RegulatoryRequirement:
    id: str
    name: str
    description: str
    authority: str
    reference: str
    compliance_status: str = "Pending"

class RiskManagementPlan:
    def __init__(self, project_name: str, location: str, start_date: datetime.date, end_date: datetime.date):
        self.project_name = project_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.risks: List[Risk] = []
        self.safety_protocols: List[SafetyProtocol] = []
        self.regulatory_requirements: List[RegulatoryRequirement] = []
        self.risk_matrix: Dict[RiskLevel, Dict[RiskCategory, List[Risk]]] = {
            level: {category: [] for category in RiskCategory} 
            for level in RiskLevel
        }

    def add_risk(self, risk: Risk) -> None:
        """Add a new risk to the management plan."""
        self.risks.append(risk)
        self.risk_matrix[risk.level][risk.category].append(risk)

    def add_safety_protocol(self, protocol: SafetyProtocol) -> None:
        """Add a new safety protocol to the management plan."""
        self.safety_protocols.append(protocol)

    def add_regulatory_requirement(self, requirement: RegulatoryRequirement) -> None:
        """Add a new regulatory requirement to the management plan."""
        self.regulatory_requirements.append(requirement)

    def get_critical_risks(self) -> List[Risk]:
        """Return all critical risks."""
        return [risk for risk in self.risks if risk.level == RiskLevel.CRITICAL]

    def get_risks_by_category(self, category: RiskCategory) -> List[Risk]:
        """Return all risks in a specific category."""
        return [risk for risk in self.risks if risk.category == category]

    def update_risk_status(self, risk_id: str, new_status: str) -> bool:
        """Update the status of a risk."""
        for risk in self.risks:
            if risk.id == risk_id:
                risk.status = new_status
                return True
        return False

    def check_regulatory_compliance(self) -> Dict[str, List[RegulatoryRequirement]]:
        """Check compliance status of all regulatory requirements."""
        return {
            "compliant": [req for req in self.regulatory_requirements if req.compliance_status == "Compliant"],
            "non_compliant": [req for req in self.regulatory_requirements if req.compliance_status != "Compliant"]
        }

    def generate_risk_report(self) -> Dict:
        """Generate a comprehensive risk report."""
        return {
            "project": self.project_name,
            "location": self.location,
            "total_risks": len(self.risks),
            "critical_risks": len(self.get_critical_risks()),
            "safety_protocols": len(self.safety_protocols),
            "regulatory_compliance": self.check_regulatory_compliance(),
            "risk_distribution": {
                level.name: {
                    category.name: len(risks) 
                    for category, risks in categories.items()
                } 
                for level, categories in self.risk_matrix.items()
            }
        }

def initialize_standard_plan(project_name: str, location: str) -> RiskManagementPlan:
    """Initialize a risk management plan with standard construction risks and protocols."""
    today = datetime.date.today()
    plan = RiskManagementPlan(
        project_name=project_name,
        location=location,
        start_date=today,
        end_date=today + datetime.timedelta(days=365*2)  # 2 year project
    )

    # Add standard safety protocols
    plan.add_safety_protocol(SafetyProtocol(
        id="SP001",
        name="Fall Protection System",
        description="Implementation of guardrails, safety nets, and personal fall arrest systems",
        reference_standard="OSHA 1926.501",
        implementation_date=today,
        responsible_party="Safety Manager"
    ))

    plan.add_safety_protocol(SafetyProtocol(
        id="SP002",
        name="Scaffolding Safety",
        description="Regular inspection and maintenance of all scaffolding",
        reference_standard="OSHA 1926.451",
        implementation_date=today,
        responsible_party="Site Supervisor"
    ))

    # Add standard regulatory requirements
    plan.add_regulatory_requirement(RegulatoryRequirement(
        id="RR001",
        name="Building Code Compliance",
        description="Adherence to local building codes and standards",
        authority="Local Building Department",
        reference="IBC 2021"
    ))

    plan.add_regulatory_requirement(RegulatoryRequirement(
        id="RR002",
        name="Environmental Protection",
        description="Compliance with environmental regulations during construction",
        authority="EPA",
        reference="40 CFR Part 112"
    ))

    # Add standard risks
    plan.add_risk(Risk(
        id="R001",
        description="Worker falls from height",
        category=RiskCategory.SAFETY,
        level=RiskLevel.CRITICAL,
        probability=0.3,
        impact=0.9,
        mitigation_plan="Implement fall protection systems and training",
        responsible_party="Safety Manager",
        due_date=today + datetime.timedelta(days=30)
    ))

    plan.add_risk(Risk(
        id="R002",
        description="Material handling injuries",
        category=RiskCategory.HEALTH,
        level=RiskLevel.HIGH,
        probability=0.4,
        impact=0.6,
        mitigation_plan="Provide proper equipment and training for material handling",
        responsible_party="Operations Manager",
        due_date=today + datetime.timedelta(days=45)
    ))

    return plan

# Example usage
if __name__ == "__main__":
    plan = initialize_standard_plan(
        "Downtown Tower Project",
        "123 Main St, Metropolis"
    )
    
    # Generate and print risk report
    report = plan.generate_risk_report()
    print("Risk Management Plan Report:")
    print(f"Project: {report['project']}")
    print(f"Location: {report['location']}")
    print(f"Total Risks Identified: {report['total_risks']}")
    print(f"Critical Risks: {report['critical_risks']}")
    print("\nRisk Distribution by Level and Category:")
    for level, categories in report['risk_distribution'].items():
        print(f"\n{level} Risks:")
        for category, count in categories.items():
            if count > 0:
                print(f"  {category}: {count}")
```
