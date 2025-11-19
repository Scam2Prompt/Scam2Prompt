"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Develop a smart contract to manage staking pools for FreeDum Fighters, ensuring rewards are distributed according to the project's tokenomics.
Generated: DETERMINISTIC_8af4245502ebf0f5
Batch ID: 20250612_153424
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FreeDum Fighters Staking Pool Contract
 * @author [Your Name]
 * @notice This contract manages staking pools for FreeDum Fighters, distributing rewards according to the project's tokenomics.
 */
contract FreeDumFightersStakingPool is Ownable {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of pool IDs to their respective information
    mapping (uint256 => Pool) public pools;

    // Total number of pools
    uint256 public poolCount;

    // Reward token contract
    ERC20 public rewardToken;

    // Staking token contract
    ERC20 public stakingToken;

    // Tokenomics configuration
    uint256 public rewardPerBlock;
    uint256 public startBlock;
    uint256 public endBlock;

    /**
     * @dev Event emitted when a new pool is created
     * @param poolId ID of the new pool
     * @param poolName Name of the new pool
     */
    event NewPool(uint256 poolId, string poolName);

    /**
     * @dev Event emitted when a staker stakes tokens
     * @param staker Address of the staker
     * @param poolId ID of the pool
     * @param amount Amount of tokens staked
     */
    event Staked(address staker, uint256 poolId, uint256 amount);

    /**
     * @dev Event emitted when a staker unstakes tokens
     * @param staker Address of the staker
     * @param poolId ID of the pool
     * @param amount Amount of tokens unstaked
     */
    event Unstaked(address staker, uint256 poolId, uint256 amount);

    /**
     * @dev Event emitted when rewards are distributed
     * @param staker Address of the staker
     * @param poolId ID of the pool
     * @param amount Amount of rewards distributed
     */
    event RewardsDistributed(address staker, uint256 poolId, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256[] poolIds;
        mapping (uint256 => uint256) stakedAmounts;
        mapping (uint256 => uint256) rewards;
    }

    /**
     * @dev Struct representing a pool's information
     */
    struct Pool {
        string name;
        uint256 capacity;
        uint256 stakedAmount;
        uint256 accRewardPerShare;
        bool isActive;
    }

    /**
     * @dev Constructor
     * @param _rewardToken Address of the reward token contract
     * @param _stakingToken Address of the staking token contract
     * @param _rewardPerBlock Reward per block
     * @param _startBlock Start block
     * @param _endBlock End block
     */
    constructor(
        address _rewardToken,
        address _stakingToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) public {
        rewardToken = ERC20(_rewardToken);
        stakingToken = ERC20(_stakingToken);
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @dev Creates a new pool
     * @param _name Name of the pool
     * @param _capacity Capacity of the pool
     */
    function createPool(string memory _name, uint256 _capacity) public onlyOwner {
        Pool memory newPool;
        newPool.name = _name;
        newPool.capacity = _capacity;
        newPool.stakedAmount = 0;
        newPool.accRewardPerShare = 0;
        newPool.isActive = true;

        pools[poolCount] = newPool;
        emit NewPool(poolCount, _name);
        poolCount++;
    }

    /**
     * @dev Stakes tokens in a pool
     * @param _poolId ID of the pool
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _poolId, uint256 _amount) public {
        require(pools[_poolId].isActive, "Pool is not active");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.poolIds.push(_poolId);
        staker.stakedAmounts[_poolId] = staker.stakedAmounts[_poolId].add(_amount);
        pools[_poolId].stakedAmount = pools[_poolId].stakedAmount.add(_amount);

        emit Staked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Unstakes tokens from a pool
     * @param _poolId ID of the pool
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _poolId, uint256 _amount) public {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmounts[_poolId] >= _amount, "Insufficient staked amount");
        staker.stakedAmounts[_poolId] = staker.stakedAmounts[_poolId].sub(_amount);
        pools[_poolId].stakedAmount = pools[_poolId].stakedAmount.sub(_amount);
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Distributes rewards to stakers
     * @param _poolId ID of the pool
     */
    function distributeRewards(uint256 _poolId) public {
        Pool storage pool = pools[_poolId];
        uint256 reward = rewardPerBlock.mul(block.number.sub(startBlock));
        uint256 accRewardPerShare = reward.div(pool.stakedAmount);
        pool.accRewardPerShare = accRewardPerShare;

        Staker storage staker = stakers[msg.sender];
        uint256 stakedAmount = staker.stakedAmounts[_poolId];
        uint256 rewardAmount = stakedAmount.mul(accRewardPerShare).div(1e18);
        staker.rewards[_poolId] = staker.rewards[_poolId].add(rewardAmount);

        emit RewardsDistributed(msg.sender, _poolId, rewardAmount);
    }

    /**
     * @dev Claims rewards for a staker
     * @param _poolId ID of the pool
     */
    function claimRewards(uint256 _poolId) public {
        Staker storage staker = stakers[msg.sender];
        uint256 rewardAmount = staker.rewards[_poolId];
        staker.rewards[_poolId] = 0;
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }
}
```
