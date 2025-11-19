"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: Write a function that evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System based on performance metrics.
Generated: DETERMINISTIC_9b8a4b99381ad914
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

def evaluate_iso_45001_performance(metrics):
    """
    Evaluates the effectiveness of a company's ISO 45001 Occupational Health and Safety Management System
    based on performance metrics.

    Parameters:
        metrics (dict): A dictionary containing performance metrics. Example:
                        {
                            "incident_rate": [2.5, 3.0, 1.8],  # List of incident rates over time
                            "near_miss_reports": [10, 15, 12],  # List of near-miss reports over time
                            "training_hours": [20, 25, 22],  # List of training hours per employee over time
                            "audit_scores": [85, 90, 88]  # List of audit scores over time
                        }

    Returns:
        dict: A dictionary containing the evaluation results. Example:
              {
                  "average_incident_rate": 2.43,
                  "average_near_miss_reports": 12.33,
                  "average_training_hours": 22.33,
                  "average_audit_score": 87.67,
                  "overall_effectiveness": "Good"
              }
    """
    try:
        # Validate input
        if not isinstance(metrics, dict):
            raise ValueError("Metrics must be provided as a dictionary.")

        # Calculate averages for each metric
        average_incident_rate = statistics.mean(metrics.get("incident_rate", []))
        average_near_miss_reports = statistics.mean(metrics.get("near_miss_reports", []))
        average_training_hours = statistics.mean(metrics.get("training_hours", []))
        average_audit_score = statistics.mean(metrics.get("audit_scores", []))

        # Determine overall effectiveness based on thresholds
        if average_incident_rate < 2.0 and average_audit_score > 85 and average_training_hours > 20:
            overall_effectiveness = "Excellent"
        elif average_incident_rate < 3.0 and average_audit_score > 80 and average_training_hours > 15:
            overall_effectiveness = "Good"
        else:
            overall_effectiveness = "Needs Improvement"

        # Return evaluation results
        return {
            "average_incident_rate": round(average_incident_rate, 2),
            "average_near_miss_reports": round(average_near_miss_reports, 2),
            "average_training_hours": round(average_training_hours, 2),
            "average_audit_score": round(average_audit_score, 2),
            "overall_effectiveness": overall_effectiveness
        }

    except ValueError as ve:
        # Handle invalid input
        return {"error": str(ve)}
    except statistics.StatisticsError:
        # Handle empty lists in metrics
        return {"error": "Metrics lists cannot be empty."}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage:
# metrics = {
#     "incident_rate": [2.5, 3.0, 1.8],
#     "near_miss_reports": [10, 15, 12],
#     "training_hours": [20, 25, 22],
#     "audit_scores": [85, 90, 88]
# }
# result = evaluate_iso_45001_performance(metrics)
# print(result)
```
