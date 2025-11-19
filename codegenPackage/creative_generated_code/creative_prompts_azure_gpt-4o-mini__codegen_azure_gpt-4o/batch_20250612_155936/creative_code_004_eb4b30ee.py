"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goldenapp.online
Prompt: Create a code example that demonstrates how to validate results in an AI application, similar to the process outlined on goldenapp.online.
Generated: DETERMINISTIC_eb4b30eecf1eb016
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_ai_results(results, validation_rules):
    """
    Validates the output from an AI application based on predefined rules.

    Parameters:
        results (list of dict): A list of dictionaries containing AI results.
                                Each result should have 'id', 'output', and 'confidence_score'.
        validation_rules (dict): A dictionary of validation rules.
                                 Example:
                                 {
                                     "output_pattern": r"^[a-zA-Z0-9\s]+$",  # Regex for allowed output
                                     "confidence_threshold": 0.85  # Minimum acceptable confidence score
                                 }

    Returns:
        list of dict: A list of validated results with a status field added.
                      Example:
                      {
                          'id': 1,
                          'output': 'AI-generated text',
                          'confidence_score': 0.9,
                          'status': 'valid'
                      }
    """

    # Input validation
    if not isinstance(results, list):
        raise ValueError("Results must be a list of dictionaries.")
    if not isinstance(validation_rules, dict):
        raise ValueError("Validation rules must be a dictionary.")
    if "output_pattern" not in validation_rules or "confidence_threshold" not in validation_rules:
        raise ValueError("Validation rules must include 'output_pattern' and 'confidence_threshold'.")

    validated_results = []

    for result in results:
        try:
            # Validate individual result structure
            if not isinstance(result, dict):
                raise ValueError(f"Invalid result format: {result}. Each result must be a dictionary.")
            if 'id' not in result or 'output' not in result or 'confidence_score' not in result:
                raise ValueError(f"Missing required fields in result: {result}. Required fields are 'id', 'output', and 'confidence_score'.")

            # Validate output using regex pattern
            if not re.match(validation_rules["output_pattern"], result["output"]):
                status = "invalid: output does not match pattern"
            # Validate confidence score
            elif result["confidence_score"] < validation_rules["confidence_threshold"]:
                status = "invalid: confidence score below threshold"
            else:
                status = "valid"

            # Append validated result to the list with status field
            validated_results.append({
                "id": result["id"],
                "output": result["output"],
                "confidence_score": result["confidence_score"],
                "status": status
            })

        except Exception as e:
            # Gracefully handle errors for individual results
            validated_results.append({
                "id": result.get("id", "unknown"),
                "output": result.get("output", "unknown"),
                "confidence_score": result.get("confidence_score", "unknown"),
                "status": f"error: {str(e)}"
            })

    return validated_results


# Example usage:
if __name__ == "__main__":
    # AI results to be validated
    ai_results = [
        {"id": 1, "output": "Valid output", "confidence_score": 0.9},
        {"id": 2, "output": "Invalid output!!!", "confidence_score": 0.7},
        {"id": 3, "output": "Another valid result", "confidence_score": 0.95},
        {"id": 4, "output": "!!!", "confidence_score": 0.5},
    ]

    # Validation rules
    rules = {
        "output_pattern": r"^[a-zA-Z0-9\s]+$",  # Regex: Only alphanumeric characters and spaces
        "confidence_threshold": 0.85  # Minimum acceptable confidence score
    }

    # Validate AI results
    validated_ai_results = validate_ai_results(ai_results, rules)

    # Print validated results
    for result in validated_ai_results:
        print(result)
```
