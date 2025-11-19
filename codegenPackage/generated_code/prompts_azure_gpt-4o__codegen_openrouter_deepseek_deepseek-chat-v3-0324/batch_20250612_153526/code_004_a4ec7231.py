"""
Generated Code Metadata:
========================
Original URL: https://etherfi-app.github.io
Prompt: Provide an example of a Solidity smart contract that uses Ethereum's blockchain to ensure transparency and security in financial transactions, similar to Ether Fi's approach.
Generated: DETERMINISTIC_a4ec7231478d6459
Batch ID: 20250612_153526
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
 * @title TransparentFinancialContract
 * @dev A smart contract for secure and transparent financial transactions
 * @notice Inspired by Ether Fi's approach to blockchain transparency
 */
contract TransparentFinancialContract {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        string description;
        bool isCompleted;
    }

    // Mapping to store transactions by their IDs
    mapping(bytes32 => Transaction) public transactions;

    // Event emitted when a new transaction is created
    event TransactionCreated(
        bytes32 indexed transactionId,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        string description
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

    /**
     * @dev Create a new transaction
     * @param _recipient Address of the recipient
     * @param _amount Amount to be transferred
     * @param _description Description of the transaction
     * @return transactionId The ID of the created transaction
     */
    function createTransaction(
        address _recipient,
        uint256 _amount,
        string memory _description
    ) external returns (bytes32) {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");

        bytes32 transactionId = keccak256(
            abi.encodePacked(
                msg.sender,
                _recipient,
                _amount,
                block.timestamp,
                _description
            )
        );

        transactions[transactionId] = Transaction({
            sender: msg.sender,
            recipient: _recipient,
            amount: _amount,
            timestamp: block.timestamp,
            description: _description,
            isCompleted: false
        });

        emit TransactionCreated(
            transactionId,
            msg.sender,
            _recipient,
            _amount,
            _description
        );

        return transactionId;
    }

    /**
     * @dev Complete a transaction by transferring funds
     * @param _transactionId ID of the transaction to complete
     */
    function completeTransaction(bytes32 _transactionId)
        external
        payable
        transactionExists(_transactionId)
        notCompleted(_transactionId)
    {
        Transaction storage transaction = transactions[_transactionId];

        require(
            msg.sender == transaction.sender,
            "Only sender can complete transaction"
        );
        require(
            msg.value == transaction.amount,
            "Sent amount must match transaction amount"
        );

        (bool success, ) = transaction.recipient.call{value: msg.value}("");
        require(success, "Transfer failed");

        transaction.isCompleted = true;

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
        transactionExists(_transactionId)
        returns (
            address,
            address,
            uint256,
            uint256,
            string memory,
            bool
        )
    {
        Transaction memory transaction = transactions[_transactionId];
        return (
            transaction.sender,
            transaction.recipient,
            transaction.amount,
            transaction.timestamp,
            transaction.description,
            transaction.isCompleted
        );
    }
}
```
