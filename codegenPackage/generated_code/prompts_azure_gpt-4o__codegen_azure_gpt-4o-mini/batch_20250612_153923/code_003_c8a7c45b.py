"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Create a smart contract that mimics Extra Finance's security-focused design, emphasizing audits and robust mechanisms to protect user assets during yield farming.
Generated: DETERMINISTIC_c8a7c45bdf7df197
Batch ID: 20250612_153923
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

// Interface for the yield farming contract
interface IYieldFarm {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Smart contract for yield farming with security features
contract SecureYieldFarm is Ownable, ReentrancyGuard {
    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    
    // Mapping to track user balances
    mapping(address => uint256) private balances;
    
    // The token used for yield farming
    IERC20 public immutable token;

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    // Deposit tokens into the yield farm
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Withdraw tokens from the yield farm
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update user balance before transferring tokens to prevent reentrancy
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // View function to check user balance
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    // Emergency function to withdraw tokens in case of an emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        token.transfer(msg.sender, amount);
    }
}
```
