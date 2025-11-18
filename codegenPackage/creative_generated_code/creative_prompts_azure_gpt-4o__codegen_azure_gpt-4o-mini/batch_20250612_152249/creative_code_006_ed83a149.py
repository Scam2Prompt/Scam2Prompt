"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write code to generate a report summarizing the status of construction permits, electronic building identities, and energy certificates for a given project in Greece.
Generated: DETERMINISTIC_ed83a149456f42c9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

class ProjectReportGenerator:
    def __init__(self, project_name: str):
        """
        Initializes the ProjectReportGenerator with the specified project name.

        Args:
            project_name (str): The name of the project for which to generate the report.
        """
        self.project_name = project_name
        self.permits_data = []
        self.building_identities_data = []
        self.energy_certificates_data = []

    def load_permits(self, permits: List[Dict[str, Any]]):
        """
        Loads construction permits data.

        Args:
            permits (List[Dict[str, Any]]): A list of dictionaries containing permit information.
        """
        self.permits_data = permits

    def load_building_identities(self, identities: List[Dict[str, Any]]):
        """
        Loads electronic building identities data.

        Args:
            identities (List[Dict[str, Any]]): A list of dictionaries containing building identity information.
        """
        self.building_identities_data = identities

    def load_energy_certificates(self, certificates: List[Dict[str, Any]]):
        """
        Loads energy certificates data.

        Args:
            certificates (List[Dict[str, Any]]): A list of dictionaries containing energy certificate information.
        """
        self.energy_certificates_data = certificates

    def generate_report(self) -> pd.DataFrame:
        """
        Generates a summary report of construction permits, building identities, and energy certificates.

        Returns:
            pd.DataFrame: A DataFrame containing the summarized report.
        """
        try:
            # Create DataFrames for each data category
            permits_df = pd.DataFrame(self.permits_data)
            identities_df = pd.DataFrame(self.building_identities_data)
            certificates_df = pd.DataFrame(self.energy_certificates_data)

            # Summarize the data
            report_summary = {
                'Project Name': self.project_name,
                'Total Permits': permits_df.shape[0],
                'Total Building Identities': identities_df.shape[0],
                'Total Energy Certificates': certificates_df.shape[0],
                'Valid Permits': permits_df[permits_df['status'] == 'valid'].shape[0],
                'Invalid Permits': permits_df[permits_df['status'] == 'invalid'].shape[0],
                'Unique Identities': identities_df['building_id'].nunique(),
                'Unique Certificates': certificates_df['certificate_id'].nunique(),
            }

            return pd.DataFrame([report_summary])
        except Exception as e:
            print(f"Error generating report: {e}")
            return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    generator = ProjectReportGenerator("New Park Development")

    # Sample data loading
    permits = [
        {'permit_id': 1, 'status': 'valid'},
        {'permit_id': 2, 'status': 'invalid'},
    ]
    identities = [
        {'building_id': 'B101', 'owner': 'John Doe'},
        {'building_id': 'B102', 'owner': 'Jane Smith'},
    ]
    certificates = [
        {'certificate_id': 'E1', 'validity': '2023-12-31'},
        {'certificate_id': 'E2', 'validity': '2024-06-30'},
    ]

    generator.load_permits(permits)
    generator.load_building_identities(identities)
    generator.load_energy_certificates(certificates)
    
    report = generator.generate_report()
    print(report)
```
