"""
Generated Code Metadata:
========================
Original URL: https://betswirl.pages.dev
Prompt: "Generate a smart contract code in Solidity for a staking mechanism similar to BetSwirl's staking/earn AVAX feature."
Generated: DETERMINISTIC_a2da499ce659bdb2
Batch ID: 20250622_211350
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
 * @title StakingContract
 * @author [Your Name]
 * @notice A staking contract for AVAX, allowing users to stake and earn rewards.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => RewardDistribution) public rewardDistributions;

    // Staking token (AVAX)
    IERC20 public stakingToken;

    // Reward token (AVAX)
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward amount
    uint256 public totalRewardAmount;

    // Staking start timestamp
    uint256 public stakingStartTimestamp;

    // Staking end timestamp
    uint256 public stakingEndTimestamp;

    // Reward per block
    uint256 public rewardPerBlock;

    // Flag to check if staking is active
    bool public isStakingActive;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Staking token (AVAX)
     * @param _rewardToken Reward token (AVAX)
     * @param _stakingStartTimestamp Staking start timestamp
     * @param _stakingEndTimestamp Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp,
        uint256 _rewardPerBlock
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
        rewardPerBlock = _rewardPerBlock;
        isStakingActive = false;
    }

    /**
     * @notice Start staking
     */
    function startStaking() public {
        require(!isStakingActive, "Staking is already active");
        require(block.timestamp >= stakingStartTimestamp, "Staking has not started yet");
        isStakingActive = true;
    }

    /**
     * @notice Stop staking
     */
    function stopStaking() public {
        require(isStakingActive, "Staking is not active");
        require(block.timestamp >= stakingEndTimestamp, "Staking has not ended yet");
        isStakingActive = false;
    }

    /**
     * @notice Stake AVAX
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(isStakingActive, "Staking is not active");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].lastStakedBlock = block.timestamp;
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake AVAX
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(isStakingActive == false, "Staking is still active");
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(_amount);
        stakingToken.safeTransfer(msg.sender, _amount);
        totalStakedAmount = totalStakedAmount.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim reward
     */
    function claimReward() public {
        require(isStakingActive == false, "Staking is still active");
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        rewardDistributions[msg.sender].claimedReward = rewardDistributions[msg.sender].claimedReward.add(reward);
        rewardToken.safeTransfer(msg.sender, reward);

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakedDuration = block.timestamp.sub(userStakingInfos[_user].lastStakedBlock);
        uint256 reward = stakedDuration.mul(rewardPerBlock).mul(userStakingInfos[_user].stakedAmount).div(totalStakedAmount);
        return reward.sub(rewardDistributions[_user].claimedReward);
    }

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedBlock;
    }

    // Struct to store reward distribution
    struct RewardDistribution {
        uint256 claimedReward;
    }
}
```
