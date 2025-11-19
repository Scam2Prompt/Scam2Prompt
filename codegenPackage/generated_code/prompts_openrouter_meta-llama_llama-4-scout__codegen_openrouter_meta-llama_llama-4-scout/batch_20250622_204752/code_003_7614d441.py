"""
Generated Code Metadata:
========================
Original URL: https://joincommonwealth.net
Prompt: Design a simple staking and unstaking system using Solidity for a cryptocurrency project like Commonwealth.
Generated: DETERMINISTIC_7614d441b4699b02
Batch ID: 20250622_204752
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking and Unstaking System
 * @author [Your Name]
 * @notice This contract provides a simple staking and unstaking system for a cryptocurrency project.
 */
contract StakingSystem is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user staking rewards
    mapping (address => uint256) public stakingRewards;

    // Total staked amount
    uint256 public totalStaked;

    // Staking reward rate (per block)
    uint256 public stakingRewardRate;

    // Staking token address
    IERC20 public stakingToken;

    // Unstaking cooldown period (in blocks)
    uint256 public unstakingCooldownPeriod;

    // Mapping of user unstaking cooldowns
    mapping (address => uint256) public unstakingCooldowns;

    /**
     * @dev Constructor
     * @param _stakingTokenAddress Address of the staking token
     * @param _stakingRewardRate Staking reward rate (per block)
     * @param _unstakingCooldownPeriod Unstaking cooldown period (in blocks)
     */
    constructor(
        address _stakingTokenAddress,
        uint256 _stakingRewardRate,
        uint256 _unstakingCooldownPeriod
    ) public {
        stakingToken = IERC20(_stakingTokenAddress);
        stakingRewardRate = _stakingRewardRate;
        unstakingCooldownPeriod = _unstakingCooldownPeriod;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external nonReentrant {
        require(stakingBalances[msg.sender] > 0, "No staked tokens");

        // Check unstaking cooldown period
        require(unstakingCooldowns[msg.sender] == 0 || block.number >= unstakingCooldowns[msg.sender], "Unstaking cooldown period not over");

        // Calculate user's staking reward
        uint256 reward = calculateStakingReward(msg.sender);

        // Update user's staking reward
        stakingRewards[msg.sender] = stakingRewards[msg.sender].add(reward);

        // Transfer tokens and reward to user
        require(stakingToken.transfer(msg.sender, stakingBalances[msg.sender]), "Token transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset user's staking balance and unstaking cooldown
        stakingBalances[msg.sender] = 0;
        unstakingCooldowns[msg.sender] = block.number.add(unstakingCooldownPeriod);

        // Update total staked amount
        totalStaked = totalStaked.sub(stakingBalances[msg.sender]);

        // Emit event
        emit Unstaked(msg.sender, stakingBalances[msg.sender], reward);
    }

    /**
     * @dev Calculate staking reward for a user
     * @param _user User address
     * @return Staking reward
     */
    function calculateStakingReward(address _user) internal view returns (uint256) {
        // Calculate staking reward based on user's staking balance and staking reward rate
        return stakingBalances[_user].mul(stakingRewardRate);
    }

    /**
     * @dev Get user's staking information
     * @param _user User address
     * @return Staking balance, staking reward, and unstaking cooldown
     */
    function getStakingInfo(address _user) external view returns (uint256, uint256, uint256) {
        return (stakingBalances[_user], stakingRewards[_user], unstakingCooldowns[_user]);
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
}
```
