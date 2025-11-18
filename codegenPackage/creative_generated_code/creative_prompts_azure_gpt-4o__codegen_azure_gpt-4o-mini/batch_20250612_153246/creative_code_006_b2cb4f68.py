"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saisbank.com
Prompt: Suggest methods for integrating Thermomed's cabin tracking system with external reporting tools or databases.
Generated: DETERMINISTIC_b2cb4f68cf5cecbb
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
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
import json
import requests
from typing import Any, Dict, List

class CabinTrackingIntegration:
    def __init__(self, api_url: str):
        """
        Initialize the integration with the given API URL.

        :param api_url: The base URL for the external reporting tool or database API.
        """
        self.api_url = api_url

    def fetch_cabin_data(self) -> List[Dict[str, Any]]:
        """
        Fetch cabin tracking data from Thermomed's system.

        :return: A list of cabin tracking records.
        :raises Exception: If data fetching fails.
        """
        try:
            response = requests.get(f"{self.api_url}/cabin-tracking")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch cabin data: {str(e)}")

    def transform_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform the data to match the format required by the external reporting tool.

        :param data: The raw cabin tracking data.
        :return: The transformed data.
        """
        transformed_data = []
        for record in data:
            transformed_record = {
                "cabin_id": record.get("id"),
                "status": record.get("status"),
                "timestamp": record.get("timestamp"),
                "location": {
                    "latitude": record.get("location").get("lat"),
                    "longitude": record.get("location").get("lon"),
                }
            }
            transformed_data.append(transformed_record)
        return transformed_data

    def send_data_to_reporting_tool(self, transformed_data: List[Dict[str, Any]]) -> None:
        """
        Send the transformed data to the external reporting tool or database.

        :param transformed_data: The data to be sent.
        :raises Exception: If data sending fails.
        """
        try:
            response = requests.post(f"{self.api_url}/reporting", json=transformed_data)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            raise Exception(f"Failed to send data to reporting tool: {str(e)}")

    def integrate(self) -> None:
        """
        Execute the integration process: fetch, transform, and send data.
        """
        try:
            raw_data = self.fetch_cabin_data()
            transformed_data = self.transform_data(raw_data)
            self.send_data_to_reporting_tool(transformed_data)
            print("Data integration completed successfully.")
        except Exception as e:
            print(f"Integration process failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    api_url = "https://example.com/api"  # Replace with the actual API URL
    integration = CabinTrackingIntegration(api_url)
    integration.integrate()
```
