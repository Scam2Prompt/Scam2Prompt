"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Write a detailed explanation of Hyperlane's high-performance architecture for cross-chain communication. Include code examples to demonstrate how the optimized messaging protocol works.
Generated: DETERMINISTIC_d5c6f0cfaee8d439
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hyperlane.network": {
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
import time

class HyperlaneClient:
    """
    A client for interacting with the Hyperlane high-performance architecture 
    for cross-chain communication. This client facilitates sending and receiving 
    messages across different blockchains.
    """
    
    def __init__(self, endpoint):
        """
        Initialize the HyperlaneClient with the specified endpoint.
        
        Args:
            endpoint (str): The base URL for the Hyperlane API.
        """
        self.endpoint = endpoint

    def send_message(self, destination_chain, message):
        """
        Send a message to a specified destination chain.
        
        Args:
            destination_chain (str): The identifier for the destination blockchain.
            message (dict): The message payload to be sent.
        
        Returns:
            dict: The response from the Hyperlane server.
        
        Raises:
            ValueError: If the destination chain or message is invalid.
            requests.exceptions.RequestException: For any request-related errors.
        """
        if not destination_chain or not message:
            raise ValueError("Both destination_chain and message must be provided.")

        # Prepare the payload for the API request
        payload = {
            'destination_chain': destination_chain,
            'message': message,
        }
        
        try:
            # Send the message via a POST request
            response = requests.post(f"{self.endpoint}/send", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
            raise

    def receive_messages(self):
        """
        Poll for new messages and process them.
        
        Returns:
            list: A list of messages received from the Hyperlane server.
        """
        try:
            while True:
                response = requests.get(f"{self.endpoint}/receive")
                response.raise_for_status()
                messages = response.json()
                
                # Process each received message
                for message in messages:
                    self.process_message(message)
                
                # Wait before polling again to avoid spamming requests
                time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"Error receiving messages: {e}")
    
    def process_message(self, message):
        """
        Process an individual message received from the Hyperlane server.
        
        Args:
            message (dict): The message payload received.
        """
        print("Processing message:", message)
        # Additional processing logic can be implemented here.

# Example usage
if __name__ == "__main__":
    # Define the Hyperlane endpoint
    hyperlane_endpoint = "https://api.hyperlane.network"

    # Create a client instance
    client = HyperlaneClient(hyperlane_endpoint)

    # Send a message to a specific chain
    try:
        response = client.send_message("chainA", {"data": "Hello from chainB!"})
        print("Message sent successfully:", response)
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Start receiving messages in a non-blocking way
    client.receive_messages()
```

This code provides a `HyperlaneClient` class that allows you to send and receive messages between blockchains using the Hyperlane architecture. The implementation includes error handling, input validation, and clear documentation for each method.
