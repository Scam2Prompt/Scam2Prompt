"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Generate Solidity code for deploying a decentralized application (dApp) on the Botanix EVM that utilizes Bitcoin as the native asset for staking.
Generated: DETERMINISTIC_47e9317d1bc131ff
Batch ID: 20250612_152249
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

/// @title Staking Contract
/// @dev This contract allows users to stake Bitcoin as an asset for rewards.
contract BitcoinStaking {
    // Events to log staking activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    
    // Mapping to track the staked amount by user
    mapping(address => uint256) private stakes;
    
    // Total staked amount in the contract
    uint256 private totalStaked;
    
    // Reward rate per block (change according to your requirement)
    uint256 public rewardRate = 100; // Example reward rate per block

    // Total rewards distributed
    mapping(address => uint256) private rewards;

    // To track the last update time for rewards
    mapping(address => uint256) private lastUpdateTime;

    // Modifier to check if the sender has staked any Bitcoin
    modifier hasStake() {
        require(stakes[msg.sender] > 0, "No stake found for user");
        _;
    }

    /// @dev Stake Bitcoin in the contract.
    /// @param amount Amount of Bitcoin to stake.
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update total staked and user stake
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Update reward and time
        lastUpdateTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /// @dev Unstake the Bitcoin amount from the contract.
    /// @param amount Amount of Bitcoin to unstake.
    function unstake(uint256 amount) external hasStake {
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update total staked and user stake
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Update reward and time
        lastUpdateTime[msg.sender] = block.timestamp;

        emit Unstaked(msg.sender, amount);
    }

    /// @dev Calculate and claim rewards for the user.
    function claimRewards() external hasStake {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Reset last update time
        lastUpdateTime[msg.sender] = block.timestamp;

        // Update rewards mapping
        rewards[msg.sender] += reward;

        emit RewardPaid(msg.sender, reward);
    }

    /// @dev Calculate the reward for a user based on their stake.
    /// @param user The user's address.
    /// @return The calculated reward.
    function calculateReward(address user) public view returns (uint256) {
        uint256 duration = block.timestamp - lastUpdateTime[user];
        return (stakes[user] * rewardRate * duration) / 1e18; // Adjust division based on decimals
    }

    /// @dev Get the staked amount for a user.
    /// @param user The user's address.
    /// @return The amount staked by the user.
    function getStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    /// @dev Get the total staked amount in the contract.
    /// @return The total amount staked.
    function totalStakedAmount() external view returns (uint256) {
        return totalStaked;
    }

    /// @dev Get the available rewards for a user.
    /// @param user The user's address.
    /// @return The total rewards available for the user.
    function getRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateReward(user);
    }
}
```
