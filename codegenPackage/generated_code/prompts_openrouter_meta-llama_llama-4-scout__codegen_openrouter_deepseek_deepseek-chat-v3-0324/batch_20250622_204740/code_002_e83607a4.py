"""
Generated Code Metadata:
========================
Original URL: https://multihelp.pages.dev
Prompt: "Generate a smart contract code for a decentralized application that requires secure, trustless transactions and censorship resistance, using Solidity for Ethereum."
Generated: DETERMINISTIC_e83607a4e3d7848b
Batch ID: 20250622_204740
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
 * @dev A smart contract for secure, trustless transactions with censorship resistance
 */
contract SecureTrustlessTransaction {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address receiver;
        uint256 amount;
        string description;
        bool isCompleted;
        uint256 timestamp;
    }

    // Mapping to store transactions by their ID
    mapping(bytes32 => Transaction) public transactions;

    // Event emitted when a new transaction is created
    event TransactionCreated(
        bytes32 indexed transactionId,
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        string description,
        uint256 timestamp
    );

    // Event emitted when a transaction is completed
    event TransactionCompleted(bytes32 indexed transactionId);

    // Modifier to check if the transaction exists
    modifier transactionExists(bytes32 _transactionId) {
        require(
            transactions[_transactionId].sender != address(0),
            "Transaction does not exist"
        );
        _;
    }

    // Modifier to check if the transaction is not completed
    modifier notCompleted(bytes32 _transactionId) {
        require(
            !transactions[_transactionId].isCompleted,
            "Transaction already completed"
        );
        _;
    }

    // Modifier to check if the caller is the sender
    modifier onlySender(bytes32 _transactionId) {
        require(
            msg.sender == transactions[_transactionId].sender,
            "Only sender can call this function"
        );
        _;
    }

    // Modifier to check if the caller is the receiver
    modifier onlyReceiver(bytes32 _transactionId) {
        require(
            msg.sender == transactions[_transactionId].receiver,
            "Only receiver can call this function"
        );
        _;
    }

    /**
     * @dev Create a new transaction
     * @param _receiver Address of the receiver
     * @param _amount Amount to be transferred
     * @param _description Description of the transaction
     * @return transactionId The ID of the created transaction
     */
    function createTransaction(
        address _receiver,
        uint256 _amount,
        string memory _description
    ) external payable returns (bytes32) {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == _amount, "Sent value must match amount");

        bytes32 transactionId = keccak256(
            abi.encodePacked(
                msg.sender,
                _receiver,
                _amount,
                _description,
                block.timestamp
            )
        );

        transactions[transactionId] = Transaction({
            sender: msg.sender,
            receiver: _receiver,
            amount: _amount,
            description: _description,
            isCompleted: false,
            timestamp: block.timestamp
        });

        emit TransactionCreated(
            transactionId,
            msg.sender,
            _receiver,
            _amount,
            _description,
            block.timestamp
        );

        return transactionId;
    }

    /**
     * @dev Complete a transaction (receiver confirms receipt)
     * @param _transactionId ID of the transaction to complete
     */
    function completeTransaction(bytes32 _transactionId)
        external
        transactionExists(_transactionId)
        notCompleted(_transactionId)
        onlyReceiver(_transactionId)
    {
        Transaction storage transaction = transactions[_transactionId];
        transaction.isCompleted = true;

        payable(transaction.receiver).transfer(transaction.amount);

        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Cancel a transaction (sender can cancel if not completed)
     * @param _transactionId ID of the transaction to cancel
     */
    function cancelTransaction(bytes32 _transactionId)
        external
        transactionExists(_transactionId)
        notCompleted(_transactionId)
        onlySender(_transactionId)
    {
        Transaction storage transaction = transactions[_transactionId];
        transaction.isCompleted = true;

        payable(transaction.sender).transfer(transaction.amount);

        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Get transaction details
     * @param _transactionId ID of the transaction
     * @return Transaction details
     */
    function getTransaction(bytes32 _transactionId)
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
        Transaction memory transaction = transactions[_transactionId];
        return (
            transaction.sender,
            transaction.receiver,
            transaction.amount,
            transaction.description,
            transaction.isCompleted,
            transaction.timestamp
        );
    }
}
```
