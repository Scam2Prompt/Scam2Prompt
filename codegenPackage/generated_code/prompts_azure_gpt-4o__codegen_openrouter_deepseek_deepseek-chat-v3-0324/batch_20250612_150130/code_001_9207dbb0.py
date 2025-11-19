"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Generate a smart contract in Solidity that facilitates decentralized finance transactions without intermediaries, ensuring transparency and low transaction fees, as outlined by Gas Profit.
Generated: DETERMINISTIC_9207dbb06803d448
Batch ID: 20250612_150130
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
 * @title GasProfitDeFi
 * @dev A decentralized finance smart contract for peer-to-peer transactions
 * with transparency and low gas fees.
 */
contract GasProfitDeFi {
    // Struct to represent a transaction
    struct Transaction {
        address sender;
        address receiver;
        uint256 amount;
        uint256 timestamp;
        bool isCompleted;
    }

    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Array to store all transactions
    Transaction[] public transactions;

    // Events for logging important actions
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Transfer(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        uint256 transactionId
    );

    /**
     * @dev Deposit funds into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from the contract
     * @param amount The amount to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Transfer funds to another address
     * @param receiver The address to receive the funds
     * @param amount The amount to transfer
     * @return transactionId The ID of the created transaction
     */
    function transfer(address receiver, uint256 amount) external returns (uint256) {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[receiver] += amount;

        uint256 transactionId = transactions.length;
        transactions.push(Transaction({
            sender: msg.sender,
            receiver: receiver,
            amount: amount,
            timestamp: block.timestamp,
            isCompleted: true
        }));

        emit Transfer(msg.sender, receiver, amount, transactionId);
        return transactionId;
    }

    /**
     * @dev Get the total number of transactions
     * @return count The total number of transactions
     */
    function getTransactionCount() external view returns (uint256) {
        return transactions.length;
    }

    /**
     * @dev Get transaction details by ID
     * @param transactionId The ID of the transaction
     * @return sender The sender's address
     * @return receiver The receiver's address
     * @return amount The transaction amount
     * @return timestamp The transaction timestamp
     * @return isCompleted Whether the transaction is completed
     */
    function getTransaction(uint256 transactionId) external view returns (
        address sender,
        address receiver,
        uint256 amount,
        uint256 timestamp,
        bool isCompleted
    ) {
        require(transactionId < transactions.length, "Invalid transaction ID");
        Transaction storage transaction = transactions[transactionId];
        return (
            transaction.sender,
            transaction.receiver,
            transaction.amount,
            transaction.timestamp,
            transaction.isCompleted
        );
    }

    /**
     * @dev Get the balance of a user
     * @param user The address of the user
     * @return balance The user's balance
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
