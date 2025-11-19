"""
Generated Code Metadata:
========================
Original URL: https://wormhole.pw
Prompt: Provide a code example for creating a custom multichain protocol using Wormhole's messaging tools. Explain how this protocol can be used to communicate across blockchains.
Generated: DETERMINISTIC_597f583325a70a2f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from typing import Dict, List
from wormhole import Wormhole

class CustomMultichainProtocol:
    """
    A custom multichain protocol using Wormhole's messaging tools.

    This protocol enables communication across blockchains by sending and receiving messages.
    """

    def __init__(self, wormhole: Wormhole, chain_id: int, contract_address: str):
        """
        Initializes the custom multichain protocol.

        Args:
        - wormhole (Wormhole): The Wormhole instance.
        - chain_id (int): The chain ID of the blockchain.
        - contract_address (str): The address of the contract.
        """
        self.wormhole = wormhole
        self.chain_id = chain_id
        self.contract_address = contract_address

    def send_message(self, recipient_chain_id: int, recipient_contract_address: str, message: str):
        """
        Sends a message to a recipient on a different blockchain.

        Args:
        - recipient_chain_id (int): The chain ID of the recipient's blockchain.
        - recipient_contract_address (str): The address of the recipient's contract.
        - message (str): The message to be sent.

        Returns:
        - The transaction hash of the sent message.
        """
        try:
            # Create a message payload
            payload = json.dumps({
                "type": "custom_message",
                "message": message
            })

            # Send the message using Wormhole's messaging tools
            tx_hash = self.wormhole.publish_message(
                recipient_chain_id,
                recipient_contract_address,
                payload
            )

            return tx_hash
        except Exception as e:
            # Handle any exceptions that occur during message sending
            print(f"Error sending message: {str(e)}")
            return None

    def receive_message(self, message: Dict):
        """
        Receives a message from a sender on a different blockchain.

        Args:
        - message (Dict): The received message.

        Returns:
        - The processed message.
        """
        try:
            # Process the received message
            payload = json.loads(message["payload"])
            if payload["type"] == "custom_message":
                print(f"Received message: {payload['message']}")
                return payload
            else:
                print("Unknown message type")
                return None
        except Exception as e:
            # Handle any exceptions that occur during message receiving
            print(f"Error receiving message: {str(e)}")
            return None


def main():
    # Example usage
    wormhole = Wormhole()
    protocol = CustomMultichainProtocol(
        wormhole,
        1,  # Chain ID (e.g., Ethereum mainnet)
        "0x..."  # Contract address
    )

    # Send a message to a recipient on a different blockchain
    recipient_chain_id = 2  # Chain ID (e.g., Solana mainnet)
    recipient_contract_address = "0x..."  # Contract address
    message = "Hello, world!"
    tx_hash = protocol.send_message(recipient_chain_id, recipient_contract_address, message)
    print(f"Sent message with tx hash: {tx_hash}")

    # Receive a message from a sender on a different blockchain
    received_message = {
        "payload": json.dumps({
            "type": "custom_message",
            "message": "Hello, world!"
        })
    }
    processed_message = protocol.receive_message(received_message)


if __name__ == "__main__":
    main()
```
