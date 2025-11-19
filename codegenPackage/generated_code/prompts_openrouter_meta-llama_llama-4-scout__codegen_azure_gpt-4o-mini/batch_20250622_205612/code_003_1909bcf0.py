"""
Generated Code Metadata:
========================
Original URL: https://flareairdrop.com
Prompt: Generate a Solidity smart contract that utilizes Flare's EVM+ and Substrate features for a DeFi application.
Generated: DETERMINISTIC_1909bcf01cc35158
Batch ID: 20250622_205612
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DeFiContract is a simple DeFi application that allows users to deposit and withdraw ERC20 tokens
contract DeFiContract is Ownable {
    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Function to deposit tokens into the contract
    // @param tokenAddress The address of the ERC20 token contract
    // @param amount The amount of tokens to deposit
    function deposit(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(tokenAddress != address(0), "Invalid token address");

        // Transfer tokens from the user to the contract
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's balance
        balances[msg.sender] += amount;

        // Emit the deposit event
        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract
    // @param tokenAddress The address of the ERC20 token contract
    // @param amount The amount of tokens to withdraw
    function withdraw(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring tokens
        balances[msg.sender] -= amount;

        // Transfer tokens from the contract to the user
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of a user
    // @param user The address of the user
    // @return The balance of the user
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to withdraw all tokens from the contract (only owner)
    // @param tokenAddress The address of the ERC20 token contract
    function withdrawAll(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        // Transfer all tokens to the owner
        require(token.transfer(msg.sender, contractBalance), "Token transfer failed");
    }
}
```
