"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Write code to implement a discovery process for buyers of video content, leveraging blockchain technology to enhance transparency and efficiency, as described in the MILC Project.
Generated: DETERMINISTIC_dae100c54ec5aeb4
Batch ID: 20250612_151027
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
"""
A Python implementation of a discovery process for buyers of video content using blockchain technology. 
This code leverages smart contracts on the Ethereum blockchain to enhance transparency and efficiency.
"""

from web3 import Web3, exceptions

# Constants for the blockchain network
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CONTRACT_ADDRESS = "0xYourSmartContractAddressHere"
ABI = [
    # Replace with your smart contract's ABI
]

# Establish a connection to the Ethereum blockchain
class BlockchainClient:
    def __init__(self, infura_url, contract_address, abi):
        """
        Initialize the Blockchain client with the specified Infura URL, contract address, and ABI.
        """
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum blockchain.")
        
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)
    
    def get_content_list(self):
        """
        Fetch the list of available video content from the blockchain.
        Returns:
            list: A list of available video content metadata.
        """
        try:
            # Assuming the smart contract has a function `getContentList` for fetching content metadata
            content_list = self.contract.functions.getContentList().call()
            return content_list
        except exceptions.ContractLogicError as e:
            raise RuntimeError(f"Smart contract error: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

    def get_content_details(self, content_id):
        """
        Fetch detailed metadata for a specific video content by content ID.
        Args:
            content_id (int): The ID of the video content.
        Returns:
            dict: Detailed metadata for the specified content.
        """
        try:
            # Assuming the smart contract has a function `getContentDetails` for fetching details
            content_details = self.contract.functions.getContentDetails(content_id).call()
            return content_details
        except exceptions.ContractLogicError as e:
            raise RuntimeError(f"Smart contract error: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Buyer Discovery Process
class BuyerDiscovery:
    def __init__(self, blockchain_client):
        """
        Initialize the Buyer Discovery process with a Blockchain client.
        """
        self.blockchain_client = blockchain_client
    
    def discover_content(self):
        """
        Discovery process for buyers to identify available video content.
        Returns:
            list: A list of video content available for purchase.
        """
        try:
            content_list = self.blockchain_client.get_content_list()
            return content_list
        except RuntimeError as e:
            print(f"Error during content discovery: {str(e)}")
            return []

    def fetch_content_details(self, content_id):
        """
        Fetch details of the selected video content.
        Args:
            content_id (int): The ID of the video content.
        Returns:
            dict: Detailed metadata of the selected content.
        """
        try:
            content_details = self.blockchain_client.get_content_details(content_id)
            return content_details
        except RuntimeError as e:
            print(f"Error fetching content details: {str(e)}")
            return {}

# Main usage example
if __name__ == "__main__":
    try:
        # Initialize the Blockchain client
        blockchain_client = BlockchainClient(INFURA_URL, CONTRACT_ADDRESS, ABI)
        
        # Initialize the buyer discovery process
        buyer_discovery = BuyerDiscovery(blockchain_client)
        
        # Discover available content
        print("Discovering content...")
        content_list = buyer_discovery.discover_content()
        for content in content_list:
            print(f"Content ID: {content['id']}, Title: {content['title']}")
        
        # Fetch details of a specific content
        content_id_to_fetch = 1  # Replace with the actual content ID
        print(f"\nFetching details for content ID {content_id_to_fetch}...")
        content_details = buyer_discovery.fetch_content_details(content_id_to_fetch)
        print(content_details)
    except ConnectionError as e:
        print(f"Blockchain connection error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```

### Instructions:
1. Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
2. Replace `0xYourSmartContractAddressHere` with the address of your smart contract.
3. Replace the `ABI` list with the ABI of your smart contract.
4. Ensure your smart contract implements the required functions (`getContentList` and `getContentDetails`) as described in this code.
