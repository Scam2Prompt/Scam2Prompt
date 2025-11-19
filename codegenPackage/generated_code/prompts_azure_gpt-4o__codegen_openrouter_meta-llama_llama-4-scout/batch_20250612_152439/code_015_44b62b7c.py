"""
Generated Code Metadata:
========================
Original URL: https://lavanet.pages.dev
Prompt: Generate a code example using LavaSDK to fetch real-time analytics data for the Lava blockchain.
Generated: DETERMINISTIC_44b62b7cd59ca248
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from lavaclient import LavaClient

class LavaAnalytics:
    def __init__(self, node_url, api_key):
        """
        Initialize LavaClient with node URL and API key.

        Args:
        - node_url (str): URL of the Lava node.
        - api_key (str): API key for authentication.
        """
        self.node_url = node_url
        self.api_key = api_key
        self.client = LavaClient(node_url, api_key)

    def get_realtime_analytics(self):
        """
        Fetch real-time analytics data from the Lava blockchain.

        Returns:
        - dict: Real-time analytics data.
        """
        try:
            # Use LavaClient to fetch real-time analytics data
            response = self.client.analytics.get_realtime_analytics()
            return response
        except Exception as e:
            # Handle any exceptions that occur during the request
            print(f"Error fetching real-time analytics: {str(e)}")
            return None

    def get_chain_analytics(self, chain_id):
        """
        Fetch real-time analytics data for a specific chain.

        Args:
        - chain_id (str): ID of the chain.

        Returns:
        - dict: Real-time analytics data for the specified chain.
        """
        try:
            # Use LavaClient to fetch real-time analytics data for a specific chain
            response = self.client.analytics.get_chain_analytics(chain_id)
            return response
        except Exception as e:
            # Handle any exceptions that occur during the request
            print(f"Error fetching chain analytics for {chain_id}: {str(e)}")
            return None


def main():
    # Set node URL and API key
    node_url = os.environ.get("LAVA_NODE_URL")
    api_key = os.environ.get("LAVA_API_KEY")

    if not node_url or not api_key:
        print("Please set LAVA_NODE_URL and LAVA_API_KEY environment variables.")
        return

    # Initialize LavaAnalytics
    lava_analytics = LavaAnalytics(node_url, api_key)

    # Fetch real-time analytics data
    realtime_analytics = lava_analytics.get_realtime_analytics()
    print("Real-time Analytics:")
    print(json.dumps(realtime_analytics, indent=4))

    # Fetch real-time analytics data for a specific chain
    chain_id = "lava"
    chain_analytics = lava_analytics.get_chain_analytics(chain_id)
    print(f"\nReal-time Analytics for {chain_id}:")
    print(json.dumps(chain_analytics, indent=4))


if __name__ == "__main__":
    main()
```
