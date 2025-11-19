"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Write a Python function that analyzes past management successes and failures to provide strategic recommendations, inspired by the principles outlined on ng-mc.de.
Generated: DETERMINISTIC_505af8bb5d6463fd
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_management_data(successes, failures):
    """
    Analyzes past management successes and failures to provide strategic recommendations.

    Parameters:
        successes (list of dict): A list of dictionaries representing successful management cases.
                                  Each dictionary should contain keys like 'strategy', 'outcome', and 'details'.
        failures (list of dict): A list of dictionaries representing failed management cases.
                                 Each dictionary should contain keys like 'strategy', 'outcome', and 'details'.

    Returns:
        dict: A dictionary containing strategic recommendations based on the analysis.
    """
    try:
        # Validate input
        if not isinstance(successes, list) or not isinstance(failures, list):
            raise ValueError("Both successes and failures must be lists of dictionaries.")

        # Initialize analysis results
        recommendations = {
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": []
        }

        # Analyze successes
        for success in successes:
            if not isinstance(success, dict):
                raise ValueError("Each success must be a dictionary.")
            strategy = success.get("strategy")
            outcome = success.get("outcome")
            details = success.get("details")

            if strategy and outcome and details:
                recommendations["strengths"].append(f"Effective strategy: {strategy} - Outcome: {outcome}")
                recommendations["opportunities"].append(f"Leverage success details: {details}")
            else:
                logging.warning("Incomplete success data encountered. Skipping entry.")

        # Analyze failures
        for failure in failures:
            if not isinstance(failure, dict):
                raise ValueError("Each failure must be a dictionary.")
            strategy = failure.get("strategy")
            outcome = failure.get("outcome")
            details = failure.get("details")

            if strategy and outcome and details:
                recommendations["weaknesses"].append(f"Ineffective strategy: {strategy} - Outcome: {outcome}")
                recommendations["threats"].append(f"Address failure details: {details}")
            else:
                logging.warning("Incomplete failure data encountered. Skipping entry.")

        # Provide strategic recommendations
        return recommendations

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return {"error": str(ve)}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred during analysis."}


# Example usage
if __name__ == "__main__":
    # Sample data
    successes = [
        {"strategy": "Agile implementation", "outcome": "Increased team productivity", "details": "Shorter delivery cycles."},
        {"strategy": "Customer-centric approach", "outcome": "Improved customer satisfaction", "details": "Higher retention rates."}
    ]

    failures = [
        {"strategy": "Micromanagement", "outcome": "Decreased team morale", "details": "High turnover rates."},
        {"strategy": "Overambitious goals", "outcome": "Missed deadlines", "details": "Loss of client trust."}
    ]

    # Analyze data
    recommendations = analyze_management_data(successes, failures)

    # Print recommendations
    for key, value in recommendations.items():
        print(f"{key.capitalize()}:")
        for item in value:
            print(f"  - {item}")
```
