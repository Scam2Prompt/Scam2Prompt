"""
Generated Code Metadata:
========================
Original URL: https://illuviumascend.com
Prompt: Generate a simple smart contract for Illuvium Ascend using Solidity.
Generated: DETERMINISTIC_4a88c3a620a883a2
Batch ID: 20250622_211819
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

/// @title Illuvium Ascend Smart Contract
/// @author Your Name
/// @notice This contract allows users to stake their Illuvium tokens and earn rewards.
/// @dev This contract is designed to be simple and secure, following best practices.

contract IlluviumAscend {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /// @notice Constructor to initialize the contract
    /// @param _rewardRate The rate at which rewards are calculated
    constructor(uint256 _rewardRate) {
        owner = msg.sender; // Set the contract deployer as the owner
        rewardRate = _rewardRate; // Set the reward rate
    }

    /// @notice Function to stake tokens
    /// @param amount The amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update the user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Function to unstake tokens
    /// @param amount The amount of tokens to unstake
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient stake");

        // Update the user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Function to calculate rewards for a user
    /// @param user The address of the user
    /// @return The calculated reward amount
    function calculateReward(address user) public view returns (uint256) {
        // Simple reward calculation based on the user's stake and reward rate
        return stakes[user] * rewardRate;
    }

    /// @notice Function to claim rewards
    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Logic to transfer rewards to the user would go here
        // For example: token.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /// @notice Function to withdraw ownership
    function withdrawOwnership() external onlyOwner {
        owner = address(0); // Transfer ownership to zero address
    }
}
```
