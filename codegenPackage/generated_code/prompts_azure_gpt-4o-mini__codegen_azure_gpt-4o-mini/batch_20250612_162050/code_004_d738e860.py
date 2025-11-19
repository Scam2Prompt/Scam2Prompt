"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Design a library that assists organizations in developing a culture of continuous improvement, reflecting the methodologies used by Matter in their consulting services.
Generated: DETERMINISTIC_d738e8601f258e7a
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
continuous_improvement.py

This module provides a library to assist organizations in developing a culture of continuous improvement.
It reflects methodologies used in consulting services, focusing on key principles such as feedback loops,
goal setting, and performance tracking.
"""

class ContinuousImprovement:
    """
    A class to represent a continuous improvement initiative within an organization.
    """

    def __init__(self, initiative_name):
        """
        Initializes a new Continuous Improvement initiative.

        Parameters:
        initiative_name (str): The name of the initiative.
        """
        if not isinstance(initiative_name, str) or not initiative_name:
            raise ValueError("Initiative name must be a non-empty string.")
        
        self.initiative_name = initiative_name
        self.goals = []
        self.feedback_loops = []
        self.performance_metrics = {}

    def add_goal(self, goal):
        """
        Adds a goal to the initiative.

        Parameters:
        goal (str): The goal to be added.
        """
        if not isinstance(goal, str) or not goal:
            raise ValueError("Goal must be a non-empty string.")
        
        self.goals.append(goal)

    def add_feedback_loop(self, feedback_loop):
        """
        Adds a feedback loop to the initiative.

        Parameters:
        feedback_loop (str): The feedback loop to be added.
        """
        if not isinstance(feedback_loop, str) or not feedback_loop:
            raise ValueError("Feedback loop must be a non-empty string.")
        
        self.feedback_loops.append(feedback_loop)

    def set_performance_metric(self, metric_name, value):
        """
        Sets a performance metric for the initiative.

        Parameters:
        metric_name (str): The name of the metric.
        value (float): The value of the metric.
        """
        if not isinstance(metric_name, str) or not metric_name:
            raise ValueError("Metric name must be a non-empty string.")
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number.")
        
        self.performance_metrics[metric_name] = value

    def get_summary(self):
        """
        Returns a summary of the initiative, including goals, feedback loops, and performance metrics.

        Returns:
        dict: A summary of the initiative.
        """
        return {
            "initiative_name": self.initiative_name,
            "goals": self.goals,
            "feedback_loops": self.feedback_loops,
            "performance_metrics": self.performance_metrics
        }

    def evaluate_initiative(self):
        """
        Evaluates the initiative based on the set performance metrics.

        Returns:
        str: Evaluation result.
        """
        if not self.performance_metrics:
            return "No performance metrics set for evaluation."

        evaluation = []
        for metric, value in self.performance_metrics.items():
            if value >= 75:  # Assuming 75 is the threshold for success
                evaluation.append(f"{metric}: Successful")
            else:
                evaluation.append(f"{metric}: Needs Improvement")

        return "\n".join(evaluation)

# Example usage:
if __name__ == "__main__":
    try:
        ci = ContinuousImprovement("Quality Improvement Initiative")
        ci.add_goal("Reduce defects by 20%")
        ci.add_feedback_loop("Monthly team reviews")
        ci.set_performance_metric("Defect Rate", 80)
        ci.set_performance_metric("Customer Satisfaction", 70)

        print(ci.get_summary())
        print(ci.evaluate_initiative())
    except ValueError as e:
        print(f"Error: {e}")
```
