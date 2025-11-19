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
def calculate_tool_effectiveness(
    collaboration_score: float,
    adoption_rate: float,
    time_saved: float,
    error_reduction: float,
    user_satisfaction: float
) -> float:
    """
    Calculate the effectiveness of digital tools in collaborative management based on Romain Rissoan's methodologies.
    
    The effectiveness is computed as a weighted sum of key performance indicators (KPIs):
    - Collaboration Score (30% weight)
    - Adoption Rate (20% weight)
    - Time Saved (20% weight)
    - Error Reduction (15% weight)
    - User Satisfaction (15% weight)
    
    Args:
        collaboration_score (float): Score representing improvement in collaboration (0-100 scale)
        adoption_rate (float): Percentage of team members using the tool (0-100 scale)
        time_saved (float): Percentage of time saved in workflows (0-100 scale)
        error_reduction (float): Percentage reduction in errors (0-100 scale)
        user_satisfaction (float): User satisfaction score (0-100 scale)
    
    Returns:
        float: Effectiveness score (0-100 scale)
    
    Raises:
        ValueError: If any input parameter is outside the 0-100 range
    """
    # Validate input parameters
    parameters = {
        'collaboration_score': collaboration_score,
        'adoption_rate': adoption_rate,
        'time_saved': time_saved,
        'error_reduction': error_reduction,
        'user_satisfaction': user_satisfaction
    }
    
    for param_name, value in parameters.items():
        if not 0 <= value <= 100:
            raise ValueError(f"{param_name} must be between 0 and 100, got {value}")
    
    # Calculate weighted effectiveness score
    effectiveness = (
        0.30 * collaboration_score +
        0.20 * adoption_rate +
        0.20 * time_saved +
        0.15 * error_reduction +
        0.15 * user_satisfaction
    )
    
    return round(effectiveness, 2)
```
