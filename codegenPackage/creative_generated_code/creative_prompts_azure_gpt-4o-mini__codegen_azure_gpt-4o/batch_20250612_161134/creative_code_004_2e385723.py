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
    // Event declaration to log transaction details.
    event TransactionLog(
        address indexed sender, // Address initiating the transaction
        uint256 indexed timestamp, // Unix timestamp of the transaction
        uint256 amount, // Amount involved in the transaction
        string transactionType // Type of transaction (e.g., "Buy", "Sell", "Transfer")
    );

    /**
     * @dev Logs a transaction's details by emitting the TransactionLog event.
     * @param sender The address initiating the transaction.
     * @param amount The amount involved in the transaction.
     * @param transactionType The type of transaction (e.g., "Buy", "Sell", "Transfer").
     */
    function logTransaction(
        address sender,
        uint256 amount,
        string memory transactionType
    ) external {
        require(amount > 0, "Transaction amount must be greater than zero");
        require(bytes(transactionType).length > 0, "Transaction type cannot be empty");

        // Emit the TransactionLog event with the provided details.
        emit TransactionLog(sender, block.timestamp, amount, transactionType);
    }
}
```
