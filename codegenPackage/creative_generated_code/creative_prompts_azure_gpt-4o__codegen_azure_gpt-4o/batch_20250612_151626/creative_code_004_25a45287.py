"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmos-mixer.com
Prompt: Implement a Solidity smart contract that ensures ATOM transactions are sent from standard wallets (non-contract/multisig wallets), as required by Cosmos-Mixer.com.
Generated: DETERMINISTIC_25a4528784cb34dd
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Cosmos Mixer Transaction Validator
 * @dev This contract ensures that ATOM transactions are sent from standard (EOA) wallets only.
 * It prohibits transactions from contract-based or multisig wallets.
 */

contract CosmosMixerValidator {
    // Address to receive the ATOM transactions
    address public cosmosReceiver;

    // Event emitted when a valid transaction is received
    event ValidTransaction(address indexed sender, uint256 amount);

    // Modifier to check if the sender is an externally owned account (EOA)
    modifier onlyEOA() {
        require(tx.origin == msg.sender, "Transactions from non-EOA wallets are not allowed");
        _;
    }

    /**
     * @dev Constructor to initialize the cosmosReceiver address
     * @param _cosmosReceiver Address that will receive the ATOM transactions
     */
    constructor(address _cosmosReceiver) {
        require(_cosmosReceiver != address(0), "Receiver address cannot be the zero address");
        cosmosReceiver = _cosmosReceiver;
    }

    /**
     * @dev Function to validate and forward ATOM transactions from EOA wallets
     * @notice Only EOA wallets are allowed to call this function
     */
    function forwardTransaction() external payable onlyEOA {
        require(msg.value > 0, "Transaction amount must be greater than zero");

        // Forward the funds to the cosmosReceiver
        (bool success, ) = cosmosReceiver.call{value: msg.value}("");
        require(success, "Failed to forward funds to the receiver");

        // Emit an event for a valid transaction
        emit ValidTransaction(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function to prevent accidental transfers directly to the contract
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental transfers directly to the contract
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
