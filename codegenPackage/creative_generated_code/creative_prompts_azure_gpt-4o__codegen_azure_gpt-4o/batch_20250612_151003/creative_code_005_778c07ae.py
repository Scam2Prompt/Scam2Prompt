"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-w.pages.dev
Prompt: Provide an example of how to implement staking and harvesting functionality for assets using the DApp Synchronizer Panel.
Generated: DETERMINISTIC_778c07aed8f9a385
Batch ID: 20250612_151003
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
 * @title Staking and Harvesting Contract
 * @dev This contract provides functionality for staking assets and harvesting rewards.
 */
contract StakingAndHarvesting {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of assets staked

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
        uint256 reward; // Accumulated reward
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No stake found for the user");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake assets.
     * @param amount The amount of assets to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Calculate pending rewards if the user already has a stake
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].reward += calculateReward(msg.sender);
        }

        // Update staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to harvest their accumulated rewards.
     */
    function harvest() external hasStake(msg.sender) {
        uint256 reward = calculateReward(msg.sender) + stakes[msg.sender].reward;
        require(reward > 0, "No rewards available");

        // Reset rewards
        stakes[msg.sender].reward = 0;
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer reward (mocked here as a simple message, replace with token/ETH transfer logic)
        // Note: In production, integrate ERC20 or relevant token transfer logic.
        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Allows a user to withdraw their staked assets.
     */
    function withdraw() external hasStake(msg.sender) {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "No assets staked");

        uint256 reward = calculateReward(msg.sender) + stakes[msg.sender].reward;

        // Update staking data
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].reward = 0;
        stakes[msg.sender].timestamp = 0;
        totalStaked -= amount;

        // Transfer staked assets and rewards back to the user
        // Note: In production, integrate ERC20 or relevant token transfer logic.
        emit Withdrawn(msg.sender, amount);
        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a given user based on their stake and time elapsed.
     * @param user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory stakeData = stakes[user];
        uint256 timeElapsed = block.timestamp - stakeData.timestamp;
        return stakeData.amount * rewardRate * timeElapsed / 1e18; // Adjust division for decimals
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
