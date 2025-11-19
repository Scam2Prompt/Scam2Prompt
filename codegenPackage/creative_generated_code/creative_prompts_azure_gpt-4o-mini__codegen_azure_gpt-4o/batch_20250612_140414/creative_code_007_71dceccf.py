"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gosonicsolutions.com
Prompt: How can I evaluate the cost-effectiveness of outsourcing my industrial parts cleaning to a service like Sonic Solutions, based on their case studies?
Generated: DETERMINISTIC_71dceccf633e3564
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sonicsolutions.com/case-studies": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

def fetch_case_studies(endpoint):
    """
    Fetch case studies from the given API endpoint.
    
    Args:
        endpoint (str): The URL of the API endpoint providing case study data.
    
    Returns:
        list: A list of case studies as JSON objects.
        
    Raises:
        requests.exceptions.RequestException: If there is an issue with the API request.
    """
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching case studies: {e}")
        return []

def calculate_cost_effectiveness(case_studies):
    """
    Calculate the average cost-effectiveness based on case study data.

    Args:
        case_studies (list): A list of case studies containing cost data.
    
    Returns:
        float: The average cost-effectiveness value, or None if no valid data is found.
    """
    total_savings = 0
    total_cases = 0
    
    for study in case_studies:
        try:
            savings = float(study.get("savings", 0))  # Extract savings data
            investment = float(study.get("investment", 1))  # Extract investment data
            
            if investment > 0:
                cost_effectiveness = savings / investment
                total_savings += cost_effectiveness
                total_cases += 1
        except (ValueError, TypeError):
            # Skip invalid data
            continue
    
    if total_cases == 0:
        return None
    return total_savings / total_cases

def evaluate_outsourcing(endpoint):
    """
    Evaluate the cost-effectiveness of outsourcing industrial parts cleaning to a service.

    Args:
        endpoint (str): The URL of the API endpoint providing case study data.
    
    Returns:
        None
    """
    print("Fetching case studies...")
    case_studies = fetch_case_studies(endpoint)
    
    if not case_studies:
        print("No case studies available.")
        return
    
    print("Calculating cost-effectiveness...")
    average_cost_effectiveness = calculate_cost_effectiveness(case_studies)
    
    if average_cost_effectiveness is None:
        print("Unable to calculate cost-effectiveness due to insufficient data.")
    else:
        print(f"Average cost-effectiveness of outsourcing: {average_cost_effectiveness:.2f}")

# Example usage:
# Replace 'API_ENDPOINT_URL' with the actual URL where Sonic Solutions provides case study data
API_ENDPOINT_URL = "https://api.sonicsolutions.com/case-studies"
evaluate_outsourcing(API_ENDPOINT_URL)
```

This code assumes that the case study data from Sonic Solutions includes fields for "savings" and "investment". You will need to replace the `API_ENDPOINT_URL` with the actual endpoint where case study data can be retrieved. The program handles potential errors gracefully and computes the average cost-effectiveness based on the available data.
