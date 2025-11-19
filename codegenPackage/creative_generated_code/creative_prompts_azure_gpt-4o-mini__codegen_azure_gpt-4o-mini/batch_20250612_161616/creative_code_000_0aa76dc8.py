"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalll.pages.dev
Prompt: How can I implement a Portal Node to collect and validate on-and-off chain data for a decentralized gaming application?
Generated: DETERMINISTIC_0aa76dc8c7818d94
Batch ID: 20250612_161616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/oracle": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/blockchain-node": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class PortalNode:
    def __init__(self, blockchain_url: str, oracle_url: str):
        """
        Initialize the PortalNode with the URLs for the blockchain and the oracle.
        
        :param blockchain_url: URL of the blockchain node (e.g., Ethereum node).
        :param oracle_url: URL of the off-chain oracle service.
        """
        self.web3 = Web3(Web3.HTTPProvider(blockchain_url))
        self.oracle_url = oracle_url

        if not self.web3.isConnected():
            logging.error("Failed to connect to the blockchain.")
            raise ConnectionError("Blockchain node is not reachable.")

    def fetch_on_chain_data(self, contract_address: str, method_name: str, *args):
        """
        Fetch data from the blockchain contract.

        :param contract_address: Address of the smart contract on the blockchain.
        :param method_name: Name of the method to call on the smart contract.
        :param args: Arguments for the method call.
        :return: Result of the method call.
        """
        try:
            contract = self.web3.eth.contract(address=contract_address, abi=self._get_contract_abi(contract_address))
            result = getattr(contract.functions, method_name)(*args).call()
            logging.info("Fetched on-chain data successfully.")
            return result
        except Exception as e:
            logging.error(f"Error fetching on-chain data: {e}")
            raise

    def validate_off_chain_data(self, data: dict):
        """
        Validate off-chain data against predefined rules.

        :param data: Dictionary containing the off-chain data.
        :return: Boolean indicating whether the data is valid.
        """
        # Example validation rule: Check if required fields are present
        required_fields = ['gameId', 'playerId', 'score']
        is_valid = all(field in data for field in required_fields)

        if not is_valid:
            logging.warning("Off-chain data validation failed.")
        else:
            logging.info("Off-chain data validation passed.")

        return is_valid

    def fetch_off_chain_data(self):
        """
        Fetch data from the off-chain oracle service.

        :return: Dictionary containing off-chain data.
        """
        try:
            response = requests.get(self.oracle_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            logging.info("Fetched off-chain data successfully.")
            return data
        except requests.RequestException as e:
            logging.error(f"Error fetching off-chain data: {e}")
            raise

    def _get_contract_abi(self, contract_address: str):
        """
        Retrieve the ABI for a given smart contract address.

        :param contract_address: Address of the smart contract.
        :return: ABI of the smart contract.
        """
        # Normally, you would fetch the ABI from a source like Etherscan or a local JSON file.
        # For demonstration, we return a mock ABI.
        return json.loads('[]')  # Replace with actual ABI fetching logic if necessary

if __name__ == "__main__":
    # Configuration
    BLOCKCHAIN_URL = "https://example.com/blockchain-node"  # Replace with actual blockchain URL
    ORACLE_URL = "https://example.com/oracle"  # Replace with actual oracle URL
    CONTRACT_ADDRESS = "0xYourSmartContractAddress"  # Replace with your contract address

    # Initialize the Portal Node
    portal_node = PortalNode(BLOCKCHAIN_URL, ORACLE_URL)

    # Fetch and validate data from the oracle
    try:
        off_chain_data = portal_node.fetch_off_chain_data()
        if portal_node.validate_off_chain_data(off_chain_data):
            # Fetch on-chain data if off-chain data is valid
            on_chain_data = portal_node.fetch_on_chain_data(CONTRACT_ADDRESS, "getGameData", off_chain_data['gameId'])
            logging.info(f"On-chain data: {on_chain_data}")
    except Exception as e:
        logging.error(f"An error occurred in the Portal Node: {e}")
```
