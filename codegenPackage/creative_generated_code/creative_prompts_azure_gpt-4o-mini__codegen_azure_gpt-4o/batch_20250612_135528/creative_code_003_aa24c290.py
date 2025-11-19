"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetvietnam.wordpress.com
Prompt: Create an API call example for interacting with StarkNet's decentralized network for a dApp.
Generated: DETERMINISTIC_aa24c29019596b8f
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.starknet.node/api": {
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

# StarkNet API base URL (adjust endpoint as needed for your environment)
STARKNET_API_BASE_URL = "https://example.starknet.node/api"

def call_starknet_api(endpoint, payload):
    """
    Makes an API call to the StarkNet network.
    
    Args:
        endpoint (str): The specific API endpoint to call.
        payload (dict): The JSON payload to send with the request.
    
    Returns:
        dict: The JSON response from the StarkNet API.
    
    Raises:
        Exception: If the API call fails or returns an error.
    """
    # Construct the full URL for the API endpoint
    url = f"{STARKNET_API_BASE_URL}/{endpoint}"
    
    try:
        # Make the POST request to the StarkNet API
        response = requests.post(url, json=payload, timeout=30)  # Set a 30-second timeout
        
        # Raise an exception if the response status code indicates an error
        response.raise_for_status()
        
        # Parse the response as JSON
        response_data = response.json()
        
        # Check for errors in the API response
        if "error" in response_data:
            raise Exception(f"StarkNet API error: {response_data['error']}")
        
        return response_data  # Return the successful response
    except requests.exceptions.Timeout:
        raise Exception("The request to StarkNet API timed out.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while making the API call: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example payload for interacting with StarkNet
    example_payload = {
        "contract_address": "0x0123456789abcdef",
        "entry_point": "get_balance",
        "calldata": ["12345"]
    }
    
    try:
        # Call the StarkNet API with the example payload
        response = call_starknet_api("call_contract", example_payload)
        
        # Print the successful response
        print("API Response:", response)
    except Exception as e:
        # Print the error message if the API call failed
        print("Error:", str(e))
```
