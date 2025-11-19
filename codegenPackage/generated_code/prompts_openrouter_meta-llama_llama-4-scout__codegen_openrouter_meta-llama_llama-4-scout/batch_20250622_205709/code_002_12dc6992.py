"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-io.web.app
Prompt: Generate a smart contract in Solidity that allows users to stake $SCOTTY tokens and earn rewards based on the project's staking mechanism.
Generated: DETERMINISTIC_12dc69928cf2584b
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract for staking $SCOTTY tokens and earning rewards.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different staking periods
    mapping (uint256 => RewardRate) public rewardRates;

    // $SCOTTY token contract
    IERC20 public scottyToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token contract (assuming $SCOTTY as reward token for simplicity)
    IERC20 public rewardToken;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _scottyToken $SCOTTY token contract address
     * @param _rewardToken Reward token contract address
     */
    constructor(address _scottyToken, address _rewardToken) public {
        require(_scottyToken != address(0) && _rewardToken != address(0), "Invalid token address");

        scottyToken = IERC20(_scottyToken);
        rewardToken = IERC20(_rewardToken);

        // Initialize reward rates for different staking periods (in days)
        rewardRates[7] = RewardRate(100, 7); // 100% APY for 7-day staking
        rewardRates[30] = RewardRate(500, 30); // 500% APY for 30-day staking
    }

    /**
     * @dev Stake $SCOTTY tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakingStartTime = block.timestamp;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $SCOTTY tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(_amount);

        // Transfer tokens from contract to user
        require(scottyToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update total staked tokens
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 stakingPeriod = block.timestamp.sub(userStakingInfos[msg.sender].stakingStartTime);
        uint256 reward = calculateReward(userStakingInfos[msg.sender].stakedAmount, stakingPeriod);

        require(reward > 0, "No rewards to claim");

        // Transfer rewards to user
        require(rewardToken.transfer(msg.sender, reward), "Reward token transfer failed");

        // Reset user staking start time
        userStakingInfos[msg.sender].stakingStartTime = block.timestamp;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward based on staking amount and period
     * @param _stakedAmount Staked amount
     * @param _stakingPeriod Staking period in seconds
     * @return Reward amount
     */
    function calculateReward(uint256 _stakedAmount, uint256 _stakingPeriod) internal view returns (uint256) {
        uint256 reward = 0;

        // Iterate through reward rates for different staking periods
        for (uint256 i = 0; i < 2; i++) {
            uint256 period = i == 0 ? 7 days : 30 days;
            RewardRate memory rate = rewardRates[period];

            if (_stakingPeriod >= period) {
                reward = reward.add(_stakedAmount.mul(rate.rate).div(100).mul(_stakingPeriod.div(period)));
            }
        }

        return reward;
    }

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingStartTime;
    }

    // Struct to store reward rate information
    struct RewardRate {
        uint256 rate; // APY rate
        uint256 period; // Staking period in days
    }
}
```
