"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiggfg7harzlrxx3ccklh6kjolvxmejdxtqnqqtcadvfp5c5zzddbu.ipfs.dweb.link
Prompt: Write a Python script to interact with MyShell Labs' APIs for transforming user ideas into AI-native apps using generative AI models.
Generated: DETERMINISTIC_cd913e5a3d6b28ce
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.myshelllabs.com/v1": {
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

class MyShellAPI:
    """
    A class to interact with MyShell Labs' API for transforming user ideas into AI-native apps.
    """

    BASE_URL = "https://api.myshelllabs.com/v1"  # Base URL for MyShell Labs API

    def __init__(self, api_key: str):
        """
        Initializes the MyShellAPI with the provided API key.
        
        Parameters:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def transform_idea(self, idea: str) -> dict:
        """
        Transforms the user's idea into an AI-native app using the generative AI model.

        Parameters:
            idea (str): The user's idea to be transformed.

        Returns:
            dict: The response from the API containing the transformed app details.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/transform"
        payload = {"idea": idea}

        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log the error
            raise

    def get_app_status(self, app_id: str) -> dict:
        """
        Retrieves the status of a generated app.

        Parameters:
            app_id (str): The unique identifier of the app.

        Returns:
            dict: The response from the API containing the app status.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/apps/{app_id}/status"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log the error
            raise

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    my_shell_api = MyShellAPI(API_KEY)

    user_idea = "Create a personalized study planner app."  # Example user idea

    try:
        transformed_app = my_shell_api.transform_idea(user_idea)
        print("Transformed App:", transformed_app)

        app_id = transformed_app.get("app_id")  # Assume the response contains an app_id
        app_status = my_shell_api.get_app_status(app_id)
        print("App Status:", app_status)
    except Exception as e:
        print(f"Error during API interaction: {e}")
```
