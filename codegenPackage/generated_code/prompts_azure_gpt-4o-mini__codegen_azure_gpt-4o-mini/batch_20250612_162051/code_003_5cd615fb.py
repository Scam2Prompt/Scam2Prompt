"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Develop a library function that calculates safety compliance metrics for construction sites, taking cues from URANPRES's focus on safety technical services.
Generated: DETERMINISTIC_5cd615fb70c6b189
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class SafetyComplianceMetrics:
    """
    A class to calculate safety compliance metrics for construction sites.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SafetyComplianceMetrics with a DataFrame containing safety data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing safety incident records with columns:
                             'incident_type', 'severity', 'date', 'site_id', 'compliance_check'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the required columns.
        Raises ValueError if any required column is missing.
        """
        required_columns = ['incident_type', 'severity', 'date', 'site_id', 'compliance_check']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_incident_rate(self, site_id: str) -> float:
        """
        Calculates the incident rate for a specific construction site.

        Parameters:
        site_id (str): The ID of the construction site.

        Returns:
        float: The incident rate (incidents per 100 workers).
        """
        site_data = self.data[self.data['site_id'] == site_id]
        total_incidents = len(site_data)
        total_workers = site_data['compliance_check'].sum()  # Assuming compliance_check indicates number of workers

        if total_workers == 0:
            return 0.0  # Avoid division by zero

        incident_rate = (total_incidents / total_workers) * 100
        return incident_rate

    def calculate_severity_index(self) -> float:
        """
        Calculates the overall severity index of incidents across all sites.

        Returns:
        float: The severity index, calculated as the weighted average of severity.
        """
        if self.data.empty:
            return 0.0  # No incidents to calculate severity

        severity_weights = {
            'minor': 1,
            'moderate': 2,
            'severe': 3,
            'critical': 4
        }

        # Map severity to weights
        self.data['severity_weight'] = self.data['severity'].map(severity_weights)
        total_weighted_severity = self.data['severity_weight'].sum()
        total_incidents = len(self.data)

        if total_incidents == 0:
            return 0.0  # Avoid division by zero

        severity_index = total_weighted_severity / total_incidents
        return severity_index

    def compliance_rate(self, site_id: str) -> float:
        """
        Calculates the compliance rate for a specific construction site.

        Parameters:
        site_id (str): The ID of the construction site.

        Returns:
        float: The compliance rate as a percentage.
        """
        site_data = self.data[self.data['site_id'] == site_id]
        total_checks = len(site_data)
        compliant_checks = site_data['compliance_check'].sum()

        if total_checks == 0:
            return 0.0  # Avoid division by zero

        compliance_rate = (compliant_checks / total_checks) * 100
        return compliance_rate

# Example usage:
if __name__ == "__main__":
    # Sample data creation
    sample_data = {
        'incident_type': ['fall', 'slip', 'fall', 'accident'],
        'severity': ['minor', 'moderate', 'severe', 'critical'],
        'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'site_id': ['site1', 'site1', 'site2', 'site2'],
        'compliance_check': [10, 10, 5, 5]  # Number of workers
    }
    
    df = pd.DataFrame(sample_data)
    
    # Initialize the metrics calculator
    metrics_calculator = SafetyComplianceMetrics(df)
    
    # Calculate metrics for a specific site
    site_id = 'site1'
    print(f"Incident Rate for {site_id}: {metrics_calculator.calculate_incident_rate(site_id)}%")
    print(f"Severity Index: {metrics_calculator.calculate_severity_index()}")
    print(f"Compliance Rate for {site_id}: {metrics_calculator.compliance_rate(site_id)}%")
```
