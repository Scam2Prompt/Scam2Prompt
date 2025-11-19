"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-it.web.app
Prompt: Generate a Python script that utilizes the Artificial Intelligence Virtual Machine (AIVM) for executing AI tasks on the Lightchain blockchain.
Generated: DETERMINISTIC_b3efbf9747a4779e
Batch ID: 20250612_155751
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lightchain.ai/v1/aivm": {
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

class AIVMClient:
    """
    A client to interact with the Artificial Intelligence Virtual Machine (AIVM) on the Lightchain blockchain.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the AIVMClient with the base URL and API key.

        :param base_url: The base URL of the AIVM API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None) -> dict:
        """
        Make an HTTP request to the AIVM API.

        :param endpoint: The API endpoint to hit.
        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request (for POST).
        :return: The JSON response from the API.
        :raises Exception: If the request fails or the response is not valid JSON.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response

        except requests.exceptions.RequestException as e:
            raise Exception(f"HTTP Request failed: {e}")
        except json.JSONDecodeError:
            raise Exception("Failed to decode JSON response")

    def execute_ai_task(self, task_data: dict) -> dict:
        """
        Execute an AI task on the AIVM.

        :param task_data: The data for the AI task.
        :return: The result of the AI task execution.
        """
        try:
            response = self._make_request("execute", method='POST', data=task_data)
            return response
        except Exception as e:
            raise Exception(f"Failed to execute AI task: {e}")

if __name__ == "__main__":
    # Configuration
    BASE_URL = "https://api.lightchain.ai/v1/aivm"  # Replace with the actual AIVM base URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Initialize the AIVM client
    client = AIVMClient(BASE_URL, API_KEY)

    # Example task data
    task_data = {
        "model": "text-generation",
        "input": "Hello, world!",
        "parameters": {
            "max_length": 50,
            "temperature": 0.7
        }
    }

    try:
        # Execute AI task
        result = client.execute_ai_task(task_data)
        print("AI Task Result:", result)
    except Exception as e:
        print("Error:", e)
```
