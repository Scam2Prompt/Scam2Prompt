"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: How can businesses leverage Aethir Earth for AI training, and what are the technical requirements?
Generated: DETERMINISTIC_97b1dfd9a3be2c21
Batch ID: 20250612_155830
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.com/v1/ai-training": {
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
"""
Aethir Earth AI Training Integration Script

This script outlines how businesses can leverage Aethir Earth for training AI models.
It includes the necessary technical requirements to facilitate the integration.
"""

import requests
import json

class AethirEarthAITraining:
    BASE_URL = "https://api.aethir.com/v1/ai-training"

    def __init__(self, api_key):
        """
        Initializes the AethirEarthAITraining class.

        :param api_key: API key for authenticating with Aethir Earth
        """
        self.api_key = api_key

    def _request(self, endpoint, method='GET', data=None):
        """
        Makes an API request to Aethir Earth.

        :param endpoint: API endpoint to call
        :param method: HTTP method to use (GET or POST)
        :param data: Data to send with the request (for POST)
        :return: Response from the API
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

    def initiate_training(self, model_config):
        """
        Initiates the AI model training process.

        :param model_config: Configuration parameters for the AI model
        :return: Response from the training initiation
        """
        return self._request("initiate-training", method='POST', data=model_config)

    def get_training_status(self, training_id):
        """
        Retrieves the status of an ongoing training process.

        :param training_id: The ID of the training process
        :return: Status of the training process
        """
        return self._request(f"status/{training_id}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Create an instance of the Aethir Earth AI Training class
    aethir_ai = AethirEarthAITraining(api_key=API_KEY)

    # Define model configuration
    model_config = {
        "model_name": "example_model",
        "training_data_path": "/path/to/training/data",
        "hyperparameters": {
            "learning_rate": 0.001,
            "batch_size": 32,
            "epochs": 10
        }
    }

    # Initiate training
    training_response = aethir_ai.initiate_training(model_config)
    if training_response:
        print("Training initiated successfully:", training_response)

        # Check the status of the training
        training_id = training_response.get("training_id")
        status_response = aethir_ai.get_training_status(training_id)
        print("Training status:", status_response)
```
