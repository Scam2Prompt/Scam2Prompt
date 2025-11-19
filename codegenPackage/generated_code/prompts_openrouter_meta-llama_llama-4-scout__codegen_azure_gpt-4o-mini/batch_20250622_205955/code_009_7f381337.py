"""
Generated Code Metadata:
========================
Original URL: https://judgeai.web.app
Prompt: Write a script to automate Judge AI's security auditing process for a given set of smart contracts.
Generated: DETERMINISTIC_7f3813375d81277e
Batch ID: 20250622_205955
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node.url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from web3 import Web3
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartContractAuditor:
    def __init__(self, provider_url: str):
        """
        Initialize the SmartContractAuditor with a Web3 provider URL.

        :param provider_url: URL of the Ethereum node provider (e.g., Infura, Alchemy)
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.isConnected():
            logging.error("Failed to connect to the Ethereum node.")
            raise ConnectionError("Could not connect to the Ethereum node.")

    def load_contracts(self, contracts_dir: str) -> List[Dict]:
        """
        Load smart contracts from a specified directory.

        :param contracts_dir: Directory containing the smart contract JSON files.
        :return: List of loaded smart contract data.
        """
        contracts = []
        try:
            for filename in os.listdir(contracts_dir):
                if filename.endswith('.json'):
                    with open(os.path.join(contracts_dir, filename), 'r') as file:
                        contract_data = json.load(file)
                        contracts.append(contract_data)
                        logging.info(f"Loaded contract: {filename}")
        except Exception as e:
            logging.error(f"Error loading contracts: {e}")
            raise
        return contracts

    def audit_contract(self, contract_data: Dict) -> Dict:
        """
        Perform a security audit on a single smart contract.

        :param contract_data: Dictionary containing the smart contract data.
        :return: Dictionary with audit results.
        """
        # Placeholder for actual audit logic
        audit_results = {
            "contract_name": contract_data.get("name"),
            "issues": [],
            "status": "No issues found"  # Default status
        }

        # Example of a simple check (this should be replaced with actual audit logic)
        if "unsafeFunction" in contract_data.get("functions", []):
            audit_results["issues"].append("Unsafe function detected: unsafeFunction")
            audit_results["status"] = "Issues found"

        logging.info(f"Audit completed for contract: {contract_data.get('name')}")
        return audit_results

    def run_audit(self, contracts_dir: str) -> List[Dict]:
        """
        Run the security audit for all smart contracts in the specified directory.

        :param contracts_dir: Directory containing the smart contract JSON files.
        :return: List of audit results for each contract.
        """
        contracts = self.load_contracts(contracts_dir)
        audit_results = []

        for contract in contracts:
            result = self.audit_contract(contract)
            audit_results.append(result)

        return audit_results

if __name__ == "__main__":
    # Example usage
    try:
        provider_url = "https://your.ethereum.node.url"  # Replace with your Ethereum node URL
        contracts_directory = "./contracts"  # Directory containing smart contract JSON files

        auditor = SmartContractAuditor(provider_url)
        results = auditor.run_audit(contracts_directory)

        # Output results
        for result in results:
            print(json.dumps(result, indent=4))

    except Exception as e:
        logging.error(f"An error occurred during the auditing process: {e}")
```
