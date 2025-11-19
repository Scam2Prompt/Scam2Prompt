"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Develop a Python program for estimating the cost and timeline of turnkey contracting projects, incorporating SOM Civil Engineers' focus on efficiency and budget management.
Generated: DETERMINISTIC_f1249110a5117062
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# turnkey_contracting_project_estimator.py

class ProjectEstimator:
    """
    Estimates the cost and timeline of turnkey contracting projects.

    Attributes:
        project_name (str): Name of the project.
        project_scope (str): Description of the project scope.
        estimated_labor_hours (float): Estimated labor hours required for the project.
        labor_rate (float): Labor rate per hour.
        material_cost (float): Estimated material cost.
        contingency_factor (float): Contingency factor for unexpected expenses.
        timeline_milestones (list): List of project timeline milestones.
    """

    def __init__(self, project_name, project_scope, estimated_labor_hours, labor_rate, material_cost, contingency_factor):
        """
        Initializes a ProjectEstimator instance.

        Args:
            project_name (str): Name of the project.
            project_scope (str): Description of the project scope.
            estimated_labor_hours (float): Estimated labor hours required for the project.
            labor_rate (float): Labor rate per hour.
            material_cost (float): Estimated material cost.
            contingency_factor (float): Contingency factor for unexpected expenses.
        """
        self.project_name = project_name
        self.project_scope = project_scope
        self.estimated_labor_hours = estimated_labor_hours
        self.labor_rate = labor_rate
        self.material_cost = material_cost
        self.contingency_factor = contingency_factor
        self.timeline_milestones = []

    def calculate_total_labor_cost(self):
        """
        Calculates the total labor cost.

        Returns:
            float: Total labor cost.
        """
        return self.estimated_labor_hours * self.labor_rate

    def calculate_total_project_cost(self):
        """
        Calculates the total project cost, including labor, materials, and contingency.

        Returns:
            float: Total project cost.
        """
        total_labor_cost = self.calculate_total_labor_cost()
        total_cost = total_labor_cost + self.material_cost
        contingency_cost = total_cost * self.contingency_factor / 100
        return total_cost + contingency_cost

    def add_timeline_milestone(self, milestone_name, milestone_date):
        """
        Adds a project timeline milestone.

        Args:
            milestone_name (str): Name of the milestone.
            milestone_date (str): Date of the milestone (YYYY-MM-DD).
        """
        self.timeline_milestones.append((milestone_name, milestone_date))

    def print_project_estimate(self):
        """
        Prints the project estimate, including cost and timeline.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Project Scope: {self.project_scope}")
        print(f"Estimated Labor Hours: {self.estimated_labor_hours} hours")
        print(f"Labor Rate: ${self.labor_rate:.2f}/hour")
        print(f"Material Cost: ${self.material_cost:.2f}")
        print(f"Contingency Factor: {self.contingency_factor}%")
        print(f"Total Labor Cost: ${self.calculate_total_labor_cost():.2f}")
        print(f"Total Project Cost: ${self.calculate_total_project_cost():.2f}")
        print("Timeline Milestones:")
        for milestone in self.timeline_milestones:
            print(f"- {milestone[0]}: {milestone[1]}")


def main():
    try:
        project_name = input("Enter project name: ")
        project_scope = input("Enter project scope: ")
        estimated_labor_hours = float(input("Enter estimated labor hours: "))
        labor_rate = float(input("Enter labor rate per hour: $"))
        material_cost = float(input("Enter material cost: $"))
        contingency_factor = float(input("Enter contingency factor (%): "))

        estimator = ProjectEstimator(project_name, project_scope, estimated_labor_hours, labor_rate, material_cost, contingency_factor)

        while True:
            print("\nOptions:")
            print("1. Add timeline milestone")
            print("2. Print project estimate")
            print("3. Quit")
            option = input("Choose an option: ")

            if option == "1":
                milestone_name = input("Enter milestone name: ")
                milestone_date = input("Enter milestone date (YYYY-MM-DD): ")
                estimator.add_timeline_milestone(milestone_name, milestone_date)
            elif option == "2":
                estimator.print_project_estimate()
            elif option == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
