"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigwizt.top
Prompt: Provide code examples for integrating aaPanel with third-party monitoring tools via its API.
Generated: DETERMINISTIC_86b384d48f155f8e
Batch ID: 20250612_154002
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://your-monitoring-tool-url/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://your-aapanel-url:8888/api": {
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
"""
This script demonstrates how to integrate aaPanel with a third-party monitoring tool
by utilizing aaPanel's API to retrieve system information.
Ensure to replace placeholders with valid values for your aaPanel setup.
"""

import requests

# Constants for aaPanel API
AAPANEL_API_URL = "http://your-aapanel-url:8888/api"
API_KEY = "your-aapanel-api-key"

# Function to make a request to the aaPanel API
def call_aapanel_api(endpoint, params=None):
    """
    Makes a request to the aaPanel API.
    
    Args:
        endpoint (str): The specific API endpoint to call.
        params (dict): Parameters to include in the request.

    Returns:
        dict: Response data from the API, or an error message on failure.
    """
    try:
        # Default parameters with API key
        if params is None:
            params = {}
        params['access_key'] = API_KEY

        # Sending the request
        response = requests.post(f"{AAPANEL_API_URL}/{endpoint}", data=params)

        # Raise error if request fails
        response.raise_for_status()

        # Parse JSON response
        response_data = response.json()

        # Check for API errors
        if response_data.get('status') is False:
            raise Exception(f"API Error: {response_data.get('msg')}")
        
        return response_data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

# Example: Get disk information from aaPanel API
def get_disk_info():
    """
    Retrieves disk information from aaPanel.

    Returns:
        dict: Disk information data or error message.
    """
    endpoint = "system?action=GetDiskInfo"
    return call_aapanel_api(endpoint)

# Example: Get CPU load information from aaPanel API
def get_cpu_info():
    """
    Retrieves CPU load information from aaPanel.

    Returns:
        dict: CPU load data or error message.
    """
    endpoint = "system?action=GetCpuInfo"
    return call_aapanel_api(endpoint)

# Example: Integration with a third-party monitoring tool
def integrate_with_monitoring_tool(data):
    """
    Sends data retrieved from aaPanel to a third-party monitoring tool.
    
    Args:
        data (dict): The data to be sent.

    Returns:
        bool: True if data is successfully sent, False otherwise.
    """
    try:
        # Replace with your monitoring tool's endpoint
        monitoring_tool_url = "http://your-monitoring-tool-url/api"

        # Send data to the monitoring tool
        response = requests.post(monitoring_tool_url, json=data)
        response.raise_for_status()

        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data to monitoring tool: {e}")
        return False

# Main function
def main():
    """
    Main execution function for integrating aaPanel with monitoring tools.
    """
    # Get system information from aaPanel
    disk_info = get_disk_info()
    cpu_info = get_cpu_info()

    # Check for errors in the aaPanel responses
    if "error" in disk_info:
        print(f"Failed to retrieve disk info: {disk_info['error']}")
        return
    if "error" in cpu_info:
        print(f"Failed to retrieve CPU info: {cpu_info['error']}")
        return

    # Combine data for the monitoring tool
    system_data = {
        "disk_info": disk_info,
        "cpu_info": cpu_info
    }

    # Integrate with third-party monitoring tool
    success = integrate_with_monitoring_tool(system_data)
    if success:
        print("Successfully sent data to monitoring tool.")
    else:
        print("Failed to send data to monitoring tool.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
