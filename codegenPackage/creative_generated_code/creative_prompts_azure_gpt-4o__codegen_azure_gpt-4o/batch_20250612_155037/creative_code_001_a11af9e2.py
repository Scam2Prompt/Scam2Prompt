"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperlane.cc
Prompt: Explain how to customize the security settings of a chain using Hyperlane's modular validator system. Provide code examples for implementing a custom validator module.
Generated: DETERMINISTIC_a11af9e2a285c6f3
Batch ID: 20250612_155037
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-ethereum-node-provider": {
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
Hyperlane Custom Validator Module Implementation

This script demonstrates how to implement a custom validator module using Hyperlane's modular validator system.
Hyperlane is an interoperability platform for connecting blockchains. The modular validator system allows users to 
define custom security settings for message validation.

This example assumes the use of Python and Solidity, as Hyperlane operates in the blockchain space.
"""

# Solidity contract for a custom validator module
# Save this portion as CustomValidator.sol
pragma solidity ^0.8.0;

// Import Hyperlane's IValidator interface
import "@hyperlane-xyz/core/interfaces/IValidator.sol";

/**
 * @title CustomValidator
 * @notice Implements a custom validator module for Hyperlane.
 */
contract CustomValidator is IValidator {
    address public owner;
    mapping(bytes32 => bool) public validMessages;

    /**
     * @dev Initializes the validator contract with an owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Restricts function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "CustomValidator: Caller is not the owner");
        _;
    }

    /**
     * @dev Updates the validity of a message hash.
     * @param messageHash The hash of the message to be updated.
     * @param isValid Whether the message hash is valid.
     */
    function updateMessageValidity(bytes32 messageHash, bool isValid) external onlyOwner {
        validMessages[messageHash] = isValid;
    }

    /**
     * @dev Validates a message hash.
     * @param messageHash The hash of the message to be validated.
     * @return Returns true if the message hash is valid, otherwise false.
     */
    function isValid(bytes32 messageHash) external view override returns (bool) {
        return validMessages[messageHash];
    }
}

# Python script for deploying and interacting with the custom validator
# Save this portion as deploy_custom_validator.py
from web3 import Web3
from solcx import compile_source

# Define the Solidity source code
SOLIDITY_SOURCE = """
pragma solidity ^0.8.0;
import "@hyperlane-xyz/core/interfaces/IValidator.sol";

contract CustomValidator is IValidator {
    address public owner;
    mapping(bytes32 => bool) public validMessages;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "CustomValidator: Caller is not the owner");
        _;
    }

    function updateMessageValidity(bytes32 messageHash, bool isValid) external onlyOwner {
        validMessages[messageHash] = isValid;
    }

    function isValid(bytes32 messageHash) external view override returns (bool) {
        return validMessages[messageHash];
    }
}
"""

# Compile the Solidity contract
compiled_sol = compile_source(SOLIDITY_SOURCE)
contract_interface = compiled_sol['<stdin>:CustomValidator']

# Connect to an Ethereum node provider (e.g., Infura or local Ganache instance)
web3 = Web3(Web3.HTTPProvider("https://your-ethereum-node-provider"))

# Unlock the account used for deployment
web3.eth.default_account = web3.eth.accounts[0]

# Deploy the contract
CustomValidator = web3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)
tx_hash = CustomValidator.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Fetch the deployed contract instance
custom_validator_instance = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi']
)

# Example usage: Update a message's validity and validate it
message_hash = web3.sha3(text="example-message")
tx_hash = custom_validator_instance.functions.updateMessageValidity(message_hash, True).transact()
web3.eth.wait_for_transaction_receipt(tx_hash)

is_valid = custom_validator_instance.functions.isValid(message_hash).call()
print(f"Message validity: {is_valid}")

"""
NOTES:
1. Ensure you have the necessary dependencies installed (`web3`, `py-solc-x`, etc.).
2. Replace "https://your-ethereum-node-provider" with a valid Ethereum node provider URL.
3. Adjust gas fees and transaction parameters as needed for your environment.
"""
```
