"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Create a function that evaluates the sustainability initiatives of universities, based on the insights from the UEH special issue.
Generated: DETERMINISTIC_7f0fa1e01480d7f7
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def evaluate_sustainability_initiatives(data):
    """
    Evaluates the sustainability initiatives of universities based on provided data.

    Parameters:
        data (list): A list of dictionaries containing university information and their sustainability initiatives.
        Example format:
        [
            {
                "university_name": "Example University",
                "initiatives": [
                    {"title": "Renewable Energy Investment", "impact_score": 8, "alignment_score": 9},
                    {"title": "Recycling Program", "impact_score": 6, "alignment_score": 7}
                ]
            },
            ...
        ]

    Returns:
        dict: A dictionary with university names as keys and their overall sustainability scores as values.
    """

    if not isinstance(data, list):
        raise ValueError("Input data must be a list of dictionaries.")

    sustainability_scores = {}

    for university in data:
        try:
            university_name = university["university_name"]
            initiatives = university["initiatives"]

            if not isinstance(initiatives, list):
                raise ValueError("Initiatives must be a list.")

            total_score = 0
            for initiative in initiatives:
                # Ensure required keys exist in each initiative
                if not all(key in initiative for key in ["impact_score", "alignment_score"]):
                    raise ValueError(f"Missing required keys in initiative: {initiative}")

                # Aggregate scores (e.g., impact_score and alignment_score can be weighted later)
                impact_score = initiative["impact_score"]
                alignment_score = initiative["alignment_score"]

                # Validate scores
                if not (isinstance(impact_score, (int, float)) and isinstance(alignment_score, (int, float))):
                    raise ValueError("Scores must be integers or floats.")

                total_score += impact_score + alignment_score

            # Store the computed score for the university
            sustainability_scores[university_name] = total_score

        except KeyError as e:
            raise ValueError(f"Missing required university information: {e}")
        except ValueError as e:
            print(f"Error evaluating university {university.get('university_name', 'Unknown')}: {e}")
            continue

    return sustainability_scores


# Example Usage:
if __name__ == "__main__":
    # Sample Data
    university_data = [
        {
            "university_name": "University A",
            "initiatives": [
                {"title": "Renewable Energy Investment", "impact_score": 8, "alignment_score": 9},
                {"title": "Water Conservation Program", "impact_score": 7, "alignment_score": 8}
            ]
        },
        {
            "university_name": "University B",
            "initiatives": [
                {"title": "Carbon Neutrality Initiative", "impact_score": 9, "alignment_score": 10},
                {"title": "Recycling Program", "impact_score": 6, "alignment_score": 7}
            ]
        }
    ]

    # Evaluate and print results
    try:
        scores = evaluate_sustainability_initiatives(university_data)
        print(json.dumps(scores, indent=4))  # Pretty-print the results
    except ValueError as e:
        print(f"Error: {e}")
```
