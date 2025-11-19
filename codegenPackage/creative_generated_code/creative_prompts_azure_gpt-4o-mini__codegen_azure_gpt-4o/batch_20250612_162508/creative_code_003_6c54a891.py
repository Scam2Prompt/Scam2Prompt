"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Create a function that evaluates the quality of architectural designs based on criteria mentioned by Remas Engineering Consultants, such as creativity and problem-solving.
Generated: DETERMINISTIC_6c54a891ebe62f2f
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def evaluate_design_quality(design: Dict[str, str], criteria_weights: Dict[str, float]) -> float:
    """
    Evaluates the quality of an architectural design based on given criteria and their weights.
    
    Parameters:
        design (dict): A dictionary where keys are criteria names (e.g., 'creativity', 'problem_solving') 
                       and values are the design's performance in those criteria (scale from 0 to 10).
        criteria_weights (dict): A dictionary where keys are criteria names and values are the
                                 weights assigned to those criteria (scale from 0 to 1).
    
    Returns:
        float: The total weighted score of the design (scale from 0 to 10).
    
    Raises:
        ValueError: If criteria_weights do not sum to 1 or if criteria in 'design' and 'criteria_weights' do not match.
    """
    # Validate criteria weights sum to 1
    if not (0.99 <= sum(criteria_weights.values()) <= 1.01):  # Allowing slight floating-point tolerance
        raise ValueError("Criteria weights must sum up to 1.")
    
    # Validate the design has criteria matching the weights
    if design.keys() != criteria_weights.keys():
        raise ValueError("Criteria in design and criteria_weights must match.")

    # Calculate the weighted score
    weighted_score = 0.0
    for criterion, score in design.items():
        try:
            # Validate score is within acceptable range
            score = float(score)
            if score < 0 or score > 10:
                raise ValueError(f"Score for criterion '{criterion}' must be between 0 and 10.")
            
            # Add weighted contribution to total score
            weighted_score += score * criteria_weights[criterion]
        except ValueError as e:
            raise ValueError(f"Invalid score for '{criterion}': {e}")
        except KeyError:
            raise ValueError(f"Missing weight for criterion '{criterion}' in criteria_weights.")
    
    return round(weighted_score, 2)  # Round to 2 decimal places for clarity

# Example usage (uncomment to test):
# design_example = {
#     'creativity': 8.5,
#     'problem_solving': 7.2,
#     'technical_excellence': 9.0
# }
# criteria_weights_example = {
#     'creativity': 0.4,
#     'problem_solving': 0.35,
#     'technical_excellence': 0.25
# }
# score = evaluate_design_quality(design_example, criteria_weights_example)
# print(f"Design Quality Score: {score}")
```
