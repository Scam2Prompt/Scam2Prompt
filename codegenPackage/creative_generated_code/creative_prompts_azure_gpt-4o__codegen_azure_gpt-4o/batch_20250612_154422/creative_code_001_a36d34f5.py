"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Create a Python function that retrieves the "peers" count and "queue_length" from an Arweave node API response, similar to the structure described on the webpage.
Generated: DETERMINISTIC_a36d34f5af169cde
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net/metrics": {
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

def get_arweave_node_status(api_url: str) -> dict:
    """
    Retrieves the 'peers' count and 'queue_length' from an Arweave node API response.

    Parameters:
        api_url (str): The URL of the Arweave node API endpoint.

    Returns:
        dict: A dictionary containing 'peers' count and 'queue_length', or an error message if the request fails.
    """
    try:
        # Send GET request to the Arweave node API endpoint
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        # Extract 'peers' and 'queue_length' from the response
        peers = data.get("peers")
        queue_length = data.get("queue_length")

        # Ensure the required fields exist in the response
        if peers is None or queue_length is None:
            raise ValueError("API response does not contain required keys: 'peers' or 'queue_length'.")

        # Return the extracted data
        return {"peers": peers, "queue_length": queue_length}

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {"error": f"Network error occurred: {str(e)}"}
    except ValueError as ve:
        # Handle missing or invalid data errors
        return {"error": f"Data error: {str(ve)}"}
    except Exception as ex:
        # Handle any other unforeseen errors
        return {"error": f"An unexpected error occurred: {str(ex)}"}

# Example usage
if __name__ == "__main__":
    # Replace '<API_ENDPOINT>' with the actual URL of the Arweave node API
    api_endpoint = "https://arweave.net/metrics"
    status = get_arweave_node_status(api_endpoint)
    print(status)
```
