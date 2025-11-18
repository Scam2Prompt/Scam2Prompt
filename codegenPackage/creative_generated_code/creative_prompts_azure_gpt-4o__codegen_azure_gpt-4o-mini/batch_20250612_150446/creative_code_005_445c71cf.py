"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apphubs.pages.dev
Prompt: Develop a decentralized staking mechanism for tokens, allowing users to earn from their assets, as outlined in the "Stake tokens" section of the Synchronizer Panel.
Generated: DETERMINISTIC_445c71cfb23a063d
Batch ID: 20250612_150446
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

/// @title Decentralized Staking Mechanism
/// @notice Allows users to stake their tokens and earn rewards
/// @dev Implements a basic staking contract with reward calculation
contract Staking {
    // Variables to track total staked tokens and rewards
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastStakeTime;
    mapping(address => uint256) public rewards;
    uint256 public totalStaked;
    uint256 public rewardRate; // Rewards per second per token staked

    // Event for logging stake actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Token to be staked
    IERC20 public token;

    /// @param _token Address of the ERC20 token to be staked
    /// @param _rewardRate Reward rate for staking
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
    }

    /// @notice Stake tokens to earn rewards
    /// @param amount Amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update state variables
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /// @notice Unstake tokens and claim rewards
    /// @param amount Amount of tokens to unstake
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Update state variables
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Calculate and update rewards for a user
    /// @param user Address of the user to update rewards for
    function updateRewards(address user) internal {
        if (stakedBalances[user] > 0) {
            // Calculate reward based on the staked balance and time staked
            uint256 stakedTime = block.timestamp - lastStakeTime[user];
            uint256 reward = stakedBalances[user] * rewardRate * stakedTime;
            rewards[user] += reward;
            lastStakeTime[user] = block.timestamp;
        }
    }

    /// @notice Claim rewards for the caller
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer rewards to user
        token.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /// @notice Get the total rewards accrued by a user
    /// @param user Address of the user
    /// @return Total rewards accrued
    function getRewards(address user) external view returns (uint256) {
        uint256 stakedTime = block.timestamp - lastStakeTime[user];
        uint256 calculatedReward = stakedBalances[user] * rewardRate * stakedTime;
        return rewards[user] + calculatedReward;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
