"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a Python script that simulates the evaluation of risks in construction projects, based on the guidelines provided by the AFCO for Coordination SPS.
Generated: DETERMINISTIC_331dbd83d4ca7183
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Tuple, Optional
from enum import Enum, auto

class RiskLevel(Enum):
    """Enum representing different risk levels."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    VERY_HIGH = auto()

class RiskCategory(Enum):
    """Enum representing different risk categories."""
    SAFETY = "Safety"
    ENVIRONMENTAL = "Environmental"
    FINANCIAL = "Financial"
    SCHEDULE = "Schedule"
    QUALITY = "Quality"

class ConstructionPhase(Enum):
    """Enum representing different construction phases."""
    PLANNING = "Planning"
    DESIGN = "Design"
    PRE_CONSTRUCTION = "Pre-Construction"
    CONSTRUCTION = "Construction"
    POST_CONSTRUCTION = "Post-Construction"

class Risk:
    """Class representing a construction risk."""
    def __init__(self, 
                 name: str, 
                 category: RiskCategory, 
                 phase: ConstructionPhase, 
                 probability: float, 
                 impact: float,
                 mitigation: Optional[str] = None):
        """
        Initialize a Risk instance.
        
        Args:
            name: Name of the risk
            category: Risk category
            phase: Construction phase
            probability: Probability of occurrence (0-1)
            impact: Impact if occurs (0-1)
            mitigation: Optional mitigation strategy
        """
        self.name = name
        self.category = category
        self.phase = phase
        self.probability = probability
        self.impact = impact
        self.mitigation = mitigation

    def calculate_risk_level(self) -> RiskLevel:
        """Calculate the risk level based on probability and impact."""
        risk_score = self.probability * self.impact
        
        if risk_score < 0.1:
            return RiskLevel.LOW
        elif 0.1 <= risk_score < 0.3:
            return RiskLevel.MEDIUM
        elif 0.3 <= risk_score < 0.6:
            return RiskLevel.HIGH
        else:
            return RiskLevel.VERY_HIGH

    def to_dict(self) -> Dict:
        """Convert risk to dictionary for serialization."""
        return {
            "name": self.name,
            "category": self.category.value,
            "phase": self.phase.value,
            "probability": self.probability,
            "impact": self.impact,
            "mitigation": self.mitigation,
            "risk_level": self.calculate_risk_level().name
        }

class RiskAssessment:
    """Class for managing and evaluating construction risks."""
    def __init__(self, project_name: str):
        """Initialize a RiskAssessment instance."""
        self.project_name = project_name
        self.risks: List[Risk] = []

    def add_risk(self, risk: Risk) -> None:
        """Add a risk to the assessment."""
        self.risks.append(risk)

    def evaluate_risks(self) -> Dict[RiskLevel, List[Dict]]:
        """Evaluate all risks and return categorized by risk level."""
        evaluated_risks = {
            RiskLevel.LOW: [],
            RiskLevel.MEDIUM: [],
            RiskLevel.HIGH: [],
            RiskLevel.VERY_HIGH: []
        }
        
        for risk in self.risks:
            risk_level = risk.calculate_risk_level()
            evaluated_risks[risk_level].append(risk.to_dict())
        
        return evaluated_risks

    def get_high_priority_risks(self) -> List[Dict]:
        """Get all high and very high priority risks."""
        evaluated = self.evaluate_risks()
        return evaluated[RiskLevel.HIGH] + evaluated[RiskLevel.VERY_HIGH]

    def generate_report(self, output_format: str = "json") -> str:
        """
        Generate a risk assessment report.
        
        Args:
            output_format: Format of the report ('json' or 'text')
            
        Returns:
            The generated report as a string
            
        Raises:
            ValueError: If output_format is invalid
        """
        evaluated_risks = self.evaluate_risks()
        
        if output_format == "json":
            report = {
                "project_name": self.project_name,
                "risk_assessment": evaluated_risks,
                "high_priority_risks": self.get_high_priority_risks()
            }
            return json.dumps(report, indent=2)
        elif output_format == "text":
            report_lines = [
                f"Risk Assessment Report for Project: {self.project_name}",
                "=" * 50,
                "\nHigh Priority Risks:"
            ]
            
            for risk in self.get_high_priority_risks():
                report_lines.append(
                    f"- {risk['name']} ({risk['category']}, {risk['phase']}): "
                    f"Probability {risk['probability']*100:.1f}%, "
                    f"Impact {risk['impact']*100:.1f}%, "
                    f"Risk Level: {risk['risk_level']}"
                )
                if risk['mitigation']:
                    report_lines.append(f"  Mitigation: {risk['mitigation']}")
            
            report_lines.append("\nAll Risks by Level:")
            for level, risks in evaluated_risks.items():
                report_lines.append(f"\n{level.name} Risks ({len(risks)}):")
                for risk in risks:
                    report_lines.append(f"- {risk['name']}")
            
            return "\n".join(report_lines)
        else:
            raise ValueError("Invalid output format. Choose 'json' or 'text'.")

def generate_sample_risks() -> List[Risk]:
    """Generate sample risks for demonstration purposes."""
    risks = [
        Risk(
            "Structural collapse",
            RiskCategory.SAFETY,
            ConstructionPhase.CONSTRUCTION,
            0.05,
            0.9,
            "Regular structural integrity checks and proper safety protocols"
        ),
        Risk(
            "Material shortage",
            RiskCategory.SCHEDULE,
            ConstructionPhase.CONSTRUCTION,
            0.3,
            0.5,
            "Maintain buffer stock and multiple supplier contracts"
        ),
        Risk(
            "Design errors",
            RiskCategory.QUALITY,
            ConstructionPhase.DESIGN,
            0.2,
            0.4,
            "Implement thorough design reviews and verification processes"
        ),
        Risk(
            "Worker injury",
            RiskCategory.SAFETY,
            ConstructionPhase.CONSTRUCTION,
            0.15,
            0.6,
            "Safety training and proper PPE usage enforcement"
        ),
        Risk(
            "Budget overrun",
            RiskCategory.FINANCIAL,
            ConstructionPhase.CONSTRUCTION,
            0.4,
            0.7,
            "Regular budget reviews and contingency planning"
        ),
        Risk(
            "Environmental contamination",
            RiskCategory.ENVIRONMENTAL,
            ConstructionPhase.CONSTRUCTION,
            0.1,
            0.8,
            "Proper waste management and spill prevention measures"
        ),
        Risk(
            "Permit delays",
            RiskCategory.SCHEDULE,
            ConstructionPhase.PRE_CONSTRUCTION,
            0.25,
            0.3,
            "Early application submission and regular follow-ups"
        )
    ]
    return risks

def main():
    """Main function to demonstrate risk assessment."""
    try:
        # Create a risk assessment for a sample project
        project_name = "AFCO High-Rise Construction Project"
        assessment = RiskAssessment(project_name)
        
        # Add sample risks
        for risk in generate_sample_risks():
            assessment.add_risk(risk)
        
        # Generate and display reports
        print("\nJSON Report:")
        print(assessment.generate_report("json"))
        
        print("\nText Report:")
        print(assessment.generate_report("text"))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
