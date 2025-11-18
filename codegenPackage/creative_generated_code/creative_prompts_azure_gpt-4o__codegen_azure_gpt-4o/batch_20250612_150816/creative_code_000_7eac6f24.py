"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel-explorer.vercel.app
Prompt: Write a smart contract using FuelVM that interacts with the Fuel blockchain to track and store recent transactions. Reference the Fuel Explorer for transaction details.
Generated: DETERMINISTIC_7eac6f2426c3bef4
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

// FuelVM Smart Contract to track and store recent transactions
contract FuelTransactionTracker {
    // Maximum number of transactions to store
    uint256 public constant MAX_TRANSACTIONS = 100;

    // Struct to represent a transaction
    struct Transaction {
        string id;         // Transaction ID
        string sender;     // Sender address
        string receiver;   // Receiver address
        uint256 value;     // Value transferred
        uint256 timestamp; // Transaction timestamp
    }

    // Array to store recent transactions
    Transaction[] private recentTransactions;

    // Event to emit when a new transaction is added
    event TransactionAdded(
        string id,
        string sender,
        string receiver,
        uint256 value,
        uint256 timestamp
    );

    // Modifier to ensure no overflow of transactions in storage
    modifier checkTransactionLimit() {
        require(
            recentTransactions.length < MAX_TRANSACTIONS,
            "Transaction limit reached"
        );
        _;
    }

    // Function to add a transaction to the tracker
    // Ensures the transaction data is valid and within limits
    function addTransaction(
        string memory id,
        string memory sender,
        string memory receiver,
        uint256 value,
        uint256 timestamp
    ) public checkTransactionLimit {
        require(bytes(id).length > 0, "Transaction ID cannot be empty");
        require(bytes(sender).length > 0, "Sender cannot be empty");
        require(bytes(receiver).length > 0, "Receiver cannot be empty");
        require(value > 0, "Transaction value must be greater than zero");
        require(timestamp > 0, "Timestamp must be valid");

        // Create transaction object
        Transaction memory newTransaction = Transaction(
            id,
            sender,
            receiver,
            value,
            timestamp
        );

        // Add to the recent transactions array
        recentTransactions.push(newTransaction);

        // Emit the event for the added transaction
        emit TransactionAdded(id, sender, receiver, value, timestamp);
    }

    // Function to retrieve recent transactions
    function getRecentTransactions() public view returns (Transaction[] memory) {
        return recentTransactions;
    }

    // Function to clear all stored transactions
    // Resets the recent transactions array
    function clearTransactions() public {
        delete recentTransactions;
    }

    // Function to get the total number of stored transactions
    function getTransactionCount() public view returns (uint256) {
        return recentTransactions.length;
    }
}
```
