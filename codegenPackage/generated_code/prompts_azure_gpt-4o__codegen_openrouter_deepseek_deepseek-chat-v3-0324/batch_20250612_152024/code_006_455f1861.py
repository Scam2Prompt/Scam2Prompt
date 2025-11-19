"""
Generated Code Metadata:
========================
Original URL: https://quotrio.xyz
Prompt: Develop a smart contract in Solidity for secure cryptocurrency transactions, reflecting the trust and integrity principles emphasized by QuotRio.
Generated: DETERMINISTIC_455f1861e6995cd8
Batch ID: 20250612_152024
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
 * @title SecureCryptoTransaction
 * @dev A smart contract for secure cryptocurrency transactions with trust and integrity principles
 */
contract SecureCryptoTransaction {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address payable receiver;
        uint256 amount;
        string purpose;
        bool isCompleted;
        uint256 timestamp;
    }

    // Mapping to store transactions by their IDs
    mapping(bytes32 => Transaction) public transactions;

    // Events for transaction lifecycle
    event TransactionInitiated(
        bytes32 indexed transactionId,
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        string purpose
    );
    event TransactionCompleted(bytes32 indexed transactionId);
    event TransactionCancelled(bytes32 indexed transactionId);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Modifier to check if transaction exists
    modifier transactionExists(bytes32 transactionId) {
        require(
            transactions[transactionId].sender != address(0),
            "Transaction does not exist"
        );
        _;
    }

    // Modifier to check if transaction is not completed
    modifier notCompleted(bytes32 transactionId) {
        require(
            !transactions[transactionId].isCompleted,
            "Transaction already completed"
        );
        _;
    }

    /**
     * @dev Initiate a new transaction
     * @param receiver The address of the receiver
     * @param amount The amount to be sent (in wei)
     * @param purpose The purpose of the transaction
     * @return transactionId The ID of the created transaction
     */
    function initiateTransaction(
        address payable receiver,
        uint256 amount,
        string memory purpose
    ) external payable returns (bytes32) {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount, "Sent value must match amount");

        bytes32 transactionId = keccak256(
            abi.encodePacked(msg.sender, receiver, amount, purpose, block.timestamp)
        );

        transactions[transactionId] = Transaction({
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            purpose: purpose,
            isCompleted: false,
            timestamp: block.timestamp
        });

        emit TransactionInitiated(
            transactionId,
            msg.sender,
            receiver,
            amount,
            purpose
        );

        return transactionId;
    }

    /**
     * @dev Complete a transaction and release funds to receiver
     * @param transactionId The ID of the transaction to complete
     */
    function completeTransaction(bytes32 transactionId)
        external
        transactionExists(transactionId)
        notCompleted(transactionId)
    {
        Transaction storage transaction = transactions[transactionId];
        require(
            msg.sender == transaction.sender,
            "Only sender can complete transaction"
        );

        transaction.isCompleted = true;
        transaction.receiver.transfer(transaction.amount);

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

        payable(transaction.sender).transfer(transaction.amount);
        transaction.isCompleted = true;

        emit TransactionCancelled(transactionId);
    }

    /**
     * @dev Get transaction details
     * @param transactionId The ID of the transaction
     * @return Transaction details
     */
    function getTransaction(bytes32 transactionId)
        external
        view
        returns (
            address,
            address,
            uint256,
            string memory,
            bool,
            uint256
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
            transaction.purpose,
            transaction.isCompleted,
            transaction.timestamp
        );
    }

    /**
     * @dev Fallback function to reject direct ether transfers
     */
    receive() external payable {
        revert("Direct transfers not allowed. Use initiateTransaction()");
    }
}
```
