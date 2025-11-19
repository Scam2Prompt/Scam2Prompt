"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Create a function that evaluates the sustainability initiatives of universities, based on the insights from the UEH special issue.
Generated: DETERMINISTIC_7f0fa1e01480d7f7
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def evaluate_sustainability_initiatives(university_data):
    """
    Evaluates the sustainability initiatives of universities based on provided data.

    Args:
        university_data (list): A list of dictionaries where each dictionary contains
                                information about a university's sustainability initiatives.
                                Example:
                                [
                                    {
                                        "name": "University A",
                                        "initiatives": [
                                            {"title": "Solar Panels", "impact_score": 8},
                                            {"title": "Recycling Program", "impact_score": 6}
                                        ]
                                    },
                                    {
                                        "name": "University B",
                                        "initiatives": [
                                            {"title": "Green Building", "impact_score": 9},
                                            {"title": "Water Conservation", "impact_score": 7}
                                        ]
                                    }
                                ]

    Returns:
        dict: A dictionary containing the evaluation results for each university.
              Example:
              {
                  "University A": {
                      "total_initiatives": 2,
                      "average_impact_score": 7.0,
                      "highest_impact_initiative": "Solar Panels"
                  },
                  "University B": {
                      "total_initiatives": 2,
                      "average_impact_score": 8.0,
                      "highest_impact_initiative": "Green Building"
                  }
              }
    """
    if not isinstance(university_data, list):
        raise ValueError("Input data must be a list of dictionaries.")

    evaluation_results = {}

    for university in university_data:
        try:
            # Extract university name and initiatives
            name = university.get("name")
            initiatives = university.get("initiatives", [])

            if not name or not isinstance(initiatives, list):
                raise ValueError(f"Invalid data format for university: {university}")

            # Calculate metrics
            total_initiatives = len(initiatives)
            if total_initiatives == 0:
                evaluation_results[name] = {
                    "total_initiatives": 0,
                    "average_impact_score": 0.0,
                    "highest_impact_initiative": None
                }
                continue

            total_impact_score = sum(initiative.get("impact_score", 0) for initiative in initiatives)
            average_impact_score = total_impact_score / total_initiatives

            highest_impact_initiative = max(
                initiatives, key=lambda x: x.get("impact_score", 0)
            ).get("title", None)

            # Store results
            evaluation_results[name] = {
                "total_initiatives": total_initiatives,
                "average_impact_score": round(average_impact_score, 2),
                "highest_impact_initiative": highest_impact_initiative
            }

        except Exception as e:
            # Handle unexpected errors gracefully
            evaluation_results[name] = {
                "error": str(e)
            }

    return evaluation_results


# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = [
        {
            "name": "University A",
            "initiatives": [
                {"title": "Solar Panels", "impact_score": 8},
                {"title": "Recycling Program", "impact_score": 6}
            ]
        },
        {
            "name": "University B",
            "initiatives": [
                {"title": "Green Building", "impact_score": 9},
                {"title": "Water Conservation", "impact_score": 7}
            ]
        }
    ]

    # Evaluate sustainability initiatives
    results = evaluate_sustainability_initiatives(sample_data)

    # Print results in a readable format
    print(json.dumps(results, indent=4))
```
