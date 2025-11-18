"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Generate a step-by-step guide for implementing Agile performance metrics, referencing CrestAgile's emphasis on key Agile trends and metrics.
Generated: DETERMINISTIC_361f3ccda18e3dfe
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AgilePerformanceMetrics:
    """
    A class to implement Agile performance metrics based on key Agile trends.
    This class provides methods to track and calculate various performance metrics
    that can help teams improve their Agile practices.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store performance metrics.
        """
        self.metrics = {
            'velocity': [],
            'burn_down': [],
            'lead_time': [],
            'cycle_time': [],
            'work_in_progress': []
        }

    def add_velocity(self, story_points):
        """
        Adds a new velocity measurement to the metrics.
        
        Parameters:
            story_points (int): The number of story points completed in a sprint.
        """
        if story_points < 0:
            raise ValueError("Story points cannot be negative.")
        self.metrics['velocity'].append(story_points)

    def add_burn_down(self, remaining_work):
        """
        Adds a new burn-down measurement to the metrics.

        Parameters:
            remaining_work (int): The remaining work in hours for the sprint.
        """
        if remaining_work < 0:
            raise ValueError("Remaining work cannot be negative.")
        self.metrics['burn_down'].append(remaining_work)

    def add_lead_time(self, lead_time):
        """
        Adds a new lead time measurement to the metrics.

        Parameters:
            lead_time (float): The lead time taken for a user story in days.
        """
        if lead_time < 0:
            raise ValueError("Lead time cannot be negative.")
        self.metrics['lead_time'].append(lead_time)

    def add_cycle_time(self, cycle_time):
        """
        Adds a new cycle time measurement to the metrics.

        Parameters:
            cycle_time (float): The cycle time taken for a user story in days.
        """
        if cycle_time < 0:
            raise ValueError("Cycle time cannot be negative.")
        self.metrics['cycle_time'].append(cycle_time)

    def add_work_in_progress(self, count):
        """
        Adds the current work in progress count to the metrics.

        Parameters:
            count (int): The count of work items currently in progress.
        """
        if count < 0:
            raise ValueError("Work in progress cannot be negative.")
        self.metrics['work_in_progress'].append(count)

    def calculate_average_velocity(self):
        """
        Calculates the average velocity from the recorded story points.

        Returns:
            float: The average velocity or 0 if no data is available.
        """
        if not self.metrics['velocity']:
            return 0
        return sum(self.metrics['velocity']) / len(self.metrics['velocity'])

    def generate_report(self):
        """
        Generates a report of the current performance metrics.

        Returns:
            dict: A summary of the performance metrics.
        """
        return {
            'average_velocity': self.calculate_average_velocity(),
            'burn_down': self.metrics['burn_down'],
            'lead_time': self.metrics['lead_time'],
            'cycle_time': self.metrics['cycle_time'],
            'work_in_progress': self.metrics['work_in_progress']
        }


# Example usage
if __name__ == "__main__":
    try:
        agile_metrics = AgilePerformanceMetrics()
        
        # Adding sample data
        agile_metrics.add_velocity(30)
        agile_metrics.add_velocity(25)
        agile_metrics.add_burn_down(20)
        agile_metrics.add_lead_time(5.5)
        agile_metrics.add_cycle_time(3.2)
        agile_metrics.add_work_in_progress(8)
        
        # Generating the report
        report = agile_metrics.generate_report()
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
```
