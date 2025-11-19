"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assisterr.io
Prompt: Write a Python script that interacts with Assisterr's AI Agent Incubator to create and manage specialized language models.
Generated: DETERMINISTIC_78fe4f5afc5e5629
Batch ID: 20250612_163854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.assisterr.com/v1/models": {
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

class AIModelManager:
    """
    A class to manage the creation and interaction with specialized language models
    using Assisterr's AI Agent Incubator API.
    """

    BASE_URL = "https://api.assisterr.com/v1/models"

    def __init__(self, api_key):
        """
        Initializes the AIModelManager with an API key.

        :param api_key: str - API key for authentication
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_model(self, model_name, model_type, training_data):
        """
        Creates a new specialized language model.

        :param model_name: str - Name of the model to be created
        :param model_type: str - Type of the model (e.g., 'text', 'chat')
        :param training_data: list - List of training data samples
        :return: dict - Response from the API
        """
        data = {
            "name": model_name,
            "type": model_type,
            "training_data": training_data
        }
        response = requests.post(self.BASE_URL, headers=self.headers, data=json.dumps(data))
        
        # Error handling for API request
        if response.status_code != 201:
            self._handle_error(response)
        
        return response.json()

    def get_model(self, model_id):
        """
        Retrieves information about a specific language model.

        :param model_id: str - ID of the model to retrieve
        :return: dict - Model information
        """
        response = requests.get(f"{self.BASE_URL}/{model_id}", headers=self.headers)
        
        # Error handling for API request
        if response.status_code != 200:
            self._handle_error(response)
        
        return response.json()

    def delete_model(self, model_id):
        """
        Deletes a specified language model.

        :param model_id: str - ID of the model to delete
        :return: bool - True if deletion was successful, False otherwise
        """
        response = requests.delete(f"{self.BASE_URL}/{model_id}", headers=self.headers)
        
        # Error handling for API request
        if response.status_code != 204:
            self._handle_error(response)
        
        return True

    def _handle_error(self, response):
        """
        Handles errors from API responses.

        :param response: Response - The API response object
        :raises RuntimeError: If an error occurs
        """
        error_message = response.json().get("error", "Unknown error")
        status_code = response.status_code
        raise RuntimeError(f"Error {status_code}: {error_message}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    manager = AIModelManager(API_KEY)

    # Create a new model
    try:
        new_model = manager.create_model("SpecializedModel", "text", ["Sample training data."])
        print("Model created:", new_model)

        # Retrieve the model information
        model_info = manager.get_model(new_model["id"])
        print("Model information:", model_info)

        # Delete the model
        delete_success = manager.delete_model(new_model["id"])
        print("Model deleted successfully:", delete_success)

    except RuntimeError as e:
        print("An error occurred:", e)
```
