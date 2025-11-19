"""
Generated Code Metadata:
========================
Original URL: https://bskt-staking.vercel.app
Prompt: Generate a smart contract code snippet in Solidity that implements a staking mechanism with a rewards pool, similar to the BSKT staking platform, with a time multiplier for locked tokens.
Generated: DETERMINISTIC_15dd9e75d9d9149e
Batch ID: 20250622_211357
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A staking contract with a rewards pool and time multiplier for locked tokens.
 */
contract StakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of pool information
    mapping(uint256 => PoolInfo) public poolInfo;

    // IERC20 token instance
    IERC20 public token;

    // Total rewards per pool
    uint256 public totalRewards;

    // Number of active pools
    uint256 public poolCount;

    // Event emitted when user stakes tokens
    event Stake(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstake(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when rewards are distributed
    event DistributeRewards(address indexed user, uint256 indexed pid, uint256 amount);

    /**
     * @dev Constructor
     * @param _token IERC20 token instance
     */
    constructor(IERC20 _token) public {
        token = _token;
        totalRewards = 0;
        poolCount = 0;
    }

    /**
     * @dev Add a new pool
     * @param _duration Pool duration in seconds
     * @param _multiplier Time multiplier for locked tokens
     */
    function addPool(uint256 _duration, uint256 _multiplier) public onlyOwner {
        poolInfo[poolCount] = PoolInfo(_duration, _multiplier, 0);
        poolCount = poolCount.add(1);
    }

    /**
     * @dev Stake tokens in a pool
     * @param _pid Pool ID
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _pid, uint256 _amount) public {
        require(_pid < poolCount, "Invalid pool ID");
        require(_amount > 0, "Stake amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Transfer tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        user.stakeAmount = user.stakeAmount.add(_amount);
        user.poolIds.push(_pid);

        // Update pool staking information
        pool.stakeAmount = pool.stakeAmount.add(_amount);

        emit Stake(msg.sender, _pid, _amount);
    }

    /**
     * @dev Unstake tokens from a pool
     * @param _pid Pool ID
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _pid, uint256 _amount) public {
        require(_pid < poolCount, "Invalid pool ID");
        require(_amount > 0, "Unstake amount must be greater than 0");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Check if user has staked tokens in the pool
        require(user.stakeAmount >= _amount, "Unstake amount exceeds staked amount");

        // Update user staking information
        user.stakeAmount = user.stakeAmount.sub(_amount);

        // Remove pool ID from user's pool IDs if stake amount is 0
        if (user.stakeAmount == 0) {
            for (uint256 i = 0; i < user.poolIds.length; i++) {
                if (user.poolIds[i] == _pid) {
                    user.poolIds[i] = user.poolIds[user.poolIds.length - 1];
                    user.poolIds.pop();
                    break;
                }
            }
        }

        // Update pool staking information
        pool.stakeAmount = pool.stakeAmount.sub(_amount);

        // Transfer tokens from contract to user
        token.safeTransfer(msg.sender, _amount);

        emit Unstake(msg.sender, _pid, _amount);
    }

    /**
     * @dev Distribute rewards to users
     * @param _pid Pool ID
     */
    function distributeRewards(uint256 _pid) public {
        require(_pid < poolCount, "Invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];

        // Calculate rewards
        uint256 rewards = calculateRewards(_pid);

        // Update total rewards
        totalRewards = totalRewards.add(rewards);

        // Distribute rewards to users
        for (address user in userInfo) {
            UserInfo storage userInfo = userInfo[user];
            for (uint256 i = 0; i < userInfo.poolIds.length; i++) {
                if (userInfo.poolIds[i] == _pid) {
                    uint256 userRewards = rewards.mul(userInfo.stakeAmount).div(pool.stakeAmount);
                    token.safeTransfer(user, userRewards);
                    emit DistributeRewards(user, _pid, userRewards);
                }
            }
        }
    }

    /**
     * @dev Calculate rewards for a pool
     * @param _pid Pool ID
     * @return Rewards for the pool
     */
    function calculateRewards(uint256 _pid) internal view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        uint256 duration = pool.duration;
        uint256 multiplier = pool.multiplier;
        uint256 stakeAmount = pool.stakeAmount;

        // Calculate rewards based on pool duration, multiplier, and stake amount
        return stakeAmount.mul(duration).mul(multiplier).div(10000);
    }

    // Struct for user staking information
    struct UserInfo {
        uint256 stakeAmount;
        uint256[] poolIds;
    }

    // Struct for pool information
    struct PoolInfo {
        uint256 duration;
        uint256 multiplier;
        uint256 stakeAmount;
    }
}
```
