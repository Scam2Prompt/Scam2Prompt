"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Generate a sample query to retrieve data from Chainbase's extensive datasets for a specific blockchain project.
Generated: DETERMINISTIC_0a8c2dc0f68af23c
Batch ID: 20250612_155632
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.com/v1/": {
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

class ChainbaseAPI:
    """
    A client for interacting with the Chainbase API to retrieve data for blockchain projects.
    """

    BASE_URL = "https://api.chainbase.com/v1/"
    
    def __init__(self, api_key):
        """
        Initializes the ChainbaseAPI client with the provided API key.

        Args:
            api_key (str): The API key for accessing Chainbase services.
        """
        self.api_key = api_key

    def get_project_data(self, project_name):
        """
        Retrieves data for a specific blockchain project from Chainbase.

        Args:
            project_name (str): The name of the blockchain project to query.

        Returns:
            dict: The JSON response containing project data.

        Raises:
            ValueError: If the project_name is invalid or empty.
            Exception: If an error occurs during the API request.
        """
        if not project_name:
            raise ValueError("Project name must be provided.")

        try:
            endpoint = f"{self.BASE_URL}projects/{project_name}"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            response = requests.get(endpoint, headers=headers)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the parsed JSON response
            return response.json()

        except requests.RequestException as e:
            raise Exception(f"An error occurred while fetching project data: {str(e)}")


if __name__ == "__main__":
    # Example usage of the ChainbaseAPI
    API_KEY = "your_api_key_here"  # Replace with your Chainbase API key
    PROJECT_NAME = "example_project"  # Replace with the desired project name

    # Initialize the API client
    chainbase_client = ChainbaseAPI(API_KEY)

    try:
        # Retrieve project data
        project_data = chainbase_client.get_project_data(PROJECT_NAME)
        print(project_data)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```
