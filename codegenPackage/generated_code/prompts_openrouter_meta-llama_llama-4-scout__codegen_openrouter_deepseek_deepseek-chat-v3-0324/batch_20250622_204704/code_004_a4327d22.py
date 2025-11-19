"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Create a sample report template for ENL Consortium's company report, including sections for port operations, haulage, and construction services."
Generated: DETERMINISTIC_a4327d22247c3287
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ENL Consortium Company Report Template Generator
This script generates a standardized report template for ENL Consortium's operations.
"""

from datetime import datetime
from typing import Dict, List, Optional
import json

class ENLReportGenerator:
    """
    Generates standardized reports for ENL Consortium covering port operations,
    haulage, and construction services.
    """
    
    def __init__(self, report_title: str, period_start: str, period_end: str):
        """
        Initialize the report generator with basic metadata.
        
        Args:
            report_title: Title of the report
            period_start: Start date of reporting period (YYYY-MM-DD)
            period_end: End date of reporting period (YYYY-MM-DD)
        """
        self.report_metadata = {
            "title": report_title,
            "period": {
                "start": period_start,
                "end": period_end
            },
            "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "company": "ENL Consortium"
        }
        self.sections = {
            "port_operations": None,
            "haulage": None,
            "construction_services": None
        }
    
    def add_port_operations(self, operations: List[Dict], metrics: Dict, notes: Optional[str] = None):
        """
        Add port operations section to the report.
        
        Args:
            operations: List of operation records
            metrics: Key performance metrics
            notes: Additional notes/comments
        """
        self.sections["port_operations"] = {
            "operations": operations,
            "metrics": metrics,
            "notes": notes
        }
    
    def add_haulage(self, shipments: List[Dict], fleet_stats: Dict, incidents: Optional[List[Dict]] = None):
        """
        Add haulage section to the report.
        
        Args:
            shipments: List of shipment records
            fleet_stats: Fleet statistics
            incidents: Any incidents during the period
        """
        self.sections["haulage"] = {
            "shipments": shipments,
            "fleet_stats": fleet_stats,
            "incidents": incidents or []
        }
    
    def add_construction_services(self, projects: List[Dict], completion_stats: Dict, safety_metrics: Dict):
        """
        Add construction services section to the report.
        
        Args:
            projects: List of active/completed projects
            completion_stats: Project completion statistics
            safety_metrics: Workplace safety metrics
        """
        self.sections["construction_services"] = {
            "projects": projects,
            "completion_stats": completion_stats,
            "safety_metrics": safety_metrics
        }
    
    def validate_report(self) -> bool:
        """Validate that all required sections are populated."""
        return all(section is not None for section in self.sections.values())
    
    def generate_report(self, output_format: str = "json") -> Dict:
        """
        Generate the final report in specified format.
        
        Args:
            output_format: Format of output ('json' or 'dict')
            
        Returns:
            The complete report in requested format
            
        Raises:
            ValueError: If report is not valid or format is unsupported
        """
        if not self.validate_report():
            raise ValueError("Report is incomplete. All sections must be populated.")
        
        report = {
            "metadata": self.report_metadata,
            "sections": self.sections
        }
        
        if output_format == "json":
            return json.dumps(report, indent=2)
        elif output_format == "dict":
            return report
        else:
            raise ValueError(f"Unsupported output format: {output_format}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize report
        report = ENLReportGenerator(
            report_title="Q3 2023 Operations Report",
            period_start="2023-07-01",
            period_end="2023-09-30"
        )
        
        # Add port operations data
        port_ops = [
            {"vessel": "MV Atlantic", "cargo": "Containers", "tonnage": 45000},
            {"vessel": "MV Pacific", "cargo": "Bulk Grain", "tonnage": 32000}
        ]
        port_metrics = {"total_tonnage": 77000, "avg_turnaround": "28 hours"}
        report.add_port_operations(port_ops, port_metrics, "Increased grain shipments this quarter")
        
        # Add haulage data
        shipments = [
            {"id": "H-1001", "origin": "Port A", "destination": "Warehouse B", "weight": 24.5},
            {"id": "H-1002", "origin": "Port C", "destination": "Factory D", "weight": 18.2}
        ]
        fleet_stats = {"active_trucks": 42, "avg_utilization": "78%"}
        incidents = [{"id": "INC-2023-09-15", "description": "Minor delay due to roadworks"}]
        report.add_haulage(shipments, fleet_stats, incidents)
        
        # Add construction services data
        projects = [
            {"name": "Terminal Expansion", "status": "75% complete"},
            {"name": "Warehouse Renovation", "status": "Completed"}
        ]
        completion_stats = {"on_time": 85, "delayed": 15}
        safety_metrics = {"lost_time_injuries": 0, "safety_audits": 12}
        report.add_construction_services(projects, completion_stats, safety_metrics)
        
        # Generate and print report
        print(report.generate_report("json"))
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
