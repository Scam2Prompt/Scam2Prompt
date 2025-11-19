"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Design a simple staking system using Solidity for the Oracle Meme token (OMEME) on the Binance Smart Chain, offering a 652% reward based on dynamic percentage.
Generated: DETERMINISTIC_2ebce7eaa8a2fd41
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for Oracle Meme token (OMEME) on Binance Smart Chain
 * @author [Your Name]
 * @notice This contract allows users to stake OMEME tokens and earn rewards based on a dynamic percentage.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // OMEME token contract
    IERC20 public omemeToken;

    // Reward percentage (6.52% in this case)
    uint256 public rewardPercentage = 652;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Staking start timestamp
    uint256 public stakingStartTime;

    // Staking end timestamp (set to 0 for indefinite)
    uint256 public stakingEndTime;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    /**
     * @notice Constructor
     * @param _omemeTokenAddress Address of OMEME token contract
     */
    constructor(address _omemeTokenAddress) public {
        require(_omemeTokenAddress != address(0), "Invalid OMEME token address");
        omemeToken = IERC20(_omemeTokenAddress);
        stakingStartTime = block.timestamp;
    }

    /**
     * @notice Stake OMEME tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(stakingStartTime != 0 && block.timestamp >= stakingStartTime, "Staking not started");
        require(stakingEndTime == 0 || block.timestamp < stakingEndTime, "Staking ended");
        require(_amount > 0, "Invalid stake amount");

        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        uint256 newStakedAmount = userInfo.stakedAmount.add(_amount);

        // Transfer tokens from user to contract
        require(omemeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userInfo.stakedAmount = newStakedAmount;
        userInfo.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake OMEME tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        require(userInfo.stakedAmount >= _amount, "Insufficient staked amount");

        // Update user's staked amount and reward debt
        userInfo.stakedAmount = userInfo.stakedAmount.sub(_amount);
        userInfo.rewardDebt = userInfo.rewardDebt.add(_amount);

        // Transfer tokens from contract to user
        require(omemeToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];

        // Calculate reward
        uint256 reward = calculateReward(userInfo.stakedAmount, userInfo.lastStakeTime);

        // Update user's reward debt
        userInfo.rewardDebt = userInfo.rewardDebt.add(reward);

        // Transfer reward to user
        require(omemeToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a given staked amount and time
     * @param _stakedAmount Staked amount
     * @param _lastStakeTime Last stake time
     * @return Reward amount
     */
    function calculateReward(uint256 _stakedAmount, uint256 _lastStakeTime) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp.sub(_lastStakeTime);
        uint256 reward = _stakedAmount.mul(rewardPercentage).mul(timeElapsed) / 100 / 365 days;

        return reward;
    }

    /**
     * @notice Update reward percentage
     * @param _newRewardPercentage New reward percentage
     */
    function updateRewardPercentage(uint256 _newRewardPercentage) external onlyOwner {
        rewardPercentage = _newRewardPercentage;
    }

    /**
     * @notice Set staking end time
     * @param _stakingEndTime Staking end time
     */
    function setStakingEndTime(uint256 _stakingEndTime) external onlyOwner {
        stakingEndTime = _stakingEndTime;
    }
}
```
