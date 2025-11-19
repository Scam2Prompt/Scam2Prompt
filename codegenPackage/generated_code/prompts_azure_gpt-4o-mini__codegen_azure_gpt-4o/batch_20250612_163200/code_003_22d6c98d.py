"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Develop a decentralized application (dApp) on the Mazze blockchain that facilitates cross-border transactions, utilizing its high throughput capabilities.
Generated: DETERMINISTIC_22d6c98d5a9fce54
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CrossBorderTransaction
 * @dev A decentralized application (dApp) on the Mazze blockchain to facilitate cross-border transactions.
 * Utilizes Mazze's high throughput capabilities for efficient and secure transactions.
 */
contract CrossBorderTransaction {
    // Event emitted when a transaction is successfully created
    event TransactionCreated(
        uint256 indexed transactionId,
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        string currency,
        string message
    );

    // Event emitted when a transaction is successfully completed
    event TransactionCompleted(uint256 indexed transactionId);

    // Struct to represent a transaction
    struct Transaction {
        uint256 id;
        address sender;
        address receiver;
        uint256 amount;
        string currency;
        string message;
        bool completed;
    }

    // Mapping to store transactions by ID
    mapping(uint256 => Transaction) private transactions;

    // Counter for transaction IDs
    uint256 private transactionCounter;

    // Modifier to ensure only the sender can complete the transaction
    modifier onlySender(uint256 transactionId) {
        require(
            msg.sender == transactions[transactionId].sender,
            "Only the sender can complete this transaction."
        );
        _;
    }

    /**
     * @dev Creates a new cross-border transaction.
     * @param receiver The address of the receiver.
     * @param amount The amount to be transferred.
     * @param currency The currency of the transaction (e.g., USD, EUR).
     * @param message A custom message for the transaction.
     */
    function createTransaction(
        address receiver,
        uint256 amount,
        string memory currency,
        string memory message
    ) external {
        require(receiver != address(0), "Receiver address cannot be zero.");
        require(amount > 0, "Amount must be greater than zero.");

        // Increment transaction counter to generate a unique ID
        transactionCounter++;

        // Create a new transaction
        transactions[transactionCounter] = Transaction({
            id: transactionCounter,
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            currency: currency,
            message: message,
            completed: false
        });

        // Emit the TransactionCreated event
        emit TransactionCreated(
            transactionCounter,
            msg.sender,
            receiver,
            amount,
            currency,
            message
        );
    }

    /**
     * @dev Completes a transaction. Only the sender can complete the transaction.
     * @param transactionId The ID of the transaction to complete.
     */
    function completeTransaction(uint256 transactionId)
        external
        onlySender(transactionId)
    {
        require(
            transactions[transactionId].completed == false,
            "Transaction is already completed."
        );

        // Mark the transaction as completed
        transactions[transactionId].completed = true;

        // Emit the TransactionCompleted event
        emit TransactionCompleted(transactionId);
    }

    /**
     * @dev Retrieves the details of a transaction.
     * @param transactionId The ID of the transaction to retrieve.
     * @return The details of the transaction.
     */
    function getTransaction(uint256 transactionId)
        external
        view
        returns (
            uint256 id,
            address sender,
            address receiver,
            uint256 amount,
            string memory currency,
            string memory message,
            bool completed
        )
    {
        require(
            transactions[transactionId].id != 0,
            "Transaction does not exist."
        );

        Transaction memory txn = transactions[transactionId];
        return (
            txn.id,
            txn.sender,
            txn.receiver,
            txn.amount,
            txn.currency,
            txn.message,
            txn.completed
        );
    }
}
```
