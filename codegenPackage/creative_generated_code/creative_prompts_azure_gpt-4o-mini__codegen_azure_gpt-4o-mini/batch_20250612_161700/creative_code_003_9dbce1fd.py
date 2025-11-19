"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica13.vercel.app
Prompt: Provide an example of how to use the Matrica library to fetch home stats for a specific network.
Generated: DETERMINISTIC_9dbce1fd1871f749
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from matrica import Matrica  # Assuming Matrica is a Python library for fetching home stats

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_home_stats(network_id):
    """
    Fetches home statistics for a specific network using the Matrica library.

    Args:
        network_id (str): The unique identifier for the network.

    Returns:
        dict: A dictionary containing home statistics if successful.

    Raises:
        ValueError: If the network_id is invalid.
        Exception: For any other errors encountered during fetching.
    """
    if not isinstance(network_id, str) or not network_id:
        logger.error("Invalid network_id provided: %s", network_id)
        raise ValueError("network_id must be a non-empty string.")

    try:
        # Initialize Matrica client
        matrica_client = Matrica()

        # Fetch home stats for the given network ID
        home_stats = matrica_client.get_home_stats(network_id)

        # Log the successful retrieval of home stats
        logger.info("Successfully fetched home stats for network: %s", network_id)
        return home_stats
        
    except Exception as e:
        logger.exception("Failed to fetch home stats for network %s: %s", network_id, e)
        raise  # Re-raise the exception after logging

if __name__ == "__main__":
    # Example usage of the fetch_home_stats function
    try:
        network_id = "example_network_id"  # Replace with a valid network ID
        stats = fetch_home_stats(network_id)
        print("Home Stats:", stats)
    except Exception as e:
        print("An error occurred:", e)
```
