"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Create a script to deploy and verify a smart contract on Linea's zkEVM ecosystem, ensuring it adheres to security best practices outlined by Linea.
Generated: DETERMINISTIC_94bfe52992d08b44
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import json
import os
from web3 import Web3
from dotenv import load_dotenv
from solcx import compile_standard, install_solc
from eth_account import Account
from web3.middleware import geth_poa_middleware

# Load environment variables
load_dotenv()

# Constants
CONTRACT_NAME = "SimpleStorage"
CONTRACT_FILE = "SimpleStorage.sol"
LINEA_RPC_URL = os.getenv("LINEA_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CHAIN_ID = 59140  # Linea testnet chain ID

# Install specific Solidity compiler version
install_solc("0.8.0")

def compile_contract():
    """Compile the Solidity smart contract."""
    with open(CONTRACT_FILE, "r") as file:
        contract_source = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {CONTRACT_FILE: {"content": contract_source}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.0",
    )

    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)

    return compiled_sol

def deploy_contract(compiled_sol):
    """Deploy the compiled contract to Linea zkEVM."""
    # Get bytecode and ABI
    bytecode = compiled_sol["contracts"][CONTRACT_FILE][CONTRACT_NAME]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"][CONTRACT_FILE][CONTRACT_NAME]["abi"]

    # Connect to Linea
    w3 = Web3(Web3.HTTPProvider(LINEA_RPC_URL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Create contract instance
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Get nonce
    account = Account.from_key(PRIVATE_KEY)
    nonce = w3.eth.get_transaction_count(account.address)

    # Build transaction
    transaction = contract.constructor().build_transaction(
        {
            "chainId": CHAIN_ID,
            "gasPrice": w3.eth.gas_price,
            "from": account.address,
            "nonce": nonce,
        }
    )

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_receipt, abi

def verify_contract(w3, contract_address, abi):
    """Verify the deployed contract by interacting with it."""
    contract = w3.eth.contract(address=contract_address, abi=abi)
    
    # Example verification - call a simple function
    try:
        initial_value = contract.functions.retrieve().call()
        print(f"Initial contract value: {initial_value}")
        
        # Test a transaction
        account = Account.from_key(PRIVATE_KEY)
        nonce = w3.eth.get_transaction_count(account.address)
        
        store_txn = contract.functions.store(42).build_transaction({
            "chainId": CHAIN_ID,
            "gasPrice": w3.eth.gas_price,
            "from": account.address,
            "nonce": nonce,
        })
        
        signed_store_txn = w3.eth.account.sign_transaction(store_txn, private_key=PRIVATE_KEY)
        store_tx_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
        w3.eth.wait_for_transaction_receipt(store_tx_hash)
        
        new_value = contract.functions.retrieve().call()
        print(f"New contract value: {new_value}")
        
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

def main():
    try:
        # Compile contract
        print("Compiling contract...")
        compiled_sol = compile_contract()
        
        # Deploy contract
        print("Deploying contract...")
        tx_receipt, abi = deploy_contract(compiled_sol)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")
        
        # Verify contract
        w3 = Web3(Web3.HTTPProvider(LINEA_RPC_URL))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        print("Verifying contract...")
        if verify_contract(w3, tx_receipt.contractAddress, abi):
            print("Contract verification successful!")
        else:
            print("Contract verification failed.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
