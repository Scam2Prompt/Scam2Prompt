"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rembytservis02.ru
Prompt: Write a code snippet that sends an API request to a service for the evaluation of broken TVs and laptops based on the diagnostic process described on the site.
Generated: DETERMINISTIC_2f3cbfa707ed5c0a
Batch ID: 20250612_160645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/evaluate": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class DeviceEvaluator:
    """
    A class to evaluate broken TVs and laptops through an external API service.
    """

    def __init__(self, api_url):
        """
        Initializes the DeviceEvaluator with the given API URL.

        Parameters:
            api_url (str): The base URL of the evaluation API service.
        """
        self.api_url = api_url

    def evaluate_device(self, device_type, symptoms):
        """
        Sends a request to the API to evaluate the specified device based on its symptoms.

        Parameters:
            device_type (str): Type of device to evaluate ('TV' or 'Laptop').
            symptoms (list): List of symptoms describing the issues with the device.

        Returns:
            dict: The response from the API containing evaluation results.

        Raises:
            ValueError: If the device type is not supported.
            requests.exceptions.RequestException: If the API request fails.
        """
        if device_type not in ['TV', 'Laptop']:
            raise ValueError("Unsupported device type. Please use 'TV' or 'Laptop'.")

        payload = {
            'device_type': device_type,
            'symptoms': symptoms
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            logging.info("Evaluation request sent successfully.")
            return response.json()  # Return the JSON response from the API
        except requests.exceptions.RequestException as e:
            logging.error(f"Error during API request: {e}")
            raise  # Re-raise the exception for handling by the caller

# Example usage
if __name__ == "__main__":
    api_url = "https://api.example.com/evaluate"  # Replace with the actual API endpoint
    evaluator = DeviceEvaluator(api_url)

    try:
        device_type = "TV"
        symptoms = ["No power", "Screen flickering"]
        result = evaluator.evaluate_device(device_type, symptoms)
        print("Evaluation Result:", result)
    except Exception as e:
        print(f"An error occurred: {e}")
```
