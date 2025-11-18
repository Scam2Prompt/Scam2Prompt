"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Write a script to query Monero node status using the `monero.fail` node list.
Generated: DETERMINISTIC_760e23424a390c11
Batch ID: 20250612_151428
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://monero.fail/api/nodes": {
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

# Constants
MONERO_FAIL_API_URL = "https://monero.fail/api/nodes"
TIMEOUT_SECONDS = 10


def fetch_monero_nodes_status():
    """
    Fetches the list of Monero nodes and their statuses from the monero.fail API.

    Returns:
        A list of nodes with their respective statuses.
    """
    try:
        # Make a GET request to Monero.fail API to retrieve the nodes
        response = requests.get(MONERO_FAIL_API_URL, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)

        # Parse JSON response
        nodes_data = response.json()
        return nodes_data
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching Monero node data: {e}")
        return None
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error decoding JSON response: {e}")
        return None


def main():
    """
    Main function to query and display Monero node statuses.
    """
    print("Fetching Monero node status...")
    nodes_status = fetch_monero_nodes_status()

    if nodes_status:
        print("Monero node data fetched successfully!")
        print(json.dumps(nodes_status, indent=4))  # Pretty-print the nodes data
    else:
        print("Failed to retrieve Monero node status.")


if __name__ == "__main__":
    # Execute the main function
    main()
```
