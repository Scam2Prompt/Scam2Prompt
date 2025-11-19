"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Write a function to calculate the effectiveness of digital tools in collaborative management, referencing Romain Rissoan's methodologies.
Generated: DETERMINISTIC_5a86dee317ad844b
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Tool Effectiveness Calculator
=====================================

This module provides a function to calculate the effectiveness of digital tools 
in collaborative management based on Romain Rissoan's methodologies.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_effectiveness(tool_usage, team_engagement, task_completion):
    """
    Calculate the effectiveness of digital tools in collaborative management.

    Args:
        tool_usage (float): The percentage of team members using the digital tool.
        team_engagement (float): The average engagement score of team members.
        task_completion (float): The percentage of tasks completed on time.

    Returns:
        float: The effectiveness score of the digital tool.

    Raises:
        ValueError: If any input value is not within the range [0, 100].
    """
    # Validate input values
    if not (0 <= tool_usage <= 100 and 0 <= team_engagement <= 100 and 0 <= task_completion <= 100):
        raise ValueError("Input values must be within the range [0, 100]")

    # Calculate effectiveness score based on Romain Rissoan's methodologies
    # Assuming the weights for each factor are 30%, 40%, and 30% respectively
    effectiveness_score = (0.3 * tool_usage) + (0.4 * team_engagement) + (0.3 * task_completion)

    return effectiveness_score


def get_digital_tool_effectiveness_report(tool_usage, team_engagement, task_completion):
    """
    Generate a report on the effectiveness of digital tools in collaborative management.

    Args:
        tool_usage (float): The percentage of team members using the digital tool.
        team_engagement (float): The average engagement score of team members.
        task_completion (float): The percentage of tasks completed on time.

    Returns:
        dict: A dictionary containing the effectiveness score and recommendations.
    """
    try:
        effectiveness_score = calculate_effectiveness(tool_usage, team_engagement, task_completion)

        # Generate recommendations based on the effectiveness score
        if effectiveness_score < 60:
            recommendation = "Improve tool usage and team engagement to increase effectiveness."
        elif effectiveness_score < 80:
            recommendation = "Focus on increasing task completion rates to further improve effectiveness."
        else:
            recommendation = "The digital tool is highly effective. Continue to monitor and optimize usage."

        report = {
            "effectiveness_score": effectiveness_score,
            "recommendation": recommendation
        }

        return report

    except ValueError as e:
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    tool_usage = 80  # 80% of team members use the digital tool
    team_engagement = 85  # Average engagement score of 85
    task_completion = 90  # 90% of tasks completed on time

    report = get_digital_tool_effectiveness_report(tool_usage, team_engagement, task_completion)
    print(report)
```
