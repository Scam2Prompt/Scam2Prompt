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
 * @title SecureTrustlessTransaction
 * @dev A smart contract for secure and trustless transactions on a blockchain network.
 * Allows users to deposit funds, initiate transactions, and withdraw funds securely.
 */
contract SecureTrustlessTransaction {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address payable receiver;
        uint256 amount;
        bool isCompleted;
    }

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track transactions by their IDs
    mapping(uint256 => Transaction) public transactions;

    // Counter for transaction IDs
    uint256 public transactionCounter;

    // Events for logging activities
    event Deposited(address indexed user, uint256 amount);
    event TransactionInitiated(uint256 indexed transactionId, address indexed sender, address indexed receiver, uint256 amount);
    event TransactionCompleted(uint256 indexed transactionId);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Deposit funds into the contract.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Initiate a new transaction.
     * @param _receiver The address of the receiver.
     * @param _amount The amount to be sent.
     * @return transactionId The ID of the newly created transaction.
     */
    function initiateTransaction(address payable _receiver, uint256 _amount) external returns (uint256) {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        uint256 transactionId = transactionCounter++;
        transactions[transactionId] = Transaction({
            sender: msg.sender,
            receiver: _receiver,
            amount: _amount,
            isCompleted: false
        });

        emit TransactionInitiated(transactionId, msg.sender, _receiver, _amount);
        return transactionId;
    }

    /**
     * @dev Complete a pending transaction.
     * @param _transactionId The ID of the transaction to complete.
     */
    function completeTransaction(uint256 _transactionId) external {
        Transaction storage transaction = transactions[_transactionId];
        require(transaction.sender != address(0), "Transaction does not exist");
        require(!transaction.isCompleted, "Transaction already completed");
        require(msg.sender == transaction.receiver, "Only receiver can complete the transaction");

        transaction.isCompleted = true;
        transaction.receiver.transfer(transaction.amount);
        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Withdraw funds from the contract.
     * @param _amount The amount to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount;
        payable(msg.sender).transfer(_amount);
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param _user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address _user) external view returns (uint256) {
        return balances[_user];
    }

    /**
     * @dev Get transaction details.
     * @param _transactionId The ID of the transaction.
     * @return sender The sender's address.
     * @return receiver The receiver's address.
     * @return amount The transaction amount.
     * @return isCompleted Whether the transaction is completed.
     */
    function getTransaction(uint256 _transactionId) external view returns (
        address sender,
        address receiver,
        uint256 amount,
        bool isCompleted
    ) {
        Transaction storage transaction = transactions[_transactionId];
        require(transaction.sender != address(0), "Transaction does not exist");
        return (
            transaction.sender,
            transaction.receiver,
            transaction.amount,
            transaction.isCompleted
        );
    }
}
```
