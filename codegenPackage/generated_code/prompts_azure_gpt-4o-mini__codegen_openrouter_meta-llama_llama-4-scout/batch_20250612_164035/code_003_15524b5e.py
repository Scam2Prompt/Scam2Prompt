"""
Generated Code Metadata:
========================
Original URL: https://doglibretoken.web.app
Prompt: Develop a smart contract for a staking mechanism that allows users to stake their $DOGL tokens and earn rewards, referencing DogLibre's tokenomics.
Generated: DETERMINISTIC_15524b5e0318dc0e
Batch ID: 20250612_164035
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DogL Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake their $DOGL tokens and earn rewards.
 */
contract DogLStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different staking periods
    mapping(uint256 => RewardRate) public rewardRates;

    // $DOGL token contract
    ERC20 public doglToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token contract (e.g. $DOGL or another token)
    ERC20 public rewardToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _doglToken $DOGL token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _doglToken, address _rewardToken) public {
        require(_doglToken != address(0), "DOGL token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        doglToken = ERC20(_doglToken);
        rewardToken = ERC20(_rewardToken);

        // Initialize reward rates for different staking periods (e.g. 15 days, 30 days, 60 days)
        rewardRates[15 days] = RewardRate(100, 365); // 100% APY for 15 days
        rewardRates[30 days] = RewardRate(200, 365); // 200% APY for 30 days
        rewardRates[60 days] = RewardRate(500, 365); // 500% APY for 60 days
    }

    /**
     * @notice Stake $DOGL tokens for a specified period
     * @param _amount Amount of $DOGL tokens to stake
     * @param _period Staking period in days
     */
    function stake(uint256 _amount, uint256 _period) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(rewardRates[_period] != RewardRate(0, 0), "Invalid staking period");

        // Transfer $DOGL tokens from user to contract
        doglToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakingPeriod = _period;
        userStakingInfos[msg.sender].stakeTimestamp = block.timestamp;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $DOGL tokens
     */
    function unstake() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer $DOGL tokens and rewards back to user
        doglToken.transfer(msg.sender, userStakingInfos[msg.sender].stakedAmount);
        if (rewards > 0) {
            rewardToken.transfer(msg.sender, rewards);
        }

        // Reset user's staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakingPeriod = 0;
        userStakingInfos[msg.sender].stakeTimestamp = 0;
        userStakingInfos[msg.sender].lastClaimTimestamp = 0;

        // Update total staked tokens
        totalStaked = totalStaked.sub(userStakingInfos[msg.sender].stakedAmount);

        emit Unstaked(msg.sender, userStakingInfos[msg.sender].stakedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has no staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer rewards to user
        if (rewards > 0) {
            rewardToken.transfer(msg.sender, rewards);
            userStakingInfos[msg.sender].lastClaimTimestamp = block.timestamp;

            emit RewardsClaimed(msg.sender, rewards);
        }
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        UserStakingInfo memory userInfo = userStakingInfos[_user];

        if (userInfo.stakedAmount == 0 || userInfo.stakeTimestamp == 0) {
            return 0;
        }

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp.sub(userInfo.stakeTimestamp);

        // Calculate rewards
        uint256 rewards = userInfo.stakedAmount.mul(rewardRates[userInfo.stakingPeriod].rate).mul(stakingDuration).div(365 days).div(100);

        // Check if user has already claimed rewards
        if (userInfo.lastClaimTimestamp > 0) {
            rewards = rewards.sub(userInfo.stakedAmount.mul(rewardRates[userInfo.stakingPeriod].rate).mul(userInfo.lastClaimTimestamp.sub(userInfo.stakeTimestamp)).div(365 days).div(100));
        }

        return rewards;
    }

    // Struct for user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingPeriod;
        uint256 stakeTimestamp;
        uint256 lastClaimTimestamp;
    }

    // Struct for reward rate
    struct RewardRate {
        uint256 rate;
        uint256 period;
    }
}
```
