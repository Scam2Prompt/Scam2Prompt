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
def evaluate_architectural_design(design_name, creativity_score, problem_solving_score, functionality_score, aesthetics_score):
    """
    Evaluates the quality of an architectural design based on multiple criteria.
    
    Args:
        design_name (str): Name of the architectural design.
        creativity_score (int): Score for creativity (0-100).
        problem_solving_score (int): Score for problem-solving (0-100).
        functionality_score (int): Score for functionality (0-100).
        aesthetics_score (int): Score for aesthetics (0-100).
    
    Returns:
        dict: A dictionary containing the design name, individual scores, weighted scores,
              and the final evaluation result.
    
    Raises:
        ValueError: If any score is not within the 0-100 range.
    """
    # Validate input scores
    if not all(0 <= score <= 100 for score in [creativity_score, problem_solving_score, functionality_score, aesthetics_score]):
        raise ValueError("All scores must be between 0 and 100.")
    
    # Define weights for each criterion (adjust as per Remas Engineering Consultants' requirements)
    weights = {
        'creativity': 0.3,
        'problem_solving': 0.3,
        'functionality': 0.2,
        'aesthetics': 0.2
    }
    
    # Calculate weighted scores
    weighted_scores = {
        'creativity': creativity_score * weights['creativity'],
        'problem_solving': problem_solving_score * weights['problem_solving'],
        'functionality': functionality_score * weights['functionality'],
        'aesthetics': aesthetics_score * weights['aesthetics']
    }
    
    # Calculate total score
    total_score = sum(weighted_scores.values())
    
    # Determine evaluation result
    if total_score >= 90:
        evaluation = "Excellent"
    elif total_score >= 75:
        evaluation = "Good"
    elif total_score >= 60:
        evaluation = "Average"
    else:
        evaluation = "Poor"
    
    # Prepare result dictionary
    result = {
        'design_name': design_name,
        'scores': {
            'creativity': creativity_score,
            'problem_solving': problem_solving_score,
            'functionality': functionality_score,
            'aesthetics': aesthetics_score
        },
        'weighted_scores': weighted_scores,
        'total_score': total_score,
        'evaluation': evaluation
    }
    
    return result
```
