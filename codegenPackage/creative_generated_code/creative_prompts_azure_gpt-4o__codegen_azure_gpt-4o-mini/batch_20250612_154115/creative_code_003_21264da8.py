"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orikod.com
Prompt: Create a Solidity smart contract optimized for Arbitrum AnyTrust chains, designed for micro-payment applications with low gas fees.
Generated: DETERMINISTIC_21264da885b45918
Batch ID: 20250612_154115
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

// Contract for micro-payment applications on Arbitrum AnyTrust chains
contract MicroPayment is Ownable {
    // Event emitted when a payment is made
    event PaymentMade(address indexed payer, address indexed payee, uint256 amount, string message);

    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Function to deposit funds into the contract
    // Only the contract owner can deposit
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        // Transfer the specified amount of tokens to the contract
        IERC20 token = IERC20(address(this));
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }

    // Function to make a micro-payment
    function pay(address payee, uint256 amount, string calldata message) external {
        require(payee != address(0), "Invalid payee address");
        require(amount > 0, "Payment amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Subtract amount from sender's balance
        balances[msg.sender] -= amount;
        // Add amount to payee's balance
        balances[payee] += amount;

        emit PaymentMade(msg.sender, payee, amount, message);
    }

    // Function to withdraw funds by the payee
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Subtract amount from user's balance
        balances[msg.sender] -= amount;

        // Transfer the specified amount of tokens to the user
        IERC20 token = IERC20(address(this));
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to check the balance of an account
    function checkBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to receive ETH (fallback)
    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    // Fallback function to prevent ETH transfer failures
    fallback() external {
        revert("Direct transfers not allowed");
    }
}
```
