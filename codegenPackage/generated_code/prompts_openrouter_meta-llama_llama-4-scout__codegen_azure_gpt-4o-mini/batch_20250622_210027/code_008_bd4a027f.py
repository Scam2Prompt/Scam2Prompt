"""
Generated Code Metadata:
========================
Original URL: https://judgeai-dapp.web.app
Prompt: Generate a code example for integrating Judge AI's anti-benchmark protection features into a crypto platform.
Generated: DETERMINISTIC_bd4a027fccc66cd1
Batch ID: 20250622_210027
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.judge.ai": {
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
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JudgeAIIntegration:
    def __init__(self, api_key: str, base_url: str = "https://api.judge.ai"):
        """
        Initializes the JudgeAIIntegration class with the provided API key and base URL.

        :param api_key: The API key for authenticating with Judge AI's services.
        :param base_url: The base URL for Judge AI's API (default is set to Judge AI's API).
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint: str, data: dict) -> dict:
        """
        Makes a POST request to the specified endpoint with the provided data.

        :param endpoint: The API endpoint to send the request to.
        :param data: The data to be sent in the request body.
        :return: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            raise

    def enable_anti_benchmark(self, user_id: str) -> dict:
        """
        Enables anti-benchmark protection for a specific user.

        :param user_id: The ID of the user for whom to enable anti-benchmark protection.
        :return: The response from the Judge AI API.
        """
        endpoint = "anti-benchmark/enable"
        data = {"user_id": user_id}

        logging.info(f"Enabling anti-benchmark protection for user: {user_id}")
        return self._make_request(endpoint, data)

    def disable_anti_benchmark(self, user_id: str) -> dict:
        """
        Disables anti-benchmark protection for a specific user.

        :param user_id: The ID of the user for whom to disable anti-benchmark protection.
        :return: The response from the Judge AI API.
        """
        endpoint = "anti-benchmark/disable"
        data = {"user_id": user_id}

        logging.info(f"Disabling anti-benchmark protection for user: {user_id}")
        return self._make_request(endpoint, data)

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Judge AI API key
    judge_ai = JudgeAIIntegration(api_key='your_api_key')

    try:
        # Enable anti-benchmark protection for a user
        response_enable = judge_ai.enable_anti_benchmark(user_id='user123')
        logging.info(f"Enable response: {response_enable}")

        # Disable anti-benchmark protection for a user
        response_disable = judge_ai.disable_anti_benchmark(user_id='user123')
        logging.info(f"Disable response: {response_disable}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
