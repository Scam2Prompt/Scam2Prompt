"""
Generated Code Metadata:
========================
Original URL: https://ton4.org
Prompt: Create a smart contract using TON blockchain for secure and automated business transactions, emphasizing its security features.
Generated: DETERMINISTIC_b98e7344cace777a
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma ton-solidity >=0.47.0;

// Import necessary libraries and interfaces
import "ton-crypto.sol"; // Importing cryptographic functions for security
import "ton-evm.sol"; // Importing EVM compatibility for smart contracts

// Define the main contract
contract SecureBusinessTransaction {
    // Event to log successful transactions
    event TransactionExecuted(address indexed sender, address indexed receiver, uint256 amount, string message);

    // Struct to hold transaction details
    struct Transaction {
        address sender;
        address receiver;
        uint256 amount;
        string message;
        bool executed;
    }

    // Mapping to store transactions by their unique ID
    mapping(uint256 => Transaction) public transactions;
    uint256 public transactionCount;

    // Modifier to check if the transaction exists
    modifier transactionExists(uint256 _transactionId) {
        require(transactions[_transactionId].sender != address(0), "Transaction does not exist");
        _;
    }

    // Function to create a new transaction
    function createTransaction(address _receiver, uint256 _amount, string memory _message) public {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount > 0, "Amount must be greater than zero");

        // Increment transaction count to create a unique ID
        transactionCount++;
        transactions[transactionCount] = Transaction(msg.sender, _receiver, _amount, _message, false);
    }

    // Function to execute a transaction
    function executeTransaction(uint256 _transactionId) public transactionExists(_transactionId) {
        Transaction storage transaction = transactions[_transactionId];

        // Ensure the transaction has not been executed yet
        require(!transaction.executed, "Transaction already executed");
        require(msg.sender == transaction.sender, "Only the sender can execute this transaction");

        // Transfer the amount to the receiver
        // Note: In a real implementation, you would use a token transfer function
        // For demonstration, we assume the transfer is successful
        // token.transfer(transaction.receiver, transaction.amount);

        // Mark the transaction as executed
        transaction.executed = true;

        // Emit the transaction executed event
        emit TransactionExecuted(transaction.sender, transaction.receiver, transaction.amount, transaction.message);
    }

    // Function to get transaction details
    function getTransaction(uint256 _transactionId) public view transactionExists(_transactionId) returns (address, address, uint256, string memory, bool) {
        Transaction memory transaction = transactions[_transactionId];
        return (transaction.sender, transaction.receiver, transaction.amount, transaction.message, transaction.executed);
    }
}
```
