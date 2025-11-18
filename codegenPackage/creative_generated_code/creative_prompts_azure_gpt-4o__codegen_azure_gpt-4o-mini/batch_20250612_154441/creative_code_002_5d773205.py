"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Create a Python script using the DHL Express API to calculate shipping costs for championship belts worldwide, as offered by Belts Mania.
Generated: DETERMINISTIC_5d7732055e8b2a46
Batch ID: 20250612_154441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dhl.com": {
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

class DHLExpressAPI:
    """
    A class to interact with the DHL Express API for calculating shipping costs.
    """

    def __init__(self, api_key: str):
        """
        Initializes the DHLExpressAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the DHL Express API.
        """
        self.api_key = api_key
        self.base_url = "https://api.dhl.com"  # Base URL for the DHL API

    def calculate_shipping_cost(self, weight: float, dimensions: tuple, origin: str, destination: str) -> float:
        """
        Calculates the shipping cost for a package.

        Args:
            weight (float): The weight of the package in kilograms.
            dimensions (tuple): A tuple containing the dimensions of the package (length, width, height) in centimeters.
            origin (str): The origin postal code.
            destination (str): The destination postal code.

        Returns:
            float: The calculated shipping cost.

        Raises:
            Exception: If the API call fails or returns an error.
        """
        url = f"{self.base_url}/shipments/calculate"

        headers = {
            "DHL-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

        # Prepare the payload for the API request
        payload = {
            "weight": weight,
            "dimensions": {
                "length": dimensions[0],
                "width": dimensions[1],
                "height": dimensions[2]
            },
            "origin": origin,
            "destination": destination
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse and return the shipping cost from the response
            shipping_cost = response.json().get('cost', 0.0)
            return shipping_cost
        
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Raise an error for HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Raise a general error


def main():
    """
    Main function to calculate shipping costs for championship belts.
    """
    # Instantiate the DHL Express API client with your API key
    api_key = "YOUR_DHL_API_KEY"  # Replace with your actual DHL API key
    dhl_api = DHLExpressAPI(api_key)

    # Define the shipping parameters
    weight = 1.2  # Weight in kilograms
    dimensions = (30, 10, 5)  # Dimensions in centimeters (length, width, height)
    origin = "10001"  # Example origin postal code (New York, NY)
    destination = "90210"  # Example destination postal code (Beverly Hills, CA)

    try:
        # Calculate the shipping cost
        cost = dhl_api.calculate_shipping_cost(weight, dimensions, origin, destination)
        print(f"The shipping cost for the championship belt is: ${cost:.2f}")

    except Exception as e:
        print(f"Error calculating shipping cost: {e}")


if __name__ == "__main__":
    main()
```
