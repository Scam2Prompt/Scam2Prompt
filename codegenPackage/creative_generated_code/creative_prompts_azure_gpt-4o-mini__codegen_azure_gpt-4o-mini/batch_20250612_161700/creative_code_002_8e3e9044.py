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

```python
import pandas as pd
import json
import logging

# Configure logging for tracking purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthcareCampaignMetrics:
    """
    A class to track and manage OKR (Objectives and Key Results) and KPI (Key Performance Indicators)
    for healthcare marketing campaigns.
    """

    def __init__(self):
        self.okrs = []
        self.kpis = pd.DataFrame(columns=["Metric", "Value", "Target", "Status"])

    def add_okr(self, objective: str, key_results: list):
        """
        Add an OKR to the campaign.

        :param objective: A string representing the main objective.
        :param key_results: A list of key results associated with the objective.
        """
        self.okrs.append({"Objective": objective, "Key Results": key_results})
        logging.info(f"Added OKR: {objective}")

    def add_kpi(self, metric: str, value: float, target: float):
        """
        Add a KPI to the campaign.

        :param metric: A string representing the metric name.
        :param value: A float representing the current value of the metric.
        :param target: A float representing the target value for the metric.
        """
        status = "On Track" if value >= target else "Off Track"
        new_kpi = {"Metric": metric, "Value": value, "Target": target, "Status": status}
        self.kpis = self.kpis.append(new_kpi, ignore_index=True)
        logging.info(f"Added KPI: {metric} with value {value} and target {target}")

    def update_kpi(self, metric: str, new_value: float):
        """
        Update an existing KPI value.

        :param metric: A string representing the metric name.
        :param new_value: A float representing the new value for the metric.
        """
        try:
            if metric in self.kpis['Metric'].values:
                target = self.kpis.loc[self.kpis['Metric'] == metric, 'Target'].values[0]
                self.kpis.loc[self.kpis['Metric'] == metric, 'Value'] = new_value
                self.kpis.loc[self.kpis['Metric'] == metric, 'Status'] = "On Track" if new_value >= target else "Off Track"
                logging.info(f"Updated KPI: {metric} to new value {new_value}")
            else:
                raise ValueError(f"Metric '{metric}' not found.")
        except Exception as e:
            logging.error(f"Error updating KPI: {str(e)}")

    def export_metrics(self, filename: str):
        """
        Export the OKR and KPI data to a JSON file.

        :param filename: A string representing the filename for export.
        """
        data = {
            "OKRs": self.okrs,
            "KPIs": self.kpis.to_dict(orient='records')
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Metrics exported successfully to {filename}")
        except IOError as e:
            logging.error(f"Failed to export metrics: {str(e)}")

# Sample usage
if __name__ == "__main__":
    campaign_metrics = HealthcareCampaignMetrics()
    
    # Adding OKRs
    campaign_metrics.add_okr("Increase Patient Engagement", ["Reach 500 new patients", "Improve website visits by 30%"])
    
    # Adding KPIs
    campaign_metrics.add_kpi("New Patients", 400, 500)
    campaign_metrics.add_kpi("Website Visits", 3000, 3900)

    # Updating a KPI
    campaign_metrics.update_kpi("New Patients", 450)

    # Exporting metrics to JSON
    campaign_metrics.export_metrics("healthcare_campaign_metrics.json")
```
