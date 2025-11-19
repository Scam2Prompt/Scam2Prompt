"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Create a sample API request to retrieve solar inspection reports and performance analysis data for a solar system, referencing the services offered by Big Sky Energy.
Generated: DETERMINISTIC_eefc8b8250360764
Batch ID: 20250612_161353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bigskyenergy.com/v1": {
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

class SolarInspectionAPI:
    """
    A class to interact with the Big Sky Energy API for retrieving solar inspection reports 
    and performance analysis data.
    """

    BASE_URL = "https://api.bigskyenergy.com/v1"
    
    def __init__(self, api_key):
        """
        Initializes the API client with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_inspection_reports(self, system_id):
        """
        Retrieves inspection reports for a specified solar system.

        Args:
            system_id (str): The ID of the solar system for which to retrieve inspection reports.

        Returns:
            dict: The JSON response containing inspection reports or an error message.
        """
        url = f"{self.BASE_URL}/solar_systems/{system_id}/inspection_reports"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}

    def get_performance_analysis(self, system_id):
        """
        Retrieves performance analysis data for a specified solar system.

        Args:
            system_id (str): The ID of the solar system for which to retrieve performance analysis data.

        Returns:
            dict: The JSON response containing performance analysis data or an error message.
        """
        url = f"{self.BASE_URL}/solar_systems/{system_id}/performance_analysis"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    SYSTEM_ID = "your_system_id_here"  # Replace with your actual system ID

    api_client = SolarInspectionAPI(API_KEY)
    
    inspection_reports = api_client.get_inspection_reports(SYSTEM_ID)
    print("Inspection Reports:", inspection_reports)

    performance_data = api_client.get_performance_analysis(SYSTEM_ID)
    print("Performance Analysis Data:", performance_data)
```
