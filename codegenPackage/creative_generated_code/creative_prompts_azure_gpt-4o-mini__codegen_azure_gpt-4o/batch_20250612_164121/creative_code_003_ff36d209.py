"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://precipitateai.web.app
Prompt: Create an API call to interact with the Precipitate infrastructure for managing AI data on public blockchains.
Generated: DETERMINISTIC_ff36d209a1925200
Batch ID: 20250612_164121
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.precipitate.io": {
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

class PrecipitateAPI:
    """
    A class to interact with the Precipitate infrastructure for managing AI data on public blockchains.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client.

        Args:
            base_url (str): The base URL of the Precipitate API.
            api_key (str): API key for authentication.
        """
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def make_request(self, endpoint, method="GET", payload=None):
        """
        Makes an API call to the specified endpoint.

        Args:
            endpoint (str): API endpoint to interact with.
            method (str): HTTP method (GET, POST, PUT, DELETE). Default is "GET".
            payload (dict): Data to send with the request. Default is None.

        Returns:
            dict: Response from the API.
        """
        url = f"{self.base_url}/{endpoint}"

        try:
            # Choose the appropriate HTTP method
            if method.upper() == "GET":
                response = requests.get(url, headers=self.headers)
            elif method.upper() == "POST":
                response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            elif method.upper() == "PUT":
                response = requests.put(url, headers=self.headers, data=json.dumps(payload))
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError("Invalid HTTP method specified.")

            # Raise exception for HTTP errors
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the API request: {e}")
            return {"error": str(e)}
        except ValueError as ve:
            print(f"Value error: {ve}")
            return {"error": str(ve)}

    def upload_ai_data(self, data):
        """
        Uploads AI data to the blockchain via Precipitate.

        Args:
            data (dict): The AI data to be uploaded.

        Returns:
            dict: Response from the API.
        """
        endpoint = "upload-ai-data"
        return self.make_request(endpoint, method="POST", payload=data)

    def retrieve_ai_data(self, data_id):
        """
        Retrieves AI data from the blockchain.

        Args:
            data_id (str): The ID of the data to retrieve.

        Returns:
            dict: Response from the API.
        """
        endpoint = f"retrieve-ai-data/{data_id}"
        return self.make_request(endpoint, method="GET")

    def delete_ai_data(self, data_id):
        """
        Deletes AI data from the blockchain.

        Args:
            data_id (str): The ID of the data to delete.

        Returns:
            dict: Response from the API.
        """
        endpoint = f"delete-ai-data/{data_id}"
        return self.make_request(endpoint, method="DELETE")


# Example usage:
if __name__ == "__main__":
    # Replace with actual base URL and API key
    BASE_URL = "https://api.precipitate.io"
    API_KEY = "your_api_key_here"

    # Initialize the API client
    api_client = PrecipitateAPI(BASE_URL, API_KEY)

    # Example to upload AI data
    ai_data = {
        "name": "Sample AI Model",
        "description": "A sample model for demonstration purposes.",
        "data": {
            "type": "model",
            "metadata": {
                "creator": "John Doe",
                "version": "1.0"
            }
        }
    }
    upload_response = api_client.upload_ai_data(ai_data)
    print("Upload Response:", upload_response)

    # Example to retrieve AI data
    data_id = "12345"
    retrieve_response = api_client.retrieve_ai_data(data_id)
    print("Retrieve Response:", retrieve_response)

    # Example to delete AI data
    delete_response = api_client.delete_ai_data(data_id)
    print("Delete Response:", delete_response)
```
