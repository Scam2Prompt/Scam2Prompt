"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write a script to automate the generation of annual reports summarizing the association's achievements, including metrics like programs executed, beneficiaries reached, and partnerships established.
Generated: DETERMINISTIC_dbc42e17b67531eb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import datetime
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='report_generator.log'
)
logger = logging.getLogger(__name__)

class AnnualReportGenerator:
    """Generates annual reports for an association's achievements."""
    
    def __init__(self, year: Optional[int] = None):
        """Initialize the report generator with a specific year.
        
        Args:
            year: The year for which to generate the report. Defaults to current year.
        """
        self.year = year if year else datetime.datetime.now().year
        self.report_data = {
            'year': self.year,
            'programs_executed': 0,
            'beneficiaries_reached': 0,
            'partnerships_established': 0,
            'program_details': [],
            'partnership_details': []
        }
    
    def add_program(self, name: str, beneficiaries: int, description: str = "") -> None:
        """Add a program to the report.
        
        Args:
            name: Name of the program.
            beneficiaries: Number of beneficiaries reached.
            description: Optional description of the program.
        """
        try:
            if not name or beneficiaries < 0:
                raise ValueError("Invalid program data")
                
            self.report_data['programs_executed'] += 1
            self.report_data['beneficiaries_reached'] += beneficiaries
            self.report_data['program_details'].append({
                'name': name,
                'beneficiaries': beneficiaries,
                'description': description
            })
            logger.info(f"Added program: {name}")
        except Exception as e:
            logger.error(f"Error adding program: {e}")
            raise
    
    def add_partnership(self, organization: str, description: str = "") -> None:
        """Add a partnership to the report.
        
        Args:
            organization: Name of the partner organization.
            description: Optional description of the partnership.
        """
        try:
            if not organization:
                raise ValueError("Organization name cannot be empty")
                
            self.report_data['partnerships_established'] += 1
            self.report_data['partnership_details'].append({
                'organization': organization,
                'description': description
            })
            logger.info(f"Added partnership with: {organization}")
        except Exception as e:
            logger.error(f"Error adding partnership: {e}")
            raise
    
    def generate_json_report(self, filename: str) -> None:
        """Generate a JSON report file.
        
        Args:
            filename: Output filename for the JSON report.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.report_data, f, indent=4)
            logger.info(f"JSON report generated: {filename}")
        except Exception as e:
            logger.error(f"Error generating JSON report: {e}")
            raise
    
    def generate_csv_report(self, filename: str) -> None:
        """Generate a CSV report file.
        
        Args:
            filename: Output filename for the CSV report.
        """
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    'Year',
                    'Programs Executed',
                    'Beneficiaries Reached',
                    'Partnerships Established'
                ])
                
                # Write data
                writer.writerow([
                    self.report_data['year'],
                    self.report_data['programs_executed'],
                    self.report_data['beneficiaries_reached'],
                    self.report_data['partnerships_established']
                ])
                
                # Write program details if available
                if self.report_data['program_details']:
                    writer.writerow([])
                    writer.writerow(['Program Name', 'Beneficiaries', 'Description'])
                    for program in self.report_data['program_details']:
                        writer.writerow([
                            program['name'],
                            program['beneficiaries'],
                            program['description']
                        ])
                
                # Write partnership details if available
                if self.report_data['partnership_details']:
                    writer.writerow([])
                    writer.writerow(['Partner Organization', 'Description'])
                    for partner in self.report_data['partnership_details']:
                        writer.writerow([
                            partner['organization'],
                            partner['description']
                        ])
            
            logger.info(f"CSV report generated: {filename}")
        except Exception as e:
            logger.error(f"Error generating CSV report: {e}")
            raise
    
    def get_summary(self) -> Dict:
        """Return a summary of the report data.
        
        Returns:
            A dictionary containing the report summary.
        """
        return {
            'year': self.report_data['year'],
            'programs_executed': self.report_data['programs_executed'],
            'beneficiaries_reached': self.report_data['beneficiaries_reached'],
            'partnerships_established': self.report_data['partnerships_established']
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        report = AnnualReportGenerator(2023)
        
        # Add programs
        report.add_program("Education Initiative", 500, "Providing scholarships to underprivileged students")
        report.add_program("Health Camp", 1200, "Free medical checkups in rural areas")
        report.add_program("Vocational Training", 300, "Skill development workshops")
        
        # Add partnerships
        report.add_partnership("ABC Foundation", "Collaboration on education programs")
        report.add_partnership("XYZ Corp", "Funding for health initiatives")
        
        # Generate reports
        report.generate_json_report("annual_report_2023.json")
        report.generate_csv_report("annual_report_2023.csv")
        
        # Print summary
        print("Report Summary:")
        print(json.dumps(report.get_summary(), indent=2))
        
    except Exception as e:
        logger.critical(f"Failed to generate reports: {e}")
        print(f"An error occurred: {e}")
```
