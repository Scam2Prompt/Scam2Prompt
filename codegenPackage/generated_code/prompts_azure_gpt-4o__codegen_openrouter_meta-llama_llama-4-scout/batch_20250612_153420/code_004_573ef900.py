"""
Generated Code Metadata:
========================
Original URL: https://elephantrewards.pages.dev
Prompt: Write a Solidity contract that implements a referral rewards system, paying out 1% rewards via staking, inspired by Elephant Money Farms' partner rewards feature.
Generated: DETERMINISTIC_573ef900626e6312
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralRewardsContract
 * @author [Your Name]
 * @notice A contract that implements a referral rewards system, paying out 1% rewards via staking.
 */
contract ReferralRewardsContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user to referrer
    mapping(address => address) public referrals;

    // Mapping of referrer to total rewards earned
    mapping(address => uint256) public rewards;

    // Mapping of user to total staked amount
    mapping(address => uint256) public stakedAmounts;

    // The reward token
    IERC20 public rewardToken;

    // The staking token
    IERC20 public stakingToken;

    // Reward percentage
    uint256 public constant REWARD_PERCENTAGE = 100; // 1%

    /**
     * @notice Constructor
     * @param _rewardToken The address of the reward token
     * @param _stakingToken The address of the staking token
     */
    constructor(address _rewardToken, address _stakingToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingToken != address(0), "Staking token address cannot be zero");

        rewardToken = IERC20(_rewardToken);
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @notice Set referral
     * @param _referrer The address of the referrer
     */
    function setReferral(address _referrer) external {
        require(_referrer != address(0), "Referrer address cannot be zero");
        referrals[msg.sender] = _referrer;
    }

    /**
     * @notice Stake
     * @param _amount The amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer staking token from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staked amount
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(_amount);

        // Check if user has a referrer
        if (referrals[msg.sender] != address(0)) {
            // Calculate reward
            uint256 reward = _amount.mul(REWARD_PERCENTAGE).div(10000);

            // Update rewards for referrer
            rewards[referrals[msg.sender]] = rewards[referrals[msg.sender]].add(reward);

            // Transfer reward to referrer
            rewardToken.safeTransfer(referrals[msg.sender], reward);
        }
    }

    /**
     * @notice Unstake
     * @param _amount The amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= _amount, "Insufficient staked amount");

        // Update staked amount
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(_amount);

        // Transfer staking token from contract to user
        stakingToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        require(rewards[msg.sender] > 0, "No rewards to claim");

        // Store reward amount
        uint256 rewardAmount = rewards[msg.sender];

        // Reset rewards for user
        rewards[msg.sender] = 0;

        // Transfer reward to user
        rewardToken.safeTransfer(msg.sender, rewardAmount);
    }
}
```
