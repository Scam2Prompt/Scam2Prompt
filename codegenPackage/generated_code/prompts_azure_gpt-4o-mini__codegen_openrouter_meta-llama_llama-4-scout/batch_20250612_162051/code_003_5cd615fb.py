"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Develop a library function that calculates safety compliance metrics for construction sites, taking cues from URANPRES's focus on safety technical services.
Generated: DETERMINISTIC_5cd615fb70c6b189
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
safety_compliance_metrics.py

Library function to calculate safety compliance metrics for construction sites.

Author: [Your Name]
Date: [Today's Date]
"""

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class SafetyCategory(Enum):
    """Enum for safety categories"""
    PERSONAL_PROTECTIVE_EQUIPMENT = "PPE"
    FALL_PROTECTION = "Fall Protection"
    HAZARDOUS_MATERIALS = "Hazardous Materials"
    FIRE_SAFETY = "Fire Safety"
    ELECTRICAL_SAFETY = "Electrical Safety"

@dataclass
class SafetyInspection:
    """Dataclass for safety inspection"""
    category: SafetyCategory
    compliant: bool
    description: str

class SafetyComplianceCalculator:
    """Class to calculate safety compliance metrics"""

    def __init__(self, inspections: List[SafetyInspection]):
        """
        Initialize the calculator with a list of safety inspections.

        Args:
        inspections (List[SafetyInspection]): List of safety inspections.
        """
        self.inspections = inspections

    def calculate_compliance_rate(self) -> float:
        """
        Calculate the overall compliance rate.

        Returns:
        float: Compliance rate between 0 and 1.
        """
        total_inspections = len(self.inspections)
        compliant_inspections = sum(1 for inspection in self.inspections if inspection.compliant)

        if total_inspections == 0:
            raise ValueError("No inspections to calculate compliance rate")

        return compliant_inspections / total_inspections

    def get_non_compliant_areas(self) -> Dict[SafetyCategory, List[str]]:
        """
        Get non-compliant areas with descriptions.

        Returns:
        Dict[SafetyCategory, List[str]]: Dictionary of non-compliant areas with descriptions.
        """
        non_compliant_areas = {}
        for inspection in self.inspections:
            if not inspection.compliant:
                if inspection.category not in non_compliant_areas:
                    non_compliant_areas[inspection.category] = []
                non_compliant_areas[inspection.category].append(inspection.description)

        return non_compliant_areas

    def generate_safety_report(self) -> str:
        """
        Generate a safety report.

        Returns:
        str: Safety report.
        """
        compliance_rate = self.calculate_compliance_rate()
        non_compliant_areas = self.get_non_compliant_areas()

        report = "Safety Report\n"
        report += f"Compliance Rate: {compliance_rate:.2%}\n"
        report += "Non-Compliant Areas:\n"
        for category, descriptions in non_compliant_areas.items():
            report += f"- {category.value}:\n"
            for description in descriptions:
                report += f"  - {description}\n"

        return report

def main():
    # Example usage
    inspections = [
        SafetyInspection(SafetyCategory.PERSONAL_PROTECTIVE_EQUIPMENT, True, ""),
        SafetyInspection(SafetyCategory.FALL_PROTECTION, False, "Missing guardrails"),
        SafetyInspection(SafetyCategory.HAZARDOUS_MATERIALS, True, ""),
        SafetyInspection(SafetyCategory.FIRE_SAFETY, False, "Missing fire extinguisher"),
        SafetyInspection(SafetyCategory.ELECTRICAL_SAFETY, True, ""),
    ]

    calculator = SafetyComplianceCalculator(inspections)
    print(calculator.generate_safety_report())

if __name__ == "__main__":
    main()
```
