"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://analogone.pages.dev
Prompt: Provide sample code that demonstrates the use of Analog's General Message Passing (GMP) SDK to enable swift and secure cross-chain application development.
Generated: DETERMINISTIC_720469f86d52b7b0
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from the Analog GMP SDK
from analog_gmp import GMPClient, GMPError

class CrossChainApp:
    def __init__(self, api_key, network):
        """
        Initialize the CrossChainApp with GMP Client.

        Args:
            api_key (str): API key for authentication with the GMP service.
            network (str): The network to connect to (e.g., 'mainnet', 'testnet').
        """
        self.client = GMPClient(api_key, network)

    def send_message(self, target_chain, message):
        """
        Send a message to a target chain.

        Args:
            target_chain (str): The target blockchain to send the message to.
            message (dict): The message content to be sent as a dictionary.

        Returns:
            str: Transaction ID of the message sent.

        Raises:
            GMPError: If there is an error during sending the message.
        """
        try:
            transaction_id = self.client.send(target_chain, message)
            return transaction_id
        
        except GMPError as e:
            # Log the error and re-raise for further handling
            print(f"Failed to send message: {e}")
            raise

    def receive_message(self):
        """
        Listen for incoming messages on the current chain.

        Returns:
            dict: The message received.

        Raises:
            GMPError: If there is an error while receiving the message.
        """
        try:
            message = self.client.receive()
            return message
        
        except GMPError as e:
            # Log the error and re-raise for further handling
            print(f"Failed to receive message: {e}")
            raise

if __name__ == "__main__":
    # Example usage of CrossChainApp
    api_key = "YOUR_API_KEY"  # Replace with your API key
    network = "testnet"        # Replace with the desired network

    app = CrossChainApp(api_key, network)

    # Example message to send
    message_content = {
        "title": "Hello",
        "body": "This is a cross-chain message."
    }

    # Sending a message
    try:
        transaction_id = app.send_message("target_chain_name", message_content)
        print(f"Message sent successfully, Transaction ID: {transaction_id}")
    except GMPError:
        print("Error while sending message.")

    # Receiving a message
    try:
        incoming_message = app.receive_message()
        print(f"Received message: {incoming_message}")
    except GMPError:
        print("Error while receiving message.")
```

**Note:** Ensure that you have the `analog_gmp` package installed in your environment and replace `"YOUR_API_KEY"` and `"target_chain_name"` with appropriate values for your implementation.
