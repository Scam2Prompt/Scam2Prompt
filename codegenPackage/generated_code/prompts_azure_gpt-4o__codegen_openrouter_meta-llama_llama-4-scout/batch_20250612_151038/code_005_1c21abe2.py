"""
Generated Code Metadata:
========================
Original URL: https://opsec-1ne.pages.dev
Prompt: Develop a smart contract to integrate staking functionality for $OPSEC tokens, following the roadmap outlined for governance and DePIN development.
Generated: DETERMINISTIC_1c21abe2cab0a4a4
Batch ID: 20250612_151038
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
 * @title OpsecStakingContract
 * @author [Your Name]
 * @notice This contract provides staking functionality for $OPSEC tokens.
 */
contract OpsecStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of staking pool IDs to their information
    mapping(uint256 => StakingPool) public stakingPools;

    // $OPSEC token contract
    ERC20 public opsecToken;

    // Total number of staking pools
    uint256 public poolCount;

    // Event emitted when a new staking pool is created
    event NewStakingPool(uint256 indexed poolId, uint256 rewardRate, uint256 duration);

    // Event emitted when a staker stakes tokens
    event Staked(address indexed staker, uint256 indexed poolId, uint256 amount);

    // Event emitted when a staker unstakes tokens
    event Unstaked(address indexed staker, uint256 indexed poolId, uint256 amount);

    // Event emitted when a staker claims rewards
    event RewardsClaimed(address indexed staker, uint256 indexed poolId, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256[] poolIds; // IDs of pools the staker is participating in
        mapping(uint256 => uint256) stakedAmounts; // Amounts staked in each pool
        mapping(uint256 => uint256) rewardsEarned; // Rewards earned in each pool
    }

    /**
     * @dev Struct representing a staking pool's information
     */
    struct StakingPool {
        uint256 rewardRate; // Reward rate per second
        uint256 duration; // Duration of the staking pool in seconds
        uint256 startTime; // Start time of the staking pool
        uint256 endTime; // End time of the staking pool
        uint256 totalStaked; // Total amount staked in the pool
    }

    /**
     * @dev Constructor
     * @param _opsecToken Address of the $OPSEC token contract
     */
    constructor(address _opsecToken) {
        opsecToken = ERC20(_opsecToken);
    }

    /**
     * @dev Creates a new staking pool
     * @param _rewardRate Reward rate per second
     * @param _duration Duration of the staking pool in seconds
     */
    function createStakingPool(uint256 _rewardRate, uint256 _duration) public {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        StakingPool memory newPool;
        newPool.rewardRate = _rewardRate;
        newPool.duration = _duration;
        newPool.startTime = block.timestamp;
        newPool.endTime = block.timestamp.add(_duration);

        stakingPools[poolCount] = newPool;
        emit NewStakingPool(poolCount, _rewardRate, _duration);
        poolCount++;
    }

    /**
     * @dev Stakes $OPSEC tokens in a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) public {
        require(stakingPools[_poolId].startTime != 0, "Pool does not exist");
        require(stakingPools[_poolId].startTime <= block.timestamp && block.timestamp < stakingPools[_poolId].endTime, "Pool is not active");
        require(opsecToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(_amount > 0, "Staking amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        staker.poolIds.push(_poolId);
        staker.stakedAmounts[_poolId] = staker.stakedAmounts[_poolId].add(_amount);
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.add(_amount);

        opsecToken.transferFrom(msg.sender, address(this), _amount);
        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Unstakes $OPSEC tokens from a pool
     * @param _poolId ID of the staking pool
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) public {
        require(stakingPools[_poolId].startTime != 0, "Pool does not exist");
        require(stakingPools[_poolId].startTime <= block.timestamp && block.timestamp <= stakingPools[_poolId].endTime, "Pool is not active");
        require(stakers[msg.sender].stakedAmounts[_poolId] >= _amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmounts[_poolId] = staker.stakedAmounts[_poolId].sub(_amount);
        stakingPools[_poolId].totalStaked = stakingPools[_poolId].totalStaked.sub(_amount);

        opsecToken.transfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Claims rewards for a staker
     * @param _poolId ID of the staking pool
     */
    function claimRewards(uint256 _poolId) public {
        require(stakingPools[_poolId].startTime != 0, "Pool does not exist");
        require(stakingPools[_poolId].startTime <= block.timestamp && block.timestamp <= stakingPools[_poolId].endTime, "Pool is not active");

        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender, _poolId);
        staker.rewardsEarned[_poolId] = staker.rewardsEarned[_poolId].add(rewards);

        opsecToken.transfer(msg.sender, rewards);
        emit RewardsClaimed(msg.sender, _poolId, rewards);
    }

    /**
     * @dev Calculates rewards for a staker in a pool
     * @param _staker Address of the staker
     * @param _poolId ID of the staking pool
     * @return Rewards earned by the staker
     */
    function calculateRewards(address _staker, uint256 _poolId) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 stakedAmount = staker.stakedAmounts[_poolId];
        uint256 timeElapsed = block.timestamp.sub(stakingPools[_poolId].startTime);
        uint256 rewards = stakedAmount.mul(stakingPools[_poolId].rewardRate).mul(timeElapsed);

        return rewards.sub(staker.rewardsEarned[_poolId]);
    }
}
```
