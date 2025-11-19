"""
Generated Code Metadata:
========================
Original URL: https://testai-qhn.pages.dev
Prompt: Create a Solidity function that locks staked AITECH tokens for a specified duration and applies tier-based reward boosts, ensuring compatibility with EVM chains.
Generated: DETERMINISTIC_693de21611dba2e2
Batch ID: 20250612_152656
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AITECH Staking Contract
 * @author [Your Name]
 * @notice This contract manages the staking of AITECH tokens, applying tier-based reward boosts.
 */
contract AITECHStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => StakingInfo) public stakingInfo;

    // Mapping of tier-based reward boosts
    mapping(uint256 => RewardBoost) public rewardBoosts;

    // AITECH token contract
    IERC20 public aitechToken;

    // Minimum staking duration
    uint256 public minStakingDuration;

    // Maximum staking duration
    uint256 public maxStakingDuration;

    // Event emitted when a user stakes AITECH tokens
    event Staked(address indexed user, uint256 amount, uint256 duration);

    // Event emitted when a user's staking period ends
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _aitechToken Address of the AITECH token contract
     * @param _minStakingDuration Minimum staking duration in seconds
     * @param _maxStakingDuration Maximum staking duration in seconds
     */
    constructor(
        address _aitechToken,
        uint256 _minStakingDuration,
        uint256 _maxStakingDuration
    ) public {
        require(_aitechToken != address(0), "AITECH token address cannot be zero");
        require(_minStakingDuration > 0, "Minimum staking duration must be greater than 0");
        require(_maxStakingDuration > _minStakingDuration, "Maximum staking duration must be greater than minimum");

        aitechToken = IERC20(_aitechToken);
        minStakingDuration = _minStakingDuration;
        maxStakingDuration = _maxStakingDuration;

        // Initialize tier-based reward boosts
        rewardBoosts[1] = RewardBoost(10, 100); // 10% boost for 1-30 days
        rewardBoosts[2] = RewardBoost(20, 365); // 20% boost for 1-365 days
        rewardBoosts[3] = RewardBoost(50, 730); // 50% boost for 1-730 days
    }

    /**
     * @dev Stake AITECH tokens for a specified duration
     * @param _amount Amount of AITECH tokens to stake
     * @param _duration Staking duration in seconds
     */
    function stake(uint256 _amount, uint256 _duration) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than 0");
        require(_duration >= minStakingDuration && _duration <= maxStakingDuration, "Invalid staking duration");

        // Transfer AITECH tokens to the contract
        require(aitechToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer AITECH tokens");

        // Update user's staking information
        stakingInfo[msg.sender].stakedAmount = stakingInfo[msg.sender].stakedAmount.add(_amount);
        stakingInfo[msg.sender].stakingDuration = _duration;
        stakingInfo[msg.sender].stakingEndTime = block.timestamp.add(_duration);

        emit Staked(msg.sender, _amount, _duration);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(stakingInfo[msg.sender].stakingEndTime <= block.timestamp, "Staking period has not ended");

        // Calculate rewards with tier-based boost
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer rewards to the user
        require(aitechToken.transfer(msg.sender, rewards), "Failed to transfer rewards");

        emit RewardsClaimed(msg.sender, rewards);

        // Reset user's staking information
        stakingInfo[msg.sender].stakedAmount = 0;
        stakingInfo[msg.sender].stakingDuration = 0;
        stakingInfo[msg.sender].stakingEndTime = 0;
    }

    /**
     * @dev Unstake AITECH tokens
     */
    function unstake() external nonReentrant {
        require(stakingInfo[msg.sender].stakingEndTime <= block.timestamp, "Staking period has not ended");

        // Transfer staked AITECH tokens back to the user
        require(aitechToken.transfer(msg.sender, stakingInfo[msg.sender].stakedAmount), "Failed to transfer AITECH tokens");

        emit Unstaked(msg.sender, stakingInfo[msg.sender].stakedAmount);

        // Reset user's staking information
        stakingInfo[msg.sender].stakedAmount = 0;
        stakingInfo[msg.sender].stakingDuration = 0;
        stakingInfo[msg.sender].stakingEndTime = 0;
    }

    /**
     * @dev Calculate rewards with tier-based boost
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingDuration = stakingInfo[_user].stakingDuration;
        uint256 boostPercentage = getBoostPercentage(stakingDuration);

        // Assuming a fixed reward rate of 10%
        uint256 rewardRate = 10;
        uint256 rewards = stakingInfo[_user].stakedAmount.mul(rewardRate).mul(boostPercentage).div(100);

        return rewards;
    }

    /**
     * @dev Get tier-based boost percentage
     * @param _stakingDuration Staking duration in seconds
     * @return Boost percentage
     */
    function getBoostPercentage(uint256 _stakingDuration) internal view returns (uint256) {
        for (uint256 i = 1; i <= 3; i++) {
            if (_stakingDuration >= rewardBoosts[i].minDuration && _stakingDuration <= rewardBoosts[i].maxDuration) {
                return rewardBoosts[i].boostPercentage;
            }
        }

        return 0;
    }

    struct StakingInfo {
        uint256 stakedAmount;
        uint256 stakingDuration;
        uint256 stakingEndTime;
    }

    struct RewardBoost {
        uint256 boostPercentage;
        uint256 maxDuration;
        uint256 minDuration;
    }
}
```
