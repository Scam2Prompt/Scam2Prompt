"""
Generated Code Metadata:
========================
Original URL: https://sophon-3zc.pages.dev
Prompt: Provide an example of a smart contract for managing token farming pools, inspired by the "Farm" tab functionality on the Sophon platform.
Generated: DETERMINISTIC_0f4595e4e59b18e0
Batch ID: 20250612_151143
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Token Farming Pool Contract
 * @author [Your Name]
 * @notice This contract manages token farming pools, allowing users to deposit and withdraw tokens.
 */
contract TokenFarmingPool is Ownable {
    using SafeMath for uint256;

    // Mapping of pool IDs to their respective details
    mapping(uint256 => Pool) public pools;

    // Mapping of user addresses to their pool shares
    mapping(address => mapping(uint256 => uint256)) public userShares;

    // Mapping of user addresses to their reward debt
    mapping(address => mapping(uint256 => uint256)) public userRewardDebt;

    // Event emitted when a new pool is created
    event NewPool(uint256 indexed poolId, IERC20 indexed token, uint256 allocPoint);

    // Event emitted when a user deposits tokens into a pool
    event Deposit(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user withdraws tokens from a pool
    event Withdraw(address indexed user, uint256 indexed poolId, uint256 amount);

    // Event emitted when a user harvests rewards from a pool
    event Harvest(address indexed user, uint256 indexed poolId, uint256 amount);

    // Structure representing a farming pool
    struct Pool {
        IERC20 token; // Token being farmed
        uint256 allocPoint; // Allocation points for the pool
        uint256 lastRewardTime; // Last time rewards were distributed
        uint256 accTokenPerShare; // Accumulated tokens per share
        uint256 totalStaked; // Total tokens staked in the pool
    }

    // Total allocation points for all pools
    uint256 public totalAllocPoint;

    // Token used for rewards
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Constructor
    constructor(IERC20 _rewardToken, uint256 _rewardPerBlock) public {
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Creates a new farming pool for the given token and allocation points.
     * @param _token Token to be farmed
     * @param _allocPoint Allocation points for the pool
     */
    function addPool(IERC20 _token, uint256 _allocPoint) public onlyOwner {
        require(_allocPoint > 0, "Allocation points must be greater than 0");

        // Update total allocation points
        totalAllocPoint = totalAllocPoint.add(_allocPoint);

        // Create a new pool
        pools[uint256(ObjectType.poolCounter)] = Pool({
            token: _token,
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp,
            accTokenPerShare: 0,
            totalStaked: 0
        });

        // Increment pool counter
        ObjectType.poolCounter.increment();

        // Emit event
        emit NewPool(uint256(ObjectType.poolCounter) - 1, _token, _allocPoint);
    }

    /**
     * @dev Updates the allocation points for a pool.
     * @param _poolId ID of the pool to update
     * @param _allocPoint New allocation points for the pool
     */
    function updatePool(uint256 _poolId, uint256 _allocPoint) public onlyOwner {
        require(_allocPoint >= 0, "Allocation points must be greater than or equal to 0");

        // Update total allocation points
        totalAllocPoint = totalAllocPoint.sub(pools[_poolId].allocPoint).add(_allocPoint);

        // Update pool allocation points
        pools[_poolId].allocPoint = _allocPoint;

        // Update pool last reward time
        pools[_poolId].lastRewardTime = block.timestamp;
    }

    /**
     * @dev Deposits tokens into a pool.
     * @param _poolId ID of the pool to deposit into
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _poolId, uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Get the pool
        Pool storage pool = pools[_poolId];

        // Update pool
        updatePool(_poolId);

        // Transfer tokens to the pool
        pool.token.transferFrom(msg.sender, address(this), _amount);

        // Update user's shares
        userShares[msg.sender][_poolId] = userShares[msg.sender][_poolId].add(_amount);

        // Update pool total staked
        pool.totalStaked = pool.totalStaked.add(_amount);

        // Emit event
        emit Deposit(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Withdraws tokens from a pool.
     * @param _poolId ID of the pool to withdraw from
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _poolId, uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");

        // Get the pool
        Pool storage pool = pools[_poolId];

        // Update pool
        updatePool(_poolId);

        // Check user's shares
        require(userShares[msg.sender][_poolId] >= _amount, "Insufficient shares");

        // Update user's shares
        userShares[msg.sender][_poolId] = userShares[msg.sender][_poolId].sub(_amount);

        // Update pool total staked
        pool.totalStaked = pool.totalStaked.sub(_amount);

        // Transfer tokens to the user
        pool.token.transfer(msg.sender, _amount);

        // Emit event
        emit Withdraw(msg.sender, _poolId, _amount);
    }

    /**
     * @dev Harvests rewards from a pool.
     * @param _poolId ID of the pool to harvest from
     */
    function harvest(uint256 _poolId) public {
        // Get the pool
        Pool storage pool = pools[_poolId];

        // Update pool
        updatePool(_poolId);

        // Calculate user's reward
        uint256 reward = userShares[msg.sender][_poolId].mul(pool.accTokenPerShare).div(1e12);

        // Update user's reward debt
        userRewardDebt[msg.sender][_poolId] = userShares[msg.sender][_poolId].mul(pool.accTokenPerShare).div(1e12);

        // Transfer reward to the user
        rewardToken.transfer(msg.sender, reward);

        // Emit event
        emit Harvest(msg.sender, _poolId, reward);
    }

    /**
     * @dev Updates a pool.
     * @param _poolId ID of the pool to update
     */
    function updatePool(uint256 _poolId) internal {
        // Get the pool
        Pool storage pool = pools[_poolId];

        // Calculate accumulated tokens per share
        uint256 tokenReward = rewardPerBlock.mul(pool.allocPoint).div(totalAllocPoint);
        pool.accTokenPerShare = pool.accTokenPerShare.add(tokenReward.mul(1e12).div(pool.totalStaked));

        // Update pool last reward time
        pool.lastRewardTime = block.timestamp;
    }

    // Library for managing counters
    library ObjectType {
        uint256 public poolCounter;
    }
}
```
