"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedsolutionchain.pages.dev
Prompt: Provide an example of how to connect to Dapps while troubleshooting connection errors, referencing the Secured Solution Chain's approach.
Generated: DETERMINISTIC_53afb24bd3dfd87b
Batch ID: 20250612_163443
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
import web3
from web3 import Web3, exceptions

# Define a function to connect to a DApp
def connect_to_dapp(infura_url):
    """
    Connects to a decentralized application (DApp) using the provided Infura URL.
    
    Args:
        infura_url (str): The Infura endpoint for connecting to the Ethereum network.
    
    Returns:
        Web3: An instance of the Web3 connection to the Ethereum network.
    
    Raises:
        ConnectionError: If unable to connect to the Ethereum network.
    """
    try:
        # Initialize a Web3 connection
        w3 = Web3(Web3.HTTPProvider(infura_url))
        
        # Check if the connection is successful
        if not w3.isConnected():
            raise ConnectionError("Unable to connect to the Ethereum network. Please check the Infura URL.")
        
        print("Successfully connected to the DApp.")
        return w3
    
    except exceptions.InvalidAddress as e:
        raise ConnectionError(f"Invalid Infura URL provided: {e}")
    except Exception as e:
        raise ConnectionError(f"An error occurred while connecting to the DApp: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual Infura project URL
    infura_project_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    
    try:
        w3_instance = connect_to_dapp(infura_project_url)
        # Further interactions with the DApp can be placed here
        
    except ConnectionError as ce:
        print(ce)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
