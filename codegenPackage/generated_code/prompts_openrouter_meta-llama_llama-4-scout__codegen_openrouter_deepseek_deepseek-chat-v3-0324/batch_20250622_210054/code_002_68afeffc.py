"""
Generated Code Metadata:
========================
Original URL: https://app-explorer.pages.dev
Prompt: Generate a smart contract code for a Dapp that requires secure and trustless transactions on a decentralized network.
Generated: DETERMINISTIC_68afeffc3bae3f64
Batch ID: 20250622_210054
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
 * @title SecureTrustlessTransaction
 * @dev A smart contract for secure and trustless transactions on a decentralized network
 */
contract SecureTrustlessTransaction {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address receiver;
        uint256 amount;
        uint256 timestamp;
        bool isCompleted;
    }

    // Mapping to store transactions by their ID
    mapping(bytes32 => Transaction) public transactions;

    // Event emitted when a new transaction is created
    event TransactionCreated(
        bytes32 indexed transactionId,
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        uint256 timestamp
    );

    // Event emitted when a transaction is completed
    event TransactionCompleted(bytes32 indexed transactionId);

    // Modifier to check if the transaction exists
    modifier transactionExists(bytes32 transactionId) {
        require(
            transactions[transactionId].sender != address(0),
            "Transaction does not exist"
        );
        _;
    }

    // Modifier to check if the transaction is not completed
    modifier notCompleted(bytes32 transactionId) {
        require(
            !transactions[transactionId].isCompleted,
            "Transaction already completed"
        );
        _;
    }

    /**
     * @dev Create a new transaction
     * @param receiver The address of the receiver
     * @param amount The amount to be transferred
     * @return transactionId The ID of the created transaction
     */
    function createTransaction(address receiver, uint256 amount)
        external
        payable
        returns (bytes32)
    {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Sent value must match amount");

        bytes32 transactionId = keccak256(
            abi.encodePacked(msg.sender, receiver, amount, block.timestamp)
        );

        transactions[transactionId] = Transaction({
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            timestamp: block.timestamp,
            isCompleted: false
        });

        emit TransactionCreated(
            transactionId,
            msg.sender,
            receiver,
            amount,
            block.timestamp
        );

        return transactionId;
    }

    /**
     * @dev Complete a transaction
     * @param transactionId The ID of the transaction to complete
     */
    function completeTransaction(bytes32 transactionId)
        external
        transactionExists(transactionId)
        notCompleted(transactionId)
    {
        Transaction storage transaction = transactions[transactionId];

        require(
            msg.sender == transaction.receiver,
            "Only receiver can complete transaction"
        );

        transaction.isCompleted = true;
        payable(transaction.receiver).transfer(transaction.amount);

        emit TransactionCompleted(transactionId);
    }

    /**
     * @dev Cancel a transaction and refund the sender
     * @param transactionId The ID of the transaction to cancel
     */
    function cancelTransaction(bytes32 transactionId)
        external
        transactionExists(transactionId)
        notCompleted(transactionId)
    {
        Transaction storage transaction = transactions[transactionId];

        require(
            msg.sender == transaction.sender,
            "Only sender can cancel transaction"
        );

        transaction.isCompleted = true;
        payable(transaction.sender).transfer(transaction.amount);

        emit TransactionCompleted(transactionId);
    }

    /**
     * @dev Get transaction details
     * @param transactionId The ID of the transaction
     * @return sender The sender's address
     * @return receiver The receiver's address
     * @return amount The transaction amount
     * @return timestamp The transaction creation timestamp
     * @return isCompleted Whether the transaction is completed
     */
    function getTransaction(bytes32 transactionId)
        external
        view
        returns (
            address sender,
            address receiver,
            uint256 amount,
            uint256 timestamp,
            bool isCompleted
        )
    {
        Transaction storage transaction = transactions[transactionId];
        require(
            transaction.sender != address(0),
            "Transaction does not exist"
        );

        return (
            transaction.sender,
            transaction.receiver,
            transaction.amount,
            transaction.timestamp,
            transaction.isCompleted
        );
    }
}
```
