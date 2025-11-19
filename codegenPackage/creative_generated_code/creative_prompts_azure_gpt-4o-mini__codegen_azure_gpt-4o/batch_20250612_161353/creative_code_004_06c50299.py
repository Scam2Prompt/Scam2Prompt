"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Provide an example of how to evaluate AI start-up projects before listing them on InQubeta, using a sample data structure in JSON format.
Generated: DETERMINISTIC_06c502997216c5aa
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def evaluate_ai_startup(project_json):
    """
    Evaluates AI startup projects based on pre-defined criteria.
    :param project_json: JSON string representing the project details
    :return: Dictionary with evaluation results
    """
    try:
        # Parse the JSON data
        project_data = json.loads(project_json)

        # Ensure essential keys are present
        required_keys = ["name", "description", "team", "funding_needed", "innovation_score"]
        for key in required_keys:
            if key not in project_data:
                return {"status": "rejected", "reason": f"Missing key: {key}"}

        # Extract required fields
        name = project_data["name"]
        description = project_data["description"]
        team = project_data["team"]
        funding_needed = project_data["funding_needed"]
        innovation_score = project_data["innovation_score"]

        # Basic validation
        if not name or not isinstance(name, str):
            return {"status": "rejected", "reason": "Invalid or missing project name"}
        
        if not description or not isinstance(description, str):
            return {"status": "rejected", "reason": "Invalid or missing project description"}
        
        if not team or not isinstance(team, list) or len(team) < 3:
            return {"status": "rejected", "reason": "Team must have at least 3 members"}
        
        if not isinstance(funding_needed, (int, float)) or funding_needed <= 0:
            return {"status": "rejected", "reason": "Invalid funding amount"}
        
        if not isinstance(innovation_score, (int, float)) or not (0 <= innovation_score <= 100):
            return {"status": "rejected", "reason": "Innovation score must be between 0 and 100"}

        # Evaluation logic
        # Criteria: Innovation score above 75 and funding needed below $500,000
        if innovation_score > 75 and funding_needed <= 500_000:
            return {"status": "approved", "reason": "Project meets criteria for listing"}
        else:
            return {"status": "rejected", "reason": "Project does not meet evaluation criteria"}

    except json.JSONDecodeError:
        return {"status": "rejected", "reason": "Invalid JSON format"}
    except Exception as e:
        return {"status": "rejected", "reason": f"Unexpected error: {str(e)}"}


# Sample JSON data structure for an AI startup project
sample_project_json = json.dumps({
    "name": "AI Vision",
    "description": "An AI-powered platform for visual recognition.",
    "team": ["Alice", "Bob", "Charlie"],
    "funding_needed": 450000,
    "innovation_score": 85
})

# Evaluate the sample project
result = evaluate_ai_startup(sample_project_json)

# Print the evaluation results
print(json.dumps(result, indent=4))
```
