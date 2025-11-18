"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophan.xyz
Prompt: Write a smart contract that utilizes SOPH tokens to reward users for engagement in loyalty programs, as described in Sophon's platform features.
Generated: DETERMINISTIC_da03abb5493298ca
Batch ID: 20250612_153854
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

// Interface for the SOPH token contract
interface ISOPHToken {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

// Smart contract to manage loyalty rewards using SOPH tokens
contract LoyaltyRewards {
    // Address of the SOPH token contract
    ISOPHToken public sophToken;

    // Mapping to track user rewards
    mapping(address => uint256) private userRewards;

    // Event to emit when rewards are issued
    event RewardsIssued(address indexed user, uint256 amount);

    // Constructor to set the SOPH token contract address
    constructor(address _sophTokenAddress) {
        require(_sophTokenAddress != address(0), "Invalid token address");
        sophToken = ISOPHToken(_sophTokenAddress);
    }

    // Function to issue rewards to a user
    function issueRewards(address user, uint256 amount) external {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");
        
        // Update the user's total rewards
        userRewards[user] += amount;

        // Emit an event for the rewards issued
        emit RewardsIssued(user, amount);
    }

    // Function to claim rewards for the user
    function claimRewards() external {
        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "No rewards available to claim");

        // Reset user's rewards to zero before transferring tokens
        userRewards[msg.sender] = 0;

        // Transfer SOPH tokens to the user
        require(sophToken.transfer(msg.sender, rewards), "Token transfer failed");
    }

    // Function to view the balance of rewards for a user
    function viewRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }
}
```
