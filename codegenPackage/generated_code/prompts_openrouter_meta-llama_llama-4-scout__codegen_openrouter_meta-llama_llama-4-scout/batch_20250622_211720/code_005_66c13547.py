"""
Generated Code Metadata:
========================
Original URL: https://stakewise.eu
Prompt: Design a basic staking contract in Solidity that could underpin a service similar to Stakewise, including functions for stake, withdraw, and claim rewards.
Generated: DETERMINISTIC_66c1354759f6b3d1
Batch ID: 20250622_211720
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice A basic staking contract that allows users to stake, withdraw, and claim rewards.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => RewardDistribution) public rewardDistributions;

    // Staking token address
    IERC20 public stakingToken;

    // Reward token address
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

    // Event emitted when user withdraws
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when reward distribution is updated
    event RewardDistributionUpdated(address indexed distributor, uint256 amount);

    /**
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
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
    function startStaking() public onlyOwner {
        require(!isStakingActive, "Staking is already active");
        require(block.timestamp >= stakingStartTimestamp, "Staking has not started yet");
        isStakingActive = true;
    }

    /**
     * @notice Stop staking
     */
    function stopStaking() public onlyOwner {
        require(isStakingActive, "Staking is not active");
        isStakingActive = false;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(isStakingActive, "Staking is not active");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient staking token balance");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastClaimedBlock = block.timestamp;

        totalStakedAmount = totalStakedAmount.add(_amount);

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw staked tokens
     */
    function withdraw() public nonReentrant {
        require(isStakingActive == false, "Staking is still active");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked amount to withdraw");

        uint256 stakedAmount = userStakingInfos[msg.sender].stakedAmount;
        userStakingInfos[msg.sender].stakedAmount = 0;

        totalStakedAmount = totalStakedAmount.sub(stakedAmount);

        stakingToken.safeTransfer(msg.sender, stakedAmount);

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public nonReentrant {
        require(isStakingActive == false, "Staking is still active");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked amount to claim rewards");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        uint256 rewardAmount = calculateReward(userStakingInfo);

        userStakingInfo.lastClaimedBlock = block.timestamp;
        userStakingInfo.claimedRewards = userStakingInfo.claimedRewards.add(rewardAmount);

        totalRewardAmount = totalRewardAmount.add(rewardAmount);

        rewardToken.safeTransfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Update reward distribution
     * @param _distributor Distributor address
     * @param _amount Reward amount
     */
    function updateRewardDistribution(address _distributor, uint256 _amount) public onlyOwner {
        rewardDistributions[_distributor] = RewardDistribution(_distributor, _amount);

        emit RewardDistributionUpdated(_distributor, _amount);
    }

    /**
     * @notice Calculate reward for a user
     * @param _userStakingInfo User staking information
     * @return Reward amount
     */
    function calculateReward(UserStakingInfo storage _userStakingInfo) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp.sub(_userStakingInfo.lastClaimedBlock);
        uint256 reward = _userStakingInfo.stakedAmount.mul(rewardPerBlock).mul(stakingDuration);

        return reward;
    }

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastClaimedBlock;
        uint256 claimedRewards;
    }

    // Struct to store reward distribution
    struct RewardDistribution {
        address distributor;
        uint256 amount;
    }

    // Modifier to restrict access to owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    // Get owner address
    address public owner;

    constructor() public {
        owner = msg.sender;
    }
}
```
