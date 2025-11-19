"""
Generated Code Metadata:
========================
Original URL: https://base--chain.pages.dev
Prompt: Write a Python script using Web3.py library to deploy a smart contract on Base, an Ethereum L2 solution by Coinbase, and interact with it using EVM equivalent code.
Generated: DETERMINISTIC_ddb2bc8ca1843c84
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from web3 import Web3
from solcx import compile_source

# Ensure solc is installed and set up
from solcx import install_solc
install_solc('0.8.0')  # Install Solidity compiler version 0.8.0

# Load environment variables for sensitive data
from dotenv import load_dotenv
load_dotenv()

# Constants
BASE_RPC_URL = os.getenv("BASE_RPC_URL")  # Base L2 RPC URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the deployer account
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")  # Address of the deployer account

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Base RPC URL.")

# Ensure the account is unlocked and valid
if not web3.isAddress(ACCOUNT_ADDRESS):
    raise ValueError("Invalid account address.")

# Solidity source code for the smart contract
contract_source_code = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;

    event DataStored(uint256 data);

    function set(uint256 x) public {
        storedData = x;
        emit DataStored(x);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
"""

# Compile the Solidity contract
compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])
contract_id, contract_interface = compiled_sol.popitem()

# Extract ABI and bytecode
contract_abi = contract_interface["abi"]
contract_bytecode = contract_interface["bin"]

# Create contract object
SimpleStorage = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

# Get the nonce for the deployer account
nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)

# Build the transaction for contract deployment
transaction = SimpleStorage.constructor().build_transaction({
    "chainId": web3.eth.chain_id,
    "gas": 3000000,
    "gasPrice": web3.to_wei("10", "gwei"),
    "nonce": nonce,
})

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction receipt
print("Deploying contract...")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed at address: {tx_receipt.contractAddress}")

# Interact with the deployed contract
contract_instance = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_abi
)

# Function to set a value in the contract
def set_value(value):
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    transaction = contract_instance.functions.set(value).build_transaction({
        "chainId": web3.eth.chain_id,
        "gas": 200000,
        "gasPrice": web3.to_wei("10", "gwei"),
        "nonce": nonce,
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Setting value...")
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Value set successfully. Transaction hash: {tx_receipt.transactionHash.hex()}")

# Function to get the stored value from the contract
def get_value():
    value = contract_instance.functions.get().call()
    print(f"Stored value: {value}")
    return value

# Example usage
if __name__ == "__main__":
    try:
        set_value(42)  # Set a value in the contract
        get_value()    # Retrieve the value from the contract
    except Exception as e:
        print(f"An error occurred: {e}")
```
