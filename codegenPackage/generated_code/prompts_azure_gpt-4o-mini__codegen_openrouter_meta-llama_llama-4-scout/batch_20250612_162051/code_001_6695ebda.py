"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Write a Python script that interacts with an API to retrieve detailed information about high-performance vehicles, focusing on features like historical data and condition checks as highlighted by Galopin Automobile.
Generated: DETERMINISTIC_6695ebda5cd65a4f
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.galopin-automobile.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json

class VehicleAPI:
    """
    A class used to interact with the Galopin Automobile API.

    Attributes:
    ----------
    api_url : str
        The base URL of the Galopin Automobile API.
    api_key : str
        The API key for authentication.

    Methods:
    -------
    get_vehicle_info(vehicle_id)
        Retrieves detailed information about a vehicle.
    get_historical_data(vehicle_id)
        Retrieves historical data about a vehicle.
    perform_condition_check(vehicle_id)
        Performs a condition check on a vehicle.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the VehicleAPI class.

        Parameters:
        ----------
        api_url : str
            The base URL of the Galopin Automobile API.
        api_key : str
            The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_vehicle_info(self, vehicle_id):
        """
        Retrieves detailed information about a vehicle.

        Parameters:
        ----------
        vehicle_id : str
            The ID of the vehicle.

        Returns:
        -------
        dict
            A dictionary containing the vehicle's information.

        Raises:
        ------
        requests.exceptions.RequestException
            If the API request fails.
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(f'{self.api_url}/vehicles/{vehicle_id}', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_historical_data(self, vehicle_id):
        """
        Retrieves historical data about a vehicle.

        Parameters:
        ----------
        vehicle_id : str
            The ID of the vehicle.

        Returns:
        -------
        dict
            A dictionary containing the vehicle's historical data.

        Raises:
        ------
        requests.exceptions.RequestException
            If the API request fails.
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(f'{self.api_url}/vehicles/{vehicle_id}/history', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def perform_condition_check(self, vehicle_id):
        """
        Performs a condition check on a vehicle.

        Parameters:
        ----------
        vehicle_id : str
            The ID of the vehicle.

        Returns:
        -------
        dict
            A dictionary containing the vehicle's condition check results.

        Raises:
        ------
        requests.exceptions.RequestException
            If the API request fails.
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.post(f'{self.api_url}/vehicles/{vehicle_id}/condition-check', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


def main():
    api_url = 'https://api.galopin-automobile.com/v1'
    api_key = 'your_api_key_here'
    vehicle_id = 'vehicle_id_here'

    vehicle_api = VehicleAPI(api_url, api_key)

    vehicle_info = vehicle_api.get_vehicle_info(vehicle_id)
    print("Vehicle Info:")
    print(json.dumps(vehicle_info, indent=4))

    historical_data = vehicle_api.get_historical_data(vehicle_id)
    print("\nHistorical Data:")
    print(json.dumps(historical_data, indent=4))

    condition_check_results = vehicle_api.perform_condition_check(vehicle_id)
    print("\nCondition Check Results:")
    print(json.dumps(condition_check_results, indent=4))


if __name__ == "__main__":
    main()
```
