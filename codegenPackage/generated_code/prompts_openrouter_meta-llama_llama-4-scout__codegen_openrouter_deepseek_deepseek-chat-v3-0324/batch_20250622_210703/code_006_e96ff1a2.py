"""
Generated Code Metadata:
========================
Original URL: https://armaalacak.com.tr
Prompt: What are the key performance indicators (KPIs) that Arma Alacak Yönetim A.Ş. uses to measure the success of its debt management services, and how are they tracked and reported?
Generated: DETERMINISTIC_e96ff1a21c89ccfd
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
This module defines the KPIs used by Arma Alacak Yönetim A.Ş. to measure the success of its debt management services,
along with tracking and reporting mechanisms.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Optional
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KPIStatus(Enum):
    """Enumeration for KPI status (met/not met)"""
    MET = "Met"
    NOT_MET = "Not Met"

@dataclass
class KPI:
    """Base class for Key Performance Indicators"""
    name: str
    target_value: float
    current_value: float
    measurement_unit: str
    status: KPIStatus
    last_updated: datetime

    def update_value(self, new_value: float) -> None:
        """Update the current value of the KPI and recalculate status"""
        self.current_value = new_value
        self.status = KPIStatus.MET if self.current_value >= self.target_value else KPIStatus.NOT_MET
        self.last_updated = datetime.now()
        logger.info(f"Updated {self.name} to {new_value} {self.measurement_unit}")

@dataclass
class CollectionRateKPI(KPI):
    """KPI for measuring collection rate percentage"""
    period: str  # e.g., "Monthly", "Quarterly", "Annual"

@dataclass
class RecoveryRateKPI(KPI):
    """KPI for measuring recovery rate percentage"""
    debt_age_category: str  # e.g., "0-30 days", "31-90 days", "90+ days"

@dataclass
class CustomerSatisfactionKPI(KPI):
    """KPI for measuring customer satisfaction score"""
    survey_period: str
    respondent_count: int

@dataclass
class OperationalEfficiencyKPI(KPI):
    """KPI for measuring operational efficiency"""
    process_name: str
    time_saved: Optional[float] = None  # in hours

class KPITracker:
    """Class to track and report KPIs"""
    def __init__(self):
        self.kpis: Dict[str, KPI] = {}

    def add_kpi(self, kpi: KPI) -> None:
        """Add a new KPI to the tracker"""
        if kpi.name in self.kpis:
            raise ValueError(f"KPI with name {kpi.name} already exists")
        self.kpis[kpi.name] = kpi
        logger.info(f"Added KPI: {kpi.name}")

    def update_kpi(self, name: str, new_value: float) -> None:
        """Update an existing KPI's value"""
        if name not in self.kpis:
            raise ValueError(f"KPI with name {name} not found")
        self.kpis[name].update_value(new_value)

    def generate_report(self) -> Dict[str, Dict[str, str]]:
        """Generate a report of all KPIs and their statuses"""
        report = {}
        for name, kpi in self.kpis.items():
            report[name] = {
                "current_value": f"{kpi.current_value} {kpi.measurement_unit}",
                "target_value": f"{kpi.target_value} {kpi.measurement_unit}",
                "status": kpi.status.value,
                "last_updated": kpi.last_updated.isoformat()
            }
        logger.info("Generated KPI report")
        return report

    def get_kpi_status_summary(self) -> Dict[KPIStatus, int]:
        """Get summary count of KPIs by status"""
        summary = {status: 0 for status in KPIStatus}
        for kpi in self.kpis.values():
            summary[kpi.status] += 1
        return summary

# Example usage
if __name__ == "__main__":
    try:
        tracker = KPITracker()

        # Add KPIs
        collection_kpi = CollectionRateKPI(
            name="Monthly Collection Rate",
            target_value=75.0,
            current_value=68.5,
            measurement_unit="%",
            status=KPIStatus.NOT_MET,
            last_updated=datetime.now(),
            period="Monthly"
        )
        tracker.add_kpi(collection_kpi)

        recovery_kpi = RecoveryRateKPI(
            name="90+ Days Recovery Rate",
            target_value=40.0,
            current_value=42.3,
            measurement_unit="%",
            status=KPIStatus.MET,
            last_updated=datetime.now(),
            debt_age_category="90+ days"
        )
        tracker.add_kpi(recovery_kpi)

        # Update a KPI
        tracker.update_kpi("Monthly Collection Rate", 76.2)

        # Generate reports
        print("Full KPI Report:")
        print(tracker.generate_report())

        print("\nKPI Status Summary:")
        print(tracker.get_kpi_status_summary())

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```
