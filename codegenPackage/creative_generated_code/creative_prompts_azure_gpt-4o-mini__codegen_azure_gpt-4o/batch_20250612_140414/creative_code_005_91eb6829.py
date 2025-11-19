"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: Create a function that compares different cleaning methods (ultrasonic, pyrolysis, jet washing) for industrial parts, using criteria outlined in Sonic Solutions' knowledge center.
Generated: DETERMINISTIC_91eb6829a8765fe3
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Initialize logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def compare_cleaning_methods(parts_type, criteria):
    """
    Compare cleaning methods for industrial parts based on given criteria.

    Args:
        parts_type (str): Type of industrial parts being cleaned (e.g., "metal", "ceramic").
        criteria (dict): Dictionary containing criteria for comparison. Keys could include:
            - "efficiency": How well the method cleans (1-10 scale).
            - "cost": Cost involved in cleaning (low, medium, high).
            - "environmental_impact": Environmental impact of the method (low, medium, high).
            - "safety": Safety level during cleaning (low, medium, high).

    Returns:
        dict: Comparison results with recommended cleaning method.
    """

    # Define cleaning methods and their attributes
    cleaning_methods = {
        "ultrasonic": {
            "efficiency": 9,
            "cost": "medium",
            "environmental_impact": "low",
            "safety": "high"
        },
        "pyrolysis": {
            "efficiency": 8,
            "cost": "high",
            "environmental_impact": "medium",
            "safety": "medium"
        },
        "jet_washing": {
            "efficiency": 7,
            "cost": "low",
            "environmental_impact": "medium",
            "safety": "high"
        }
    }
    
    # Validate input criteria
    if not isinstance(criteria, dict):
        logging.error("Criteria must be provided as a dictionary.")
        raise ValueError("Invalid criteria format. Expected dictionary.")

    # Validate parts type input
    if not isinstance(parts_type, str) or not parts_type:
        logging.error("Invalid parts type. Expected non-empty string.")
        raise ValueError("Invalid parts type format. Expected a non-empty string.")
    
    # Function to calculate score for each cleaning method based on criteria
    def calculate_score(method_attributes, user_criteria):
        score = 0
        for key, value in user_criteria.items():
            # Check if criterion exists for the method
            if key in method_attributes:
                method_value = method_attributes[key]
                if isinstance(value, int):  # Numeric comparison (e.g., efficiency)
                    score += abs(value - method_value)
                elif isinstance(value, str):  # Categorical comparison (e.g., cost, safety)
                    if value.lower() == method_value.lower():
                        score += 1
        return score

    # Compare methods and determine the best one
    results = {}
    for method, attributes in cleaning_methods.items():
        results[method] = calculate_score(attributes, criteria)
    
    # Recommend the method with the highest score
    recommended_method = max(results, key=results.get)

    logging.info("Comparison complete. Recommended cleaning method: %s", recommended_method)

    return {
        "recommended_method": recommended_method,
        "scores": results
    }

# Example usage
if __name__ == "__main__":
    try:
        criteria_example = {
            "efficiency": 8,
            "cost": "medium",
            "environmental_impact": "low",
            "safety": "high"
        }
        parts_type_example = "metal"
        
        comparison_result = compare_cleaning_methods(parts_type_example, criteria_example)
        print("Comparison Result:", comparison_result)
    except Exception as ex:
        logging.error("An error occurred: %s", ex)
```
