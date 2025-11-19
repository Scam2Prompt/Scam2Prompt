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
"""
Strategic Planning Tool for Organizations
This script implements a tool to identify and monitor Key Performance Indicators (KPIs) 
based on Matter's approach to strategic planning. It allows organizations to define goals, 
set KPIs, track progress, and generate reports.
"""

import json
import datetime


class StrategicPlanningTool:
    def __init__(self):
        """
        Initialize the strategic planning tool with an empty list of goals and KPIs.
        """
        self.goals = []  # List to store organizational goals
        self.kpis = []   # List to store KPIs

    def add_goal(self, name, description):
        """
        Add a new goal to the system.

        :param name: Name of the goal
        :param description: Description of the goal
        """
        goal = {
            "id": len(self.goals) + 1,
            "name": name,
            "description": description,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.goals.append(goal)
        print(f"Goal '{name}' added successfully.")

    def add_kpi(self, name, description, target_value, goal_id):
        """
        Add a new KPI to the system.

        :param name: Name of the KPI
        :param description: Description of the KPI
        :param target_value: Target value for the KPI
        :param goal_id: ID of the associated goal
        """
        # Validate goal ID
        if not any(goal["id"] == goal_id for goal in self.goals):
            print(f"Error: Goal ID {goal_id} does not exist.")
            return

        kpi = {
            "id": len(self.kpis) + 1,
            "name": name,
            "description": description,
            "target_value": target_value,
            "current_value": 0,  # Default initial value
            "goal_id": goal_id,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.kpis.append(kpi)
        print(f"KPI '{name}' added successfully.")

    def update_kpi(self, kpi_id, current_value):
        """
        Update the current value of a KPI.

        :param kpi_id: ID of the KPI to update
        :param current_value: New current value for the KPI
        """
        # Find the KPI by ID
        kpi = next((kpi for kpi in self.kpis if kpi["id"] == kpi_id), None)
        if not kpi:
            print(f"Error: KPI ID {kpi_id} does not exist.")
            return

        kpi["current_value"] = current_value
        print(f"KPI '{kpi['name']}' updated successfully.")

    def generate_report(self):
        """
        Generate a report of all goals and their associated KPIs.

        :return: JSON-formatted report
        """
        report = {"goals": []}
        for goal in self.goals:
            goal_kpis = [kpi for kpi in self.kpis if kpi["goal_id"] == goal["id"]]
            report["goals"].append({
                "goal": goal,
                "kpis": goal_kpis
            })
        return json.dumps(report, indent=4)

    def display_report(self):
        """
        Display the generated report in a readable format.
        """
        report = self.generate_report()
        print("Strategic Planning Report:")
        print(report)


# Example usage
if __name__ == "__main__":
    # Initialize the tool
    tool = StrategicPlanningTool()

    # Add goals
    tool.add_goal("Increase Revenue", "Focus on increasing revenue by 20% this year.")
    tool.add_goal("Improve Customer Satisfaction", "Enhance customer experience and satisfaction.")

    # Add KPIs
    tool.add_kpi("Monthly Revenue", "Track monthly revenue growth.", 100000, goal_id=1)
    tool.add_kpi("Customer Satisfaction Score", "Measure customer satisfaction on a scale of 1-10.", 9, goal_id=2)

    # Update KPI values
    tool.update_kpi(kpi_id=1, current_value=75000)
    tool.update_kpi(kpi_id=2, current_value=8)

    # Display the report
    tool.display_report()
```
