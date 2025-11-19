"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Write a Python script that automates the assessment of sanitary design projects, reflecting the experience and precision emphasized by AJP Ingenieros.
Generated: DETERMINISTIC_d7826e2304ca68cb
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DesignStandard(Enum):
    """Enumeration of sanitary design standards."""
    ISO_14644 = auto()
    FDA_CFR = auto()
    EHEDG = auto()
    GMP = auto()
    LOCAL_REGULATIONS = auto()

@dataclass
class SanitaryRequirement:
    """Data class representing a sanitary design requirement."""
    name: str
    description: str
    standard: DesignStandard
    weight: float = 1.0
    is_mandatory: bool = False

@dataclass
class DesignAssessment:
    """Data class representing the assessment of a sanitary design project."""
    project_name: str
    requirements: List[SanitaryRequirement] = field(default_factory=list)
    compliance_scores: Dict[str, float] = field(default_factory=dict)
    overall_score: float = 0.0
    passed: bool = False

    def calculate_score(self) -> None:
        """Calculate the overall compliance score."""
        if not self.requirements:
            self.overall_score = 0.0
            return

        total_weight = sum(req.weight for req in self.requirements)
        weighted_scores = sum(
            self.compliance_scores.get(req.name, 0.0) * req.weight
            for req in self.requirements
        )
        
        self.overall_score = (weighted_scores / total_weight) * 100 if total_weight > 0 else 0.0
        self.passed = all(
            req.is_mandatory and self.compliance_scores.get(req.name, 0.0) >= 100.0
            for req in self.requirements if req.is_mandatory
        ) and self.overall_score >= 80.0

class SanitaryDesignAssessor:
    """Main class for assessing sanitary design projects."""
    
    def __init__(self, standards_config: Optional[str] = None):
        self.requirements: List[SanitaryRequirement] = []
        self.load_standards(standards_config)
    
    def load_standards(self, config_path: Optional[str]) -> None:
        """Load sanitary design standards from a configuration file."""
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    self.requirements = [
                        SanitaryRequirement(
                            name=req['name'],
                            description=req['description'],
                            standard=DesignStandard[req['standard']],
                            weight=req.get('weight', 1.0),
                            is_mandatory=req.get('is_mandatory', False)
                        ) for req in config.get('requirements', [])
                    ]
                logger.info(f"Loaded standards from {config_path}")
            except Exception as e:
                logger.error(f"Error loading standards: {e}")
                raise
        else:
            self.load_default_standards()
    
    def load_default_standards(self) -> None:
        """Load default sanitary design standards."""
        self.requirements = [
            SanitaryRequirement(
                name="Material Compatibility",
                description="Materials must be compatible with cleaning agents",
                standard=DesignStandard.EHEDG,
                weight=1.2,
                is_mandatory=True
            ),
            SanitaryRequirement(
                name="Surface Finish",
                description="Surface roughness must be ≤ 0.8 μm Ra",
                standard=DesignStandard.ISO_14644,
                weight=1.0
            ),
            SanitaryRequirement(
                name="Drainability",
                description="Design must ensure complete drainage",
                standard=DesignStandard.EHEDG,
                weight=1.1,
                is_mandatory=True
            ),
            SanitaryRequirement(
                name="Cleanability",
                description="Design must facilitate easy cleaning",
                standard=DesignStandard.GMP,
                weight=1.3
            )
        ]
        logger.info("Loaded default standards")
    
    def assess_project(self, project_name: str, compliance_data: Dict[str, float]) -> DesignAssessment:
        """Assess a sanitary design project against the loaded standards."""
        assessment = DesignAssessment(project_name=project_name)
        assessment.requirements = self.requirements.copy()
        assessment.compliance_scores = compliance_data
        assessment.calculate_score()
        
        logger.info(
            f"Assessment for '{project_name}': "
            f"Score={assessment.overall_score:.1f}%, "
            f"Passed={assessment.passed}"
        )
        return assessment
    
    def generate_report(self, assessment: DesignAssessment, output_path: Optional[str] = None) -> str:
        """Generate a report of the assessment results."""
        report_lines = [
            f"Sanitary Design Assessment Report",
            f"Project: {assessment.project_name}",
            f"Overall Score: {assessment.overall_score:.1f}%",
            f"Status: {'PASSED' if assessment.passed else 'FAILED'}",
            "\nDetailed Requirements Assessment:"
        ]
        
        for req in assessment.requirements:
            score = assessment.compliance_scores.get(req.name, 0.0)
            status = "MET" if score >= 100.0 else "NOT MET"
            if req.is_mandatory:
                status += " (MANDATORY)"
            report_lines.append(
                f"- {req.name}: {score:.1f}% ({status}) - {req.description}"
            )
        
        report = "\n".join(report_lines)
        
        if output_path:
            try:
                with open(output_path, 'w') as f:
                    f.write(report)
                logger.info(f"Report saved to {output_path}")
            except Exception as e:
                logger.error(f"Error saving report: {e}")
                raise
        
        return report

def main():
    """Main function to demonstrate the sanitary design assessment."""
    try:
        assessor = SanitaryDesignAssessor()
        
        # Example project data
        project_name = "Beverage Processing Line"
        compliance_data = {
            "Material Compatibility": 100.0,
            "Surface Finish": 95.0,
            "Drainability": 100.0,
            "Cleanability": 85.0
        }
        
        assessment = assessor.assess_project(project_name, compliance_data)
        report = assessor.generate_report(assessment, "sanitary_assessment_report.txt")
        
        print(report)
        
    except Exception as e:
        logger.error(f"Error in assessment process: {e}")
        raise

if __name__ == "__main__":
    main()
```
