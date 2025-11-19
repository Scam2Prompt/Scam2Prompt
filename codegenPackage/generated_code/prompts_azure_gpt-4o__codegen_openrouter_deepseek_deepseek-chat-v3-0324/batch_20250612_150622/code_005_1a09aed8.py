"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Develop a Solidity contract for Kabosu's ecosystem wallet, incorporating features mentioned in Phase 3 of the roadmap.
Generated: DETERMINISTIC_1a09aed8d0a0ef41
Batch ID: 20250612_150622
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract KabosuEcosystemWallet is Ownable, ReentrancyGuard {
    // Struct to store transaction details
    struct Transaction {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        string description;
        bool isCompleted;
    }

    // Kabosu token interface
    IERC20 public kabosuToken;

    // Transaction history
    Transaction[] public transactions;

    // Wallet balances
    mapping(address => uint256) public balances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event Transfer(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        string description
    );
    event TransactionCompleted(uint256 indexed transactionId);

    // Constructor
    constructor(address _kabosuTokenAddress) {
        require(
            _kabosuTokenAddress != address(0),
            "Invalid token address"
        );
        kabosuToken = IERC20(_kabosuTokenAddress);
    }

    // Deposit Kabosu tokens into the wallet
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        bool success = kabosuToken.transferFrom(
            msg.sender,
            address(this),
            _amount
        );
        require(success, "Token transfer failed");

        balances[msg.sender] += _amount;

        transactions.push(
            Transaction({
                sender: msg.sender,
                recipient: address(this),
                amount: _amount,
                timestamp: block.timestamp,
                description: "Deposit",
                isCompleted: true
            })
        );

        emit Deposit(msg.sender, _amount);
    }

    // Withdraw Kabosu tokens from the wallet
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            balances[msg.sender] >= _amount,
            "Insufficient balance"
        );

        balances[msg.sender] -= _amount;

        bool success = kabosuToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        transactions.push(
            Transaction({
                sender: address(this),
                recipient: msg.sender,
                amount: _amount,
                timestamp: block.timestamp,
                description: "Withdrawal",
                isCompleted: true
            })
        );

        emit Withdrawal(msg.sender, _amount);
    }

    // Transfer Kabosu tokens to another wallet user
    function transfer(
        address _recipient,
        uint256 _amount,
        string memory _description
    ) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            balances[msg.sender] >= _amount,
            "Insufficient balance"
        );
        require(_recipient != address(0), "Invalid recipient address");

        balances[msg.sender] -= _amount;
        balances[_recipient] += _amount;

        uint256 transactionId = transactions.length;
        transactions.push(
            Transaction({
                sender: msg.sender,
                recipient: _recipient,
                amount: _amount,
                timestamp: block.timestamp,
                description: _description,
                isCompleted: true
            })
        );

        emit Transfer(msg.sender, _recipient, _amount, _description);
        emit TransactionCompleted(transactionId);
    }

    // Get user balance
    function getBalance(address _user) external view returns (uint256) {
        return balances[_user];
    }

    // Get transaction count
    function getTransactionCount() external view returns (uint256) {
        return transactions.length;
    }

    // Get transaction details by ID
    function getTransaction(uint256 _transactionId)
        external
        view
        returns (
            address sender,
            address recipient,
            uint256 amount,
            uint256 timestamp,
            string memory description,
            bool isCompleted
        )
    {
        require(
            _transactionId < transactions.length,
            "Invalid transaction ID"
        );
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

    // Emergency withdrawal function for owner (only for stuck tokens)
    function emergencyWithdraw(address _tokenAddress) external onlyOwner {
        require(
            _tokenAddress != address(kabosuToken),
            "Cannot withdraw Kabosu tokens"
        );

        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = token.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }
}
```
