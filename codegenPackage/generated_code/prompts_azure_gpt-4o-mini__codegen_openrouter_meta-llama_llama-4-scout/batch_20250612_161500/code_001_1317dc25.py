"""
Generated Code Metadata:
========================
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a smart contract for a staking pool that supports different reward rates and compounding options for AITECH tokens, similar to those outlined on the Solidus AI Tech platform.
Generated: DETERMINISTIC_1317dc25a3084b73
Batch ID: 20250612_161500
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AITECH Staking Pool Contract
 * @author [Your Name]
 * @notice This contract manages a staking pool for AITECH tokens with different reward rates and compounding options.
 */
contract AITECHStakingPool is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // AITECH token contract
    IERC20 public aitechToken;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of reward rates for different staking periods
    mapping(uint256 => RewardRate) public rewardRates;

    // Mapping of compounding options
    mapping(uint256 => CompoundingOption) public compoundingOptions;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes AITECH tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes AITECH tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are compounded
    event RewardsCompounded(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _aitechToken AITECH token contract address
     */
    constructor(address _aitechToken) {
        require(_aitechToken != address(0), "AITECH token address cannot be zero");
        aitechToken = IERC20(_aitechToken);

        // Initialize reward rates and compounding options
        rewardRates[1] = RewardRate(100, 365); // 100% APY for 1 year
        rewardRates[3] = RewardRate(200, 365); // 200% APY for 3 years
        compoundingOptions[1] = CompoundingOption(1 days, 1); // daily compounding for 1 year
        compoundingOptions[3] = CompoundingOption(1 weeks, 3); // weekly compounding for 3 years
    }

    /**
     * @dev Stake AITECH tokens for a specified period
     * @param _amount Amount of AITECH tokens to stake
     * @param _period Staking period (in years)
     */
    function stake(uint256 _amount, uint256 _period) public {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(rewardRates[_period].rate > 0, "Invalid staking period");

        // Transfer AITECH tokens to the contract
        aitechToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        UserInfo storage user = userInfo[msg.sender];
        user.stakedAmount = user.stakedAmount.add(_amount);
        user.stakingPeriod = _period;
        user.lastCompoundingTime = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake AITECH tokens
     */
    function unstake() public {
        UserInfo storage user = userInfo[msg.sender];
        require(user.stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens and rewards to the user
        aitechToken.safeTransfer(msg.sender, user.stakedAmount.add(rewards));

        // Reset user staking information
        user.stakedAmount = 0;
        user.stakingPeriod = 0;
        user.lastCompoundingTime = 0;

        // Update total staked amount
        totalStaked = totalStaked.sub(user.stakedAmount);

        emit Unstaked(msg.sender, user.stakedAmount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public {
        UserInfo storage user = userInfo[msg.sender];
        require(user.stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer rewards to the user
        aitechToken.safeTransfer(msg.sender, rewards);

        // Update user staking information
        user.lastCompoundingTime = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Compound rewards
     */
    function compoundRewards() public {
        UserInfo storage user = userInfo[msg.sender];
        require(user.stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Add rewards to user's staked amount
        user.stakedAmount = user.stakedAmount.add(rewards);

        // Update user staking information
        user.lastCompoundingTime = block.timestamp;

        emit RewardsCompounded(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        RewardRate storage rewardRate = rewardRates[user.stakingPeriod];
        CompoundingOption storage compoundingOption = compoundingOptions[user.stakingPeriod];

        // Calculate time elapsed since last compounding
        uint256 timeElapsed = block.timestamp.sub(user.lastCompoundingTime);

        // Calculate rewards
        uint256 rewards = user.stakedAmount.mul(rewardRate.rate).mul(timeElapsed) / 365 days / 100;

        // Apply compounding
        if (compoundingOption.compoundingFrequency > 0) {
            uint256 compoundingPeriods = timeElapsed / compoundingOption.compoundingFrequency;
            rewards = rewards.mul(compoundingPeriods);
        }

        return rewards;
    }

    // Structs

    struct UserInfo {
        uint256 stakedAmount;
        uint256 stakingPeriod;
        uint256 lastCompoundingTime;
    }

    struct RewardRate {
        uint256 rate;
        uint256 duration;
    }

    struct CompoundingOption {
        uint256 compoundingFrequency;
        uint256 compoundingPeriod;
    }
}
```
