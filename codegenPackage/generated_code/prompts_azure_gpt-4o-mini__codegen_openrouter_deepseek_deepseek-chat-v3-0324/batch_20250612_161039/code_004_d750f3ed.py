"""
Generated Code Metadata:
========================
Original URL: https://popofrog-6s6.pages.dev
Prompt: Outline a step-by-step guide for implementing a staking feature for the $FROP token, focusing on the two pools mentioned in the Popo project.
Generated: DETERMINISTIC_d750f3ed6b657cee
Batch ID: 20250612_161039
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FropStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastStakeTime; // Timestamp of last stake
    }

    // Struct to store pool information
    struct PoolInfo {
        IERC20 stakingToken;   // Address of staking token contract
        uint256 allocPoint;    // Allocation points assigned to this pool
        uint256 lastRewardTime; // Last time reward distribution occurred
        uint256 accRewardPerShare; // Accumulated rewards per share
        uint256 totalStaked;   // Total tokens staked in this pool
        uint256 lockDuration;  // Duration tokens are locked (in seconds)
    }

    // The FROP token
    IERC20 public immutable fropToken;

    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;

    // Reward tokens distributed per second
    uint256 public rewardPerSecond;

    // Total allocation points across all pools
    uint256 public totalAllocPoint;

    // Array of pools
    PoolInfo[] public poolInfo;

    // Info of each user that stakes tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;

    // Events
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardPerSecondUpdated(uint256 oldRate, uint256 newRate);

    constructor(
        IERC20 _fropToken,
        IERC20 _rewardToken,
        uint256 _rewardPerSecond
    ) {
        require(address(_fropToken) != address(0), "Frop token cannot be zero address");
        require(address(_rewardToken) != address(0), "Reward token cannot be zero address");

        fropToken = _fropToken;
        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
    }

    // Add a new staking pool
    function addPool(
        IERC20 _stakingToken,
        uint256 _allocPoint,
        uint256 _lockDuration,
        bool _withUpdate
    ) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                stakingToken: _stakingToken,
                allocPoint: _allocPoint,
                lastRewardTime: block.timestamp,
                accRewardPerShare: 0,
                totalStaked: 0,
                lockDuration: _lockDuration
            })
        );
    }

    // Update the given pool's allocation point
    function setPoolAllocation(
        uint256 _pid,
        uint256 _allocPoint,
        bool _withUpdate
    ) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }
        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;
    }

    // Update reward rate
    function setRewardPerSecond(uint256 _rewardPerSecond) external onlyOwner {
        massUpdatePools();
        emit RewardPerSecondUpdated(rewardPerSecond, _rewardPerSecond);
        rewardPerSecond = _rewardPerSecond;
    }

    // Update all pools
    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    // Update reward variables of the given pool
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.timestamp <= pool.lastRewardTime) {
            return;
        }
        if (pool.totalStaked == 0) {
            pool.lastRewardTime = block.timestamp;
            return;
        }
        uint256 timeElapsed = block.timestamp - pool.lastRewardTime;
        uint256 reward = (timeElapsed * rewardPerSecond * pool.allocPoint) / totalAllocPoint;
        
        pool.accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        pool.lastRewardTime = block.timestamp;
    }

    // Deposit tokens to stake in a pool
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        updatePool(_pid);
        
        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
            }
        }
        
        if (_amount > 0) {
            pool.stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            pool.totalStaked += _amount;
            user.lastStakeTime = block.timestamp;
        }
        
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw staked tokens from a pool
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        require(user.amount >= _amount, "Withdraw amount exceeds balance");
        require(block.timestamp >= user.lastStakeTime + pool.lockDuration, "Tokens are still locked");
        
        updatePool(_pid);
        
        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
        }
        
        if (_amount > 0) {
            user.amount -= _amount;
            pool.totalStaked -= _amount;
            pool.stakingToken.safeTransfer(msg.sender, _amount);
        }
        
        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e12;
        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw(uint256 _pid) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        require(block.timestamp >= user.lastStakeTime + pool.lockDuration, "Tokens are still locked");
        
        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;
        pool.totalStaked -= amount;
        
        pool.stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    // Safe reward transfer function
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            rewardToken.safeTransfer(_to, rewardBal);
        } else {
            rewardToken.safeTransfer(_to, _amount);
        }
    }

    // View function to see pending rewards
    function pendingRewards(uint256 _pid, address _user) external view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][_user];
        uint256 accRewardPerShare = pool.accRewardPerShare;
        if (block.timestamp > pool.lastRewardTime && pool.totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - pool.lastRewardTime;
            uint256 reward = (timeElapsed * rewardPerSecond * pool.allocPoint) / totalAllocPoint;
            accRewardPerShare += (reward * 1e12) / pool.totalStaked;
        }
        return (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
    }

    // View function to get pool count
    function poolLength() external view returns (uint256) {
        return poolInfo
