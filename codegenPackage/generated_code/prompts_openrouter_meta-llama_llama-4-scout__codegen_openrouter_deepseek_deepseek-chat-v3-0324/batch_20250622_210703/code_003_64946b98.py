"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Develop a risk assessment plan for an industrial facility in Peru, including considerations for electrical, mechanical, and civil engineering aspects, based on Marod Consultores' experience in providing consulting services for industrial and energy sectors."
Generated: DETERMINISTIC_64946b98637a1810
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Facility Risk Assessment Tool for Peru
Based on Marod Consultores' experience in industrial and energy sectors
"""

import json
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Optional
import datetime

class RiskLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class AssessmentArea(Enum):
    ELECTRICAL = "Electrical Systems"
    MECHANICAL = "Mechanical Equipment"
    CIVIL = "Civil Infrastructure"
    ENVIRONMENTAL = "Environmental Factors"
    PROCESS = "Process Safety"

@dataclass
class RiskFactor:
    id: str
    description: str
    area: AssessmentArea
    potential_impact: str
    mitigation_measures: List[str]
    probability: float  # 0.0 to 1.0
    consequence: float  # 0.0 to 1.0
    
    @property
    def risk_score(self) -> float:
        return self.probability * self.consequence
    
    @property
    def risk_level(self) -> RiskLevel:
        score = self.risk_score
        if score < 0.2:
            return RiskLevel.LOW
        elif score < 0.4:
            return RiskLevel.MEDIUM
        elif score < 0.6:
            return RiskLevel.HIGH
        else:
            return RiskLevel.CRITICAL

@dataclass
class FacilityAssessment:
    facility_name: str
    location: str
    assessment_date: datetime.date
    assessor: str
    risk_factors: List[RiskFactor] = field(default_factory=list)
    
    def add_risk_factor(self, risk_factor: RiskFactor):
        self.risk_factors.append(risk_factor)
    
    def get_risk_summary(self) -> Dict[RiskLevel, int]:
        summary = {level: 0 for level in RiskLevel}
        for factor in self.risk_factors:
            summary[factor.risk_level] += 1
        return summary
    
    def get_critical_risks(self) -> List[RiskFactor]:
        return [f for f in self.risk_factors if f.risk_level == RiskLevel.CRITICAL]
    
    def to_json(self) -> str:
        return json.dumps({
            "facility_name": self.facility_name,
            "location": self.location,
            "assessment_date": self.assessment_date.isoformat(),
            "assessor": self.assessor,
            "risk_factors": [
                {
                    "id": f.id,
                    "description": f.description,
                    "area": f.area.value,
                    "potential_impact": f.potential_impact,
                    "mitigation_measures": f.mitigation_measures,
                    "probability": f.probability,
                    "consequence": f.consequence,
                    "risk_score": f.risk_score,
                    "risk_level": f.risk_level.name
                }
                for f in self.risk_factors
            ]
        }, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'FacilityAssessment':
        data = json.loads(json_str)
        assessment = cls(
            facility_name=data["facility_name"],
            location=data["location"],
            assessment_date=datetime.date.fromisoformat(data["assessment_date"]),
            assessor=data["assessor"]
        )
        
        for factor_data in data["risk_factors"]:
            factor = RiskFactor(
                id=factor_data["id"],
                description=factor_data["description"],
                area=AssessmentArea(factor_data["area"]),
                potential_impact=factor_data["potential_impact"],
                mitigation_measures=factor_data["mitigation_measures"],
                probability=factor_data["probability"],
                consequence=factor_data["consequence"]
            )
            assessment.add_risk_factor(factor)
        
        return assessment

class RiskAssessmentGenerator:
    """Generates standard risk assessments based on Marod Consultores' templates"""
    
    @staticmethod
    def generate_electrical_risks() -> List[RiskFactor]:
        return [
            RiskFactor(
                id="ELEC-001",
                description="Inadequate electrical protection systems",
                area=AssessmentArea.ELECTRICAL,
                potential_impact="Equipment damage, fire hazard, personnel injury",
                mitigation_measures=[
                    "Implement proper circuit protection",
                    "Regular testing of protection devices",
                    "Staff training on electrical safety"
                ],
                probability=0.3,
                consequence=0.7
            ),
            RiskFactor(
                id="ELEC-002",
                description="Overloaded electrical circuits",
                area=AssessmentArea.ELECTRICAL,
                potential_impact="Equipment failure, fire risk",
                mitigation_measures=[
                    "Conduct load analysis",
                    "Upgrade capacity where needed",
                    "Implement load monitoring"
                ],
                probability=0.4,
                consequence=0.5
            )
        ]
    
    @staticmethod
    def generate_mechanical_risks() -> List[RiskFactor]:
        return [
            RiskFactor(
                id="MECH-001",
                description="Improper equipment maintenance",
                area=AssessmentArea.MECHANICAL,
                potential_impact="Equipment failure, production downtime",
                mitigation_measures=[
                    "Implement preventive maintenance program",
                    "Train maintenance personnel",
                    "Establish spare parts inventory"
                ],
                probability=0.5,
                consequence=0.6
            ),
            RiskFactor(
                id="MECH-002",
                description="Lack of safety guards on moving parts",
                area=AssessmentArea.MECHANICAL,
                potential_impact="Personnel injury, equipment damage",
                mitigation_measures=[
                    "Install proper guarding",
                    "Conduct safety audits",
                    "Implement lockout/tagout procedures"
                ],
                probability=0.3,
                consequence=0.8
            )
        ]
    
    @staticmethod
    def generate_civil_risks() -> List[RiskFactor]:
        return [
            RiskFactor(
                id="CIVIL-001",
                description="Structural integrity concerns",
                area=AssessmentArea.CIVIL,
                potential_impact="Building collapse, personnel injury",
                mitigation_measures=[
                    "Conduct structural assessment",
                    "Implement reinforcement measures",
                    "Regular inspections"
                ],
                probability=0.2,
                consequence=0.9
            ),
            RiskFactor(
                id="CIVIL-002",
                description="Inadequate seismic protection",
                area=AssessmentArea.CIVIL,
                potential_impact="Structural damage during earthquakes",
                mitigation_measures=[
                    "Seismic retrofitting",
                    "Implement earthquake response plan",
                    "Staff training on evacuation procedures"
                ],
                probability=0.3,
                consequence=0.8
            )
        ]
    
    @staticmethod
    def generate_standard_assessment(facility_name: str, location: str, assessor: str) -> FacilityAssessment:
        """Generate a standard assessment with common risk factors"""
        assessment = FacilityAssessment(
            facility_name=facility_name,
            location=location,
            assessment_date=datetime.date.today(),
            assessor=assessor
        )
        
        for risk in RiskAssessmentGenerator.generate_electrical_risks():
            assessment.add_risk_factor(risk)
        
        for risk in RiskAssessmentGenerator.generate_mechanical_risks():
            assessment.add_risk_factor(risk)
        
        for risk in RiskAssessmentGenerator.generate_civil_risks():
            assessment.add_risk_factor(risk)
        
        return assessment

