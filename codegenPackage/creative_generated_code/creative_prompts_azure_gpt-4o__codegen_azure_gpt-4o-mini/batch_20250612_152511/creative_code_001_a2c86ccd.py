"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanetworks.pages.dev
Prompt: How can I use LavaSDK to send a relay request to fetch node information from the Axelar blockchain? Provide a code example.
Generated: DETERMINISTIC_a2c86ccdef8d0ac9
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from the LavaSDK
from lavsdk import LavaSDK
from lavsdk.exceptions import LavaSDKError

# Initialize the LavaSDK client with the appropriate configuration
def initialize_lava_sdk(api_key):
    """
    Initializes the LavaSDK client with the provided API key.

    :param api_key: str - The API key for accessing the LavaSDK
    :return: LavaSDK - An instance of the LavaSDK client
    """
    try:
        return LavaSDK(api_key=api_key)
    except LavaSDKError as e:
        raise RuntimeError("Failed to initialize LavaSDK: " + str(e))

# Function to send a relay request to fetch node information from Axelar blockchain
def fetch_node_information(lava_sdk, chain_name):
    """
    Sends a relay request to fetch node information from the specified blockchain.

    :param lava_sdk: LavaSDK - An instance of the LavaSDK client
    :param chain_name: str - The name of the blockchain (e.g., 'axelar')
    :return: dict - The node information retrieved from the blockchain
    """
    try:
        response = lava_sdk.relay.request(
            chain=chain_name,
            method='GET',
            endpoint='/node/information'
        )
        return response
    except LavaSDKError as e:
        raise RuntimeError("Failed to fetch node information: " + str(e))

# Main function to execute the process
def main():
    """
    Main function to execute the LavaSDK relay request to fetch node information.
    """
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your LavaSDK API key
    chain_name = 'axelar'  # The blockchain for which to fetch information

    # Initialize the LavaSDK client
    lava_sdk = initialize_lava_sdk(api_key)

    # Fetch node information
    try:
        node_info = fetch_node_information(lava_sdk, chain_name)
        print("Node Information:", node_info)
    except RuntimeError as e:
        print("Error:", e)

# Entry point of the script
if __name__ == '__main__':
    main()
```
