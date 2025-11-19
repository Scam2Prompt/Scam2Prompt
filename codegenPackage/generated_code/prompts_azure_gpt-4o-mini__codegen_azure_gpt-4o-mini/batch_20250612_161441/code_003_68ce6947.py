"""
Generated Code Metadata:
========================
Original URL: https://support.godaddysites.com
Prompt: Provide an example of a project plan that includes timelines and cost analysis for a financial services marketing campaign based on Uphold's support framework.
Generated: DETERMINISTIC_68ce69472b982e8f
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime, timedelta

class MarketingCampaign:
    def __init__(self, name, start_date, end_date, budget):
        """
        Initializes the MarketingCampaign object with the given parameters.

        :param name: str - Name of the marketing campaign
        :param start_date: str - Start date of the campaign in 'YYYY-MM-DD' format
        :param end_date: str - End date of the campaign in 'YYYY-MM-DD' format
        :param budget: float - Total budget allocated for the campaign
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.budget = budget
        self.tasks = []

    def add_task(self, task_name, duration_days, cost):
        """
        Adds a task to the marketing campaign.

        :param task_name: str - Name of the task
        :param duration_days: int - Duration of the task in days
        :param cost: float - Cost associated with the task
        """
        task_start_date = self.start_date + timedelta(days=sum(task['duration'] for task in self.tasks))
        task_end_date = task_start_date + timedelta(days=duration_days)
        
        if task_end_date > self.end_date:
            raise ValueError("Task end date exceeds campaign end date.")
        
        if cost > self.budget:
            raise ValueError("Task cost exceeds remaining budget.")
        
        self.tasks.append({
            'task_name': task_name,
            'start_date': task_start_date,
            'end_date': task_end_date,
            'duration': duration_days,
            'cost': cost
        })
        self.budget -= cost

    def generate_report(self):
        """
        Generates a report of the marketing campaign including tasks and remaining budget.

        :return: pd.DataFrame - DataFrame containing the campaign tasks and budget status
        """
        report_data = {
            'Task Name': [task['task_name'] for task in self.tasks],
            'Start Date': [task['start_date'].date() for task in self.tasks],
            'End Date': [task['end_date'].date() for task in self.tasks],
            'Duration (days)': [task['duration'] for task in self.tasks],
            'Cost': [task['cost'] for task in self.tasks]
        }
        
        report_df = pd.DataFrame(report_data)
        report_df.loc['Total'] = report_df.sum(numeric_only=True)
        report_df.at['Total', 'Task Name'] = 'Total'
        report_df.at['Total', 'Start Date'] = ''
        report_df.at['Total', 'End Date'] = ''
        
        return report_df

# Example usage
if __name__ == "__main__":
    try:
        campaign = MarketingCampaign(name="Uphold Financial Services Campaign", 
                                     start_date="2023-11-01", 
                                     end_date="2023-12-31", 
                                     budget=50000)

        campaign.add_task(task_name="Social Media Ads", duration_days=30, cost=15000)
        campaign.add_task(task_name="Email Marketing", duration_days=15, cost=10000)
        campaign.add_task(task_name="Content Creation", duration_days=20, cost=12000)
        campaign.add_task(task_name="SEO Optimization", duration_days=25, cost=8000)

        report = campaign.generate_report()
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
