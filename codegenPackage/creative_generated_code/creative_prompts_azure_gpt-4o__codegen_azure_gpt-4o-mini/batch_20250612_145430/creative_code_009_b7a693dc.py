"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-fork-marekhauzr-main-419labs.vercel.app
Prompt: Write code to interact with StarkEx projects within the StarkNet ecosystem, using APIs or libraries referenced on the webpage.
Generated: DETERMINISTIC_b7a693dc82ac2b5f
Batch ID: 20250612_145430
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starkex.com/v1": {
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

class StarkExAPI:
    """
    A class to interact with the StarkEx API for projects within the StarkNet ecosystem.
    """

    BASE_URL = "https://api.starkex.com/v1"  # Base URL for the StarkEx API

    def __init__(self, api_key):
        """
        Initializes the StarkExAPI class with the provided API key.

        :param api_key: str - The API key for authenticating requests
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Helper method to make an API request.

        :param endpoint: str - The API endpoint to call
        :param method: str - The HTTP method to use (GET, POST, etc.)
        :param data: dict - The data to send with the request (for POST requests)

        :return: dict - The JSON response from the server
        :raises Exception: If the request fails or the response is invalid
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method")

            # Raise an error for bad responses
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except ValueError as ve:
            raise Exception(f"Invalid response: {str(ve)}")

    def get_project_info(self, project_id):
        """
        Fetches project information by project ID.

        :param project_id: str - The ID of the StarkEx project

        :return: dict - The project information
        """
        endpoint = f"projects/{project_id}"
        return self._make_request(endpoint)

    def create_order(self, order_data):
        """
        Creates a new order in the StarkEx ecosystem.

        :param order_data: dict - The data for the new order

        :return: dict - The response indicating the result of the order creation
        """
        endpoint = "orders"
        return self._make_request(endpoint, method='POST', data=order_data)

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    starkex_api = StarkExAPI(API_KEY)

    try:
        # Fetch project information
        project_info = starkex_api.get_project_info("project_id_here")  # Replace with actual project ID
        print("Project Info:", project_info)

        # Create a new order
        new_order = {
            "amount": 100,
            "currency": "ETH",
            "user_id": "user_id_here"  # Replace with actual user ID
        }
        order_response = starkex_api.create_order(new_order)
        print("Order Response:", order_response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
