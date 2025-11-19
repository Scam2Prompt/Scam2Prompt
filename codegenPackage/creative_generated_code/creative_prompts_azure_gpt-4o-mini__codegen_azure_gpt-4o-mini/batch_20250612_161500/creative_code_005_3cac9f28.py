"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ae.pages.dev
Prompt: Create a Solidity contract that mirrors the DOGE20 staking mechanism for educational purposes, focusing on reward distribution over two years.
Generated: DETERMINISTIC_3cac9f28a2733e7d
Batch ID: 20250612_161500
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20Staking
 * @dev A contract that mimics the DOGE20 staking mechanism for educational purposes.
 * The contract allows users to stake their tokens and earn rewards over a period of two years.
 */
contract DOGE20Staking is Ownable {
    IERC20 public stakingToken; // ERC20 token to be staked
    uint256 public constant REWARD_DURATION = 730 days; // Total duration for rewards (2 years)
    uint256 public totalStaked; // Total staked tokens
    uint256 public rewardRate; // Reward rate per token per second
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakingTime; // Last time the user staked tokens
    mapping(address => uint256) public rewards; // Rewards accumulated by each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to stake.
     * @param _rewardRate Reward rate per token per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        stakingToken = _stakingToken;
        rewardRate = _rewardRate; // Set the reward rate
    }

    /**
     * @dev Stake a specified amount of tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update rewards before staking
        _updateRewards(msg.sender);
        
        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastStakingTime[msg.sender] = block.timestamp; // Update last staking time
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake a specified amount of tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);
        
        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer rewards to user (in staking tokens)
        stakingToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        if (stakedAmount[user] > 0) {
            // Calculate how long the user has been staking
            uint256 timeStaked = block.timestamp - lastStakingTime[user];
            // Calculate rewards based on the time staked and reward rate
            rewards[user] += (timeStaked * rewardRate * stakedAmount[user]) / 1e18;
            lastStakingTime[user] = block.timestamp; // Update the last staking time
        }
    }

    /**
     * @dev Get the total rewards of a user.
     * @param user Address of the user.
     * @return Total rewards accumulated by the user.
     */
    function getTotalRewards(address user) external view returns (uint256) {
        uint256 timeStaked = block.timestamp - lastStakingTime[user];
        return rewards[user] + (timeStaked * rewardRate * stakedAmount[user]) / 1e18;
    }
}
```
