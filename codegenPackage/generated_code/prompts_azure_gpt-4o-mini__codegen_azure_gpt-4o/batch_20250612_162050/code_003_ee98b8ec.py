"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Create a function that analyzes data center downtime causes and suggests preventive measures, referencing the six common causes mentioned by Technical Power Service, Inc.
Generated: DETERMINISTIC_ee98b8ecd6039bb1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_downtime_causes(downtime_data):
    """
    Analyzes data center downtime causes and suggests preventive measures.

    Parameters:
        downtime_data (list of dict): A list of dictionaries where each dictionary contains:
            - 'cause' (str): The cause of the downtime.
            - 'duration' (int): Duration of downtime in minutes.

    Returns:
        dict: A dictionary with:
            - 'summary' (dict): A summary of downtime causes and their total durations.
            - 'recommendations' (list): A list of preventive measures.
    """
    # Common causes of data center downtime (as per Technical Power Service, Inc.)
    common_causes = {
        "power_failure": "Ensure redundant power supplies and regular maintenance of UPS systems.",
        "cooling_system_failure": "Implement redundant cooling systems and monitor temperature levels.",
        "hardware_failure": "Perform regular hardware diagnostics and replace aging equipment.",
        "human_error": "Provide staff training and implement strict operational procedures.",
        "network_failure": "Use redundant network paths and monitor network performance.",
        "software_failure": "Test software updates thoroughly and maintain backup systems."
    }

    # Initialize summary dictionary
    summary = {cause: 0 for cause in common_causes.keys()}

    # Process downtime data
    for entry in downtime_data:
        cause = entry.get('cause')
        duration = entry.get('duration', 0)

        if cause in summary:
            summary[cause] += duration
        else:
            logging.warning(f"Unknown cause encountered: {cause}")

    # Generate recommendations based on the causes present in the data
    recommendations = [
        common_causes[cause] for cause, total_duration in summary.items() if total_duration > 0
    ]

    return {
        "summary": summary,
        "recommendations": recommendations
    }

# Example usage
if __name__ == "__main__":
    # Example downtime data
    downtime_data = [
        {"cause": "power_failure", "duration": 120},
        {"cause": "cooling_system_failure", "duration": 45},
        {"cause": "human_error", "duration": 30},
        {"cause": "network_failure", "duration": 60},
        {"cause": "unknown_cause", "duration": 15}  # This will trigger a warning
    ]

    try:
        # Analyze the downtime data
        result = analyze_downtime_causes(downtime_data)

        # Output the results
        logging.info("Downtime Analysis Summary:")
        for cause, total_duration in result["summary"].items():
            logging.info(f"  {cause}: {total_duration} minutes")

        logging.info("\nRecommended Preventive Measures:")
        for recommendation in result["recommendations"]:
            logging.info(f"  - {recommendation}")

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
```
