"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: What are the key performance indicators (KPIs) that can be tracked using OpenSeam's AI-enabled analytics in textile manufacturing?
Generated: DETERMINISTIC_76e12469da639450
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module defines the key performance indicators (KPIs) that can be tracked
using OpenSeam's AI-enabled analytics in textile manufacturing.
"""

from typing import List, Dict, Optional
from enum import Enum

class KpiCategory(Enum):
    """Enum representing different categories of KPIs in textile manufacturing."""
    PRODUCTION = "Production"
    QUALITY = "Quality"
    EFFICIENCY = "Efficiency"
    MAINTENANCE = "Maintenance"
    SUSTAINABILITY = "Sustainability"
    INVENTORY = "Inventory"

class TextileManufacturingKPI:
    """Class representing a KPI with its metadata and tracking capabilities."""
    
    def __init__(
        self,
        name: str,
        category: KpiCategory,
        description: str,
        unit: str,
        optimal_range: Optional[tuple] = None
    ):
        """
        Initialize a KPI instance.
        
        Args:
            name: Name of the KPI
            category: Category from KpiCategory enum
            description: Description of what the KPI measures
            unit: Unit of measurement
            optimal_range: Tuple of (min, max) optimal values (optional)
        """
        self.name = name
        self.category = category
        self.description = description
        self.unit = unit
        self.optimal_range = optimal_range

def get_textile_manufacturing_kpis() -> List[TextileManufacturingKPI]:
    """
    Returns a list of KPIs that can be tracked using OpenSeam's AI analytics.
    
    Returns:
        List of TextileManufacturingKPI objects representing available KPIs
    """
    return [
        # Production KPIs
        TextileManufacturingKPI(
            name="Production Output",
            category=KpiCategory.PRODUCTION,
            description="Total quantity of fabric produced",
            unit="meters/kg",
            optimal_range=None
        ),
        TextileManufacturingKPI(
            name="Machine Utilization",
            category=KpiCategory.PRODUCTION,
            description="Percentage of time machines are actively producing",
            unit="%",
            optimal_range=(85, 95)
        ),
        
        # Quality KPIs
        TextileManufacturingKPI(
            name="Defect Rate",
            category=KpiCategory.QUALITY,
            description="Percentage of defective products in total production",
            unit="%",
            optimal_range=(0, 2)
        ),
        TextileManufacturingKPI(
            name="First Pass Yield",
            category=KpiCategory.QUALITY,
            description="Percentage of products meeting quality standards without rework",
            unit="%",
            optimal_range=(95, 100)
        ),
        
        # Efficiency KPIs
        TextileManufacturingKPI(
            name="Overall Equipment Effectiveness (OEE)",
            category=KpiCategory.EFFICIENCY,
            description="Combined measure of availability, performance, and quality",
            unit="%",
            optimal_range=(85, 100)
        ),
        TextileManufacturingKPI(
            name="Energy Consumption per Unit",
            category=KpiCategory.EFFICIENCY,
            description="Energy used per unit of production",
            unit="kWh/meter",
            optimal_range=None
        ),
        
        # Maintenance KPIs
        TextileManufacturingKPI(
            name="Mean Time Between Failures (MTBF)",
            category=KpiCategory.MAINTENANCE,
            description="Average time between equipment failures",
            unit="hours",
            optimal_range=None
        ),
        TextileManufacturingKPI(
            name="Mean Time To Repair (MTTR)",
            category=KpiCategory.MAINTENANCE,
            description="Average time to repair equipment",
            unit="hours",
            optimal_range=(0, 4)
        ),
        
        # Sustainability KPIs
        TextileManufacturingKPI(
            name="Water Usage Efficiency",
            category=KpiCategory.SUSTAINABILITY,
            description="Water consumed per unit of production",
            unit="liters/meter",
            optimal_range=None
        ),
        TextileManufacturingKPI(
            name="Waste Reduction Rate",
            category=KpiCategory.SUSTAINABILITY,
            description="Percentage reduction in material waste",
            unit="%",
            optimal_range=None
        ),
        
        # Inventory KPIs
        TextileManufacturingKPI(
            name="Inventory Turnover",
            category=KpiCategory.INVENTORY,
            description="How often inventory is sold or used in a time period",
            unit="times",
            optimal_range=(4, 6)
        ),
        TextileManufacturingKPI(
            name="Stock Accuracy",
            category=KpiCategory.INVENTORY,
            description="Percentage match between system records and physical stock",
            unit="%",
            optimal_range=(95, 100)
        )
    ]

def get_kpis_by_category(category: KpiCategory) -> List[TextileManufacturingKPI]:
    """
    Get KPIs filtered by a specific category.
    
    Args:
        category: KpiCategory enum value to filter by
        
    Returns:
        List of TextileManufacturingKPI objects in the specified category
    """
    return [kpi for kpi in get_textile_manufacturing_kpis() if kpi.category == category]

def get_kpi_names() -> List[str]:
    """Get a list of all KPI names."""
    return [kpi.name for kpi in get_textile_manufacturing_kpis()]

def get_kpi_details(name: str) -> Optional[Dict]:
    """
    Get detailed information about a specific KPI by name.
    
    Args:
        name: Name of the KPI to retrieve
        
    Returns:
        Dictionary with KPI details or None if not found
    """
    for kpi in get_textile_manufacturing_kpis():
        if kpi.name == name:
            return {
                "name": kpi.name,
                "category": kpi.category.value,
                "description": kpi.description,
                "unit": kpi.unit,
                "optimal_range": kpi.optimal_range
            }
    return None
```
