"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Generate code to test the uptime and response of a web server that displays "Success! Your new web server is ready to use." using Python's requests library.
Generated: DETERMINISTIC_6987c0f5b448b359
Batch ID: 20250612_151239
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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
from datetime import datetime

def test_web_server(url):
    """
    Tests the uptime and response of a web server.
    
    Parameters:
        url (str): The URL of the web server to test.

    Returns:
        dict: A dictionary containing the status code, response time, and success status.
    """
    try:
        # Record the start time for response time calculation
        start_time = datetime.now()
        
        # Make a GET request to the provided URL
        response = requests.get(url)
        
        # Record the end time for response time calculation
        end_time = datetime.now()
        
        # Calculate response time in milliseconds
        response_time_ms = (end_time - start_time).total_seconds() * 1000
        
        # Extract and verify response content
        is_success = "Success! Your new web server is ready to use." in response.text
        
        # Return the test results in a structured format
        return {
            "status_code": response.status_code,
            "response_time_ms": response_time_ms,
            "is_success": is_success
        }
    except requests.exceptions.RequestException as e:
        # Handle request errors and return relevant details
        return {
            "error": str(e),
            "status_code": None,
            "response_time_ms": None,
            "is_success": False
        }

if __name__ == "__main__":
    # Define the target web server URL
    target_url = "http://example.com"  # Replace with the actual URL
    
    # Run the test
    result = test_web_server(target_url)
    
    # Print the results
    if "error" in result:
        print(f"Error occurred while testing the server: {result['error']}")
    else:
        print(f"Status Code: {result['status_code']}")
        print(f"Response Time: {result['response_time_ms']} ms")
        print(f"Is Success Response: {result['is_success']}")
```
