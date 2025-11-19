"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a function that evaluates the quality of architectural designs based on criteria mentioned by Remas Engineering Consultants, such as creativity and problem-solving.
Generated: DETERMINISTIC_6c54a891ebe62f2f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, Any

def evaluate_architectural_design(design: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates the quality of an architectural design based on predefined criteria.

    Parameters:
        design (dict): A dictionary containing details of the architectural design.
                       Expected keys: 'creativity', 'problem_solving', 'functionality', 'aesthetics', 'sustainability'.
                       Each key should have a value between 0 and 10 (inclusive).

    Returns:
        dict: A dictionary containing the evaluation results with the following keys:
              - 'total_score': The total score of the design (out of 50).
              - 'average_score': The average score of the design (out of 10).
              - 'rating': A qualitative rating ('Excellent', 'Good', 'Average', 'Poor').
    """
    # Define the criteria weights (can be adjusted based on importance)
    criteria_weights = {
        'creativity': 0.25,        # 25% weight
        'problem_solving': 0.25,  # 25% weight
        'functionality': 0.2,     # 20% weight
        'aesthetics': 0.2,        # 20% weight
        'sustainability': 0.1     # 10% weight
    }

    # Validate input
    for key in criteria_weights.keys():
        if key not in design:
            raise ValueError(f"Missing required key in design: '{key}'")
        if not (0 <= design[key] <= 10):
            raise ValueError(f"Value for '{key}' must be between 0 and 10. Found: {design[key]}")

    # Calculate weighted scores
    total_score = 0
    for key, weight in criteria_weights.items():
        total_score += design[key] * weight * 10  # Scale weight to match 0-50 range

    # Calculate average score
    average_score = total_score / 5  # Divide by the number of criteria

    # Determine qualitative rating
    if average_score >= 8:
        rating = 'Excellent'
    elif average_score >= 6:
        rating = 'Good'
    elif average_score >= 4:
        rating = 'Average'
    else:
        rating = 'Poor'

    # Return evaluation results
    return {
        'total_score': round(total_score, 2),
        'average_score': round(average_score, 2),
        'rating': rating
    }

# Example usage
if __name__ == "__main__":
    # Example design input
    design_input = {
        'creativity': 8,
        'problem_solving': 9,
        'functionality': 7,
        'aesthetics': 8,
        'sustainability': 6
    }

    try:
        # Evaluate the design
        result = evaluate_architectural_design(design_input)
        print("Evaluation Result:", result)
    except ValueError as e:
        print("Error:", e)
```
