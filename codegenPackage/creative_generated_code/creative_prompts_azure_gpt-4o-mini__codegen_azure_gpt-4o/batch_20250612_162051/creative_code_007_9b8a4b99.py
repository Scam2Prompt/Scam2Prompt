"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def evaluate_iso_45001_performance(metrics):
    """
    Evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety 
    Management System based on provided performance metrics.

    Parameters:
        metrics (dict): A dictionary containing performance metrics. Expected keys:
            - 'incident_rate': List of incident rates over time (lower is better).
            - 'audit_scores': List of audit scores over time (higher is better).
            - 'employee_training_hours': List of average employee training hours over time (higher is better).
            - 'corrective_actions_implemented': List of the number of corrective actions implemented (higher is better).

    Returns:
        dict: A dictionary containing overall performance evaluation with keys:
            - 'incident_rate_trend': Trend (improving, worsening, stable) for incident rates.
            - 'audit_score_trend': Trend (improving, worsening, stable) for audit scores.
            - 'training_hours_trend': Trend (improving, worsening, stable) for training hours.
            - 'corrective_actions_trend': Trend (improving, worsening, stable) for corrective actions.
            - 'overall_effectiveness': Finalized evaluation ('Effective', 'Needs Improvement', 'Critical').
    """
    try:
        # Helper function to calculate trend
        def calculate_trend(data):
            # Ensure data has enough points for trend analysis
            if len(data) < 2:
                return "insufficient data"
            
            # Calculate slope using linear regression
            slope = statistics.mean(data[i + 1] - data[i] for i in range(len(data) - 1))
            if slope > 0:
                return "improving"
            elif slope < 0:
                return "worsening"
            else:
                return "stable"

        # Validate metrics input
        if not isinstance(metrics, dict) or not metrics:
            raise ValueError("Metrics must be a non-empty dictionary containing performance data.")

        required_keys = {'incident_rate', 'audit_scores', 'employee_training_hours', 'corrective_actions_implemented'}
        if not required_keys.issubset(metrics.keys()):
            raise ValueError(f"Metrics dictionary must contain the following keys: {required_keys}")

        # Calculate trends for each metric
        trends = {
            'incident_rate_trend': calculate_trend(metrics['incident_rate']),
            'audit_score_trend': calculate_trend(metrics['audit_scores']),
            'training_hours_trend': calculate_trend(metrics['employee_training_hours']),
            'corrective_actions_trend': calculate_trend(metrics['corrective_actions_implemented']),
        }

        # Evaluate overall effectiveness
        if all(value == "improving" for value in trends.values()):
            overall_effectiveness = "Effective"
        elif "worsening" in trends.values():
            overall_effectiveness = "Needs Improvement"
        else:
            overall_effectiveness = "Critical"

        # Return result as a dictionary
        return {**trends, 'overall_effectiveness': overall_effectiveness}

    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": str(e)}


# Example usage:
metrics = {
    'incident_rate': [5, 4, 3, 2],
    'audit_scores': [70, 75, 80, 85],
    'employee_training_hours': [10, 12, 15, 20],
    'corrective_actions_implemented': [3, 4, 5, 6],
}

result = evaluate_iso_45001_performance(metrics)
print(result)
```
