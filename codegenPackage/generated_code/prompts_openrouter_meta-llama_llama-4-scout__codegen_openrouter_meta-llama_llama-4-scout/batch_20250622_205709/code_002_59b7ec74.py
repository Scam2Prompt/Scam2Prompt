"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: Generate a Solidity code snippet for a staking pool with a 365-day lock term and a 8.87% compounding reward APY.
Generated: DETERMINISTIC_59b7ec7407415997
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title StakingPool
 * @author [Your Name]
 * @notice A staking pool with a 365-day lock term and an 8.87% compounding reward APY.
 */
contract StakingPool is ReentrancyGuard {
    using SafeMath for uint256;

    // Constants
    uint256 public constant LOCK_TERM = 365 days;
    uint256 public constant REWARD_APY = 887; // 8.87%

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Staking token
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward amount
    uint256 public totalRewardAmount;

    // Staking start timestamp
    uint256 public stakingStartTime;

    /**
     * @param _stakingToken The staking token address.
     * @param _rewardToken The reward token address.
     */
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) public {
        require(address(_stakingToken) != address(0), "Staking token address cannot be zero");
        require(address(_rewardToken) != address(0), "Reward token address cannot be zero");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;

        stakingStartTime = block.timestamp;
    }

    /**
     * @notice Stake tokens for a 365-day lock term.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount == 0, "User has already staked");

        // Transfer staking tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer staking tokens");

        // Update user staking information
        userStakingInfos[msg.sender] = UserStakingInfo({
            stakedAmount: _amount,
            stakedTime: block.timestamp
        });

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);
    }

    /**
     * @notice Claim rewards and unstake tokens after the lock term.
     */
    function claimRewards() external nonReentrant {
        UserStakingInfo storage userInfo = userStakingInfos[msg.sender];
        require(userInfo.stakedAmount > 0, "User has not staked");
        require(block.timestamp >= userInfo.stakedTime.add(LOCK_TERM), "Lock term has not expired");

        // Calculate reward amount
        uint256 rewardAmount = calculateRewardAmount(userInfo.stakedAmount);

        // Update user staking information
        userInfo.stakedAmount = 0;
        userInfo.rewardAmount = userInfo.rewardAmount.add(rewardAmount);

        // Transfer reward tokens to user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Failed to transfer reward tokens");

        // Transfer staking tokens to user
        require(stakingToken.transfer(msg.sender, userInfo.stakedAmount), "Failed to transfer staking tokens");

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(userInfo.stakedAmount);
    }

    /**
     * @notice Calculate reward amount based on staked amount and lock term.
     * @param _stakedAmount The staked amount.
     * @return The reward amount.
     */
    function calculateRewardAmount(uint256 _stakedAmount) internal view returns (uint256) {
        // Calculate reward rate per second
        uint256 rewardRatePerSecond = REWARD_APY.mul(10**18).div(365 days);

        // Calculate reward amount
        uint256 rewardAmount = _stakedAmount.mul(rewardRatePerSecond).mul(LOCK_TERM);

        return rewardAmount;
    }

    /**
     * @dev Struct for user staking information.
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedTime;
        uint256 rewardAmount;
    }
}
```
