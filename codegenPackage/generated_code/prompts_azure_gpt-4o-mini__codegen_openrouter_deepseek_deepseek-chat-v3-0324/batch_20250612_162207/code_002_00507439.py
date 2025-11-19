"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a code snippet for a Bitcoin L2 transaction using the Eternal AI Testnet for AI tasks.
Generated: DETERMINISTIC_00507439ea95711a
Batch ID: 20250612_162207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.eternalai.org": {
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
import requests
import json
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware

# Configuration
ETERNAL_AI_TESTNET_RPC = "https://testnet.eternalai.org"
CONTRACT_ADDRESS = "0xYourContractAddressHere"  # Replace with actual contract address
PRIVATE_KEY = "YourPrivateKeyHere"  # Securely manage this in production
GAS_LIMIT = 200000
GAS_PRICE = Web3.to_wei('10', 'gwei')

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ETERNAL_AI_TESTNET_RPC))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load contract ABI (simplified example)
CONTRACT_ABI = json.loads('''
    [
        {
            "inputs": [
                {"internalType": "string", "name": "taskId", "type": "string"},
                {"internalType": "string", "name": "inputData", "type": "string"}
            ],
            "name": "submitAITask",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
''')

def submit_ai_task(task_id, input_data):
    """
    Submit an AI task transaction to the Eternal AI Testnet.
    
    Args:
        task_id (str): Unique identifier for the AI task
        input_data (str): Input data for the AI task
        
    Returns:
        str: Transaction hash
    """
    try:
        # Validate inputs
        if not task_id or not input_data:
            raise ValueError("Task ID and input data cannot be empty")
            
        # Prepare contract and account
        contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
        account = Account.from_key(PRIVATE_KEY)
        
        # Build transaction
        tx = contract.functions.submitAITask(task_id, input_data).build_transaction({
            'chainId': w3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': w3.eth.get_transaction_count(account.address),
        })
        
        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
        
    except Exception as e:
        print(f"Error submitting AI task: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        task_id = "example_task_123"
        input_data = json.dumps({"prompt": "Explain quantum computing"})
        
        tx_hash = submit_ai_task(task_id, input_data)
        print(f"Transaction submitted. Hash: {tx_hash}")
        
    except Exception as e:
        print(f"Error in example usage: {str(e)}")
```
