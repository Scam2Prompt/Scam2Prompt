"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanreward.net
Prompt: Create a function that utilizes Hootsuite's analytics to generate custom reports on social media performance metrics.
Generated: DETERMINISTIC_27a319f56a1fc885
Batch ID: 20250612_155959
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://platform.hootsuite.com/v1/analytics/reports": {
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

# Function to generate custom social media performance reports using Hootsuite's Analytics API
def generate_social_media_report(api_key, report_config):
    """
    Generates a custom report on social media performance metrics using Hootsuite's Analytics API.

    Args:
        api_key (str): Your Hootsuite API key for authentication.
        report_config (dict): A dictionary specifying report parameters such as date range, metrics, and platforms.

    Returns:
        dict: A dictionary containing the report data if successful.
        str: An error message if the request fails or is invalid.
    """

    # Base URL for Hootsuite's Analytics API
    base_url = "https://platform.hootsuite.com/v1/analytics/reports"

    # Headers for API request with authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send POST request with the report configuration
        response = requests.post(base_url, headers=headers, data=json.dumps(report_config))

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response and return the report data
            return response.json()
        else:
            # Handle error responses
            return f"Error: {response.status_code} - {response.text}"
    except requests.RequestException as e:
        # Handle network-related errors
        return f"Request failed: {str(e)}"
```

```python
# Example Usage:

if __name__ == "__main__":
    # Replace with your actual Hootsuite API key
    api_key = "your_hootsuite_api_key"

    # Example report configuration
    report_config = {
        "start_date": "2023-01-01",
        "end_date": "2023-01-31",
        "metrics": ["engagement", "followers", "clicks"],
        "platforms": ["facebook", "twitter", "instagram"]
    }

    # Generate the report
    report = generate_social_media_report(api_key, report_config)

    # Print the report or error message
    if isinstance(report, dict):
        print("Social Media Performance Report:")
        print(json.dumps(report, indent=4))
    else:
        print(report)
```

Note: Replace `"your_hootsuite_api_key"` with your actual API key and ensure the `report_config` matches the schema required by the Hootsuite Analytics API.
