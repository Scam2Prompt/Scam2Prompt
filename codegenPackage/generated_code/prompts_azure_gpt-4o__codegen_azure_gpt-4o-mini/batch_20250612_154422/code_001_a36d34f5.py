"""
Generated Code Metadata:
========================
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Create a Python function that retrieves the "peers" count and "queue_length" from an Arweave node API response, similar to the structure described on the webpage.
Generated: DETERMINISTIC_a36d34f5af169cde
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-arweave-node-url": {
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

def get_arweave_node_metrics(node_url):
    """
    Retrieves the 'peers' count and 'queue_length' from an Arweave node API response.

    Args:
        node_url (str): The URL of the Arweave node API.

    Returns:
        dict: A dictionary containing 'peers' count and 'queue_length'.
    
    Raises:
        ValueError: If the response does not contain the expected data.
        requests.RequestException: If there is an issue with the HTTP request.
    """
    try:
        # Send a GET request to the Arweave node API
        response = requests.get(f"{node_url}/info")
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        data = response.json()

        # Extract 'peers' and 'queue_length' from the response
        peers_count = data.get('peers')
        queue_length = data.get('queue_length')

        # Check if the required fields are present
        if peers_count is None or queue_length is None:
            raise ValueError("Response does not contain 'peers' or 'queue_length'.")

        return {
            'peers': peers_count,
            'queue_length': queue_length
        }

    except requests.RequestException as e:
        # Handle HTTP request errors
        print(f"HTTP request failed: {e}")
        raise
    except ValueError as e:
        # Handle value errors related to response content
        print(f"Value error: {e}")
        raise
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise

# Example usage (uncomment to use):
# node_url = "http://your-arweave-node-url"
# metrics = get_arweave_node_metrics(node_url)
# print(metrics)
```
