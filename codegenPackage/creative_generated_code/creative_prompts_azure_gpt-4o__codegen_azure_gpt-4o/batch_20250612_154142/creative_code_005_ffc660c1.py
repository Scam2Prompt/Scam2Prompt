"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write code to interact with the Aethir API for retrieving GPU node statistics, including location and earnings data, as described in the Aethir ecosystem documentation.
Generated: DETERMINISTIC_ffc660c1d19f5647
Batch ID: 20250612_154142
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.io/v1/": {
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

# Define constants for the Aethir API
API_BASE_URL = "https://api.aethir.io/v1/"  # Base URL for the Aethir API
ENDPOINT_GPU_STATS = "gpu_nodes/stats"      # Endpoint to retrieve GPU node statistics
API_KEY = "YOUR_API_KEY_HERE"              # Your Aethir API key (replace with actual key)

def get_gpu_node_statistics(api_key):
    """
    Fetch GPU node statistics, including location and earnings, from the Aethir API.
    
    Args:
        api_key (str): The API key for authentication.
    
    Returns:
        dict: Parsed JSON response containing GPU node statistics.
    
    Raises:
        Exception: If the API request fails or response is invalid.
    """
    url = f"{API_BASE_URL}{ENDPOINT_GPU_STATS}"
    headers = {
        "Authorization": f"Bearer {api_key}",  # Bearer token for authentication
        "Content-Type": "application/json"    # Request content type
    }

    try:
        # Make the GET request to the Aethir API
        response = requests.get(url, headers=headers)
        
        # Raise an exception if the response status code is not successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Ensure the response contains the expected data
        if not isinstance(data, dict):
            raise ValueError("Unexpected response format: Expected a JSON object.")

        return data

    except requests.exceptions.RequestException as e:
        # Catch HTTP request errors
        raise Exception(f"Error while making API request: {e}")

    except ValueError as e:
        # Handle response parsing errors
        raise Exception(f"Error while processing API response: {e}")

# Main function
if __name__ == "__main__":
    try:
        # Fetch GPU node statistics
        gpu_stats = get_gpu_node_statistics(API_KEY)

        # Print the retrieved statistics
        print("GPU Node Statistics:")
        print(f"Location: {gpu_stats.get('location', 'Unknown')}")
        print(f"Earnings: {gpu_stats.get('earnings', 'Unknown')}")
    except Exception as error:
        # Handle any errors gracefully
        print(f"An error occurred: {error}")
```

*Note: Replace `"YOUR_API_KEY_HERE"` with your actual Aethir API key to run the code successfully. Ensure you have the `requests` library installed (`pip install requests`) before executing the script.*
