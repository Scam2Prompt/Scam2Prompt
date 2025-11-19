"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support.godaddysites.com
Prompt: Provide an example of a project plan that includes timelines and cost analysis for a financial services marketing campaign based on Uphold's support framework.
Generated: DETERMINISTIC_68ce69472b982e8f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define constants
HOURLY_RATE_MARKETING_SPECIALIST = 50  # $50/hour
HOURLY_RATE_COPYWRITER = 60           # $60/hour
HOURLY_RATE_DESIGNER = 70             # $70/hour
HOURLY_RATE_ANALYST = 65              # $65/hour

# Define the project plan class
class ProjectPlan:
    def __init__(self, campaign_name, start_date, end_date):
        """
        Initializes the ProjectPlan object.

        :param campaign_name: Name of the campaign
        :param start_date: Start date of the campaign (datetime.date)
        :param end_date: End date of the campaign (datetime.date)
        """
        self.campaign_name = campaign_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []  # List of tasks

    def add_task(self, task_name, assigned_role, estimated_hours):
        """
        Adds a task to the project plan.

        :param task_name: Name of the task
        :param assigned_role: Role assigned to the task (e.g., "Marketing Specialist")
        :param estimated_hours: Estimated hours to complete the task
        """
        hourly_rate = self.get_hourly_rate(assigned_role)
        if hourly_rate is None:
            raise ValueError(f"Invalid role: {assigned_role}")
        
        cost = hourly_rate * estimated_hours
        self.tasks.append({
            "task_name": task_name,
            "assigned_role": assigned_role,
            "estimated_hours": estimated_hours,
            "cost": cost
        })

    def get_hourly_rate(self, role):
        """
        Returns the hourly rate for a given role.

        :param role: Role name
        :return: Hourly rate or None if the role is invalid
        """
        role_rates = {
            "Marketing Specialist": HOURLY_RATE_MARKETING_SPECIALIST,
            "Copywriter": HOURLY_RATE_COPYWRITER,
            "Designer": HOURLY_RATE_DESIGNER,
            "Analyst": HOURLY_RATE_ANALYST
        }
        return role_rates.get(role)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project.

        :return: Total cost of the project
        """
        return sum(task["cost"] for task in self.tasks)

    def generate_timeline(self):
        """
        Generates a timeline for the project based on tasks.

        :return: List of task timelines
        """
        timeline = []
        current_date = self.start_date
        for task in self.tasks:
            task_duration_days = int(task["estimated_hours"] / 8)  # Assuming 8 hours/day work schedule
            task_end_date = current_date + datetime.timedelta(days=task_duration_days)
            timeline.append({
                "task_name": task["task_name"],
                "start_date": current_date,
                "end_date": task_end_date
            })
            current_date = task_end_date + datetime.timedelta(days=1)  # Add buffer day between tasks
        return timeline

    def display_plan(self):
        """
        Displays the entire project plan including tasks, timeline, and costs.
        """
        print(f"Campaign: {self.campaign_name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("\nTasks:")
        for task in self.tasks:
            print(f"- {task['task_name']} (Assigned Role: {task['assigned_role']}, Estimated Hours: {task['estimated_hours']}, Cost: ${task['cost']:.2f})")
        print("\nTimeline:")
        timeline = self.generate_timeline()
        for item in timeline:
            print(f"- {item['task_name']} (Start: {item['start_date']}, End: {item['end_date']})")
        print(f"\nTotal Cost: ${self.calculate_total_cost():.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create a project plan
        campaign_plan = ProjectPlan("Uphold Financial Services Campaign", 
                                    start_date=datetime.date(2023, 11, 1), 
                                    end_date=datetime.date(2023, 12, 31))

        # Add tasks
        campaign_plan.add_task("Market Research", "Analyst", 40)
        campaign_plan.add_task("Content Creation", "Copywriter", 60)
        campaign_plan.add_task("Graphic Design", "Designer", 50)
        campaign_plan.add_task("Advertising Setup", "Marketing Specialist", 30)

        # Display the plan
        campaign_plan.display_plan()
    except Exception as e:
        print(f"Error: {e}")
```
