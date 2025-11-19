"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that includes a reward distribution mechanism based on the user's share of the staking pool fees, as described in the HEHE ecosystem.
Generated: DETERMINISTIC_ca490eb83e70f900
Batch ID: 20250612_153517
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
 * @title HEHE Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $HEHE tokens and earn rewards based on their share of the staking pool fees.
 */
contract HEHEStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // $HEHE token contract
    IERC20 public heheToken;

    // Staking pool address
    address public stakingPool;

    // Reward distribution interval (in seconds)
    uint256 public rewardInterval;

    // Last reward distribution timestamp
    uint256 public lastRewardDistribution;

    // Total staked amount
    uint256 public totalStaked;

    // Total reward accumulated
    uint256 public totalReward;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfo;

    // Mapping of reward distribution history
    mapping(uint256 => RewardDistribution) public rewardDistributions;

    // Event emitted when a user stakes $HEHE tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes $HEHE tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 rewardAmount);

    /**
     * @param _heheToken $HEHE token contract address
     * @param _stakingPool Staking pool address
     * @param _rewardInterval Reward distribution interval (in seconds)
     */
    constructor(
        address _heheToken,
        address _stakingPool,
        uint256 _rewardInterval
    ) public {
        heheToken = IERC20(_heheToken);
        stakingPool = _stakingPool;
        rewardInterval = _rewardInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Stake $HEHE tokens
     * @param _amount Amount of $HEHE tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer $HEHE tokens from user to contract
        heheToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStakingInfo[msg.sender].stakedAmount = userStakingInfo[msg.sender].stakedAmount.add(_amount);
        userStakingInfo[msg.sender].lastStakeTimestamp = block.timestamp;

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $HEHE tokens
     * @param _amount Amount of $HEHE tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user's staking information
        userStakingInfo[msg.sender].stakedAmount = userStakingInfo[msg.sender].stakedAmount.sub(_amount);

        // Transfer $HEHE tokens from contract to user
        heheToken.safeTransfer(msg.sender, _amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to users
     */
    function distributeRewards() external nonReentrant {
        require(msg.sender == stakingPool, "Only staking pool can distribute rewards");

        // Calculate reward amount
        uint256 rewardAmount = calculateRewardAmount();

        // Update total reward accumulated
        totalReward = totalReward.add(rewardAmount);

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;

        // Create a new reward distribution entry
        rewardDistributions[block.timestamp] = RewardDistribution(rewardAmount, totalStaked);

        emit RewardsDistributed(rewardAmount);

        // Distribute rewards to users
        distributeRewardsToUsers(rewardAmount);
    }

    /**
     * @notice Calculate reward amount
     * @return Reward amount
     */
    function calculateRewardAmount() internal view returns (uint256) {
        // TO DO: implement reward calculation logic
        return 0;
    }

    /**
     * @notice Distribute rewards to users
     * @param _rewardAmount Reward amount to distribute
     */
    function distributeRewardsToUsers(uint256 _rewardAmount) internal {
        // Iterate through all users and distribute rewards based on their share of the staking pool
        for (address user in userStakingInfo) {
            UserStakingInfo memory userInfo = userStakingInfo[user];
            uint256 userReward = _rewardAmount.mul(userInfo.stakedAmount).div(totalStaked);
            heheToken.safeTransfer(user, userReward);
        }
    }

    /**
     * @notice Get user's staking information
     * @param _user User address
     * @return User's staking information
     */
    function getUserStakingInfo(address _user) external view returns (UserStakingInfo memory) {
        return userStakingInfo[_user];
    }

    /**
     * @dev Struct representing user's staking information
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakeTimestamp;
    }

    /**
     * @dev Struct representing reward distribution entry
     */
    struct RewardDistribution {
        uint256 rewardAmount;
        uint256 totalStaked;
    }
}
```
