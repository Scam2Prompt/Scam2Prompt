"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardusdctoken.com
Prompt: Create a step-by-step guide for integrating the RewardUSDC Token (RUSDC) contract into a decentralized wallet application, ensuring compatibility and automatic USDC reward distribution.
Generated: DETERMINISTIC_5752a0d117a7323d
Batch ID: 20250612_154542
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the RewardUSDC Token
interface IRewardUSDC is IERC20 {
    function distributeRewards(address recipient, uint256 amount) external returns (bool);
}

contract Wallet {
    // Address of the RUSDC token contract
    IRewardUSDC public rusdcToken;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    // Constructor to set the RUSDC token address
    constructor(address _rusdcTokenAddress) {
        require(_rusdcTokenAddress != address(0), "Invalid token address");
        rusdcToken = IRewardUSDC(_rusdcTokenAddress);
    }

    // Function to deposit funds to the wallet
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer USDC to the wallet
        bool success = rusdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Update user balance
        userBalances[msg.sender] += amount;
    }

    // Function to withdraw funds from the wallet
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer USDC back to the user
        bool success = rusdcToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }

    // Function to distribute rewards automatically
    function distributeRewards(address recipient, uint256 amount) external returns (bool) {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[recipient] > 0, "Recipient has no balance");

        // Distributing rewards using the RUSDC token contract
        bool success = rusdcToken.distributeRewards(recipient, amount);
        require(success, "Reward distribution failed");

        emit RewardsDistributed(recipient, amount);
        return true;
    }
}
```

This Solidity code implements a decentralized wallet application that integrates the RewardUSDC Token contract. It includes functionality for depositing and withdrawing funds, as well as distributing USDC rewards to users. Each function implements error handling and emits relevant events to ensure clarity and maintainability.
