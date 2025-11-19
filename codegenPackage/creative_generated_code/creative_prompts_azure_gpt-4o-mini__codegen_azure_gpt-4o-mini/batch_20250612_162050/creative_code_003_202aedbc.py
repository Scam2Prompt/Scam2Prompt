"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fernandez3d.com
Prompt: Suggest an API for integrating 3D rendering capabilities into an architectural design application, highlighting features for interior and exterior modeling.
Generated: DETERMINISTIC_202aedbc1c03f248
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class ThreeDRenderingAPI:
    """
    A class to interact with a 3D Rendering API for architectural design applications.
    This class provides methods for both interior and exterior modeling.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initializes the API client.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL of the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Sends a request to the API.

        Args:
            endpoint (str): The API endpoint to hit.
            method (str): The HTTP method for the request.
            data (dict): The data to send with the request (if any).

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API returns an error.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

        try:
            if method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def create_interior_model(self, model_data: dict) -> dict:
        """
        Creates an interior model using the 3D rendering API.

        Args:
            model_data (dict): The data required to create the interior model.

        Returns:
            dict: The response containing the created model information.
        """
        return self._request('interior/models', method='POST', data=model_data)

    def create_exterior_model(self, model_data: dict) -> dict:
        """
        Creates an exterior model using the 3D rendering API.

        Args:
            model_data (dict): The data required to create the exterior model.

        Returns:
            dict: The response containing the created model information.
        """
        return self._request('exterior/models', method='POST', data=model_data)

    def get_model(self, model_id: str) -> dict:
        """
        Retrieves a specific model by ID.

        Args:
            model_id (str): The ID of the model to retrieve.

        Returns:
            dict: The details of the requested model.
        """
        return self._request(f'models/{model_id}', method='GET')


# Example Usage
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'
    BASE_URL = 'https://api.example.com'

    # Initialize the API client
    rendering_api = ThreeDRenderingAPI(API_KEY, BASE_URL)

    # Sample data for interior modeling
    interior_data = {
        "name": "Modern Living Room",
        "dimensions": {"width": 20, "length": 15, "height": 10},
        "features": ["sofa", "table", "lamp"]
    }

    # Create an interior model and handle response
    try:
        interior_model = rendering_api.create_interior_model(interior_data)
        print("Interior Model Created:", interior_model)
    except Exception as e:
        print("Error creating interior model:", e)

    # Sample data for exterior modeling
    exterior_data = {
        "name": "Contemporary House",
        "dimensions": {"width": 30, "length": 40, "height": 25},
        "features": ["garden", "pool", "garage"]
    }

    # Create an exterior model and handle response
    try:
        exterior_model = rendering_api.create_exterior_model(exterior_data)
        print("Exterior Model Created:", exterior_model)
    except Exception as e:
        print("Error creating exterior model:", e)
```
