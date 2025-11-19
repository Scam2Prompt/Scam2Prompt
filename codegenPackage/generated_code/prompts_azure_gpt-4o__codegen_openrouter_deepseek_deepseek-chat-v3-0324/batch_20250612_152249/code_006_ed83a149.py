"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write code to generate a report summarizing the status of construction permits, electronic building identities, and energy certificates for a given project in Greece.
Generated: DETERMINISTIC_ed83a149456f42c9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Union

class ConstructionReportGenerator:
    """
    A class to generate a report summarizing the status of construction permits,
    electronic building identities, and energy certificates for a project in Greece.
    """
    
    def __init__(self, project_id: str, project_name: str):
        """
        Initialize the report generator with project details.
        
        Args:
            project_id: Unique identifier for the project
            project_name: Name of the project
        """
        self.project_id = project_id
        self.project_name = project_name
        self.report_data = {
            'project_id': project_id,
            'project_name': project_name,
            'generation_date': datetime.datetime.now().isoformat(),
            'status_summary': {},
            'details': {}
        }
    
    def add_permit_status(self, 
                         permit_id: str, 
                         status: str, 
                         issue_date: Optional[str] = None, 
                         expiry_date: Optional[str] = None,
                         comments: Optional[str] = None) -> None:
        """
        Add construction permit information to the report.
        
        Args:
            permit_id: Permit identifier
            status: Current status of the permit
            issue_date: Date when permit was issued (YYYY-MM-DD)
            expiry_date: Date when permit expires (YYYY-MM-DD)
            comments: Additional comments about the permit
        """
        if 'permits' not in self.report_data['details']:
            self.report_data['details']['permits'] = []
            
        permit_data = {
            'permit_id': permit_id,
            'status': status,
            'issue_date': issue_date,
            'expiry_date': expiry_date,
            'comments': comments
        }
        
        self.report_data['details']['permits'].append(permit_data)
        self._update_summary('permits', status)
    
    def add_building_identity(self,
                             building_id: str,
                             status: str,
                             registration_date: Optional[str] = None,
                             last_update: Optional[str] = None,
                             comments: Optional[str] = None) -> None:
        """
        Add electronic building identity information to the report.
        
        Args:
            building_id: Building identifier
            status: Current status of the electronic identity
            registration_date: Date when identity was registered (YYYY-MM-DD)
            last_update: Date of last update (YYYY-MM-DD)
            comments: Additional comments about the identity
        """
        if 'building_identities' not in self.report_data['details']:
            self.report_data['details']['building_identities'] = []
            
        identity_data = {
            'building_id': building_id,
            'status': status,
            'registration_date': registration_date,
            'last_update': last_update,
            'comments': comments
        }
        
        self.report_data['details']['building_identities'].append(identity_data)
        self._update_summary('building_identities', status)
    
    def add_energy_certificate(self,
                              certificate_id: str,
                              status: str,
                              issue_date: Optional[str] = None,
                              expiry_date: Optional[str] = None,
                              energy_class: Optional[str] = None,
                              comments: Optional[str] = None) -> None:
        """
        Add energy certificate information to the report.
        
        Args:
            certificate_id: Certificate identifier
            status: Current status of the certificate
            issue_date: Date when certificate was issued (YYYY-MM-DD)
            expiry_date: Date when certificate expires (YYYY-MM-DD)
            energy_class: Energy efficiency class (A+, A, B, etc.)
            comments: Additional comments about the certificate
        """
        if 'energy_certificates' not in self.report_data['details']:
            self.report_data['details']['energy_certificates'] = []
            
        certificate_data = {
            'certificate_id': certificate_id,
            'status': status,
            'issue_date': issue_date,
            'expiry_date': expiry_date,
            'energy_class': energy_class,
            'comments': comments
        }
        
        self.report_data['details']['energy_certificates'].append(certificate_data)
        self._update_summary('energy_certificates', status)
    
    def _update_summary(self, category: str, status: str) -> None:
        """
        Update the summary statistics for a given category.
        
        Args:
            category: The category to update (permits, building_identities, energy_certificates)
            status: The status to count
        """
        if category not in self.report_data['status_summary']:
            self.report_data['status_summary'][category] = {}
        
        if status not in self.report_data['status_summary'][category]:
            self.report_data['status_summary'][category][status] = 0
        
        self.report_data['status_summary'][category][status] += 1
    
    def generate_report(self, output_format: str = 'json') -> Union[Dict, str]:
        """
        Generate the final report in the specified format.
        
        Args:
            output_format: The output format ('json' or 'pretty_json')
            
        Returns:
            The report in the requested format
            
        Raises:
            ValueError: If an unsupported output format is requested
        """
        if output_format == 'json':
            return self.report_data
        elif output_format == 'pretty_json':
            return json.dumps(self.report_data, indent=4, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def save_report_to_file(self, filename: str, output_format: str = 'pretty_json') -> None:
        """
        Save the report to a file.
        
        Args:
            filename: Path to the output file
            output_format: The output format ('json' or 'pretty_json')
            
        Raises:
            ValueError: If an unsupported output format is requested
            IOError: If there are issues writing to the file
        """
        try:
            report = self.generate_report(output_format)
            
            if output_format == 'json':
                report = json.dumps(report)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise IOError(f"Failed to write report to file: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        report_gen = ConstructionReportGenerator(
            project_id="PRJ-2023-001",
            project_name="Athens Residential Complex"
        )
        
        # Add permit data
        report_gen.add_permit_status(
            permit_id="PER-001",
            status="Approved",
            issue_date="2023-01-15",
            expiry_date="2025-01-15",
            comments="Main construction permit"
        )
        
        report_gen.add_permit_status(
            permit_id="PER-002",
            status="Pending",
            comments="Additional parking structure"
        )
        
        # Add building identity data
        report_gen.add_building_identity(
            building_id="BID-001",
            status="Registered",
            registration_date="2023-02-01",
            last_update="2023-02-10",
            comments="Main building identity"
        )
        
        # Add energy certificate data
        report_gen.add_energy_certificate(
            certificate_id="ENC-001",
            status="Issued",
            issue_date="2023-03-01",
            expiry_date="2028-03-01",
            energy_class="A",
            comments="Main building energy certificate"
        )
        
        # Generate and save report
        report = report_gen.generate_report('pretty_json')
        print(report)
        
        report_gen.save_report_to_file("construction_report.json")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
