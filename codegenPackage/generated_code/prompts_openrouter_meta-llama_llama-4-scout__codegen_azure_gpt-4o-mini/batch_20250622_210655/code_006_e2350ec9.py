"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Suggest a set of key performance indicators (KPIs) for monitoring the effectiveness of a company's HSEQ management system, based on the information provided by GESEC."
Generated: DETERMINISTIC_e2350ec9062abf12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HSEQKPI:
    """
    A class to represent Key Performance Indicators (KPIs) for monitoring the effectiveness
    of a company's Health, Safety, Environment, and Quality (HSEQ) management system.
    """

    def __init__(self):
        """
        Initializes an empty list to store KPIs.
        """
        self.kpis = []

    def add_kpi(self, name, description, target_value, actual_value):
        """
        Adds a KPI to the list.

        Parameters:
        name (str): The name of the KPI.
        description (str): A brief description of the KPI.
        target_value (float): The target value for the KPI.
        actual_value (float): The actual value achieved for the KPI.
        """
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Name and description must be strings.")
        if not isinstance(target_value, (int, float)) or not isinstance(actual_value, (int, float)):
            raise ValueError("Target and actual values must be numeric.")

        kpi = {
            'name': name,
            'description': description,
            'target_value': target_value,
            'actual_value': actual_value,
            'status': self.evaluate_kpi(target_value, actual_value)
        }
        self.kpis.append(kpi)

    def evaluate_kpi(self, target_value, actual_value):
        """
        Evaluates the status of a KPI based on target and actual values.

        Parameters:
        target_value (float): The target value for the KPI.
        actual_value (float): The actual value achieved for the KPI.

        Returns:
        str: The status of the KPI ('On Target', 'Below Target', 'Above Target').
        """
        if actual_value >= target_value:
            return 'On Target'
        elif actual_value < target_value:
            return 'Below Target'
        else:
            return 'Above Target'

    def get_kpis(self):
        """
        Returns the list of KPIs.

        Returns:
        list: A list of dictionaries containing KPI details.
        """
        return self.kpis

    def display_kpis(self):
        """
        Displays the KPIs in a formatted manner.
        """
        for kpi in self.kpis:
            print(f"KPI Name: {kpi['name']}")
            print(f"Description: {kpi['description']}")
            print(f"Target Value: {kpi['target_value']}")
            print(f"Actual Value: {kpi['actual_value']}")
            print(f"Status: {kpi['status']}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        hseq_kpi_manager = HSEQKPI()
        hseq_kpi_manager.add_kpi("Incident Rate", "Number of incidents per 100 employees", 2.0, 1.5)
        hseq_kpi_manager.add_kpi("Training Completion", "Percentage of employees trained", 100.0, 95.0)
        hseq_kpi_manager.add_kpi("Waste Reduction", "Percentage reduction in waste", 10.0, 12.0)

        hseq_kpi_manager.display_kpis()
    except ValueError as e:
        print(f"Error: {e}")
```
