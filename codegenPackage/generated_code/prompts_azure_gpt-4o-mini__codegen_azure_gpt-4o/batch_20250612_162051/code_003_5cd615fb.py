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
# safety_compliance.py

from typing import List, Dict, Union

class SafetyComplianceMetrics:
    """
    A class to calculate safety compliance metrics for construction sites.
    """

    def __init__(self):
        """
        Initializes the SafetyComplianceMetrics class.
        """
        pass

    @staticmethod
    def calculate_compliance_score(violations: int, inspections: int) -> float:
        """
        Calculate the compliance score based on the number of violations and inspections.

        Args:
            violations (int): The number of safety violations recorded.
            inspections (int): The number of safety inspections conducted.

        Returns:
            float: The compliance score as a percentage (0.0 to 100.0).

        Raises:
            ValueError: If inspections is zero or negative.
        """
        if inspections <= 0:
            raise ValueError("Number of inspections must be greater than zero.")
        
        # Compliance score is inversely proportional to violations
        compliance_score = max(0.0, 100.0 - (violations / inspections) * 100.0)
        return round(compliance_score, 2)

    @staticmethod
    def generate_report(sites_data: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, float]]]:
        """
        Generate a safety compliance report for multiple construction sites.

        Args:
            sites_data (List[Dict[str, Union[str, int]]]): A list of dictionaries containing site data.
                Each dictionary should have the following keys:
                - 'site_name' (str): The name of the construction site.
                - 'violations' (int): The number of safety violations recorded.
                - 'inspections' (int): The number of safety inspections conducted.

        Returns:
            List[Dict[str, Union[str, float]]]: A list of dictionaries containing the compliance report.
                Each dictionary will have the following keys:
                - 'site_name' (str): The name of the construction site.
                - 'compliance_score' (float): The compliance score as a percentage.
        """
        report = []

        for site in sites_data:
            try:
                site_name = site.get('site_name', 'Unknown Site')
                violations = site.get('violations', 0)
                inspections = site.get('inspections', 0)

                # Calculate compliance score
                compliance_score = SafetyComplianceMetrics.calculate_compliance_score(violations, inspections)

                # Append the result to the report
                report.append({
                    'site_name': site_name,
                    'compliance_score': compliance_score
                })
            except ValueError as e:
                # Handle errors gracefully and log them
                report.append({
                    'site_name': site.get('site_name', 'Unknown Site'),
                    'compliance_score': f"Error: {str(e)}"
                })

        return report


# Example usage (if this script is run directly)
if __name__ == "__main__":
    # Sample data for construction sites
    sites = [
        {'site_name': 'Site A', 'violations': 5, 'inspections': 50},
        {'site_name': 'Site B', 'violations': 0, 'inspections': 20},
        {'site_name': 'Site C', 'violations': 10, 'inspections': 0},  # This will trigger an error
    ]

    # Generate the compliance report
    metrics = SafetyComplianceMetrics()
    compliance_report = metrics.generate_report(sites)

    # Print the report
    for site_report in compliance_report:
        print(site_report)
```
