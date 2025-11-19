"""
Generated Code Metadata:
========================
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Create a Python function that retrieves the "peers" count and "queue_length" from an Arweave node API response, similar to the structure described on the webpage.
Generated: DETERMINISTIC_a36d34f5af169cde
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Any, Optional

def get_arweave_node_stats(api_url: str) -> Optional[Dict[str, Any]]:
    """
    Retrieves peers count and queue length from an Arweave node API.

    Args:
        api_url: The URL of the Arweave node API endpoint.

    Returns:
        A dictionary containing 'peers' and 'queue_length' if successful, None otherwise.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        
        # Extract peers count and queue length from the response
        peers = data.get('peers')
        queue_length = data.get('queue_length')
        
        if peers is None or queue_length is None:
            raise ValueError("Required fields not found in API response")
            
        return {
            'peers': peers,
            'queue_length': queue_length
        }
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Invalid data format: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None
```
