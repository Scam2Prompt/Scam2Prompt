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
  "https://monitoring-tool-url.com/api/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-aapanel-url.com/api": {
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

class AAPanelAPI:
    """
    A class to interact with aaPanel's API for server monitoring integration.
    """

    def __init__(self, api_url, api_token):
        """
        Initializes the AAPanelAPI with the given API URL and token.

        :param api_url: str - The base URL for the aaPanel API.
        :param api_token: str - The API token for authentication.
        """
        self.api_url = api_url
        self.api_token = api_token

    def _send_request(self, endpoint, method='GET', data=None):
        """
        Sends a request to the aaPanel API.

        :param endpoint: str - The API endpoint to interact with.
        :param method: str - The HTTP method to use ('GET', 'POST', etc.).
        :param data: dict - The data to send with the request (for POST requests).
        :return: dict - The JSON response from the API.
        :raises Exception: If an error occurs during the API request.
        """
        url = f"{self.api_url}/{endpoint}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }

        try:
            if method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

    def get_system_info(self):
        """
        Retrieves system information from aaPanel.

        :return: dict - System information data.
        """
        return self._send_request('getSystemInfo')

    def get_service_status(self):
        """
        Retrieves the status of services from aaPanel.

        :return: dict - Service status data.
        """
        return self._send_request('getServiceStatus')

    def get_resource_usage(self):
        """
        Retrieves resource usage statistics from aaPanel.

        :return: dict - Resource usage data.
        """
        return self._send_request('getResourceUsage')

    def integrate_with_monitoring_tool(self, monitoring_tool_url, resource_data):
        """
        Sends resource data to a third-party monitoring tool.

        :param monitoring_tool_url: str - The endpoint of the third-party monitoring tool.
        :param resource_data: dict - The resource data to send.
        :raises Exception: If an error occurs during the integration process.
        """
        try:
            response = requests.post(monitoring_tool_url, json=resource_data)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred while sending data to monitoring tool: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred while integrating with monitoring tool: {err}")

# Example usage:
if __name__ == "__main__":
    api_url = "https://your-aapanel-url.com/api"  # Replace with your aaPanel API URL
    api_token = "your_api_token"                    # Replace with your aaPanel API token

    # Initialize the AAPanelAPI
    aa_panel = AAPanelAPI(api_url, api_token)

    try:
        # Get system information
        system_info = aa_panel.get_system_info()
        print("System Info:", system_info)

        # Get service status
        service_status = aa_panel.get_service_status()
        print("Service Status:", service_status)

        # Get resource usage
        resource_usage = aa_panel.get_resource_usage()
        print("Resource Usage:", resource_usage)

        # Example integration with a monitoring tool
        monitoring_tool_url = "https://monitoring-tool-url.com/api/data"
        aa_panel.integrate_with_monitoring_tool(monitoring_tool_url, resource_usage)

    except Exception as e:
        print(f"An error occurred: {e}")
```
