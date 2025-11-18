"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcoinmixer.com
Prompt: Create a smart contract in Solidity that supports depositing USDC, mixing through multiple layers, and withdrawing randomized outputs, inspired by the features of USDC Mixer.
Generated: DETERMINISTIC_35c832eebb3dd12d
Batch ID: 20250612_150234
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

contract USDCMixer is Ownable, ReentrancyGuard {
    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // USDC token interface
    IERC20 public usdcToken;

    // Mapping to track user deposits
    mapping(address => uint256) private userBalances;

    // Constructor to set the USDC token address
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "Invalid USDC address");
        usdcToken = IERC20(_usdcToken);
    }

    // Function to deposit USDC into the mixer
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer USDC from the user to the contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "USDC transfer failed");

        // Update user balance
        userBalances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw a randomized amount of USDC
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        
        // Simulate mixing and randomization (this is a placeholder)
        // In a real scenario, you would implement a mixing algorithm here
        uint256 mixedAmount = amount; // Replace with actual mixing logic
        
        // Update user balance before transferring
        userBalances[msg.sender] -= amount;

        // Transfer USDC from the contract to the user
        bool success = usdcToken.transfer(msg.sender, mixedAmount);
        require(success, "USDC transfer failed");

        emit Withdrawn(msg.sender, mixedAmount);
    }

    // Function to check user balance
    function balanceOf(address user) external view returns (uint256) {
        return userBalances[user];
    }

    // Function to withdraw contract's balance in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer USDC to the owner
        bool success = usdcToken.transfer(msg.sender, amount);
        require(success, "Emergency withdrawal failed");
    }
}
```
