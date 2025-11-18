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
  "http://your-arweave-node-url": {
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

def get_arweave_node_metrics(node_url):
    """
    Retrieves the 'peers' count and 'queue_length' from an Arweave node API response.

    Args:
        node_url (str): The URL of the Arweave node API.

    Returns:
        dict: A dictionary containing the 'peers' count and 'queue_length'.
    
    Raises:
        ValueError: If the response does not contain the expected keys.
        requests.RequestException: If there is an issue with the request to the API.
    """
    try:
        # Make a GET request to the Arweave node API
        response = requests.get(f"{node_url}/info")
        
        # Raise an exception for HTTP error responses
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()

        # Extract required metrics
        peers_count = data.get("peers")
        queue_length = data.get("queue_length")

        # Check if the required metrics are present in the response
        if peers_count is None or queue_length is None:
            raise ValueError("Response does not contain 'peers' or 'queue_length' keys.")

        # Return the extracted metrics as a dictionary
        return {
            "peers": peers_count,
            "queue_length": queue_length
        }

    except requests.RequestException as e:
        # Handle any request-related exceptions
        print(f"Error retrieving data from the Arweave node: {e}")
        raise
    except ValueError as e:
        # Handle cases where the expected data structure is not present
        print(f"Data processing error: {e}")
        raise

# Example usage (uncomment when running the code):
# metrics = get_arweave_node_metrics("http://your-arweave-node-url")
# print(metrics)
```
