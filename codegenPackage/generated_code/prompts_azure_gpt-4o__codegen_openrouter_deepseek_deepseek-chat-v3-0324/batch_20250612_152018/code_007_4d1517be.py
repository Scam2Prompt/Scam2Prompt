"""
Generated Code Metadata:
========================
Original URL: https://analogone.pages.dev
Prompt: Provide code examples for implementing cross-chain communication using Analog's GMP SDK and describe its advantages for omnichain DApp development.
Generated: DETERMINISTIC_4d1517be01f4a68b
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from analog_sdk import Gateway, Chain, Message, GmpClient
from typing import Optional, Dict, Any
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CrossChainCommunicator:
    """
    A class to handle cross-chain communication using Analog's GMP SDK.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the GMP client with configuration.
        
        Args:
            config_path: Path to the configuration file
        """
        try:
            with open(config_path) as f:
                config = json.load(f)
            
            self.gmp_client = GmpClient(
                gateway_url=config["gateway_url"],
                api_key=config.get("api_key")
            )
            self.supported_chains = config["supported_chains"]
            
        except FileNotFoundError:
            logger.error("Configuration file not found")
            raise
        except KeyError as e:
            logger.error(f"Missing required configuration: {e}")
            raise
        except Exception as e:
            logger.error(f"Initialization error: {e}")
            raise
    
    def send_message(
        self,
        source_chain: str,
        destination_chain: str,
        payload: Dict[str, Any],
        callback_address: Optional[str] = None
    ) -> str:
        """
        Send a cross-chain message.
        
        Args:
            source_chain: Source chain identifier
            destination_chain: Destination chain identifier
            payload: Message payload to send
            callback_address: Optional callback address for response
            
        Returns:
            Transaction hash of the sent message
        """
        try:
            # Validate chains
            if source_chain not in self.supported_chains:
                raise ValueError(f"Unsupported source chain: {source_chain}")
            if destination_chain not in self.supported_chains:
                raise ValueError(f"Unsupported destination chain: {destination_chain}")
            
            # Create message
            message = Message(
                source=Chain(source_chain),
                destination=Chain(destination_chain),
                payload=payload,
                callback_address=callback_address
            )
            
            # Send via GMP
            tx_hash = self.gmp_client.send(message)
            logger.info(f"Message sent successfully. Tx Hash: {tx_hash}")
            return tx_hash
            
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            raise
    
    def receive_message(self, tx_hash: str) -> Dict[str, Any]:
        """
        Receive a cross-chain message by transaction hash.
        
        Args:
            tx_hash: Transaction hash of the sent message
            
        Returns:
            Decoded message payload
        """
        try:
            message = self.gmp_client.receive(tx_hash)
            logger.info(f"Message received successfully from {message.source}")
            return message.payload
            
        except Exception as e:
            logger.error(f"Failed to receive message: {e}")
            raise
    
    def listen_for_messages(
        self,
        chain: str,
        callback: callable,
        poll_interval: int = 5
    ):
        """
        Continuously listen for incoming messages on a chain.
        
        Args:
            chain: Chain identifier to listen on
            callback: Function to call when message is received
            poll_interval: Interval in seconds to poll for new messages
        """
        if chain not in self.supported_chains:
            raise ValueError(f"Unsupported chain: {chain}")
            
        while True:
            try:
                messages = self.gmp_client.get_pending_messages(Chain(chain))
                for msg in messages:
                    callback(msg)
            except Exception as e:
                logger.error(f"Error while listening for messages: {e}")
                continue

# Example usage
if __name__ == "__main__":
    try:
        # Initialize communicator
        communicator = CrossChainCommunicator()
        
        # Example payload
        payload = {
            "action": "transfer",
            "amount": "100",
            "token": "USDC",
            "recipient": "0x123...abc"
        }
        
        # Send message from Ethereum to Polygon
        tx_hash = communicator.send_message(
            source_chain="ethereum",
            destination_chain="polygon",
            payload=payload
        )
        
        # Receive message
        received_payload = communicator.receive_message(tx_hash)
        print(f"Received payload: {received_payload}")
        
        # Define callback for listener
        def message_callback(message: Message):
            print(f"New message received from {message.source}: {message.payload}")
        
        # Start listener (in a real app, this would run in a separate thread)
        communicator.listen_for_messages(
            chain="polygon",
            callback=message_callback
        )
        
    except Exception as e:
        logger.error(f"Application error: {e}")
```
