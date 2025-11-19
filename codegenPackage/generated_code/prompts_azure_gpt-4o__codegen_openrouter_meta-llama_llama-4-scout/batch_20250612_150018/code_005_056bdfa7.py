"""
Generated Code Metadata:
========================
Original URL: https://berachain.tryethernal.com
Prompt: Provide an example of using the Ethernal API to monitor real-time updates on Ethereum network activity.
Generated: DETERMINISTIC_056bdfa7b95344d0
Batch ID: 20250612_150018
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
from websocket import create_connection

class EthernalAPI:
    """
    A class to interact with the Ethernal API.

    Attributes:
        url (str): The URL of the Ethernal API WebSocket endpoint.
        ws (websocket): The WebSocket connection object.
    """

    def __init__(self, url="wss://ws.ethernal.io"):
        """
        Initializes the EthernalAPI object.

        Args:
            url (str, optional): The URL of the Ethernal API WebSocket endpoint. Defaults to "wss://ws.ethernal.io".
        """
        self.url = url
        self.ws = None

    def connect(self):
        """
        Establishes a connection to the Ethernal API WebSocket endpoint.

        Raises:
            Exception: If the connection fails.
        """
        try:
            self.ws = create_connection(self.url)
            print("Connected to Ethernal API")
        except Exception as e:
            print(f"Failed to connect to Ethernal API: {e}")
            raise

    def disconnect(self):
        """
        Closes the connection to the Ethernal API WebSocket endpoint.
        """
        if self.ws:
            self.ws.close()
            self.ws = None
            print("Disconnected from Ethernal API")

    def subscribe(self, event_type):
        """
        Subscribes to a specific event type.

        Args:
            event_type (str): The type of event to subscribe to (e.g., "block", "transaction", etc.).

        Raises:
            Exception: If the subscription fails.
        """
        if not self.ws:
            raise Exception("Not connected to Ethernal API")

        try:
            subscription_request = json.dumps({
                "method": "subscribe",
                "params": [event_type],
                "id": 1,
                "jsonrpc": "2.0"
            })
            self.ws.send(subscription_request)
            print(f"Subscribed to {event_type} events")
        except Exception as e:
            print(f"Failed to subscribe to {event_type} events: {e}")
            raise

    def listen(self):
        """
        Listens for incoming events.

        Yields:
            dict: The incoming event.
        """
        if not self.ws:
            raise Exception("Not connected to Ethernal API")

        while True:
            try:
                message = self.ws.recv()
                yield json.loads(message)
            except Exception as e:
                print(f"Error listening for events: {e}")
                break

def main():
    # Create an EthernalAPI object
    ethernal_api = EthernalAPI()

    try:
        # Connect to the Ethernal API
        ethernal_api.connect()

        # Subscribe to block events
        ethernal_api.subscribe("block")

        # Listen for incoming block events
        for event in ethernal_api.listen():
            print(json.dumps(event, indent=4))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Disconnect from the Ethernal API
        ethernal_api.disconnect()

if __name__ == "__main__":
    main()
```
