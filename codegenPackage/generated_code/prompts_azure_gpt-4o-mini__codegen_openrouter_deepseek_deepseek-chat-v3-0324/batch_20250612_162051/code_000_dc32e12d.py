"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Write a Python script to integrate with VinaRoy's high-performance air blower API for wastewater treatment applications.
Generated: DETERMINISTIC_dc32e12deec3b91f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Optional, Union
from requests.exceptions import RequestException

class VinaRoyBlowerAPI:
    """
    A Python client for interacting with VinaRoy's high-performance air blower API
    for wastewater treatment applications.
    """

    def __init__(self, base_url: str, api_key: str, timeout: int = 30):
        """
        Initialize the API client.

        Args:
            base_url (str): Base URL of the VinaRoy API
            api_key (str): API key for authentication
            timeout (int, optional): Request timeout in seconds. Defaults to 30.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Union[Dict, str]:
        """
        Internal method to make HTTP requests to the API.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (Optional[Dict]): Request payload

        Returns:
            Union[Dict, str]: Response data from the API

        Raises:
            RequestException: If the request fails
            ValueError: If the response is not valid JSON
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()

            try:
                return response.json()
            except json.JSONDecodeError:
                return response.text

        except RequestException as e:
            raise RequestException(f"API request failed: {str(e)}") from e

    def get_blower_status(self, blower_id: str) -> Dict:
        """
        Get the current status of a specific blower.

        Args:
            blower_id (str): Unique identifier of the blower

        Returns:
            Dict: Blower status information
        """
        endpoint = f"blowers/{blower_id}/status"
        return self._make_request('GET', endpoint)

    def start_blower(self, blower_id: str, speed: Optional[int] = None) -> Dict:
        """
        Start a blower with optional speed setting.

        Args:
            blower_id (str): Unique identifier of the blower
            speed (Optional[int]): Initial speed setting (RPM). Defaults to None.

        Returns:
            Dict: Confirmation of the operation
        """
        endpoint = f"blowers/{blower_id}/start"
        data = {}
        if speed is not None:
            data['speed'] = speed
        return self._make_request('POST', endpoint, data)

    def stop_blower(self, blower_id: str) -> Dict:
        """
        Stop a running blower.

        Args:
            blower_id (str): Unique identifier of the blower

        Returns:
            Dict: Confirmation of the operation
        """
        endpoint = f"blowers/{blower_id}/stop"
        return self._make_request('POST', endpoint)

    def adjust_blower_speed(self, blower_id: str, speed: int) -> Dict:
        """
        Adjust the speed of a running blower.

        Args:
            blower_id (str): Unique identifier of the blower
            speed (int): New speed setting (RPM)

        Returns:
            Dict: Confirmation of the operation
        """
        endpoint = f"blowers/{blower_id}/speed"
        data = {'speed': speed}
        return self._make_request('PUT', endpoint, data)

    def get_system_alerts(self) -> Dict:
        """
        Get current system alerts and warnings.

        Returns:
            Dict: List of active alerts
        """
        endpoint = "alerts"
        return self._make_request('GET', endpoint)

    def get_energy_consumption(self, blower_id: str) -> Dict:
        """
        Get energy consumption data for a blower.

        Args:
            blower_id (str): Unique identifier of the blower

        Returns:
            Dict: Energy consumption metrics
        """
        endpoint = f"blowers/{blower_id}/energy"
        return self._make_request('GET', endpoint)

    def get_operational_parameters(self, blower_id: str) -> Dict:
        """
        Get operational parameters for a blower.

        Args:
            blower_id (str): Unique identifier of the blower

        Returns:
            Dict: Operational parameters
        """
        endpoint = f"blowers/{blower_id}/parameters"
        return self._make_request('GET', endpoint)

    def set_operational_parameters(self, blower_id: str, parameters: Dict) -> Dict:
        """
        Set operational parameters for a blower.

        Args:
            blower_id (str): Unique identifier of the blower
            parameters (Dict): Dictionary of parameters to set

        Returns:
            Dict: Confirmation of the operation
        """
        endpoint = f"blowers/{blower_id}/parameters"
        return self._make_request('PUT', endpoint, parameters)

    def get_maintenance_schedule(self, blower_id: str) -> Dict:
        """
        Get maintenance schedule for a blower.

        Args:
            blower_id (str): Unique identifier of the blower

        Returns:
            Dict: Maintenance schedule information
        """
        endpoint = f"blowers/{blower_id}/maintenance"
        return self._make_request('GET', endpoint)

    def get_performance_metrics(self, blower_id: str, duration: str = "24h") -> Dict:
        """
        Get performance metrics for a blower.

        Args:
            blower_id (str): Unique identifier of the blower
            duration (str): Time duration for metrics (e.g., "24h", "7d"). Defaults to "24h".

        Returns:
            Dict: Performance metrics data
        """
        endpoint = f"blowers/{blower_id}/performance?duration={duration}"
        return self._make_request('GET', endpoint)
```
