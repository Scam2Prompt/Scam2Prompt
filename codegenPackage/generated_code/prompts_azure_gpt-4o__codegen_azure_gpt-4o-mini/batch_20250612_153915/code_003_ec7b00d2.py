"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Create a smart contract in Solidity that handles reward distribution for a gamified system like the "FREE SPIN" feature described on the TON SPIN website.
Generated: DETERMINISTIC_ec7b00d26f0a5fb4
Batch ID: 20250612_153915
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

contract FreeSpinReward {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalRewards; // Total rewards available for distribution
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards
    mapping(address => bool) public hasClaimed; // Track if a user has claimed their reward

    // Events
    event RewardDistributed(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasNotClaimed() {
        require(!hasClaimed[msg.sender], "Reward has already been claimed");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _totalRewards) {
        owner = msg.sender; // Set the contract deployer as the owner
        totalRewards = _totalRewards; // Set the total rewards
    }

    // Function to distribute rewards to a user
    function distributeReward(address user, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than zero");
        require(totalRewards >= amount, "Insufficient total rewards");

        rewards[user] += amount; // Update the user's reward balance
        totalRewards -= amount; // Decrease the total rewards
        emit RewardDistributed(user, amount); // Emit event for reward distribution
    }

    // Function for users to claim their rewards
    function claimReward() external hasNotClaimed {
        uint256 rewardAmount = rewards[msg.sender]; // Get the user's reward amount
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance and mark as claimed
        rewards[msg.sender] = 0;
        hasClaimed[msg.sender] = true;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed"); // Ensure the transfer was successful

        emit RewardClaimed(msg.sender, rewardAmount); // Emit event for reward claim
    }

    // Function to withdraw remaining funds by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed"); // Ensure the withdrawal was successful
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
