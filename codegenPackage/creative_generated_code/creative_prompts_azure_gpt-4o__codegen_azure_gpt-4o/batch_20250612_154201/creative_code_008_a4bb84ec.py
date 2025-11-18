"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain-frontend.vercel.app
Prompt: Create a function to handle wallet connection to Berachain and implement error handling for unsupported networks.
Generated: DETERMINISTIC_a4bb84ec7a13e8fd
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SUPPORTED_NETWORKS = ["Berachain"]  # List of supported networks

class WalletConnectionError(Exception):
    """Custom exception for wallet connection errors."""
    pass

def connect_to_wallet(network: str):
    """
    Connects to a wallet on the specified blockchain network.

    Args:
        network (str): The name of the blockchain network to connect to.

    Returns:
        str: Success message on successful connection.

    Raises:
        WalletConnectionError: If the network is unsupported.
    """
    try:
        # Validate if the network is supported
        if network not in SUPPORTED_NETWORKS:
            raise WalletConnectionError(f"Unsupported network: {network}. Supported networks are: {', '.join(SUPPORTED_NETWORKS)}")
        
        # Placeholder for actual wallet connection logic
        # In production, replace the following line with code that integrates with Berachain's SDK or API.
        logging.info(f"Connecting to wallet on the {network} network...")
        # Simulated successful connection
        logging.info(f"Successfully connected to the wallet on the {network} network.")
        return f"Connected to wallet on {network} network."

    except WalletConnectionError as e:
        logging.error(f"Error occurred during wallet connection: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        # Replace 'Berachain' with the desired blockchain network name
        result = connect_to_wallet("Berachain")
        print(result)
    except WalletConnectionError as e:
        print(f"Failed to connect to wallet: {e}")
```
