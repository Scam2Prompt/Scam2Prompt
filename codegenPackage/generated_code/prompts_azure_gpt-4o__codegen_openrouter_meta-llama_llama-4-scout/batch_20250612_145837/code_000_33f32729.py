"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $TUK tokens, inspired by the eTukTuk ecosystem, ensuring users can lock tokens and earn rewards based on their stake duration.
Generated: DETERMINISTIC_33f327299e68ae66
Batch ID: 20250612_145837
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
 * @title TukTukStakingContract
 * @author [Your Name]
 * @notice A staking contract for $TUK tokens, inspired by the eTukTuk ecosystem.
 */
contract TukTukStakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different stake durations
    mapping(uint256 => RewardRate) public rewardRates;

    // $TUK token contract
    IERC20 public tukToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token contract (if different from $TUK)
    IERC20 public rewardToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakeStartTime;
        uint256 stakeDuration; // in seconds
    }

    // Struct to hold reward rate information
    struct RewardRate {
        uint256 rate; // reward rate per second
        uint256 minStakeDuration; // minimum stake duration in seconds
        uint256 maxStakeDuration; // maximum stake duration in seconds
    }

    /**
     * @notice Constructor for the TukTukStakingContract
     * @param _tukToken Address of the $TUK token contract
     * @param _rewardToken Address of the reward token contract (if different from $TUK)
     */
    constructor(address _tukToken, address _rewardToken) {
        tukToken = IERC20(_tukToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize reward rates for different stake durations
        // Example: 10% APY for 1-30 days, 15% APY for 31-60 days, etc.
        rewardRates[1 days] = RewardRate(0.00011574074074074074, 1 days, 30 days); // 10% APY
        rewardRates[31 days] = RewardRate(0.0001736111111111111, 31 days, 60 days); // 15% APY
        // Add more reward rates as needed
    }

    /**
     * @notice Stake $TUK tokens for a specified duration
     * @param _amount Amount of tokens to stake
     * @param _stakeDuration Stake duration in seconds
     */
    function stake(uint256 _amount, uint256 _stakeDuration) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(_stakeDuration > 0, "Invalid stake duration");

        // Find a suitable reward rate for the stake duration
        uint256 suitableRewardRateIndex = findSuitableRewardRateIndex(_stakeDuration);
        require(suitableRewardRateIndex > 0, "No suitable reward rate found");

        // Transfer tokens from user to contract
        tukToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakeStartTime = block.timestamp;
        userStakingInfos[msg.sender].stakeDuration = _stakeDuration;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $TUK tokens
     */
    function unstake() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens and rewards back to user
        tukToken.safeTransfer(msg.sender, userStakingInfos[msg.sender].stakedAmount);
        if (rewards > 0) {
            rewardToken.safeTransfer(msg.sender, rewards);
        }

        // Reset user staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakeStartTime = 0;
        userStakingInfos[msg.sender].stakeDuration = 0;

        // Update total staked tokens
        totalStaked = totalStaked.sub(userStakingInfos[msg.sender].stakedAmount);

        emit Unstaked(msg.sender, userStakingInfos[msg.sender].stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user Address of the user
     * @return Rewards in reward token
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakeDuration = userStakingInfos[_user].stakeDuration;
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;
        uint256 stakeStartTime = userStakingInfos[_user].stakeStartTime;

        // Find a suitable reward rate for the stake duration
        uint256 suitableRewardRateIndex = findSuitableRewardRateIndex(stakeDuration);
        if (suitableRewardRateIndex == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp.sub(stakeStartTime);
        if (elapsedTime > stakeDuration) {
            elapsedTime = stakeDuration;
        }

        RewardRate memory rewardRate = rewardRates[suitableRewardRateIndex];
        uint256 rewards = stakedAmount.mul(rewardRate.rate).mul(elapsedTime);

        return rewards;
    }

    /**
     * @notice Find a suitable reward rate index for a given stake duration
     * @param _stakeDuration Stake duration in seconds
     * @return Suitable reward rate index
     */
    function findSuitableRewardRateIndex(uint256 _stakeDuration) internal view returns (uint256) {
        for (uint256 i = 1; i < 100; i++) { // Assuming 100 reward rates
            RewardRate memory rewardRate = rewardRates[i];
            if (rewardRate.minStakeDuration <= _stakeDuration && _stakeDuration <= rewardRate.maxStakeDuration) {
                return i;
            }
        }
        return 0;
    }
}
```
