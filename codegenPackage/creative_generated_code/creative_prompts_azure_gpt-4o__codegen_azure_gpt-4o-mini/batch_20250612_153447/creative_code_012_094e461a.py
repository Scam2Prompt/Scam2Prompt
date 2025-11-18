"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Create a Solidity contract for implementing low-fee transactions on a Layer 2 blockchain, inspired by the Pepe Unchained infrastructure.
Generated: DETERMINISTIC_094e461a34227f4f
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LowFeeTransaction
 * @dev A smart contract for implementing low-fee transactions on a Layer 2 blockchain.
 * Inspired by the Pepe Unchained infrastructure.
 */
contract LowFeeTransaction is Ownable, ReentrancyGuard {
    // Events
    event TransactionExecuted(address indexed sender, address indexed recipient, uint256 amount, string message);
    
    // Token used for transactions
    IERC20 public token;

    // Fee percentage, represented as a value between 0 and 10000 (to represent 0% to 100%)
    uint256 public feePercentage = 100; // 1% fee

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    /**
     * @dev Constructor to set the token used for transactions.
     * @param _token The address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero.");
        token = IERC20(_token);
    }

    /**
     * @dev Sets the fee percentage for transactions.
     * @param _feePercentage The new fee percentage (0-10000).
     */
    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10000, "Fee percentage must be between 0 and 10000.");
        feePercentage = _feePercentage;
    }

    /**
     * @dev Allows a user to deposit tokens into the contract.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero.");
        
        // Transfer tokens from sender to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed.");
        
        // Update user balance
        userBalances[msg.sender] += amount;
    }

    /**
     * @dev Executes a transaction, deducting the fee and transferring the remaining amount.
     * @param recipient The address of the recipient.
     * @param amount The amount to send.
     * @param message An optional message to record with the transaction.
     */
    function executeTransaction(address recipient, uint256 amount, string calldata message) external nonReentrant {
        require(amount > 0, "Transaction amount must be greater than zero.");
        require(userBalances[msg.sender] >= amount, "Insufficient balance.");

        // Calculate fee
        uint256 fee = (amount * feePercentage) / 10000;
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the owner (or a fee collector)
        require(token.transfer(owner(), fee), "Fee transfer failed.");

        // Transfer the remaining amount to the recipient
        require(token.transfer(recipient, amountAfterFee), "Transaction transfer failed.");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Emit transaction event
        emit TransactionExecuted(msg.sender, recipient, amountAfterFee, message);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero.");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance in contract.");
        
        // Transfer tokens to the owner
        require(token.transfer(msg.sender, amount), "Withdraw transfer failed.");
    }

    /**
     * @dev Allows users to check their balance.
     * @return The balance of the caller.
     */
    function checkBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }
}
```
