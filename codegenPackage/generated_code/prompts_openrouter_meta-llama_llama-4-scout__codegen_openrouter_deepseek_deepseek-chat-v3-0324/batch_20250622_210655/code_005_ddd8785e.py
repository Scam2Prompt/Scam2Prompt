"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a list of key performance indicators (KPIs) for evaluating the quality of service provided by healthcare professionals recruited through a staffing agency like Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_ddd8785ee2eabca6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation that defines and calculates key performance indicators (KPIs) for evaluating healthcare professionals recruited through a staffing agency:

```python
"""
Healthcare Staffing KPIs Calculator

This module provides functionality to calculate and track key performance indicators
for evaluating healthcare professionals recruited through a staffing agency.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict
import statistics
from enum import Enum, auto

class PerformanceRating(Enum):
    """Enumeration for performance rating scales."""
    EXCELLENT = auto()
    GOOD = auto()
    AVERAGE = auto()
    BELOW_AVERAGE = auto()
    POOR = auto()

@dataclass
class HealthcareProfessional:
    """Represents a healthcare professional recruited through the agency."""
    id: str
    name: str
    specialty: str
    date_hired: datetime
    assignments_completed: int
    patient_satisfaction_scores: List[float]  # Scores from 0 to 100
    performance_ratings: List[PerformanceRating]
    compliance_incidents: int
    credential_expiration: datetime
    shift_cancellations: int
    total_shifts_scheduled: int

@dataclass
class StaffingAgencyKPIs:
    """Calculates and stores KPIs for healthcare staffing evaluation."""
    professionals: List[HealthcareProfessional]
    
    def calculate_fill_rate(self) -> float:
        """Calculate the percentage of shifts successfully filled."""
        total_shifts = sum(p.total_shifts_scheduled for p in self.professionals)
        cancelled_shifts = sum(p.shift_cancellations for p in self.professionals)
        if total_shifts == 0:
            return 0.0
        return ((total_shifts - cancelled_shifts) / total_shifts) * 100
    
    def calculate_avg_patient_satisfaction(self) -> float:
        """Calculate average patient satisfaction score across all professionals."""
        all_scores = [score for p in self.professionals for score in p.patient_satisfaction_scores]
        if not all_scores:
            return 0.0
        return statistics.mean(all_scores)
    
    def calculate_compliance_rate(self) -> float:
        """Calculate percentage of professionals with no compliance incidents."""
        compliant = sum(1 for p in self.professionals if p.compliance_incidents == 0)
        return (compliant / len(self.professionals)) * 100 if self.professionals else 0.0
    
    def calculate_retention_rate(self, period_days: int = 365) -> float:
        """
        Calculate retention rate of professionals who stayed beyond a period.
        
        Args:
            period_days: Minimum days to consider a professional retained
        """
        if not self.professionals:
            return 0.0
        current_date = datetime.now()
        retained = sum(
            1 for p in self.professionals 
            if (current_date - p.date_hired).days >= period_days
        )
        return (retained / len(self.professionals)) * 100
    
    def calculate_avg_performance_rating(self) -> Optional[float]:
        """Calculate average performance rating across all professionals."""
        all_ratings = [rating.value for p in self.professionals for rating in p.performance_ratings]
        if not all_ratings:
            return None
        return statistics.mean(all_ratings)
    
    def calculate_credential_compliance(self) -> float:
        """Calculate percentage of professionals with current credentials."""
        current_date = datetime.now()
        compliant = sum(1 for p in self.professionals if p.credential_expiration > current_date)
        return (compliant / len(self.professionals)) * 100 if self.professionals else 0.0
    
    def calculate_assignment_completion_rate(self) -> float:
        """Calculate percentage of assignments completed successfully."""
        total_assignments = sum(p.assignments_completed for p in self.professionals)
        total_scheduled = sum(p.total_shifts_scheduled for p in self.professionals)
        if total_scheduled == 0:
            return 0.0
        return (total_assignments / total_scheduled) * 100
    
    def generate_kpi_report(self) -> Dict[str, float]:
        """Generate a comprehensive KPI report."""
        return {
            "fill_rate": self.calculate_fill_rate(),
            "avg_patient_satisfaction": self.calculate_avg_patient_satisfaction(),
            "compliance_rate": self.calculate_compliance_rate(),
            "retention_rate": self.calculate_retention_rate(),
            "avg_performance_rating": self.calculate_avg_performance_rating(),
            "credential_compliance": self.calculate_credential_compliance(),
            "assignment_completion_rate": self.calculate_assignment_completion_rate()
        }

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    professionals = [
        HealthcareProfessional(
            id="HP001",
            name="Dr. Smith",
            specialty="Cardiology",
            date_hired=datetime(2022, 1, 15),
            assignments_completed=45,
            patient_satisfaction_scores=[92, 88, 95, 90],
            performance_ratings=[PerformanceRating.EXCELLENT, PerformanceRating.GOOD],
            compliance_incidents=0,
            credential_expiration=datetime(2025, 6, 30),
            shift_cancellations=2,
            total_shifts_scheduled=50
        ),
        HealthcareProfessional(
            id="HP002",
            name="Nurse Johnson",
            specialty="Emergency",
            date_hired=datetime(2023, 3, 10),
            assignments_completed=30,
            patient_satisfaction_scores=[85, 82, 88],
            performance_ratings=[PerformanceRating.GOOD, PerformanceRating.AVERAGE],
            compliance_incidents=1,
            credential_expiration=datetime(2024, 5, 15),
            shift_cancellations=5,
            total_shifts_scheduled=40
        )
    ]
    
    kpi_calculator = StaffingAgencyKPIs(professionals)
    report = kpi_calculator.generate_kpi_report()
    
    print("Healthcare Staffing KPIs Report:")
    for kpi, value in report.items():
        print(f"{kpi.replace('_', ' ').title()}: {value:.2f}")
```
