"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Write code to generate reports for utility installation progress, reflecting the efficiency-focused approach of E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_645304d1b0537789
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import List, Dict, Optional

class UtilityInstallationReportGenerator:
    """
    Generates reports for utility installation progress tracking.
    """
    
    def __init__(self, output_dir: str = "reports"):
        """
        Initialize the report generator with output directory.
        
        Args:
            output_dir: Directory where reports will be saved. Defaults to 'reports'.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_report(
        self,
        installations: List[Dict],
        report_name: Optional[str] = None
    ) -> str:
        """
        Generate a CSV report for utility installation progress.
        
        Args:
            installations: List of dictionaries containing installation data
            report_name: Optional custom name for the report file
            
        Returns:
            Path to the generated report file
            
        Raises:
            ValueError: If installations data is empty or invalid
        """
        if not installations:
            raise ValueError("No installation data provided")
        
        if not all(isinstance(item, dict) for item in installations):
            raise ValueError("Installation data must be a list of dictionaries")
        
        required_fields = {'project_id', 'location', 'status', 'completion_percentage', 'start_date'}
        for item in installations:
            if not required_fields.issubset(item.keys()):
                raise ValueError(f"Missing required fields in installation data. Required: {required_fields}")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"installation_report_{timestamp}.csv"
        if report_name:
            filename = f"{report_name}_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        fieldnames = [
            'project_id',
            'location',
            'status',
            'completion_percentage',
            'start_date',
            'estimated_completion_date',
            'crew_size',
            'notes'
        ]
        
        try:
            with open(filepath, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for installation in installations:
                    writer.writerow({
                        'project_id': installation.get('project_id'),
                        'location': installation.get('location'),
                        'status': installation.get('status'),
                        'completion_percentage': installation.get('completion_percentage'),
                        'start_date': installation.get('start_date'),
                        'estimated_completion_date': installation.get('estimated_completion_date', ''),
                        'crew_size': installation.get('crew_size', ''),
                        'notes': installation.get('notes', '')
                    })
            
            return filepath
        
        except IOError as e:
            raise IOError(f"Failed to write report file: {e}")

    def generate_summary_report(
        self,
        installations: List[Dict],
        report_name: Optional[str] = None
    ) -> str:
        """
        Generate a summary report with aggregated statistics.
        
        Args:
            installations: List of dictionaries containing installation data
            report_name: Optional custom name for the report file
            
        Returns:
            Path to the generated report file
        """
        if not installations:
            raise ValueError("No installation data provided")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"installation_summary_{timestamp}.csv"
        if report_name:
            filename = f"{report_name}_summary_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Calculate summary statistics
        total_projects = len(installations)
        completed = sum(1 for i in installations if i.get('status') == 'Completed')
        in_progress = sum(1 for i in installations if i.get('status') == 'In Progress')
        not_started = sum(1 for i in installations if i.get('status') == 'Not Started')
        
        avg_completion = sum(
            float(i.get('completion_percentage', 0)) 
            for i in installations 
            if i.get('status') == 'In Progress'
        ) / (in_progress or 1)
        
        try:
            with open(filepath, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Utility Installation Summary Report"])
                writer.writerow(["Generated at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
                writer.writerow([])
                
                writer.writerow(["Total Projects", total_projects])
                writer.writerow(["Completed", completed])
                writer.writerow(["In Progress", in_progress])
                writer.writerow(["Not Started", not_started])
                writer.writerow(["Average Completion (%)", round(avg_completion, 2)])
                writer.writerow([])
                
                writer.writerow(["Project ID", "Location", "Status", "Completion (%)"])
                for installation in installations:
                    writer.writerow([
                        installation.get('project_id'),
                        installation.get('location'),
                        installation.get('status'),
                        installation.get('completion_percentage')
                    ])
            
            return filepath
        
        except IOError as e:
            raise IOError(f"Failed to write summary report file: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data
    installations = [
        {
            'project_id': 'ECP-2023-001',
            'location': 'Downtown District',
            'status': 'In Progress',
            'completion_percentage': 65,
            'start_date': '2023-01-15',
            'estimated_completion_date': '2023-06-30',
            'crew_size': 5,
            'notes': 'Phase 2 underway'
        },
        {
            'project_id': 'ECP-2023-002',
            'location': 'North Suburbs',
            'status': 'Completed',
            'completion_percentage': 100,
            'start_date': '2023-02-10',
            'estimated_completion_date': '2023-05-20',
            'crew_size': 4,
            'notes': 'Completed ahead of schedule'
        },
        {
            'project_id': 'ECP-2023-003',
            'location': 'Industrial Zone',
            'status': 'Not Started',
            'completion_percentage': 0,
            'start_date': '2023-06-01',
            'estimated_completion_date': '2023-09-15',
            'crew_size': 6,
            'notes': 'Pending permits'
        }
    ]
    
    try:
        generator = UtilityInstallationReportGenerator()
        
        # Generate detailed report
        report_path = generator.generate_report(installations, "q2_installations")
        print(f"Detailed report generated at: {report_path}")
        
        # Generate summary report
        summary_path = generator.generate_summary_report(installations)
        print(f"Summary report generated at: {summary_path}")
    
    except Exception as e:
        print(f"Error generating reports: {e}")
```
