"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Create a script to filter and categorize legal leads by case type (e.g., car accidents, bicycle accidents) and client readiness, as described by ClaimLink Legal Solutions.
Generated: DETERMINISTIC_35bcb82f1746fb55
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_and_categorize_leads(leads, case_types, readiness_threshold):
    """
    Filters and categorizes legal leads based on case type and client readiness.

    Args:
        leads (list): List of dictionaries containing lead information. 
                      Example: [{'name': 'John Doe', 'case_type': 'car accident', 'readiness_score': 85}, ...]
        case_types (list): List of case types to categorize. Example: ['car accident', 'bicycle accident']
        readiness_threshold (int): Minimum readiness score to consider a lead as ready.

    Returns:
        dict: Categorized leads by case type and readiness. Example:
              {
                  "car accident": {
                      "ready": [{'name': 'John Doe', 'case_type': 'car accident', 'readiness_score': 85}],
                      "not_ready": [...]
                  },
                  "bicycle accident": {...}
              }
    """
    categorized_leads = {case_type: {"ready": [], "not_ready": []} for case_type in case_types}

    # Iterate through leads to filter and categorize
    for lead in leads:
        case_type = lead.get('case_type')
        readiness_score = lead.get('readiness_score')
        
        if case_type in case_types:  # Check if the lead's case type is in the desired list
            if readiness_score >= readiness_threshold:
                categorized_leads[case_type]["ready"].append(lead)
            else:
                categorized_leads[case_type]["not_ready"].append(lead)
        else:
            # Log or handle unsupported case types if necessary
            pass

    return categorized_leads


def main():
    """
    Main function to demonstrate the functionality of filtering and categorizing leads.
    """
    try:
        # Example input data
        leads = [
            {"name": "John Doe", "case_type": "car accident", "readiness_score": 85},
            {"name": "Jane Smith", "case_type": "bicycle accident", "readiness_score": 65},
            {"name": "Emily Davis", "case_type": "car accident", "readiness_score": 40},
            {"name": "Michael Brown", "case_type": "bicycle accident", "readiness_score": 90},
            {"name": "Sarah Wilson", "case_type": "medical malpractice", "readiness_score": 70}
        ]
        
        case_types = ["car accident", "bicycle accident"]  # Define case types to categorize
        readiness_threshold = 50  # Define readiness threshold
        
        # Filter and categorize leads
        categorized_leads = filter_and_categorize_leads(leads, case_types, readiness_threshold)
        
        # Output the results
        print(json.dumps(categorized_leads, indent=4))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
