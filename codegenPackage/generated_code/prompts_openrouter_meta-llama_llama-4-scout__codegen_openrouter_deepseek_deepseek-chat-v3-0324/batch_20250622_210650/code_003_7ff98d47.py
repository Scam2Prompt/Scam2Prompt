"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Explain the role of data-driven decision-making in security guard management, including metrics for evaluating guard performance."
Generated: DETERMINISTIC_7ff98d47fe3332d3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Security Guard Performance Metrics and Data-Driven Decision Making System

This module provides functionality to track, analyze, and evaluate security guard performance
using key metrics for data-driven decision making in security management.
"""

import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional
import statistics
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Incident:
    """Class representing a security incident report."""
    incident_id: str
    guard_id: str
    timestamp: datetime.datetime
    incident_type: str
    severity: int  # Scale of 1-5
    resolution_time: Optional[float] = None  # In minutes
    notes: Optional[str] = None

@dataclass
class PatrolCheck:
    """Class representing a patrol check-in."""
    check_id: str
    guard_id: str
    location_id: str
    timestamp: datetime.datetime
    status: str  # "on_time", "late", "missed"

@dataclass
class GuardPerformanceMetrics:
    """Class containing calculated performance metrics for a security guard."""
    guard_id: str
    time_period: str  # e.g., "weekly", "monthly"
    incidents_handled: int
    average_resolution_time: float
    patrol_compliance_rate: float  # Percentage of on-time patrols
    missed_patrols: int
    average_severity: float
    response_time_variance: float

class SecurityGuardManager:
    """Main class for managing and evaluating security guard performance."""
    
    def __init__(self):
        self.incidents: List[Incident] = []
        self.patrol_checks: List[PatrolCheck] = []
    
    def add_incident(self, incident: Incident) -> None:
        """Add a new incident to the system."""
        try:
            self.incidents.append(incident)
            logger.info(f"Added incident {incident.incident_id} for guard {incident.guard_id}")
        except Exception as e:
            logger.error(f"Error adding incident: {e}")
            raise
    
    def add_patrol_check(self, patrol_check: PatrolCheck) -> None:
        """Add a new patrol check to the system."""
        try:
            self.patrol_checks.append(patrol_check)
            logger.info(f"Added patrol check {patrol_check.check_id} for guard {patrol_check.guard_id}")
        except Exception as e:
            logger.error(f"Error adding patrol check: {e}")
            raise
    
    def calculate_guard_metrics(self, guard_id: str, time_period: str = "weekly") -> GuardPerformanceMetrics:
        """
        Calculate performance metrics for a specific guard over a time period.
        
        Args:
            guard_id: ID of the guard to evaluate
            time_period: Time period for evaluation ("daily", "weekly", "monthly")
            
        Returns:
            GuardPerformanceMetrics object with calculated metrics
        """
        try:
            # Filter incidents and patrol checks for this guard and time period
            now = datetime.datetime.now()
            
            if time_period == "daily":
                start_time = now - datetime.timedelta(days=1)
            elif time_period == "weekly":
                start_time = now - datetime.timedelta(weeks=1)
            elif time_period == "monthly":
                start_time = now - datetime.timedelta(days=30)
            else:
                raise ValueError("Invalid time period specified")
            
            guard_incidents = [
                i for i in self.incidents 
                if i.guard_id == guard_id and i.timestamp >= start_time
            ]
            
            guard_patrols = [
                p for p in self.patrol_checks 
                if p.guard_id == guard_id and p.timestamp >= start_time
            ]
            
            # Calculate incident metrics
            incidents_handled = len(guard_incidents)
            
            resolution_times = [
                i.resolution_time for i in guard_incidents 
                if i.resolution_time is not None
            ]
            avg_resolution = statistics.mean(resolution_times) if resolution_times else 0
            
            severities = [i.severity for i in guard_incidents]
            avg_severity = statistics.mean(severities) if severities else 0
            
            # Calculate patrol metrics
            total_patrols = len(guard_patrols)
            on_time_patrols = len([p for p in guard_patrols if p.status == "on_time"])
            missed_patrols = len([p for p in guard_patrols if p.status == "missed"])
            
            compliance_rate = (on_time_patrols / total_patrols) * 100 if total_patrols > 0 else 0
            
            # Calculate response time variance
            response_variance = statistics.variance(resolution_times) if len(resolution_times) > 1 else 0
            
            return GuardPerformanceMetrics(
                guard_id=guard_id,
                time_period=time_period,
                incidents_handled=incidents_handled,
                average_resolution_time=avg_resolution,
                patrol_compliance_rate=compliance_rate,
                missed_patrols=missed_patrols,
                average_severity=avg_severity,
                response_time_variance=response_variance
            )
            
        except Exception as e:
            logger.error(f"Error calculating metrics for guard {guard_id}: {e}")
            raise
    
    def generate_performance_report(self, guard_ids: List[str], time_period: str = "weekly") -> Dict[str, GuardPerformanceMetrics]:
        """
        Generate performance reports for multiple guards.
        
        Args:
            guard_ids: List of guard IDs to evaluate
            time_period: Time period for evaluation
            
        Returns:
            Dictionary mapping guard IDs to their performance metrics
        """
        reports = {}
        for guard_id in guard_ids:
            try:
                metrics = self.calculate_guard_metrics(guard_id, time_period)
                reports[guard_id] = metrics
            except Exception as e:
                logger.error(f"Error generating report for guard {guard_id}: {e}")
                continue
        return reports
    
    def identify_top_performers(self, time_period: str = "weekly", min_incidents: int = 5) -> List[str]:
        """
        Identify top performing guards based on key metrics.
        
        Args:
            time_period: Time period to evaluate
            min_incidents: Minimum incidents handled to be considered
            
        Returns:
            List of guard IDs sorted by performance score
        """
        try:
            all_guards = {i.guard_id for i in self.incidents} | {p.guard_id for p in self.patrol_checks}
            reports = self.generate_performance_report(list(all_guards), time_period)
            
            # Filter guards with sufficient data
            qualified_guards = {
                gid: metrics for gid, metrics in reports.items() 
                if metrics.incidents_handled >= min_incidents
            }
            
            # Calculate performance score (weighted combination of metrics)
            def calculate_score(metrics: GuardPerformanceMetrics) -> float:
                return (
                    0.4 * metrics.patrol_compliance_rate +
                    0.3 * (100 - metrics.average_resolution_time) +
                    0.2 * (5 - metrics.average_severity) +
                    0.1 * (100 - metrics.response_time_variance)
                )
            
            # Sort guards by performance score
            sorted_guards = sorted(
                qualified_guards.items(),
                key=lambda x: calculate_score(x[1]),
                reverse=True
            )
            
            return [guard_id for guard_id, _ in sorted_guards]
            
        except Exception as e:
            logger.error(f"Error identifying top performers: {e}")
            raise
```
