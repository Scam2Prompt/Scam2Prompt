"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Write a program to assist in hazardous waste management, including tracking, reporting, and compliance correction, as described by iSi Environmental consultants.
Generated: DETERMINISTIC_bf4d4d6070048ebe
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class HazardousWaste:
    """Class to manage hazardous waste tracking, reporting, and compliance."""
    
    def __init__(self, data_file: str = "waste_data.json"):
        """Initialize the hazardous waste management system.
        
        Args:
            data_file: Path to JSON file storing waste data.
        """
        self.data_file = data_file
        self.waste_data = self._load_data()
        
    def _load_data(self) -> Dict:
        """Load waste data from JSON file or initialize empty structure.
        
        Returns:
            Dictionary containing waste data.
            
        Raises:
            ValueError: If data file exists but contains invalid JSON.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON in {self.data_file}")
        return {
            "waste_entries": [],
            "compliance_issues": [],
            "reports": []
        }
    
    def _save_data(self) -> None:
        """Save current waste data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.waste_data, f, indent=2)
    
    def add_waste_entry(
        self,
        waste_type: str,
        quantity: float,
        units: str,
        location: str,
        generator: str,
        hazard_class: str,
        date: Optional[str] = None
    ) -> Dict:
        """Add a new hazardous waste entry.
        
        Args:
            waste_type: Type/name of hazardous waste.
            quantity: Amount of waste.
            units: Measurement units (kg, liters, etc.).
            location: Where waste is stored.
            generator: Who generated the waste.
            hazard_class: Hazard classification code.
            date: Optional date in YYYY-MM-DD format (defaults to today).
            
        Returns:
            The created waste entry.
        """
        if not date:
            date = datetime.date.today().isoformat()
            
        entry = {
            "id": len(self.waste_data["waste_entries"]) + 1,
            "waste_type": waste_type,
            "quantity": quantity,
            "units": units,
            "location": location,
            "generator": generator,
            "hazard_class": hazard_class,
            "date": date,
            "disposed": False,
            "disposal_date": None,
            "manifest_number": None
        }
        
        self.waste_data["waste_entries"].append(entry)
        self._save_data()
        return entry
    
    def mark_as_disposed(self, entry_id: int, manifest_number: str) -> Dict:
        """Mark waste as properly disposed.
        
        Args:
            entry_id: ID of waste entry.
            manifest_number: EPA manifest number.
            
        Returns:
            Updated waste entry.
            
        Raises:
            ValueError: If entry ID doesn't exist.
        """
        for entry in self.waste_data["waste_entries"]:
            if entry["id"] == entry_id:
                entry["disposed"] = True
                entry["disposal_date"] = datetime.date.today().isoformat()
                entry["manifest_number"] = manifest_number
                self._save_data()
                return entry
        raise ValueError(f"No waste entry found with ID {entry_id}")
    
    def add_compliance_issue(
        self,
        description: str,
        severity: str,
        location: str,
        corrective_action: str,
        due_date: str
    ) -> Dict:
        """Record a compliance issue that needs correction.
        
        Args:
            description: Issue description.
            severity: Low/Medium/High.
            location: Where issue was found.
            corrective_action: Required action.
            due_date: Deadline for correction (YYYY-MM-DD).
            
        Returns:
            The created compliance issue record.
        """
        issue = {
            "id": len(self.waste_data["compliance_issues"]) + 1,
            "description": description,
            "severity": severity,
            "location": location,
            "corrective_action": corrective_action,
            "due_date": due_date,
            "resolved": False,
            "resolution_date": None
        }
        
        self.waste_data["compliance_issues"].append(issue)
        self._save_data()
        return issue
    
    def resolve_compliance_issue(self, issue_id: int) -> Dict:
        """Mark a compliance issue as resolved.
        
        Args:
            issue_id: ID of compliance issue.
            
        Returns:
            Updated compliance issue.
            
        Raises:
            ValueError: If issue ID doesn't exist.
        """
        for issue in self.waste_data["compliance_issues"]:
            if issue["id"] == issue_id:
                issue["resolved"] = True
                issue["resolution_date"] = datetime.date.today().isoformat()
                self._save_data()
                return issue
        raise ValueError(f"No compliance issue found with ID {issue_id}")
    
    def generate_waste_report(
        self,
        start_date: str,
        end_date: str,
        report_type: str = "summary"
    ) -> Dict:
        """Generate a waste management report.
        
        Args:
            start_date: Report start date (YYYY-MM-DD).
            end_date: Report end date (YYYY-MM-DD).
            report_type: Type of report ("summary" or "detailed").
            
        Returns:
            Dictionary containing report data.
        """
        start = datetime.date.fromisoformat(start_date)
        end = datetime.date.fromisoformat(end_date)
        
        filtered_entries = [
            entry for entry in self.waste_data["waste_entries"]
            if start <= datetime.date.fromisoformat(entry["date"]) <= end
        ]
        
        report = {
            "report_id": len(self.waste_data["reports"]) + 1,
            "start_date": start_date,
            "end_date": end_date,
            "report_type": report_type,
            "generated_date": datetime.date.today().isoformat(),
            "total_waste": sum(entry["quantity"] for entry in filtered_entries),
            "waste_by_type": {},
            "disposed_percentage": 0,
            "open_compliance_issues": 0
        }
        
        # Calculate waste by type
        for entry in filtered_entries:
            if entry["waste_type"] not in report["waste_by_type"]:
                report["waste_by_type"][entry["waste_type"]] = 0
            report["waste_by_type"][entry["waste_type"]] += entry["quantity"]
        
        # Calculate disposal percentage
        disposed = sum(1 for entry in filtered_entries if entry["disposed"])
        if filtered_entries:
            report["disposed_percentage"] = (disposed / len(filtered_entries)) * 100
        
        # Count open compliance issues
        report["open_compliance_issues"] = sum(
            1 for issue in self.waste_data["compliance_issues"]
            if not issue["resolved"] and 
            datetime.date.fromisoformat(issue["due_date"]) >= datetime.date.today()
        )
        
        if report_type == "detailed":
            report["entries"] = filtered_entries
            report["compliance_issues"] = [
                issue for issue in self.waste_data["compliance_issues"]
                if not issue["resolved"]
            ]
        
        self.waste_data["reports"].append(report)
        self._save_data()
        return report
    
    def get_pending_actions(self) -> Dict[str, List]:
        """Get all pending actions (undisposed waste and unresolved issues).
        
        Returns:
            Dictionary with lists of pending waste and compliance issues.
        """
        return {
            "undisposed_waste": [
                entry for entry in self.waste_data["waste_entries"]
                if not entry["disposed"]
            ],
            "unresolved_issues": [
                issue for issue in self.waste_data["compliance_issues"]
                if not issue["resolved"] and 
                datetime.date.fromisoformat(issue["due_date"]) >= datetime.date.today()
            ]
        }
    
    def export_report(self, report_id: int, format: str = "json") -> str:
        """Export a report to a specified format.
        
        Args:
            report_id: ID of report to export.
            format: Export format ("json" or "csv").
            
        Returns:
            String containing exported data.
            
        Raises:
            ValueError: If report ID doesn't exist or format is invalid.
        """
        report = None
        for r in self.waste_data["reports"]:
            if r["report_id"] == report_id:
                report = r
                break
                
        if not report:
            raise ValueError(f"No report found with ID {report_id}")
            
        if format == "json":
            return json.dumps(report, indent=2)
        elif format == "csv":
            csv_lines = [
                f"Report ID,{report['report_id']}",
                f"Date Range,{report['start_date']} to {report['end_date']}",
                f"
