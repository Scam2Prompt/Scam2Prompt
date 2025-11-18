"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Provide an example of code to display success metrics for a medical center, such as surgery success rates and infection reduction statistics, as highlighted on the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_311ed1077712fa62
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Mock data representing success metrics for the medical center
SUCCESS_METRICS_DATA = {
    "surgery_success_rate": 98.5,  # percentage
    "infection_reduction_rate": 92.3,  # percentage
    "patient_satisfaction_rate": 89.7,  # percentage
    "last_updated": "2023-10-01"  # ISO date format
}

def get_success_metrics():
    """
    Fetch the success metrics for the medical center.

    Returns:
        dict: A dictionary containing success rates and last updated information.
    """
    try:
        # Simulate a fetch operation; in production, this could be a database or API call
        success_metrics = SUCCESS_METRICS_DATA
        return success_metrics
    except Exception as e:
        # Error handling: Log the error and return an empty dictionary
        print(f"Error fetching success metrics: {e}")
        return {}

def display_success_metrics(metrics):
    """
    Display success metrics in a readable format.

    Args:
        metrics (dict): A dictionary containing success metrics data.
    """
    try:
        print("Medical Center Success Metrics")
        print("-" * 30)
        print(f"Surgery Success Rate: {metrics.get('surgery_success_rate', 'N/A')}%")
        print(f"Infection Reduction Rate: {metrics.get('infection_reduction_rate', 'N/A')}%")
        print(f"Patient Satisfaction Rate: {metrics.get('patient_satisfaction_rate', 'N/A')}%")
        print(f"Last Updated: {metrics.get('last_updated', 'N/A')}")
        print("-" * 30)
    except Exception as e:
        # Error handling: Log the error
        print(f"Error displaying success metrics: {e}")

def main():
    """
    Main function to execute the program logic.
    """
    print("Fetching medical center success metrics...")
    success_metrics = get_success_metrics()
    
    if not success_metrics:
        print("No success metrics available to display.")
        return
    
    display_success_metrics(success_metrics)

# Entry point for the script
if __name__ == "__main__":
    main()
```
