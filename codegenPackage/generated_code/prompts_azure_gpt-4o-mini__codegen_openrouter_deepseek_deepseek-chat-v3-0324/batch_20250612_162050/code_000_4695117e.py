"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Write a code snippet that implements a strategic planning tool for organizations, focusing on identifying and monitoring key performance indicators as described by Matter's approach to strategic planning.
Generated: DETERMINISTIC_4695117e5720ae93
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Strategic Planning Tool for Organizations - Key Performance Indicators (KPIs) Monitoring

This module implements a strategic planning tool based on Matter's approach to help organizations
identify, track, and monitor KPIs for strategic decision-making.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class KPI:
    """
    Represents a Key Performance Indicator with its attributes.
    """
    name: str
    description: str
    target_value: float
    current_value: float
    unit: str
    frequency: str  # e.g., 'daily', 'weekly', 'monthly', 'quarterly'
    owner: str
    last_updated: datetime = datetime.now()

    def update_value(self, new_value: float) -> None:
        """
        Update the current value of the KPI and set the last_updated timestamp.
        
        Args:
            new_value: The new value to set for the KPI
        """
        self.current_value = new_value
        self.last_updated = datetime.now()
        logger.info(f"Updated KPI '{self.name}' to {new_value} {self.unit}")

    def progress(self) -> float:
        """
        Calculate progress towards target as a percentage.
        
        Returns:
            float: Progress percentage (0-100)
        """
        if self.target_value == 0:
            return 0.0
        return (self.current_value / self.target_value) * 100

class StrategicPlan:
    """
    Represents an organization's strategic plan with associated KPIs.
    """
    
    def __init__(self, name: str, description: str, timeframe: str):
        """
        Initialize a strategic plan.
        
        Args:
            name: Name of the strategic plan
            description: Description of the plan
            timeframe: Timeframe for the plan (e.g., '2023-2025')
        """
        self.name = name
        self.description = description
        self.timeframe = timeframe
        self.kpis: Dict[str, KPI] = {}
        self.created_at = datetime.now()
        logger.info(f"Created new strategic plan: '{name}'")

    def add_kpi(self, kpi: KPI) -> None:
        """
        Add a KPI to the strategic plan.
        
        Args:
            kpi: KPI object to add
        """
        if kpi.name in self.kpis:
            raise ValueError(f"KPI with name '{kpi.name}' already exists")
        self.kpis[kpi.name] = kpi
        logger.info(f"Added KPI '{kpi.name}' to plan '{self.name}'")

    def remove_kpi(self, kpi_name: str) -> None:
        """
        Remove a KPI from the strategic plan.
        
        Args:
            kpi_name: Name of the KPI to remove
        """
        if kpi_name not in self.kpis:
            raise ValueError(f"KPI with name '{kpi_name}' not found")
        del self.kpis[kpi_name]
        logger.info(f"Removed KPI '{kpi_name}' from plan '{self.name}'")

    def get_kpi(self, kpi_name: str) -> Optional[KPI]:
        """
        Get a KPI by name.
        
        Args:
            kpi_name: Name of the KPI to retrieve
            
        Returns:
            Optional[KPI]: The KPI object if found, None otherwise
        """
        return self.kpis.get(kpi_name)

    def update_kpi_value(self, kpi_name: str, new_value: float) -> None:
        """
        Update the value of a KPI.
        
        Args:
            kpi_name: Name of the KPI to update
            new_value: New value to set
        """
        kpi = self.get_kpi(kpi_name)
        if not kpi:
            raise ValueError(f"KPI with name '{kpi_name}' not found")
        kpi.update_value(new_value)

    def get_kpi_progress(self, kpi_name: str) -> float:
        """
        Get progress percentage for a KPI.
        
        Args:
            kpi_name: Name of the KPI
            
        Returns:
            float: Progress percentage
        """
        kpi = self.get_kpi(kpi_name)
        if not kpi:
            raise ValueError(f"KPI with name '{kpi_name}' not found")
        return kpi.progress()

    def get_all_kpis(self) -> List[KPI]:
        """
        Get all KPIs in the strategic plan.
        
        Returns:
            List[KPI]: List of all KPIs
        """
        return list(self.kpis.values())

    def to_json(self) -> str:
        """
        Serialize the strategic plan to JSON.
        
        Returns:
            str: JSON string representation of the plan
        """
        plan_data = {
            "name": self.name,
            "description": self.description,
            "timeframe": self.timeframe,
            "created_at": self.created_at.isoformat(),
            "kpis": [
                {
                    "name": kpi.name,
                    "description": kpi.description,
                    "target_value": kpi.target_value,
                    "current_value": kpi.current_value,
                    "unit": kpi.unit,
                    "frequency": kpi.frequency,
                    "owner": kpi.owner,
                    "last_updated": kpi.last_updated.isoformat()
                }
                for kpi in self.kpis.values()
            ]
        }
        return json.dumps(plan_data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'StrategicPlan':
        """
        Create a StrategicPlan from JSON.
        
        Args:
            json_str: JSON string representation of the plan
            
        Returns:
            StrategicPlan: Reconstructed StrategicPlan object
        """
        plan_data = json.loads(json_str)
        plan = cls(
            name=plan_data["name"],
            description=plan_data["description"],
            timeframe=plan_data["timeframe"]
        )
        plan.created_at = datetime.fromisoformat(plan_data["created_at"])
        
        for kpi_data in plan_data["kpis"]:
            kpi = KPI(
                name=kpi_data["name"],
                description=kpi_data["description"],
                target_value=kpi_data["target_value"],
                current_value=kpi_data["current_value"],
                unit=kpi_data["unit"],
                frequency=kpi_data["frequency"],
                owner=kpi_data["owner"],
            )
            kpi.last_updated = datetime.fromisoformat(kpi_data["last_updated"])
            plan.kpis[kpi.name] = kpi
        
        return plan

# Example usage
if __name__ == "__main__":
    try:
        # Create a strategic plan
        plan = StrategicPlan(
            name="2023 Growth Strategy",
            description="Plan to increase market share and revenue in 2023",
            timeframe="2023"
        )
        
        # Add some KPIs
        revenue_kpi = KPI(
            name="Quarterly Revenue",
            description="Total revenue per quarter",
            target_value=1000000,
            current_value=750000,
            unit="USD",
            frequency="quarterly",
            owner="Finance Team"
        )
        
        customer_kpi = KPI(
            name="New Customers",
            description="Number of new customers acquired",
            target_value=500,
            current_value=320,
            unit="customers",
            frequency="monthly",
            owner="Sales Team"
        )
        
        plan.add_kpi(revenue_kpi)
        plan.add_kpi(customer_kpi)
        
        # Update a KPI value
        plan.update_kpi_value("Quarterly Revenue", 800000)
        
        # Check progress
        progress = plan.get_kpi_progress("Quarterly Revenue")
        print(f"Revenue progress: {progress:.1f}%")
        
        # Serialize to JSON
        json_data = plan.to_json()
        print("\nSerialized plan:")
        print(json_data)
        
        # Deserialize from JSON
        new_plan = StrategicPlan.from_json(json_data)
        print(f"\nDeserialized plan name: {new_plan.name}")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```
