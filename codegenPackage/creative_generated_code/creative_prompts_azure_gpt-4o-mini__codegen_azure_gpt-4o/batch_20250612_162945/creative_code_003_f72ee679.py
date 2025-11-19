"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Develop a library function that calculates the sustainability impact of various consultancy projects, in line with Dusanto Consultancy Trading OU's mission to save the planet.
Generated: DETERMINISTIC_f72ee6793c066051
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
sustainability_impact_calculator.py

This module provides a library function to calculate the sustainability impact 
of consultancy projects in alignment with Dusanto Consultancy Trading OU's 
mission to save the planet.

The function evaluates the impact across multiple dimensions such as carbon 
footprint reduction, renewable energy adoption, waste reduction, and resource 
efficiency improvements.

Example usage:
    from sustainability_impact_calculator import calculate_sustainability_impact

    project_data = {
        "carbon_footprint_reduction": 500,    # in metric tons
        "renewable_energy_adoption": 80,     # in percentage
        "waste_reduction": 300,              # in kilograms
        "resource_efficiency_improvement": 0.25  # as a decimal value
    }

    impact_score = calculate_sustainability_impact(project_data)
    print(f"Sustainability Impact Score: {impact_score}")
"""

def calculate_sustainability_impact(project_data):
    """
    Calculate the sustainability impact score for a consultancy project.

    Args:
        project_data (dict): A dictionary containing project metrics:
            - carbon_footprint_reduction (float): Reduction in carbon footprint (metric tons).
            - renewable_energy_adoption (float): Percentage of energy derived from renewable sources (0-100).
            - waste_reduction (float): Reduction in waste (kilograms).
            - resource_efficiency_improvement (float): Improvement in resource efficiency (0-1 scale).

    Returns:
        float: A sustainability impact score, normalized to a scale of 0-100.

    Raises:
        ValueError: If any required metric is missing or invalid.
    """
    # Validate input data
    required_metrics = [
        "carbon_footprint_reduction",
        "renewable_energy_adoption",
        "waste_reduction",
        "resource_efficiency_improvement"
    ]
    for metric in required_metrics:
        if metric not in project_data:
            raise ValueError(f"Missing required metric: {metric}")
        if not isinstance(project_data[metric], (int, float)) or project_data[metric] < 0:
            raise ValueError(f"Invalid value for {metric}: Must be a positive number.")

    # Weight factors for each metric (adjustable based on organizational priorities)
    weights = {
        "carbon_footprint_reduction": 0.4,
        "renewable_energy_adoption": 0.3,
        "waste_reduction": 0.2,
        "resource_efficiency_improvement": 0.1
    }

    # Calculate weighted scores for each metric
    carbon_score = (project_data["carbon_footprint_reduction"] / 1000) * weights["carbon_footprint_reduction"]
    renewable_score = (project_data["renewable_energy_adoption"] / 100) * weights["renewable_energy_adoption"]
    waste_score = (project_data["waste_reduction"] / 1000) * weights["waste_reduction"]
    efficiency_score = project_data["resource_efficiency_improvement"] * weights["resource_efficiency_improvement"]

    # Aggregate the scores to compute the final impact score
    total_score = carbon_score + renewable_score + waste_score + efficiency_score

    # Normalize the score to a scale of 0-100
    normalized_score = min(total_score * 100, 100)

    return round(normalized_score, 2)


# Example usage (for testing purposes)
if __name__ == "__main__":
    sample_project = {
        "carbon_footprint_reduction": 500,    # metric tons
        "renewable_energy_adoption": 80,     # percentage
        "waste_reduction": 300,              # kilograms
        "resource_efficiency_improvement": 0.25  # decimal value
    }

    try:
        score = calculate_sustainability_impact(sample_project)
        print(f"Sustainability Impact Score: {score}")
    except ValueError as e:
        print(f"Error: {e}")
```
