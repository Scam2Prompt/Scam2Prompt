"""
Generated Code Metadata:
========================
Original URL: https://presale-hypeloot.com
Prompt: Generate a Solidity smart contract that allows users to stake $HPLT tokens and receive daily rewards based on the amount staked, as described in the Hypeloot ecosystem.
Generated: DETERMINISTIC_542e8987babd1404
Batch ID: 20250612_161035
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
 * @title Hypeloot Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $HPLT tokens and receive daily rewards.
 */
contract HypelootStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => uint256) public rewards;

    // $HPLT token contract
    IERC20 public hpltToken;

    // Daily reward rate (1e18 = 100%)
    uint256 public dailyRewardRate;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Reward distribution interval (in seconds)
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistribution;

    // Event emitted when user stakes $HPLT tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes $HPLT tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _hpltToken $HPLT token contract address
     * @param _dailyRewardRate Daily reward rate (1e18 = 100%)
     * @param _rewardInterval Reward distribution interval (in seconds)
     */
    constructor(
        address _hpltToken,
        uint256 _dailyRewardRate,
        uint256 _rewardInterval
    ) public {
        require(_hpltToken != address(0), "Invalid HPLT token address");
        require(_dailyRewardRate > 0, "Daily reward rate must be greater than 0");
        require(_rewardInterval > 0, "Reward interval must be greater than 0");

        hpltToken = IERC20(_hpltToken);
        dailyRewardRate = _dailyRewardRate;
        rewardInterval = _rewardInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @dev Stake $HPLT tokens
     * @param _amount Amount of $HPLT tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(hpltToken.balanceOf(msg.sender) >= _amount, "Insufficient HPLT token balance");

        // Transfer $HPLT tokens to the contract
        hpltToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastStakeTimestamp = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $HPLT tokens
     * @param _amount Amount of $HPLT tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user staking information
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Transfer $HPLT tokens to the user
        hpltToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to users
     */
    function distributeRewards() external {
        require(block.timestamp.sub(lastRewardDistribution) >= rewardInterval, "Reward distribution interval not reached");

        // Calculate total rewards
        uint256 totalRewards = totalStakedAmount.mul(dailyRewardRate).div(1e18);

        // Distribute rewards to users
        for (address user in userStakingInfos) {
            UserStakingInfo storage userStakingInfo = userStakingInfos[user];
            uint256 userRewards = userStakingInfo.stakedAmount.mul(dailyRewardRate).div(1e18);
            rewards[user] = rewards[user].add(userRewards);
            emit RewardsDistributed(user, userRewards);
        }

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        uint256 userRewards = rewards[msg.sender];
        require(userRewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        hpltToken.safeTransfer(msg.sender, userRewards);

        // Reset user rewards
        rewards[msg.sender] = 0;
    }

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakeTimestamp;
    }
}
```
