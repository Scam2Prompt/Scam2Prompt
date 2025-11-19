"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-w.pages.dev
Prompt: Describe how to implement staking and harvesting of assets in a DApp using the features outlined in the DApp Synchronizer Panel.
Generated: DETERMINISTIC_420bbffc6a03d1ca
Batch ID: 20250612_163338
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
 * @title StakingAndHarvestingDApp
 * @dev This contract allows users to stake assets and harvest rewards. 
 * It is designed to integrate with a DApp Synchronizer Panel for data updates.
 */
contract StakingAndHarvestingDApp {
    // Struct to store staking information for a user
    struct Stake {
        uint256 amount;         // Amount of assets staked
        uint256 stakingTime;    // Timestamp when staking started
        uint256 reward;         // Accumulated reward
    }

    // Mapping to store stakes by user address
    mapping(address => Stake) public stakes;

    // Reward rate per second (example: 1 token per 1000 seconds)
    uint256 public rewardRate = 1e18 / 1000;

    // Event to notify staking activity
    event Staked(address indexed user, uint256 amount);

    // Event to notify harvesting activity
    event Harvested(address indexed user, uint256 reward);

    // Event to notify asset withdrawal
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Modifier to ensure a user has an active stake.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No active stake found");
        _;
    }

    /**
     * @dev Function to allow users to stake assets.
     * @param amount The amount of assets being staked.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // If the user already has a stake, update rewards before adding more
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].reward = calculateReward(msg.sender);
        }

        // Update staking details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakingTime = block.timestamp;

        // Emit event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate the current reward for a user.
     * @param user The address of the user.
     * @return reward The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakingTime;
        reward = userStake.reward + (stakingDuration * rewardRate * userStake.amount);
    }

    /**
     * @dev Function to allow users to harvest their rewards.
     */
    function harvest() external hasStake {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available for harvesting");

        // Reset reward after harvesting
        stakes[msg.sender].reward = 0;
        stakes[msg.sender].stakingTime = block.timestamp;

        // Transfer rewards (In production, replace with actual token transfer logic)
        // Example: ERC20Token.transfer(msg.sender, reward);

        // Emit event
        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Function to allow users to withdraw their staked assets.
     */
    function withdraw() external hasStake {
        uint256 amount = stakes[msg.sender].amount;
        uint256 reward = calculateReward(msg.sender);

        require(amount > 0, "No staked assets to withdraw");

        // Reset stake details
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].reward = 0;
        stakes[msg.sender].stakingTime = 0;

        // Transfer staked assets and rewards (In production, replace with actual token transfer logic)
        // Example: ERC20Token.transfer(msg.sender, amount + reward);

        // Emit events
        emit Withdrawn(msg.sender, amount);
        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the contract owner.
     * @param newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external {
        // In production, add access control (e.g., onlyOwner modifier)
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }
}
```
