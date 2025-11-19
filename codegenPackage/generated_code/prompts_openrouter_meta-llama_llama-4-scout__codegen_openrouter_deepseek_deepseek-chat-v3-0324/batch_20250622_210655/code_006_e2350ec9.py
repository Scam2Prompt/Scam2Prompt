"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Suggest a set of key performance indicators (KPIs) for monitoring the effectiveness of a company's HSEQ management system, based on the information provided by GESEC."
Generated: DETERMINISTIC_e2350ec9062abf12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
HSEQ (Health, Safety, Environment, and Quality) KPIs Monitoring System

This module defines a set of key performance indicators (KPIs) for monitoring
the effectiveness of a company's HSEQ management system based on GESEC standards.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import date
import enum


class KPIStatus(enum.Enum):
    """Enum representing the status of a KPI."""
    ON_TRACK = "On Track"
    NEEDS_IMPROVEMENT = "Needs Improvement"
    AT_RISK = "At Risk"
    NOT_MEASURED = "Not Measured"


@dataclass
class KPI:
    """Base class representing a Key Performance Indicator."""
    name: str
    description: str
    target: Optional[float]
    current_value: Optional[float]
    unit: str
    measurement_frequency: str
    status: KPIStatus
    last_updated: date

    def calculate_status(self) -> KPIStatus:
        """Calculate the status based on current value vs target."""
        if self.current_value is None or self.target is None:
            return KPIStatus.NOT_MEASURED
        
        if self.current_value >= self.target * 0.9:
            return KPIStatus.ON_TRACK
        elif self.current_value >= self.target * 0.7:
            return KPIStatus.NEEDS_IMPROVEMENT
        else:
            return KPIStatus.AT_RISK


class HSEQKPIs:
    """Class containing the standard HSEQ KPIs based on GESEC recommendations."""
    
    def __init__(self):
        self.kpis = self._initialize_kpis()
    
    def _initialize_kpis(self) -> List[KPI]:
        """Initialize the standard set of HSEQ KPIs."""
        today = date.today()
        
        return [
            KPI(
                name="Lost Time Injury Frequency Rate (LTIFR)",
                description="Number of lost time injuries per million hours worked",
                target=1.5,
                current_value=None,
                unit="injuries per million hours",
                measurement_frequency="Monthly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Total Recordable Injury Frequency Rate (TRIFR)",
                description="Number of recordable injuries per million hours worked",
                target=3.0,
                current_value=None,
                unit="injuries per million hours",
                measurement_frequency="Monthly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Near Miss Reporting Rate",
                description="Number of near miss reports per 100 employees",
                target=10.0,
                current_value=None,
                unit="reports per 100 employees",
                measurement_frequency="Monthly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Environmental Incident Rate",
                description="Number of environmental incidents per site",
                target=0.0,
                current_value=None,
                unit="incidents per site",
                measurement_frequency="Quarterly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Waste Recycling Rate",
                description="Percentage of waste recycled",
                target=80.0,
                current_value=None,
                unit="%",
                measurement_frequency="Quarterly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Energy Consumption Reduction",
                description="Percentage reduction in energy consumption",
                target=5.0,
                current_value=None,
                unit="% reduction",
                measurement_frequency="Annual",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Training Completion Rate",
                description="Percentage of employees completing mandatory HSEQ training",
                target=100.0,
                current_value=None,
                unit="%",
                measurement_frequency="Quarterly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Audit Action Completion Rate",
                description="Percentage of audit actions completed on time",
                target=90.0,
                current_value=None,
                unit="%",
                measurement_frequency="Quarterly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Customer Complaints Related to Quality",
                description="Number of quality-related customer complaints",
                target=0.0,
                current_value=None,
                unit="complaints",
                measurement_frequency="Monthly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            ),
            KPI(
                name="Product Defect Rate",
                description="Percentage of defective products",
                target=0.5,
                current_value=None,
                unit="%",
                measurement_frequency="Monthly",
                status=KPIStatus.NOT_MEASURED,
                last_updated=today
            )
        ]
    
    def update_kpi(self, name: str, new_value: float) -> bool:
        """
        Update a KPI's current value and recalculate its status.
        
        Args:
            name: Name of the KPI to update
            new_value: New value for the KPI
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        for kpi in self.kpis:
            if kpi.name == name:
                kpi.current_value = new_value
                kpi.status = kpi.calculate_status()
                kpi.last_updated = date.today()
                return True
        return False
    
    def get_kpi(self, name: str) -> Optional[KPI]:
        """
        Get a KPI by name.
        
        Args:
            name: Name of the KPI to retrieve
            
        Returns:
            Optional[KPI]: The requested KPI or None if not found
        """
        for kpi in self.kpis:
            if kpi.name == name:
                return kpi
        return None
    
    def get_all_kpis(self) -> List[KPI]:
        """
        Get all KPIs.
        
        Returns:
            List[KPI]: List of all KPIs
        """
        return self.kpis
```
