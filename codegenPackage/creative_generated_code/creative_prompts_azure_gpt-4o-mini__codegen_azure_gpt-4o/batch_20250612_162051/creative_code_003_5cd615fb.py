"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Develop a library function that calculates safety compliance metrics for construction sites, taking cues from URANPRES's focus on safety technical services.
Generated: DETERMINISTIC_5cd615fb70c6b189
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Safety Compliance Metrics Library

This library provides functions to calculate and evaluate safety compliance metrics for construction sites. 
It focuses on key metrics such as incident rates, compliance score, and safety improvements, inspired by URANPRES's safety technical services.

Author: [Your Name]
Date: [Current Date]
"""
from typing import List, Dict


class SafetyComplianceMetrics:
    """
    A class to encapsulate safety compliance calculations for construction sites.
    """

    @staticmethod
    def calculate_incident_rate(total_incidents: int, total_work_hours: int) -> float:
        """
        Calculate the incident rate per 100,000 work hours.

        Args:
            total_incidents (int): Total number of safety incidents on the site.
            total_work_hours (int): Total work hours completed on the site.

        Returns:
            float: Incident rate per 100,000 work hours.
            
        Raises:
            ValueError: If total_work_hours is zero or negative.
        """
        if total_work_hours <= 0:
            raise ValueError("Total work hours must be greater than zero.")
        return (total_incidents / total_work_hours) * 100_000

    @staticmethod
    def calculate_compliance_score(safety_checks: List[Dict[str, bool]]) -> float:
        """
        Calculate the compliance score based on site safety checks.

        Args:
            safety_checks (List[Dict[str, bool]]): List of dictionaries where each dict contains a safety check
                                                   with its status as True (compliant) or False (non-compliant).

        Returns:
            float: Compliance score as a percentage.
        """
        total_checks = len(safety_checks)
        if total_checks == 0:
            return 0.0  # No checks performed, compliance score is 0%
        
        compliant_checks = sum(1 for check in safety_checks if check.get("status", False))
        return (compliant_checks / total_checks) * 100

    @staticmethod
    def evaluate_safety_trend(incident_data: List[int]) -> str:
        """
        Evaluate the safety trend based on a historical list of incidents.

        Args:
            incident_data (List[int]): List of total incidents over a period of time (e.g., per month).

        Returns:
            str: Safety trend description ("Improving", "Stable", "Declining", or "No Data").
        """
        if not incident_data:
            return "No Data"
        if len(incident_data) < 2:
            return "Stable"  # Not enough data to determine a trend.

        # Calculate the difference between incidents in consecutive periods.
        differences = [incident_data[i+1] - incident_data[i] for i in range(len(incident_data)-1)]
        if all(diff < 0 for diff in differences):
            return "Improving"
        elif all(diff > 0 for diff in differences):
            return "Declining"
        else:
            return "Stable"

    @staticmethod
    def aggregate_metrics(incident_rate: float, compliance_score: float) -> str:
        """
        Aggregate compliance metrics into a summary rating.

        Args:
            incident_rate (float): Incident rate per 100,000 work hours.
            compliance_score (float): Compliance score as a percentage.

        Returns:
            str: Aggregate compliance rating ("Excellent", "Good", "Fair", "Poor").
        """
        if compliance_score > 90 and incident_rate < 2:
            return "Excellent"
        elif compliance_score > 75 and incident_rate < 5:
            return "Good"
        elif compliance_score > 50 and incident_rate < 8:
            return "Fair"
        else:
            return "Poor"


# Example Usage (For Testing/Integration Purposes):
if __name__ == "__main__":
    try:
        # Example data
        incidents = 4
        work_hours = 200_000
        safety_checks = [
            {"name": "Hard Hat", "status": True},
            {"name": "Safety Harness", "status": True},
            {"name": "Fire Extinguishers", "status": False},
        ]
        incident_history = [10, 8, 5, 3]

        # Calculate metrics
        incident_rate = SafetyComplianceMetrics.calculate_incident_rate(incidents, work_hours)
        compliance_score = SafetyComplianceMetrics.calculate_compliance_score(safety_checks)
        trend = SafetyComplianceMetrics.evaluate_safety_trend(incident_history)
        aggregate_rating = SafetyComplianceMetrics.aggregate_metrics(incident_rate, compliance_score)

        # Output results
        print(f"Incident Rate: {incident_rate:.2f} per 100,000 hours")
        print(f"Compliance Score: {compliance_score:.2f}%")
        print(f"Safety Trend: {trend}")
        print(f"Aggregate Rating: {aggregate_rating}")

    except Exception as e:
        print(f"Error: {e}")
```
