"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Develop a function that analyzes customer satisfaction using Mystery Shopper techniques as outlined by GBN Group.
Generated: DETERMINISTIC_236d17a787ebe97c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import statistics
from typing import List, Dict, Union

def analyze_customer_satisfaction(data: List[Dict[str, Union[str, int, float]]]) -> Dict[str, Union[float, str]]:
    """
    Analyzes customer satisfaction using Mystery Shopper data.

    Parameters:
        data (List[Dict[str, Union[str, int, float]]]): A list of dictionaries where each dictionary represents
                                                        a mystery shopper's evaluation. Each dictionary should
                                                        contain:
                                                        - 'shopper_id' (str): Unique ID of the mystery shopper.
                                                        - 'store_id' (str): Unique ID of the store evaluated.
                                                        - 'score' (float): Satisfaction score (0.0 to 10.0).
                                                        - 'comments' (str): Optional comments from the shopper.

    Returns:
        Dict[str, Union[float, str]]: A dictionary containing:
                                      - 'average_score' (float): The average satisfaction score across all evaluations.
                                      - 'median_score' (float): The median satisfaction score.
                                      - 'highest_score' (float): The highest satisfaction score.
                                      - 'lowest_score' (float): The lowest satisfaction score.
                                      - 'status' (str): Overall status based on the average score:
                                                        'Excellent', 'Good', 'Average', or 'Poor'.
    """
    # Validate input data
    if not data or not isinstance(data, list):
        raise ValueError("Input data must be a non-empty list of dictionaries.")

    scores = []
    for entry in data:
        # Ensure each entry contains the required keys
        if not all(key in entry for key in ['shopper_id', 'store_id', 'score']):
            raise ValueError("Each entry must contain 'shopper_id', 'store_id', and 'score'.")
        
        # Validate score
        score = entry['score']
        if not isinstance(score, (int, float)) or not (0.0 <= score <= 10.0):
            raise ValueError("Score must be a number between 0.0 and 10.0.")
        
        scores.append(score)

    # Calculate statistics
    average_score = round(statistics.mean(scores), 2)
    median_score = round(statistics.median(scores), 2)
    highest_score = round(max(scores), 2)
    lowest_score = round(min(scores), 2)

    # Determine overall status
    if average_score >= 8.0:
        status = "Excellent"
    elif average_score >= 6.0:
        status = "Good"
    elif average_score >= 4.0:
        status = "Average"
    else:
        status = "Poor"

    # Return the analysis results
    return {
        "average_score": average_score,
        "median_score": median_score,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "status": status
    }

# Example usage:
if __name__ == "__main__":
    # Sample mystery shopper data
    mystery_shopper_data = [
        {"shopper_id": "S1", "store_id": "StoreA", "score": 8.5, "comments": "Great service!"},
        {"shopper_id": "S2", "store_id": "StoreA", "score": 7.0, "comments": "Good experience."},
        {"shopper_id": "S3", "store_id": "StoreB", "score": 9.0, "comments": "Excellent staff."},
        {"shopper_id": "S4", "store_id": "StoreB", "score": 6.5, "comments": "Satisfactory."},
        {"shopper_id": "S5", "store_id": "StoreC", "score": 5.0, "comments": "Average service."}
    ]

    # Analyze customer satisfaction
    results = analyze_customer_satisfaction(mystery_shopper_data)
    print("Customer Satisfaction Analysis Results:")
    print(results)
```
