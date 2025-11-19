"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate a step-by-step guide for implementing Agile performance metrics, referencing CrestAgile's emphasis on key Agile trends and metrics.
Generated: DETERMINISTIC_361f3ccda18e3dfe
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AgilePerformanceMetrics:
    """
    A class to implement Agile performance metrics based on key Agile trends.
    This class provides methods to track and analyze various Agile metrics.
    """

    def __init__(self):
        """
        Initializes the AgilePerformanceMetrics class with default metrics.
        """
        self.metrics = {
            'velocity': [],
            'burn_down': [],
            'cycle_time': [],
            'lead_time': [],
            'team_happiness': []
        }

    def add_velocity(self, story_points):
        """
        Adds a new velocity measurement.

        :param story_points: The number of story points completed in a sprint.
        :raises ValueError: If story_points is not a positive integer.
        """
        if not isinstance(story_points, int) or story_points < 0:
            raise ValueError("Story points must be a positive integer.")
        self.metrics['velocity'].append(story_points)

    def add_burn_down(self, remaining_work):
        """
        Adds a new burn down measurement.

        :param remaining_work: The amount of work remaining at the end of the sprint.
        :raises ValueError: If remaining_work is not a non-negative integer.
        """
        if not isinstance(remaining_work, int) or remaining_work < 0:
            raise ValueError("Remaining work must be a non-negative integer.")
        self.metrics['burn_down'].append(remaining_work)

    def add_cycle_time(self, time_taken):
        """
        Adds a new cycle time measurement.

        :param time_taken: The time taken to complete a task in days.
        :raises ValueError: If time_taken is not a positive integer.
        """
        if not isinstance(time_taken, int) or time_taken < 0:
            raise ValueError("Time taken must be a positive integer.")
        self.metrics['cycle_time'].append(time_taken)

    def add_lead_time(self, time_taken):
        """
        Adds a new lead time measurement.

        :param time_taken: The time taken from request to delivery in days.
        :raises ValueError: If time_taken is not a positive integer.
        """
        if not isinstance(time_taken, int) or time_taken < 0:
            raise ValueError("Time taken must be a positive integer.")
        self.metrics['lead_time'].append(time_taken)

    def add_team_happiness(self, score):
        """
        Adds a new team happiness score.

        :param score: The happiness score of the team (0-10).
        :raises ValueError: If score is not between 0 and 10.
        """
        if not (0 <= score <= 10):
            raise ValueError("Happiness score must be between 0 and 10.")
        self.metrics['team_happiness'].append(score)

    def calculate_average(self, metric):
        """
        Calculates the average of a given metric.

        :param metric: The metric to calculate the average for.
        :return: The average value of the metric or None if no data is available.
        """
        if metric not in self.metrics or not self.metrics[metric]:
            return None
        return sum(self.metrics[metric]) / len(self.metrics[metric])

    def display_metrics(self):
        """
        Displays the current metrics in a readable format.
        """
        for metric, values in self.metrics.items():
            average = self.calculate_average(metric)
            print(f"{metric.capitalize()}: {values} | Average: {average:.2f}" if average is not None else f"{metric.capitalize()}: {values} | Average: N/A")


# Example usage
if __name__ == "__main__":
    agile_metrics = AgilePerformanceMetrics()

    try:
        agile_metrics.add_velocity(30)
        agile_metrics.add_burn_down(5)
        agile_metrics.add_cycle_time(2)
        agile_metrics.add_lead_time(3)
        agile_metrics.add_team_happiness(8)

        agile_metrics.display_metrics()
    except ValueError as e:
        print(f"Error: {e}")
```
