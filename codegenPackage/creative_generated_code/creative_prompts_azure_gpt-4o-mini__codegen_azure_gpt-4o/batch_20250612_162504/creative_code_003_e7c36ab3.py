"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica21.vercel.app
Prompt: Generate a function that retrieves network statistics from the Matrica platform for Solana.
Generated: DETERMINISTIC_e7c36ab37c1b82c2
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.matrica.io": {
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

def get_matrica_network_stats(api_url: str, api_key: str) -> dict:
    """
    Retrieves network statistics from the Matrica platform for Solana.

    Args:
        api_url (str): The base URL for the Matrica API.
        api_key (str): The API key to authenticate the request.

    Returns:
        dict: A dictionary containing the network statistics if the request is successful.

    Raises:
        ValueError: If the response contains an error or if the API key is invalid.
        Exception: For any unexpected errors during the request.
    """
    # Endpoint for network statistics
    endpoint = f"{api_url}/network/stats"

    # Headers for request, including authentication information
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Sending GET request to retrieve network statistics
        response = requests.get(endpoint, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            return response.json()
        elif response.status_code == 401:
            # Error handling for unauthorized access
            raise ValueError("Invalid API key provided. Please check your API key.")
        else:
            # Handle other HTTP errors
            raise ValueError(f"Failed to retrieve network statistics. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any issues related to the request itself (e.g., network errors)
        raise Exception(f"An error occurred while making the API request: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual API URL and API key
        matrica_api_url = "https://api.matrica.io"
        matrica_api_key = "your_api_key_here"

        # Retrieve network stats
        stats = get_matrica_network_stats(matrica_api_url, matrica_api_key)
        print("Network Statistics:", stats)
    except Exception as error:
        print(f"Error: {error}")
```
