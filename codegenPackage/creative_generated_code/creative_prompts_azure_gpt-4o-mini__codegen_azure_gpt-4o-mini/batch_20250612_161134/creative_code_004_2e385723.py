"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Create a Solidity event similar to `Log` in the UniswapSlippageBot contract to log specific transaction details in a decentralized application.
Generated: DETERMINISTIC_2e385723656c5c75
Batch ID: 20250612_161134
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
 * @title TransactionLogger
 * @dev A contract to log specific transaction details for a decentralized application.
 */
contract TransactionLogger {

    // Event to log transaction details
    event TransactionLogged(
        address indexed sender,      // Address of the sender
        address indexed recipient,   // Address of the recipient
        uint256 amount,             // Amount of tokens transferred
        uint256 timestamp            // Timestamp of the transaction
    );

    /**
     * @dev Function to log a transaction.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to be transferred.
     */
    function logTransaction(address recipient, uint256 amount) external {
        // Validate the recipient address
        require(recipient != address(0), "Invalid recipient address");
        // Validate the amount
        require(amount > 0, "Amount must be greater than zero");

        // Emit the transaction log event
        emit TransactionLogged(msg.sender, recipient, amount, block.timestamp);
    }
}
```