def main():
    """Example usage of the risk assessment system"""
    # Create a new assessment
    assessment = RiskAssessmentGenerator.generate_standard_assessment(
        facility_name="Industrial Plant Lima",
        location="Lima, Peru",
        assessor="Marod Consultores Team"
    )
    
    # Add a custom risk factor
    custom_risk = RiskFactor(
        id="ENV-001",
        description="Potential water contamination",
        area=AssessmentArea.ENVIRONMENTAL,
        potential_impact="Environmental damage, regulatory fines",
        mitigation_measures=[
            "Implement spill containment",
            "Regular environmental monitoring",
            "Staff training on proper waste handling"
        ],
        probability=0.4,
        consequence=0.7
    )
    assessment.add_risk_factor(custom_risk)
    
    # Generate report
    print("Risk Assessment Summary:")
    print(f"Facility: {assessment.facility_name}")
    print(f"Location: {assessment.location}")
    print(f"Assessment Date: {assessment.assessment_date}")
    print("\nRisk Levels Summary:")
    for level, count in assessment.get_risk_summary().items():
        print(f"{level.name}: {count}")
    
    print("\nCritical Risks:")
    for risk in assessment.get_critical_risks():
        print(f"- {risk.description} (Score: {risk.risk_score:.2f})")
    
    # Save to JSON
    with open("risk_assessment.json", "w") as f:
        f.write(assessment.to_json())

if __name__ == "__main__":
    main()
```
