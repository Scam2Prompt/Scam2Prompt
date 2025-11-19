"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: How can I implement a decentralized messaging network for cross-chain transactions using Particle Network's architecture?
Generated: DETERMINISTIC_4e0ce8f33ff623ad
Batch ID: 20250612_164305
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.particle.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
import requests
from web3 import Web3

# Constants for Particle Network API
PARTICLE_API_URL = "https://api.particle.network"
API_KEY = "YOUR_PARTICLE_API_KEY"

# Function to initialize a Web3 instance for a given blockchain
def initialize_web3(network_url):
    """
    Initialize a Web3 instance with the specified network URL.

    Args:
        network_url (str): The URL of the blockchain network.

    Returns:
        Web3: An initialized Web3 instance.
    """
    try:
        web3 = Web3(Web3.HTTPProvider(network_url))
        if not web3.isConnected():
            raise ConnectionError("Unable to connect to the blockchain network.")
        return web3
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Web3: {str(e)}")

# Function to send a message across chains
def send_message(from_chain, to_chain, message):
    """
    Send a message from one blockchain to another using Particle Network.

    Args:
        from_chain (str): The blockchain to send the message from.
        to_chain (str): The blockchain to send the message to.
        message (str): The message content to send.

    Returns:
        str: Transaction ID for the message sent.
    """
    try:
        url = f"{PARTICLE_API_URL}/send_message"
        data = {
            "from": from_chain,
            "to": to_chain,
            "message": message,
            "apiKey": API_KEY,
        }
        
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses

        return response.json().get('transactionId')
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error sending message: {str(e)}")

# Function to retrieve messages from a specified chain
def retrieve_messages(chain):
    """
    Retrieve messages from a specified blockchain.

    Args:
        chain (str): The blockchain to retrieve messages from.

    Returns:
        list: A list of messages retrieved from the specified blockchain.
    """
    try:
        url = f"{PARTICLE_API_URL}/retrieve_messages"
        data = {
            "chain": chain,
            "apiKey": API_KEY,
        }

        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses

        return response.json().get('messages', [])
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error retrieving messages: {str(e)}")

# Example usage of the functions
if __name__ == "__main__":
    try:
        # Initialize Web3 instances for Ethereum and Binance Smart Chain (example)
        eth_web3 = initialize_web3("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")
        bsc_web3 = initialize_web3("https://bsc-dataseed.binance.org/")

        # Send a message from Ethereum to Binance Smart Chain
        transaction_id = send_message("Ethereum", "Binance Smart Chain", "Hello from Ethereum!")
        print(f"Message sent! Transaction ID: {transaction_id}")

        # Retrieve messages from Binance Smart Chain
        messages = retrieve_messages("Binance Smart Chain")
        print("Retrieved Messages:", messages)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

Make sure to replace `YOUR_PARTICLE_API_KEY` and `YOUR_INFURA_PROJECT_ID` with your actual API keys before running the code.
