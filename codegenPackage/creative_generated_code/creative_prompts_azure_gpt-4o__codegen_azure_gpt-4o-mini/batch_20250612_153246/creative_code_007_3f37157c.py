"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saisbank.com
Prompt: Develop a REST API client in Python to interact with the Thermomed Sürekli Atık Su İzleme ve Ölçüm Sistemleri platform for data analysis.
Generated: DETERMINISTIC_3f37157c45d09cfa
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thermomed.com": {
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
from requests.exceptions import HTTPError, RequestException


class ThermomedAPIClient:
    """
    A client for interacting with the Thermomed Sürekli Atık Su İzleme ve Ölçüm Sistemleri platform 
    for data analysis through a REST API.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client with the base URL and API key.

        :param base_url: The base URL for the Thermomed API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', params=None, data=None):
        """
        Makes a request to the Thermomed API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param params: The query parameters for the request.
        :param data: The body data for the request (for POST, PUT).
        :return: The response JSON if successful, else raises an error.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}

        try:
            response = requests.request(method, url, headers=headers, params=params, json=data)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Parse and return JSON response
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

    def get_sensor_data(self, sensor_id, start_time=None, end_time=None):
        """
        Retrieve data from a specific sensor.

        :param sensor_id: The ID of the sensor to retrieve data from.
        :param start_time: (Optional) The start time for data retrieval in ISO format.
        :param end_time: (Optional) The end time for data retrieval in ISO format.
        :return: The sensor data in JSON format.
        """
        params = {
            'start_time': start_time,
            'end_time': end_time
        }
        return self._make_request(f'sensors/{sensor_id}/data', params=params)

    def get_all_sensors(self):
        """
        Retrieve a list of all sensors.

        :return: A list of sensors in JSON format.
        """
        return self._make_request('sensors')

    def analyze_data(self, sensor_id):
        """
        Perform data analysis on the specific sensor data.

        :param sensor_id: The ID of the sensor to analyze data from.
        :return: The analysis results in JSON format.
        """
        return self._make_request(f'sensors/{sensor_id}/analyze', method='POST')


if __name__ == "__main__":
    # Example usage of the ThermomedAPIClient
    BASE_URL = "https://api.thermomed.com"  # Replace with the actual API base URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    client = ThermomedAPIClient(BASE_URL, API_KEY)

    try:
        # Get all sensors
        sensors = client.get_all_sensors()
        print("Available Sensors:", sensors)

        # Example: Getting data for a specific sensor
        sensor_id = "sensor_123"  # Replace with a valid sensor ID
        data = client.get_sensor_data(sensor_id, start_time="2023-10-01T00:00:00Z", end_time="2023-10-02T00:00:00Z")
        print("Sensor Data:", data)

        # Example: Analyzing data from a specific sensor
        analysis_result = client.analyze_data(sensor_id)
        print("Analysis Result:", analysis_result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
