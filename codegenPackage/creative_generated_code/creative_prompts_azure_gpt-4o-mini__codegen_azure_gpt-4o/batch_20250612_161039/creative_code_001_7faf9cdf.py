"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Write a code snippet that demonstrates how to submit a vulnerability report using the Bugcrowd API, referencing the bug bounty portfolio of Karl Franklyn Aparece.
Generated: DETERMINISTIC_7faf9cdf8a4ae53e
Batch ID: 20250612_161039
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.bugcrowd.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/login": {
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

# Define constants for Bugcrowd API
BUGCROWD_API_BASE_URL = "https://api.bugcrowd.com/v1"
BUGCROWD_API_KEY = "your-api-key-here"  # Replace this with your actual API key
BUG_BOUNTY_PORTFOLIO = "Karl Franklyn Aparece"  # Replace with the actual portfolio name

# Function to submit a vulnerability report
def submit_vulnerability_report(title, description, severity, asset):
    """
    Submits a vulnerability report to Bugcrowd.
    
    :param title: Title of the vulnerability report.
    :param description: Detailed description of the vulnerability.
    :param severity: Severity level of the vulnerability ('low', 'medium', 'high', etc.).
    :param asset: The affected asset (e.g., URL, application name, etc.).
    :return: Response from the Bugcrowd API.
    """
    # Endpoint for submitting vulnerability reports
    endpoint = f"{BUGCROWD_API_BASE_URL}/reports"
    
    # Prepare the report payload
    payload = {
        "portfolio": BUG_BOUNTY_PORTFOLIO,  # Bug bounty portfolio name
        "title": title,
        "description": description,
        "severity": severity,
        "asset": asset
    }
    
    # Prepare the request headers
    headers = {
        "Authorization": f"Bearer {BUGCROWD_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send the POST request to the Bugcrowd API
        response = requests.post(endpoint, json=payload, headers=headers)
        
        # Raise an exception if the response has an error status
        response.raise_for_status()
        
        # Return the response JSON if successful
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log and return the error message
        print(f"Error submitting vulnerability report: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Define the vulnerability details
    title = "SQL Injection in Login Form"
    description = (
        "The login form is vulnerable to SQL injection attacks. "
        "An attacker can gain unauthorized access to the database by injecting malicious SQL queries."
    )
    severity = "high"
    asset = "https://example.com/login"

    # Submit the vulnerability report
    result = submit_vulnerability_report(title, description, severity, asset)

    # Print the result
    print("Bugcrowd API Response:", result)
```

**Note:** Replace `your-api-key-here` with your actual Bugcrowd API key, and ensure that the `portfolio` name matches the correct portfolio for Karl Franklyn Aparece.
