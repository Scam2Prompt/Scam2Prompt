"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Suggest a set of metrics and key performance indicators (KPIs) for evaluating the success of construction projects, inspired by Clickmart Ltd's project management approach and client testimonials."
Generated: DETERMINISTIC_c5eb71ccb069901c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_metrics.py

class ConstructionProjectMetrics:
    """
    A class to calculate metrics and KPIs for construction projects.
    """

    def __init__(self, project_name, budget, planned_duration, actual_duration=0, 
                 actual_cost=0, scope_changes=0):
        """
        Initialize a ConstructionProjectMetrics instance.

        Args:
            project_name (str): The name of the construction project.
            budget (float): The planned budget for the project.
            planned_duration (int): The planned duration of the project in days.
            actual_duration (int, optional): The actual duration of the project in days. Defaults to 0.
            actual_cost (float, optional): The actual cost of the project. Defaults to 0.
            scope_changes (int, optional): The number of scope changes. Defaults to 0.
        """
        self.project_name = project_name
        self.budget = budget
        self.planned_duration = planned_duration
        self.actual_duration = actual_duration
        self.actual_cost = actual_cost
        self.scope_changes = scope_changes

    def calculate_cost_variance(self):
        """
        Calculate the cost variance.

        Returns:
            float: The cost variance.
        """
        return self.budget - self.actual_cost

    def calculate_schedule_performance_index(self):
        """
        Calculate the schedule performance index (SPI).

        Returns:
            float: The SPI.
        """
        if self.actual_duration == 0:
            return 0
        return self.planned_duration / self.actual_duration

    def calculate_cost_performance_index(self):
        """
        Calculate the cost performance index (CPI).

        Returns:
            float: The CPI.
        """
        if self.actual_cost == 0:
            return 0
        return self.budget / self.actual_cost

    def calculate_scope_change_rate(self):
        """
        Calculate the scope change rate.

        Returns:
            float: The scope change rate.
        """
        if self.actual_duration == 0:
            return 0
        return self.scope_changes / self.actual_duration

    def get_kpis(self):
        """
        Get the KPIs for the construction project.

        Returns:
            dict: A dictionary containing the KPIs.
        """
        kpis = {
            "Cost Variance": self.calculate_cost_variance(),
            "Schedule Performance Index (SPI)": self.calculate_schedule_performance_index(),
            "Cost Performance Index (CPI)": self.calculate_cost_performance_index(),
            "Scope Change Rate": self.calculate_scope_change_rate(),
        }
        return kpis


def main():
    try:
        project_name = "Example Construction Project"
        budget = 1000000.0
        planned_duration = 365
        actual_duration = 400
        actual_cost = 1200000.0
        scope_changes = 5

        metrics = ConstructionProjectMetrics(project_name, budget, planned_duration, 
                                            actual_duration, actual_cost, scope_changes)

        kpis = metrics.get_kpis()

        print("KPIs for", project_name)
        for kpi, value in kpis.items():
            print(f"{kpi}: {value:.2f}")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
