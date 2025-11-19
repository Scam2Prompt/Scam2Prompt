"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaunaalerta.com.br
Prompt: Generate a summary of the health alerts in Itaúna, specifically discussing the recent notifications of severe respiratory syndrome.
Generated: DETERMINISTIC_91fa6d952e7fb8c4
Batch ID: 20250612_160804
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.healthalerts.example.com/alerts`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.healthalerts.example.com/alerts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the Python code that generates a summary of health alerts in Itaúna, specifically discussing recent notifications of severe respiratory syndrome:

```python
import requests
import json

def fetch_health_alerts(city_name):
    """
    Fetch health alerts for the specified city from a hypothetical API.

    Args:
        city_name (str): Name of the city to fetch health alerts for.

    Returns:
        dict: Parsed JSON data containing health alerts.

    Raises:
        Exception: If the API request fails or data retrieval is unsuccessful.
    """
    API_URL = "https://api.healthalerts.example.com/alerts"  # Replace with the actual API URL
    try:
        # Send a GET request to the API with the city name
        response = requests.get(API_URL, params={"city": city_name})
        response.raise_for_status()  # Raise an error for HTTP request issues

        # Parse the JSON response
        alerts_data = response.json()
        return alerts_data
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Error fetching health alerts: {req_err}")
    except json.JSONDecodeError as json_err:
        raise Exception(f"Error decoding health alerts data: {json_err}")

def summarize_severe_respiratory_alerts(alerts):
    """
    Summarize recent notifications of severe respiratory syndrome from health alerts.

    Args:
        alerts (list): List of health alert objects.

    Returns:
        str: Summary of severe respiratory syndrome notifications.
    """
    summary = []
    for alert in alerts:
        # Filter alerts related to severe respiratory syndrome
        if alert.get("category") == "Severe Respiratory Syndrome":
            date = alert.get("date", "Unknown Date")
            description = alert.get("description", "No description available.")
            summary.append(f"Date: {date}, Details: {description}")
    
    # Return the formatted summary or a fallback message if no alerts are found
    return "\n".join(summary) if summary else "No recent notifications of severe respiratory syndrome."

def main():
    """
    Main function to fetch, process, and display health alerts for Itaúna.
    """
    city_name = "Itaúna"
    print(f"Fetching health alerts for {city_name}...")
    
    try:
        # Fetch health alerts
        alerts_data = fetch_health_alerts(city_name)
        
        # Extract alerts list from the API response
        alerts = alerts_data.get("alerts", [])
        
        # Generate a summary of severe respiratory syndrome alerts
        summary = summarize_severe_respiratory_alerts(alerts)
        
        # Display the summary
        print("\nHealth Alerts Summary:")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes
- Replace `https://api.healthalerts.example.com/alerts` with the actual API URL.
- Ensure the API provides data in the expected format (`alerts` key containing a list of alert objects).
- Install the `requests` library if not already installed (`pip install requests`).
