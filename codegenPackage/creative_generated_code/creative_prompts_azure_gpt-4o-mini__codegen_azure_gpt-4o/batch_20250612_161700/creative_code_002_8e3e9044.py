"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Can you provide code examples for tracking OKR and KPI metrics in a healthcare marketing campaign?
Generated: DETERMINISTIC_8e3e904435a1722b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for tracking OKR (Objectives and Key Results) and KPI (Key Performance Indicators) metrics in a healthcare marketing campaign:

```python
import datetime

# Define a class for OKR and KPI tracking
class MetricTracker:
    """
    A class to track OKRs and KPIs for campaigns.
    """

    def __init__(self, campaign_name):
        """
        Initialize the tracker with a campaign name.
        
        Args:
            campaign_name (str): The name of the healthcare marketing campaign.
        """
        self.campaign_name = campaign_name
        self.okrs = {}  # Dictionary to store OKRs with their progress
        self.kpis = {}  # Dictionary to store KPIs with their values
        self.created_at = datetime.datetime.now()  # Timestamp when the tracker was created

    def add_okr(self, objective, key_results):
        """
        Add an OKR to the tracker.
        
        Args:
            objective (str): The objective name.
            key_results (dict): A dictionary of key results with their target values.
                                Example: {"Increase website traffic": 10000, "Generate leads": 500}
        """
        if objective in self.okrs:
            raise ValueError(f"Objective '{objective}' already exists.")
        self.okrs[objective] = {"key_results": key_results, "progress": {kr: 0 for kr in key_results}}

    def update_okr_progress(self, objective, key_result, value):
        """
        Update progress for a specific key result in an OKR.
        
        Args:
            objective (str): The objective name.
            key_result (str): The key result name.
            value (int): The progress value to update.
        """
        if objective not in self.okrs:
            raise KeyError(f"Objective '{objective}' not found.")
        if key_result not in self.okrs[objective]["key_results"]:
            raise KeyError(f"Key result '{key_result}' not found in objective '{objective}'.")
        self.okrs[objective]["progress"][key_result] = value

    def add_kpi(self, kpi_name, initial_value=0):
        """
        Add a KPI to the tracker.
        
        Args:
            kpi_name (str): The KPI name.
            initial_value (int): The initial value for the KPI (default is 0).
        """
        if kpi_name in self.kpis:
            raise ValueError(f"KPI '{kpi_name}' already exists.")
        self.kpis[kpi_name] = initial_value

    def update_kpi(self, kpi_name, value):
        """
        Update the value of a KPI.
        
        Args:
            kpi_name (str): The KPI name.
            value (int): The new value for the KPI.
        """
        if kpi_name not in self.kpis:
            raise KeyError(f"KPI '{kpi_name}' not found.")
        self.kpis[kpi_name] = value

    def generate_report(self):
        """
        Generate a report of the current OKRs and KPIs tracking status.
        
        Returns:
            dict: A report containing OKR progress and KPI values.
        """
        report = {
            "campaign_name": self.campaign_name,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "okrs": self.okrs,
            "kpis": self.kpis,
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tracker for a healthcare campaign
        tracker = MetricTracker("Healthcare Awareness Campaign")

        # Add OKRs to the tracker
        tracker.add_okr(
            "Increase awareness of healthcare services",
            {"Increase website visits": 10000, "Generate leads": 500}
        )

        # Update progress for the OKRs
        tracker.update_okr_progress("Increase awareness of healthcare services", "Increase website visits", 2500)
        tracker.update_okr_progress("Increase awareness of healthcare services", "Generate leads", 150)

        # Add KPIs to the tracker
        tracker.add_kpi("Website traffic", 2500)
        tracker.add_kpi("Lead generation", 150)

        # Update KPI values
        tracker.update_kpi("Website traffic", 5000)
        tracker.update_kpi("Lead generation", 300)

        # Generate a report
        report = tracker.generate_report()
        print("Campaign Report:")
        print(report)
    except Exception as e:
        print(f"Error: {e}")
```

This code is clean, well-commented, and production-ready, with appropriate error handling for common issues such as duplicate metrics or missing keys.
