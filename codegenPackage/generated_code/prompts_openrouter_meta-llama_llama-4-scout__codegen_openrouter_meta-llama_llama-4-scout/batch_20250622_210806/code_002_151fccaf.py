"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: "Design a simple staking system in Solidity for $MTE token holders to earn rewards from a staking rewards pool funded by trading tax, with a percentage of tax revenue allocated to the pool."
Generated: DETERMINISTIC_151fccaf0706caed
Batch ID: 20250622_210806
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
 * @title MTE Staking Contract
 * @author [Your Name]
 * @notice This contract allows $MTE token holders to stake their tokens and earn rewards from a staking rewards pool.
 */
contract MTEStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward pool allocation
    mapping (address => uint256) public rewardPoolAllocations;

    // Staking token ($MTE)
    IERC20 public stakingToken;

    // Reward token (same as staking token for simplicity)
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward pool
    uint256 public totalRewardPool;

    // Staking reward rate (per block)
    uint256 public stakingRewardRate;

    // Trading tax revenue allocator
    address public taxRevenueAllocator;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Event emitted when tax revenue is allocated to reward pool
    event TaxRevenueAllocated(uint256 amount);

    /**
     * @param _stakingToken $MTE token address
     * @param _rewardToken Reward token address (same as staking token for simplicity)
     * @param _stakingRewardRate Staking reward rate (per block)
     * @param _taxRevenueAllocator Trading tax revenue allocator address
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingRewardRate,
        address _taxRevenueAllocator
    ) public {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingRewardRate > 0, "Staking reward rate must be greater than zero");
        require(_taxRevenueAllocator != address(0), "Tax revenue allocator address cannot be zero");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingRewardRate = _stakingRewardRate;
        taxRevenueAllocator = _taxRevenueAllocator;
    }

    /**
     * @dev Stake $MTE tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient staking token balance");

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].lastUpdateBlock = block.number;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $MTE tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(_amount);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Transfer staking tokens from contract to user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimReward() external nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        // Update user's staking information
        userStakingInfos[msg.sender].lastUpdateBlock = block.number;

        // Transfer reward tokens from contract to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allocate trading tax revenue to reward pool
     * @param _amount Amount to allocate
     */
    function allocateTaxRevenue(uint256 _amount) external {
        require(msg.sender == taxRevenueAllocator, "Only tax revenue allocator can allocate revenue");
        require(_amount > 0, "Allocation amount must be greater than zero");

        // Update total reward pool
        totalRewardPool = totalRewardPool.add(_amount);

        // Transfer reward tokens from allocator to contract
        rewardToken.transferFrom(taxRevenueAllocator, address(this), _amount);

        emit TaxRevenueAllocated(_amount);
    }

    /**
     * @dev Calculate staking reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;
        uint256 blocksElapsed = block.number.sub(userStakingInfos[_user].lastUpdateBlock);
        uint256 reward = stakedAmount.mul(stakingRewardRate).mul(blocksElapsed);

        // Cap reward by total reward pool
        return reward.min(totalRewardPool);
    }

    // Struct to store user's staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastUpdateBlock;
    }
}
```
