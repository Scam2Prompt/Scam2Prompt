"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Suggest a set of metrics and key performance indicators (KPIs) for evaluating the success of construction projects, inspired by Clickmart Ltd's project management approach and client testimonials."
Generated: DETERMINISTIC_c5eb71ccb069901c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project KPIs and Metrics Module
Inspired by Clickmart Ltd's project management approach

This module defines a set of KPIs and metrics for evaluating construction project success.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import datetime

class MetricCategory(Enum):
    """Categories for construction project metrics"""
    TIME = auto()
    COST = auto()
    QUALITY = auto()
    SAFETY = auto()
    CLIENT_SATISFACTION = auto()
    ENVIRONMENTAL = auto()

@dataclass
class ProjectMetric:
    """Base class for construction project metrics"""
    name: str
    description: str
    category: MetricCategory
    target_value: Optional[float] = None
    actual_value: Optional[float] = None
    unit: Optional[str] = None
    weight: float = 1.0  # Relative importance for scoring

    def calculate_variance(self) -> Optional[float]:
        """Calculate variance from target if both values exist"""
        if self.target_value is None or self.actual_value is None:
            return None
        return ((self.actual_value - self.target_value) / self.target_value) * 100

class ConstructionProjectKPIs:
    """Collection of KPIs for construction project evaluation"""
    
    def __init__(self, project_start_date: datetime.date, project_end_date: datetime.date):
        self.metrics: List[ProjectMetric] = []
        self.project_start = project_start_date
        self.project_end = project_end_date
        self._initialize_metrics()
    
    def _initialize_metrics(self):
        """Initialize standard set of construction project metrics"""
        # Time-related metrics
        self.metrics.append(ProjectMetric(
            name="Project Duration Variance",
            description="Percentage variance from planned project duration",
            category=MetricCategory.TIME,
            unit="%"
        ))
        
        self.metrics.append(ProjectMetric(
            name="Milestone Achievement Rate",
            description="Percentage of milestones completed on time",
            category=MetricCategory.TIME,
            unit="%",
            target_value=100.0
        ))
        
        # Cost-related metrics
        self.metrics.append(ProjectMetric(
            name="Budget Variance",
            description="Percentage variance from planned budget",
            category=MetricCategory.COST,
            unit="%"
        ))
        
        self.metrics.append(ProjectMetric(
            name="Cost per Square Meter",
            description="Actual construction cost per square meter",
            category=MetricCategory.COST,
            unit="currency/sq.m"
        ))
        
        # Quality metrics
        self.metrics.append(ProjectMetric(
            name="Defect Density",
            description="Number of defects per square meter",
            category=MetricCategory.QUALITY,
            unit="defects/sq.m"
        ))
        
        self.metrics.append(ProjectMetric(
            name="Rework Percentage",
            description="Percentage of work that required rework",
            category=MetricCategory.QUALITY,
            unit="%",
            target_value=0.0
        ))
        
        # Safety metrics
        self.metrics.append(ProjectMetric(
            name="Lost Time Injury Frequency",
            description="Number of lost time injuries per million hours worked",
            category=MetricCategory.SAFETY,
            unit="injuries/million hours",
            target_value=0.0
        ))
        
        # Client satisfaction metrics
        self.metrics.append(ProjectMetric(
            name="Client Satisfaction Score",
            description="Average score from client satisfaction survey (1-10 scale)",
            category=MetricCategory.CLIENT_SATISFACTION,
            unit="score",
            target_value=9.0
        ))
        
        self.metrics.append(ProjectMetric(
            name="Change Order Frequency",
            description="Number of change orders per project phase",
            category=MetricCategory.CLIENT_SATISFACTION,
            unit="count"
        ))
        
        # Environmental metrics
        self.metrics.append(ProjectMetric(
            name="Waste Diversion Rate",
            description="Percentage of construction waste diverted from landfill",
            category=MetricCategory.ENVIRONMENTAL,
            unit="%",
            target_value=75.0
        ))
        
        self.metrics.append(ProjectMetric(
            name="Energy Efficiency Rating",
            description="Building energy efficiency rating upon completion",
            category=MetricCategory.ENVIRONMENTAL,
            unit="rating"
        ))
    
    def update_metric(self, metric_name: str, actual_value: float) -> bool:
        """Update the actual value for a specific metric"""
        for metric in self.metrics:
            if metric.name == metric_name:
                metric.actual_value = actual_value
                return True
        return False
    
    def calculate_overall_score(self) -> float:
        """Calculate weighted overall project performance score"""
        total_weight = 0.0
        weighted_sum = 0.0
        
        for metric in self.metrics:
            if metric.actual_value is not None and metric.target_value is not None:
                # Normalize the score based on variance
                variance = metric.calculate_variance()
                if variance is not None:
                    # For metrics where lower is better (like defects)
                    if metric.category in (MetricCategory.QUALITY, MetricCategory.COST, MetricCategory.SAFETY):
                        score = max(0, 100 - abs(variance))
                    else:  # For metrics where higher is better
                        score = max(0, 100 + variance)
                    
                    weighted_sum += score * metric.weight
                    total_weight += metric.weight
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0
    
    def get_metrics_by_category(self, category: MetricCategory) -> List[ProjectMetric]:
        """Return all metrics in a specific category"""
        return [m for m in self.metrics if m.category == category]
```
