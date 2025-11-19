"""
Generated Code Metadata:
========================
Original URL: https://ahsjdkkk.pages.dev
Prompt: Generate a smart contract code in Solidity for a decentralized application that requires secure and trustless transactions on a blockchain network.
Generated: DETERMINISTIC_492e3ed10a2b3dd9
Batch ID: 20250622_211508
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
 * @title SecureTransaction
 * @dev A smart contract for secure and trustless transactions on a blockchain network.
 */
contract SecureTransaction {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address receiver;
        uint256 amount;
        bool isCompleted;
    }

    // Mapping to store transactions by ID
    mapping(uint256 => Transaction) public transactions;

    // Counter for transaction IDs
    uint256 private transactionCounter;

    // Event emitted when a transaction is created
    event TransactionCreated(
        uint256 indexed transactionId,
        address indexed sender,
        address indexed receiver,
        uint256 amount
    );

    // Event emitted when a transaction is completed
    event TransactionCompleted(uint256 indexed transactionId);

    /**
     * @dev Create a new transaction.
     * @param _receiver The address of the receiver.
     * @param _amount The amount to be transferred.
     */
    function createTransaction(address _receiver, uint256 _amount) external payable {
        require(_receiver != address(0), "Receiver address cannot be zero.");
        require(_amount > 0, "Amount must be greater than zero.");
        require(msg.value == _amount, "Sent value must match the transaction amount.");

        // Increment transaction counter
        transactionCounter++;

        // Create a new transaction
        transactions[transactionCounter] = Transaction({
            sender: msg.sender,
            receiver: _receiver,
            amount: _amount,
            isCompleted: false
        });

        // Emit event for transaction creation
        emit TransactionCreated(transactionCounter, msg.sender, _receiver, _amount);
    }

    /**
     * @dev Complete a transaction by transferring funds to the receiver.
     * @param _transactionId The ID of the transaction to complete.
     */
    function completeTransaction(uint256 _transactionId) external {
        Transaction storage transaction = transactions[_transactionId];

        require(transaction.sender == msg.sender, "Only the sender can complete the transaction.");
        require(!transaction.isCompleted, "Transaction is already completed.");

        // Mark transaction as completed
        transaction.isCompleted = true;

        // Transfer funds to the receiver
        (bool success, ) = transaction.receiver.call{value: transaction.amount}("");
        require(success, "Transfer failed.");

        // Emit event for transaction completion
        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Fallback function called. No direct Ether transfers allowed.");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Receive function called. No direct Ether transfers allowed.");
    }
}
```
