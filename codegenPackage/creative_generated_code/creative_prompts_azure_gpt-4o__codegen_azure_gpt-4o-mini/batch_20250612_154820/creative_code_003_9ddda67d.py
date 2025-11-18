"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bittensor-stake.vercel.app
Prompt: Write a function to query the network stats of the Bittensor platform using its API and display the results in a readable format.
Generated: DETERMINISTIC_9ddda67d7b43d1b7
Batch ID: 20250612_154820
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bittensor.com/v1/network/stats": {
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

def get_bittensor_network_stats(api_url="https://api.bittensor.com/v1/network/stats"):
    """
    Query the Bittensor platform's network statistics using the provided API URL.

    Parameters:
        api_url (str): The URL of the Bittensor API endpoint for network stats.

    Returns:
        dict: A dictionary containing the network statistics if the request is successful.

    Raises:
        ValueError: If the response from the API is invalid or not in JSON format.
        Exception: For other issues like network errors or unsuccessful HTTP responses.
    """
    try:
        # Send a GET request to the specified API URL
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Attempt to parse the response as JSON
        stats = response.json()

        return stats

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        raise
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred: {req_err}")  # Handle network-related errors
        raise
    except ValueError as json_err:
        print(f"Error parsing JSON: {json_err}")  # Handle JSON parsing errors
        raise


def display_network_stats(stats):
    """
    Display the network statistics in a readable format.

    Parameters:
        stats (dict): A dictionary containing network statistics.
    """
    print("Bittensor Network Statistics:")
    print("-" * 30)

    for key, value in stats.items():
        print(f"{key}: {value}")

    print("-" * 30)


if __name__ == "__main__":
    try:
        # Fetch network statistics
        network_stats = get_bittensor_network_stats()
        
        # Display the fetched statistics
        display_network_stats(network_stats)

    except Exception as e:
        print(f"An error occurred: {e}")  # General error handling for unexpected issues
```
