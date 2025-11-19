"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Write a code snippet that implements a strategic planning tool for organizations, focusing on identifying and monitoring key performance indicators as described by Matter's approach to strategic planning.
Generated: DETERMINISTIC_4695117e5720ae93
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# strategic_planning_tool.py

class StrategicPlanningTool:
    """
    A tool for organizations to identify and monitor key performance indicators (KPIs) 
    based on Matter's approach to strategic planning.
    """

    def __init__(self):
        """
        Initialize the strategic planning tool with an empty dictionary to store KPIs.
        """
        self.kpis = {}

    def add_kpi(self, name, target_value, current_value=0):
        """
        Add a new KPI to the strategic planning tool.

        Args:
            name (str): The name of the KPI.
            target_value (float): The target value of the KPI.
            current_value (float, optional): The current value of the KPI. Defaults to 0.
        """
        if name in self.kpis:
            raise ValueError(f"KPI '{name}' already exists.")

        self.kpis[name] = {
            "target_value": target_value,
            "current_value": current_value
        }

    def update_kpi(self, name, current_value):
        """
        Update the current value of an existing KPI.

        Args:
            name (str): The name of the KPI.
            current_value (float): The new current value of the KPI.

        Raises:
            ValueError: If the KPI does not exist.
        """
        if name not in self.kpis:
            raise ValueError(f"KPI '{name}' does not exist.")

        self.kpis[name]["current_value"] = current_value

    def delete_kpi(self, name):
        """
        Delete a KPI from the strategic planning tool.

        Args:
            name (str): The name of the KPI.

        Raises:
            ValueError: If the KPI does not exist.
        """
        if name not in self.kpis:
            raise ValueError(f"KPI '{name}' does not exist.")

        del self.kpis[name]

    def get_kpi_progress(self, name):
        """
        Calculate the progress of a KPI as a percentage.

        Args:
            name (str): The name of the KPI.

        Returns:
            float: The progress of the KPI as a percentage.

        Raises:
            ValueError: If the KPI does not exist.
        """
        if name not in self.kpis:
            raise ValueError(f"KPI '{name}' does not exist.")

        kpi = self.kpis[name]
        progress = (kpi["current_value"] / kpi["target_value"]) * 100
        return progress

    def get_all_kpis(self):
        """
        Retrieve all KPIs and their progress.

        Returns:
            dict: A dictionary of KPIs with their progress.
        """
        kpis_progress = {}
        for name, kpi in self.kpis.items():
            progress = (kpi["current_value"] / kpi["target_value"]) * 100 if kpi["target_value"] != 0 else 0
            kpis_progress[name] = {
                "target_value": kpi["target_value"],
                "current_value": kpi["current_value"],
                "progress": progress
            }
        return kpis_progress


def main():
    try:
        tool = StrategicPlanningTool()

        # Add KPIs
        tool.add_kpi("Revenue Growth", 1000000)
        tool.add_kpi("Customer Acquisition", 1000)

        # Update KPI values
        tool.update_kpi("Revenue Growth", 500000)
        tool.update_kpi("Customer Acquisition", 500)

        # Get KPI progress
        print("Revenue Growth Progress:", tool.get_kpi_progress("Revenue Growth"), "%")
        print("Customer Acquisition Progress:", tool.get_kpi_progress("Customer Acquisition"), "%")

        # Get all KPIs
        kpis = tool.get_all_kpis()
        for name, kpi in kpis.items():
            print(f"KPI: {name}")
            print(f"Target Value: {kpi['target_value']}")
            print(f"Current Value: {kpi['current_value']}")
            print(f"Progress: {kpi['progress']}%")
            print("--------------------")

    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
```
