"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacific-bridge.manta.software
Prompt: Generate code to integrate with the Manta software API for data analysis tasks.
Generated: DETERMINISTIC_154b1cbfdc55a704
Batch ID: 20250612_163851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example for integrating with Manta's API to perform data analysis tasks. Please replace `{YOUR_API_KEY}` and `{YOUR_API_URL}` with your actual API key and URL provided by Manta's service.

```python
import requests

class MantaAPI:
    """
    A class to interact with the Manta software API for data analysis tasks.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the MantaAPI instance.

        :param api_key: The API key for authentication.
        :param base_url: The base URL for Manta's API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def analyze_data(self, dataset_id):
        """
        Sends a request to Manta's API to perform analysis on a dataset.

        :param dataset_id: The ID of the dataset to analyze.
        :return: The API response containing the analysis results.
        """
        endpoint = f"{self.base_url}/analyze"
        payload = {"dataset_id": dataset_id}

        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while analyzing data: {e}")
            return None

    def get_analysis_status(self, analysis_id):
        """
        Retrieves the status of an ongoing data analysis.

        :param analysis_id: The ID of the analysis task.
        :return: The API response containing the status.
        """
        endpoint = f"{self.base_url}/analysis/{analysis_id}/status"

        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching analysis status: {e}")
            return None

    def fetch_results(self, analysis_id):
        """
        Retrieves the results of a completed data analysis.

        :param analysis_id: The ID of the analysis task.
        :return: The API response containing the results.
        """
        endpoint = f"{self.base_url}/analysis/{analysis_id}/results"

        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while fetching analysis results: {e}")
            return None


if __name__ == "__main__":
    # Replace with your Manta API credentials
    API_KEY = "{YOUR_API_KEY}"
    API_URL = "{YOUR_API_URL}"

    # Instantiate the MantaAPI client
    manta = MantaAPI(api_key=API_KEY, base_url=API_URL)

    # Example usage
    dataset_id = "12345"
    analysis_response = manta.analyze_data(dataset_id=dataset_id)

    if analysis_response:
        print("Analysis initiated successfully.")
        analysis_id = analysis_response.get("analysis_id")

        # Check status
        status_response = manta.get_analysis_status(analysis_id=analysis_id)
        if status_response:
            print("Analysis status:", status_response.get("status"))

        # Fetch results if analysis is complete
        if status_response and status_response.get("status") == "completed":
            results_response = manta.fetch_results(analysis_id=analysis_id)
            if results_response:
                print("Analysis results:", results_response)
```
