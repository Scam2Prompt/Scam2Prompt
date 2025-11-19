"""
Generated Code Metadata:
========================
Original URL: https://dappback.firebaseapp.com
Prompt: Create a smart contract example that could be deployed and utilized with DappBack for tracking user rewards.
Generated: DETERMINISTIC_ca0e1ae9e5949752
Batch ID: 20250612_153606
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

/// @title User Rewards Tracking Smart Contract
/// @author Your Name
/// @notice This contract tracks user rewards and allows for reward distribution
/// @dev This contract is designed to be deployed on the Ethereum blockchain

contract UserRewards {
    // State variable to store the owner of the contract
    address public owner;

    // Mapping to track user rewards
    mapping(address => uint256) private rewards;

    // Event to log reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    // Event to log reward withdrawal
    event RewardWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Distribute rewards to a user
    /// @param user The address of the user receiving rewards
    /// @param amount The amount of rewards to distribute
    /// @dev Only the owner can distribute rewards
    function distributeReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        rewards[user] += amount;

        emit RewardDistributed(user, amount);
    }

    /// @notice Withdraw rewards for the caller
    /// @dev Users can withdraw their accumulated rewards
    function withdrawRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset the user's reward balance before transferring to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit RewardWithdrawn(msg.sender, amount);
    }

    /// @notice Get the reward balance of a user
    /// @param user The address of the user
    /// @return The reward balance of the user
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }

    /// @notice Allow the contract to receive Ether
    receive() external payable {}
}
```
