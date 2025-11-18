"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Create a smart contract in Solidity for staking $SCOTTY tokens, ensuring the contract includes functionality for calculating rewards based on the user's share of the staking pool and dynamic rewards rate.
Generated: DETERMINISTIC_84a2496734fb0045
Batch ID: 20250612_153526
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking $SCOTTY tokens with reward calculation based on user's share of the staking pool.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    IERC20 public scottyToken; // ERC20 token contract reference
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Dynamic reward rate per token staked
    mapping(address => uint256) public userStake; // Mapping of user address to their staked amount
    mapping(address => uint256) public rewards; // Mapping of user address to their accumulated rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the token address and initial reward rate.
     * @param _scottyToken The address of the $SCOTTY token contract.
     * @param _initialRewardRate The initial reward rate per token.
     */
    constructor(IERC20 _scottyToken, uint256 _initialRewardRate) {
        scottyToken = _scottyToken;
        rewardRate = _initialRewardRate;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(scottyToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), amount);
        
        userStake[msg.sender] = userStake[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(userStake[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        userStake[msg.sender] = userStake[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        // Transfer tokens back to user
        scottyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
        claimRewards(); // Automatically claim rewards upon unstaking
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() public {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0; // Reset rewards after claiming
        scottyToken.transfer(msg.sender, reward);
        
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        if (userStake[user] > 0) {
            // Calculate the reward based on user's share of the total staked
            uint256 userReward = userStake[user].mul(rewardRate).div(totalStaked);
            rewards[user] = rewards[user].add(userReward);
        }
    }

    /**
     * @dev Function to set a new reward rate. Only callable by the owner.
     * @param newRewardRate The new reward rate to be set.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Function to view the user's pending rewards.
     * @param user The address of the user.
     * @return The amount of pending rewards for the user.
     */
    function pendingRewards(address user) external view returns (uint256) {
        if (userStake[user] == 0) return 0;
        uint256 userReward = userStake[user].mul(rewardRate).div(totalStaked);
        return rewards[user].add(userReward);
    }
}
```
