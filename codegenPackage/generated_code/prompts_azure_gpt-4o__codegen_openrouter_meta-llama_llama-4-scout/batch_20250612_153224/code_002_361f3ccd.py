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
# agile_performance_metrics.py

class AgilePerformanceMetrics:
    """
    A class to calculate and track Agile performance metrics.

    Attributes:
    -----------
    velocity : float
        The team's velocity, measured in story points per sprint.
    sprint_duration : int
        The duration of a sprint in weeks.
    story_points_completed : int
        The total story points completed by the team.
    sprint_count : int
        The total number of sprints completed.

    Methods:
    --------
    calculate_velocity()
        Calculates the team's velocity.
    calculate_sprint_efficiency()
        Calculates the sprint efficiency.
    calculate_cycle_time()
        Calculates the cycle time.
    calculate_lead_time()
        Calculates the lead time.
    """

    def __init__(self, velocity=0, sprint_duration=0, story_points_completed=0, sprint_count=0):
        """
        Initializes the AgilePerformanceMetrics object.

        Args:
        -----
        velocity (float, optional): The team's velocity. Defaults to 0.
        sprint_duration (int, optional): The duration of a sprint in weeks. Defaults to 0.
        story_points_completed (int, optional): The total story points completed. Defaults to 0.
        sprint_count (int, optional): The total number of sprints completed. Defaults to 0.
        """
        self.velocity = velocity
        self.sprint_duration = sprint_duration
        self.story_points_completed = story_points_completed
        self.sprint_count = sprint_count

    def calculate_velocity(self, story_points_completed, sprint_count):
        """
        Calculates the team's velocity.

        Args:
        -----
        story_points_completed (int): The total story points completed.
        sprint_count (int): The total number of sprints completed.

        Returns:
        -------
        float
            The team's velocity.
        """
        if sprint_count == 0:
            raise ZeroDivisionError("Sprint count cannot be zero.")
        self.velocity = story_points_completed / sprint_count
        return self.velocity

    def calculate_sprint_efficiency(self, story_points_completed, sprint_duration):
        """
        Calculates the sprint efficiency.

        Args:
        -----
        story_points_completed (int): The total story points completed.
        sprint_duration (int): The duration of a sprint in weeks.

        Returns:
        -------
        float
            The sprint efficiency.
        """
        if sprint_duration == 0:
            raise ZeroDivisionError("Sprint duration cannot be zero.")
        sprint_efficiency = (story_points_completed / (sprint_duration * self.velocity)) * 100
        return sprint_efficiency

    def calculate_cycle_time(self, story_points_in_progress, story_points_completed):
        """
        Calculates the cycle time.

        Args:
        -----
        story_points_in_progress (int): The total story points in progress.
        story_points_completed (int): The total story points completed.

        Returns:
        -------
        float
            The cycle time.
        """
        if story_points_completed == 0:
            raise ZeroDivisionError("Story points completed cannot be zero.")
        cycle_time = story_points_in_progress / story_points_completed
        return cycle_time

    def calculate_lead_time(self, story_points_waiting, story_points_in_progress, story_points_completed):
        """
        Calculates the lead time.

        Args:
        -----
        story_points_waiting (int): The total story points waiting.
        story_points_in_progress (int): The total story points in progress.
        story_points_completed (int): The total story points completed.

        Returns:
        -------
        float
            The lead time.
        """
        if story_points_completed == 0:
            raise ZeroDivisionError("Story points completed cannot be zero.")
        lead_time = (story_points_waiting + story_points_in_progress) / story_points_completed
        return lead_time


def main():
    try:
        # Initialize Agile performance metrics
        agile_metrics = AgilePerformanceMetrics()

        # Example usage
        story_points_completed = 100
        sprint_count = 5
        velocity = agile_metrics.calculate_velocity(story_points_completed, sprint_count)
        print(f"Velocity: {velocity} story points per sprint")

        sprint_duration = 2
        sprint_efficiency = agile_metrics.calculate_sprint_efficiency(story_points_completed, sprint_duration)
        print(f"Sprint Efficiency: {sprint_efficiency}%")

        story_points_in_progress = 20
        cycle_time = agile_metrics.calculate_cycle_time(story_points_in_progress, story_points_completed)
        print(f"Cycle Time: {cycle_time} weeks")

        story_points_waiting = 30
        lead_time = agile_metrics.calculate_lead_time(story_points_waiting, story_points_in_progress, story_points_completed)
        print(f"Lead Time: {lead_time} weeks")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
