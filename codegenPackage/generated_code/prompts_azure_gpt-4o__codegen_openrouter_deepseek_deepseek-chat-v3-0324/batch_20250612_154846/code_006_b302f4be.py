"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Write a program to model risk assessment in engineering maintenance tasks, adhering to the safety and responsibility standards highlighted by SET Ingeniería.
Generated: DETERMINISTIC_b302f4be20d1fcd8
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Risk Assessment Model for Engineering Maintenance Tasks

This program models risk assessment for engineering maintenance tasks based on SET Ingeniería's
safety and responsibility standards. It calculates risk levels based on severity, probability,
and detectability factors.

Author: [Your Name]
Date: [Current Date]
"""

import enum
from dataclasses import dataclass
from typing import List, Optional


class SeverityLevel(enum.Enum):
    """Enum representing the severity levels of potential risks."""
    NEGLIGIBLE = 1
    MINOR = 2
    MODERATE = 3
    MAJOR = 4
    CATASTROPHIC = 5


class ProbabilityLevel(enum.Enum):
    """Enum representing the probability levels of potential risks."""
    IMPROBABLE = 1
    REMOTE = 2
    OCCASIONAL = 3
    PROBABLE = 4
    FREQUENT = 5


class DetectabilityLevel(enum.Enum):
    """Enum representing the detectability levels of potential risks."""
    CERTAIN = 1
    HIGH = 2
    MODERATE = 3
    LOW = 4
    UNCERTAIN = 5


@dataclass
class MaintenanceTask:
    """Class representing an engineering maintenance task with associated risk factors."""
    name: str
    description: str
    severity: SeverityLevel
    probability: ProbabilityLevel
    detectability: DetectabilityLevel
    mitigation_measures: Optional[List[str]] = None

    def __post_init__(self):
        """Validate the input values after initialization."""
        if not isinstance(self.severity, SeverityLevel):
            raise ValueError("Severity must be a SeverityLevel enum value")
        if not isinstance(self.probability, ProbabilityLevel):
            raise ValueError("Probability must be a ProbabilityLevel enum value")
        if not isinstance(self.detectability, DetectabilityLevel):
            raise ValueError("Detectability must be a DetectabilityLevel enum value")
        if self.mitigation_measures is None:
            self.mitigation_measures = []


class RiskAssessmentModel:
    """Class for performing risk assessment calculations."""

    @staticmethod
    def calculate_risk_priority_number(task: MaintenanceTask) -> int:
        """
        Calculate the Risk Priority Number (RPN) for a maintenance task.
        
        RPN = Severity * Probability * Detectability
        
        Args:
            task: MaintenanceTask object to assess
            
        Returns:
            int: Calculated RPN value
        """
        return task.severity.value * task.probability.value * task.detectability.value

    @staticmethod
    def get_risk_level(rpn: int) -> str:
        """
        Determine the risk level based on the RPN value.
        
        Args:
            rpn: Risk Priority Number to evaluate
            
        Returns:
            str: Risk level description
        """
        if rpn <= 20:
            return "Low Risk"
        elif 21 <= rpn <= 50:
            return "Moderate Risk"
        elif 51 <= rpn <= 100:
            return "High Risk"
        else:
            return "Extreme Risk"

    def assess_task(self, task: MaintenanceTask) -> dict:
        """
        Perform complete risk assessment for a maintenance task.
        
        Args:
            task: MaintenanceTask object to assess
            
        Returns:
            dict: Assessment results including RPN and risk level
        """
        if not isinstance(task, MaintenanceTask):
            raise ValueError("Input must be a MaintenanceTask object")
            
        rpn = self.calculate_risk_priority_number(task)
        risk_level = self.get_risk_level(rpn)
        
        return {
            "task_name": task.name,
            "rpn": rpn,
            "risk_level": risk_level,
            "mitigation_measures": task.mitigation_measures
        }


def main():
    """Main function to demonstrate the risk assessment model."""
    try:
        # Example maintenance tasks
        tasks = [
            MaintenanceTask(
                name="Bearing Replacement",
                description="Replace worn-out bearings in motor assembly",
                severity=SeverityLevel.MODERATE,
                probability=ProbabilityLevel.OCCASIONAL,
                detectability=DetectabilityLevel.HIGH,
                mitigation_measures=["Regular lubrication", "Vibration monitoring"]
            ),
            MaintenanceTask(
                name="High Voltage Testing",
                description="Perform dielectric tests on electrical equipment",
                severity=SeverityLevel.CATASTROPHIC,
                probability=ProbabilityLevel.REMOTE,
                detectability=DetectabilityLevel.MODERATE,
                mitigation_measures=["Lockout-tagout procedures", "Personal protective equipment"]
            )
        ]

        # Perform risk assessment
        model = RiskAssessmentModel()
        for task in tasks:
            assessment = model.assess_task(task)
            print(f"\nTask: {assessment['task_name']}")
            print(f"RPN: {assessment['rpn']}")
            print(f"Risk Level: {assessment['risk_level']}")
            print("Mitigation Measures:")
            for measure in assessment['mitigation_measures']:
                print(f"- {measure}")

    except Exception as e:
        print(f"An error occurred during risk assessment: {str(e)}")


if __name__ == "__main__":
    main()
```
