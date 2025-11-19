"""
Generated Code Metadata:
========================
Original URL: https://polygon6d.com
Prompt: Write a Solidity contract that implements staking rewards based on real-time calculations of pledged funds and staking periods, as described in Polygon6D.
Generated: DETERMINISTIC_d011312ab33f91a5
Batch ID: 20250612_150644
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingRewardsContract
 * @author [Your Name]
 * @notice This contract implements staking rewards based on real-time calculations of pledged funds and staking periods.
 */
contract StakingRewardsContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates for different staking periods
    mapping (uint256 => RewardRate) public rewardRates;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Staking token address
    IERC20 public stakingToken;

    // Reward token address
    IERC20 public rewardToken;

    // Minimum staking amount
    uint256 public minStakingAmount;

    // Maximum staking amount
    uint256 public maxStakingAmount;

    // Staking period array
    uint256[] public stakingPeriods;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _minStakingAmount Minimum staking amount
     * @param _maxStakingAmount Maximum staking amount
     * @param _stakingPeriods Staking periods
     * @param _rewardRates Reward rates for different staking periods
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _minStakingAmount,
        uint256 _maxStakingAmount,
        uint256[] memory _stakingPeriods,
        RewardRate[] memory _rewardRates
    ) public {
        require(_stakingToken != IERC20(address(0)), "Staking token address cannot be zero");
        require(_rewardToken != IERC20(address(0)), "Reward token address cannot be zero");
        require(_minStakingAmount > 0, "Minimum staking amount must be greater than zero");
        require(_maxStakingAmount > _minStakingAmount, "Maximum staking amount must be greater than minimum staking amount");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        minStakingAmount = _minStakingAmount;
        maxStakingAmount = _maxStakingAmount;
        stakingPeriods = _stakingPeriods;

        for (uint256 i = 0; i < _stakingPeriods.length; i++) {
            rewardRates[_stakingPeriods[i]] = _rewardRates[i];
        }
    }

    /**
     * @dev Stake funds
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount >= minStakingAmount && _amount <= maxStakingAmount, "Staking amount must be within the allowed range");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient staking token balance");

        // Update user's staking information
        if (userStakingInfos[msg.sender].stakedAmount > 0) {
            // User has already staked, update their staking information
            userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
            userStakingInfos[msg.sender].stakingStartTime = block.timestamp;
        } else {
            // User has not staked before, create a new staking information entry
            userStakingInfos[msg.sender] = UserStakingInfo(_amount, block.timestamp, 0);
        }

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        // Transfer staking tokens from user's wallet to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake funds
     */
    function unstake() external {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has not staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakingStartTime = 0;
        userStakingInfos[msg.sender].rewards = userStakingInfos[msg.sender].rewards.add(rewards);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(userStakingInfos[msg.sender].stakedAmount);

        // Transfer staking tokens and rewards to user's wallet
        stakingToken.transfer(msg.sender, userStakingInfos[msg.sender].stakedAmount);
        rewardToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, userStakingInfos[msg.sender].stakedAmount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has not staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's staking information
        userStakingInfos[msg.sender].rewards = userStakingInfos[msg.sender].rewards.add(rewards);

        // Transfer rewards to user's wallet
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        // Calculate staking period
        uint256 stakingPeriod = block.timestamp.sub(userStakingInfos[_user].stakingStartTime);

        // Find matching reward rate for staking period
        uint256 rewardRate = 0;
        for (uint256 i = 0; i < stakingPeriods.length; i++) {
            if (stakingPeriod >= stakingPeriods[i]) {
                rewardRate = rewardRates[stakingPeriods[i]].rate;
            }
        }

        // Calculate rewards
        uint256 rewards = userStakingInfos[_user].stakedAmount.mul(rewardRate).div(100);

        return rewards;
    }

    // Struct for user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingStartTime;
        uint256 rewards;
    }

    // Struct for reward rate
    struct RewardRate {
        uint256 rate;
    }
}
```
