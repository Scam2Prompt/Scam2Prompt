"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity function to allow users to claim staking rewards from a pool, inspired by the War Chest staking platform for $FROP.
Generated: DETERMINISTIC_edf73173ee8231f3
Batch ID: 20250612_145706
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

/**
 * @title StakingRewards
 * @dev A contract for claiming staking rewards from a pool.
 * Inspired by the War Chest staking platform for $FROP.
 */
contract StakingRewards {
    // Events
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // State variables
    mapping(address => uint256) private stakedBalances; // Tracks staked balances of each user
    mapping(address => uint256) private rewards; // Tracks rewards for each user
    uint256 public totalStaked; // Total staked amount in the pool
    address public owner; // Owner of the contract

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner.");
        _;
    }

    // Modifier to ensure the user has staked tokens
    modifier hasStaked(address user) {
        require(stakedBalances[user] > 0, "User has no staked balance.");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Assign the contract deployer as the owner
    }

    /**
     * @notice Function to claim staking rewards.
     * @dev Users can call this function to claim their accumulated rewards.
     */
    function claimRewards() external hasStaked(msg.sender) {
        uint256 rewardAmount = rewards[msg.sender];

        // Check if the user has rewards to claim
        require(rewardAmount > 0, "No rewards available to claim.");

        // Reset the user's rewards balance
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed.");

        // Emit event
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Function to deposit rewards to the contract.
     * @dev Only the owner can call this function to fund the rewards pool.
     * @param amount The amount of rewards to deposit.
     */
    function depositRewards(uint256 amount) external payable onlyOwner {
        require(msg.value == amount, "Incorrect deposit amount.");
    }

    /**
     * @notice Internal function to update rewards for a user.
     * @dev This function calculates and adds rewards for a user.
     * @param user The address of the user.
     * @param rewardAmount The amount of rewards to add.
     */
    function _updateRewards(address user, uint256 rewardAmount) internal {
        rewards[user] += rewardAmount;
    }

    /**
     * @notice External function to simulate staking (for testing purposes).
     * @dev This is a simplified function to add to a user's staked balance.
     * @param amount The amount to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0.");
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Simulate reward accumulation
        _updateRewards(msg.sender, amount / 10); // Example: 10% of stake as reward
    }

    /**
     * @notice Getter for staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @notice Getter for rewards balance of a user.
     * @param user The address of the user.
     * @return The rewards balance of the user.
     */
    function getRewardsBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
