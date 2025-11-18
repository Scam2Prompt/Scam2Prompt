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
# Import GMP SDK and other necessary libraries
from analog_sdk import GMP, KeyManager
import logging

# Initialize logging for debugging
logging.basicConfig(level=logging.INFO)

# Function to send a cross-chain message securely
def send_cross_chain_message(source_chain, destination_chain, message, sender_key):
    """
    Sends a secure message from one chain to another using Analog's GMP SDK.

    Args:
        source_chain (str): The source blockchain name.
        destination_chain (str): The destination blockchain name.
        message (str): The message to be sent.
        sender_key (str): The sender's private key for message signing.
    
    Returns:
        dict: Response from the GMP SDK.
    """
    try:
        # Initialize GMP with the sender's private key
        key_manager = KeyManager(private_key=sender_key)
        gmp = GMP(key_manager)

        # Prepare the message payload
        payload = {
            "source_chain": source_chain,
            "destination_chain": destination_chain,
            "message": message
        }

        # Send the message using GMP
        response = gmp.send_message(payload)

        # Log the response
        logging.info(f"Message successfully sent. Response: {response}")

        return response

    except Exception as e:
        # Log the error
        logging.error(f"An error occurred while sending cross-chain message: {str(e)}")
        return {"error": str(e)}

# Function to receive a cross-chain message securely
def receive_cross_chain_message(receiver_key):
    """
    Receives messages securely from other chains using Analog's GMP SDK.

    Args:
        receiver_key (str): The receiver's private key for message verification.
    
    Returns:
        list: List of received messages.
    """
    try:
        # Initialize GMP with the receiver's private key
        key_manager = KeyManager(private_key=receiver_key)
        gmp = GMP(key_manager)

        # Retrieve messages
        messages = gmp.receive_messages()

        # Log received messages
        logging.info(f"Messages successfully received: {messages}")

        return messages

    except Exception as e:
        # Log the error
        logging.error(f"An error occurred while receiving cross-chain messages: {str(e)}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Replace with actual keys and chain names
    sender_private_key = "your_sender_private_key_here"
    receiver_private_key = "your_receiver_private_key_here"
    
    # Example message
    example_message = "Hello from Chain A to Chain B!"
    
    # Send a message from Chain A to Chain B
    send_cross_chain_message("ChainA", "ChainB", example_message, sender_private_key)
    
    # Receive messages intended for Chain B
    receive_cross_chain_message(receiver_private_key)
```
