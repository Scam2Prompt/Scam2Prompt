"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write a Python script to calculate and track key safety indicators for reducing workplace incidents, following GESEC's methodology for improving organizational processes.
Generated: DETERMINISTIC_2bbdbf32fb3b0499
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class SafetyIndicatorCalculator:
    """
    A class to calculate and track key safety indicators (KSIs) for workplace safety.
    Follows GESEC's methodology for improving organizational processes.
    """

    def __init__(self, data_file: str = "safety_data.json"):
        """
        Initialize the SafetyIndicatorCalculator with a data file.
        
        Args:
            data_file (str): Path to JSON file storing safety data. Defaults to "safety_data.json".
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load safety data from JSON file. Creates file if it doesn't exist.
        
        Returns:
            Dict: Loaded safety data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            else:
                # Initialize with empty data structure
                return {
                    "incidents": [],
                    "inspections": [],
                    "trainings": [],
                    "employees": 0,
                    "work_hours": 0,
                    "metadata": {
                        "created": datetime.now().isoformat(),
                        "last_updated": datetime.now().isoformat()
                    }
                }
        except Exception as e:
            raise RuntimeError(f"Failed to load data file: {e}")

    def _save_data(self) -> None:
        """
        Save safety data to JSON file.
        """
        try:
            self.data["metadata"]["last_updated"] = datetime.now().isoformat()
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            raise RuntimeError(f"Failed to save data file: {e}")

    def add_incident(self, severity: str, date: str, description: str) -> None:
        """
        Add a workplace incident to the tracking system.
        
        Args:
            severity (str): Severity level (minor, moderate, severe, fatal)
            date (str): Date of incident in YYYY-MM-DD format
            description (str): Description of the incident
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            self.data["incidents"].append({
                "severity": severity.lower(),
                "date": date,
                "description": description
            })
            self._save_data()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        except Exception as e:
            raise RuntimeError(f"Failed to add incident: {e}")

    def add_inspection(self, date: str, passed: bool, issues_found: int) -> None:
        """
        Add a safety inspection result.
        
        Args:
            date (str): Date of inspection in YYYY-MM-DD format
            passed (bool): Whether the inspection passed
            issues_found (int): Number of safety issues found
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            self.data["inspections"].append({
                "date": date,
                "passed": passed,
                "issues_found": issues_found
            })
            self._save_data()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        except Exception as e:
            raise RuntimeError(f"Failed to add inspection: {e}")

    def add_training(self, date: str, topic: str, attendees: int) -> None:
        """
        Add a safety training record.
        
        Args:
            date (str): Date of training in YYYY-MM-DD format
            topic (str): Training topic
            attendees (int): Number of attendees
        """
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            self.data["trainings"].append({
                "date": date,
                "topic": topic,
                "attendees": attendees
            })
            self._save_data()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        except Exception as e:
            raise RuntimeError(f"Failed to add training: {e}")

    def update_workforce_metrics(self, employees: int, work_hours: float) -> None:
        """
        Update workforce metrics used for rate calculations.
        
        Args:
            employees (int): Number of employees
            work_hours (float): Total work hours in the period
        """
        try:
            if employees <= 0 or work_hours <= 0:
                raise ValueError("Employees and work hours must be positive numbers")
            self.data["employees"] = employees
            self.data["work_hours"] = work_hours
            self._save_data()
        except Exception as e:
            raise RuntimeError(f"Failed to update workforce metrics: {e}")

    def calculate_incident_rates(self) -> Dict[str, float]:
        """
        Calculate key incident rate metrics.
        
        Returns:
            Dict[str, float]: Dictionary of calculated rates including:
                - total_incidents
                - incident_rate_per_100k_hours
                - severity_distribution (dict of severity counts)
                - days_since_last_incident
        """
        if not self.data["incidents"]:
            return {
                "total_incidents": 0,
                "incident_rate_per_100k_hours": 0.0,
                "severity_distribution": {},
                "days_since_last_incident": None
            }

        try:
            total_incidents = len(self.data["incidents"])
            
            # Calculate severity distribution
            severity_counts = {}
            for incident in self.data["incidents"]:
                severity = incident["severity"]
                severity_counts[severity] = severity_counts.get(severity, 0) + 1
            
            # Calculate incident rate per 100,000 work hours
            work_hours = self.data.get("work_hours", 1)  # Avoid division by zero
            incident_rate = (total_incidents / work_hours) * 100000 if work_hours > 0 else 0
            
            # Calculate days since last incident
            last_incident_date = max(
                datetime.strptime(incident["date"], "%Y-%m-%d") 
                for incident in self.data["incidents"]
            )
            days_since_last = (datetime.now() - last_incident_date).days
            
            return {
                "total_incidents": total_incidents,
                "incident_rate_per_100k_hours": round(incident_rate, 2),
                "severity_distribution": severity_counts,
                "days_since_last_incident": days_since_last
            }
        except Exception as e:
            raise RuntimeError(f"Failed to calculate incident rates: {e}")

    def calculate_inspection_metrics(self) -> Dict[str, float]:
        """
        Calculate key inspection metrics.
        
        Returns:
            Dict[str, float]: Dictionary of calculated metrics including:
                - inspection_pass_rate
                - avg_issues_per_inspection
                - days_since_last_inspection
        """
        if not self.data["inspections"]:
            return {
                "inspection_pass_rate": 0.0,
                "avg_issues_per_inspection": 0.0,
                "days_since_last_inspection": None
            }

        try:
            total_inspections = len(self.data["inspections"])
            passed_inspections = sum(1 for i in self.data["inspections"] if i["passed"])
            total_issues = sum(i["issues_found"] for i in self.data["inspections"])
            
            pass_rate = (passed_inspections / total_inspections) * 100 if total_inspections > 0 else 0
            avg_issues = total_issues / total_inspections if total_inspections > 0 else 0
            
            # Calculate days since last inspection
            last_inspection_date = max(
                datetime.strptime(inspection["date"], "%Y-%m-%d") 
                for inspection in self.data["inspections"]
            )
            days_since_last = (datetime.now() - last_inspection_date).days
            
            return {
                "inspection_pass_rate": round(pass_rate, 1),
                "avg_issues_per_inspection": round(avg_issues, 1),
                "days_since_last_inspection": days_since_last
            }
        except Exception as e:
            raise RuntimeError(f"Failed to calculate inspection metrics: {e}")

    def calculate_training_metrics(self) -> Dict[str, float]:
        """
        Calculate key training metrics.
        
        Returns:
            Dict[str, float]: Dictionary of calculated metrics including:
                - total_trainings
                - total_attendees
                - avg_attendance_rate
                - days_since_last_training
        """
        if not self.data["trainings"]:
            return {
                "total_trainings": 0,
                "total_attendees": 0,
                "avg_attendance_rate":
