"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-en.web.app
Prompt: Provide an example of how to evaluate AI start-up projects before listing them on InQubeta, using a sample data structure in JSON format.
Generated: DETERMINISTIC_06c502997216c5aa
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def evaluate_ai_startup(project_data):
    """
    Evaluates AI startup projects based on predefined criteria.
    
    Parameters:
        project_data (dict): A dictionary containing project details.
    
    Returns:
        dict: Evaluation results with a score and status.
    """
    try:
        # Define evaluation criteria weights
        criteria_weights = {
            "innovation": 0.4,  # Weight for innovation score
            "market_potential": 0.3,  # Weight for market potential score
            "team_experience": 0.2,  # Weight for team experience score
            "funding_status": 0.1  # Weight for funding status score
        }

        # Extract scores from project data
        innovation_score = project_data.get("innovation", 0)
        market_potential_score = project_data.get("market_potential", 0)
        team_experience_score = project_data.get("team_experience", 0)
        funding_status_score = project_data.get("funding_status", 0)

        # Calculate weighted score
        total_score = (
            innovation_score * criteria_weights["innovation"] +
            market_potential_score * criteria_weights["market_potential"] +
            team_experience_score * criteria_weights["team_experience"] +
            funding_status_score * criteria_weights["funding_status"]
        )

        # Determine project status based on score
        if total_score >= 8.0:
            status = "Approved"
        elif total_score >= 5.0:
            status = "Needs Review"
        else:
            status = "Rejected"

        # Return evaluation results
        return {
            "total_score": round(total_score, 2),
            "status": status
        }

    except Exception as e:
        # Handle unexpected errors
        return {
            "error": str(e),
            "status": "Evaluation Failed"
        }


# Sample JSON data for AI startup projects
sample_projects_json = """
[
    {
        "name": "AI Vision",
        "innovation": 9.0,
        "market_potential": 8.5,
        "team_experience": 7.0,
        "funding_status": 6.0
    },
    {
        "name": "NeuroBotics",
        "innovation": 6.0,
        "market_potential": 5.5,
        "team_experience": 8.0,
        "funding_status": 4.0
    },
    {
        "name": "DataGenix",
        "innovation": 4.0,
        "market_potential": 3.5,
        "team_experience": 5.0,
        "funding_status": 2.0
    }
]
"""

# Load sample projects from JSON
try:
    projects = json.loads(sample_projects_json)

    # Evaluate each project
    for project in projects:
        evaluation_result = evaluate_ai_startup(project)
        print(f"Project: {project['name']}")
        print(f"Evaluation Result: {evaluation_result}")
        print("-" * 40)

except json.JSONDecodeError as e:
    print(f"Error loading project data: {e}")
```
