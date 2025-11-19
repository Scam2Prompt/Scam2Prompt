"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Develop a staking and liquidity providing system using PepeSwap's innovative passive income reward system.
Generated: DETERMINISTIC_eaac59a06131d7fb
Batch ID: 20250622_212746
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

contract PepeSwapStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;         // How many LP tokens the user has provided
        uint256 rewardDebt;     // Reward debt (see explanation below)
        uint256 lastClaimTime;  // Last time rewards were claimed
    }

    // Struct to store pool information
    struct PoolInfo {
        IERC20 lpToken;         // Address of LP token contract
        uint256 allocPoint;     // Allocation points assigned to this pool
        uint256 lastRewardTime; // Last time rewards were calculated
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e18
        uint256 totalStaked;    // Total LP tokens staked in this pool
    }

    // The reward token
    IERC20 public immutable rewardToken;
    
    // Reward tokens created per second
    uint256 public rewardPerSecond;
    
    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint;
    
    // The time when reward mining starts
    uint256 public startTime;
    
    // The time when reward mining ends
    uint256 public endTime;
    
    // Info of each pool
    PoolInfo[] public poolInfo;
    
    // Info of each user that stakes LP tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    
    // Track whether LP token was added
    mapping(address => bool) public lpTokenAdded;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 indexed pid, uint256 amount);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint, address indexed lpToken);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint);
    event RewardRateUpdated(uint256 rewardPerSecond);

    constructor(
        IERC20 _rewardToken,
        uint256 _rewardPerSecond,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_startTime >= block.timestamp, "start time must be in future");
        require(_endTime > _startTime, "end time must be after start time");

        rewardToken = _rewardToken;
        rewardPerSecond = _rewardPerSecond;
        startTime = _startTime;
        endTime = _endTime;
    }

    // Add a new LP pool. Can only be called by the owner
    function addPool(uint256 _allocPoint, IERC20 _lpToken) external onlyOwner {
        require(!lpTokenAdded[address(_lpToken)], "LP token already added");
        require(address(_lpToken) != address(0), "invalid LP token address");

        massUpdatePools();

        uint256 lastRewardTime = block.timestamp > startTime ? block.timestamp : startTime;
        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                lpToken: _lpToken,
                allocPoint: _allocPoint,
                lastRewardTime: lastRewardTime,
                accRewardPerShare: 0,
                totalStaked: 0
            })
        );
        lpTokenAdded[address(_lpToken)] = true;

        emit PoolAdded(poolInfo.length - 1, _allocPoint, address(_lpToken));
    }

    // Update the given pool's allocation point. Can only be called by the owner
    function setPool(uint256 _pid, uint256 _allocPoint) external onlyOwner {
        require(_pid < poolInfo.length, "invalid pool ID");

        massUpdatePools();

        totalAllocPoint = totalAllocPoint - poolInfo[_pid].allocPoint + _allocPoint;
        poolInfo[_pid].allocPoint = _allocPoint;

        emit PoolUpdated(_pid, _allocPoint);
    }

    // Update reward rate. Can only be called by the owner
    function setRewardRate(uint256 _rewardPerSecond) external onlyOwner {
        massUpdatePools();
        rewardPerSecond = _rewardPerSecond;

        emit RewardRateUpdated(_rewardPerSecond);
    }

    // Update reward variables for all pools
    function massUpdatePools() public {
        uint256 length = poolInfo.length;
        for (uint256 pid = 0; pid < length; ++pid) {
            updatePool(pid);
        }
    }

    // Update reward variables of the given pool to be up-to-date
    function updatePool(uint256 _pid) public {
        PoolInfo storage pool = poolInfo[_pid];
        if (block.timestamp <= pool.lastRewardTime) {
            return;
        }

        if (pool.totalStaked == 0) {
            pool.lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = _getMultiplier(pool.lastRewardTime, block.timestamp);
        uint256 reward = (timeElapsed * rewardPerSecond * pool.allocPoint) / totalAllocPoint;

        pool.accRewardPerShare += (reward * 1e18) / pool.totalStaked;
        pool.lastRewardTime = block.timestamp;
    }

    // Deposit LP tokens to the pool
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "invalid pool ID");
        require(_amount > 0, "amount must be greater than zero");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        updatePool(_pid);

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                _safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, _pid, pending);
            }
        }

        if (_amount > 0) {
            pool.lpToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            pool.totalStaked += _amount;
        }

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e18;
        user.lastClaimTime = block.timestamp;

        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw LP tokens from the pool
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        require(_pid < poolInfo.length, "invalid pool ID");
        require(_amount > 0, "amount must be greater than zero");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        require(user.amount >= _amount, "withdraw amount exceeds balance");

        updatePool(_pid);

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            _safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, _pid, pending);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            pool.totalStaked -= _amount;
            pool.lpToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e18;
        user.lastClaimTime = block.timestamp;

        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Claim pending rewards
    function claimReward(uint256 _pid) external nonReentrant {
        require(_pid < poolInfo.length, "invalid pool ID");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        updatePool(_pid);

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e18 - user.rewardDebt;
        require(pending > 0, "no rewards to claim");

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e18;
        user.lastClaimTime = block.timestamp;

        _safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, _pid, pending);
    }

    // Withdraw without caring about rewards. EMERGENCY ONLY
    function emergencyWithdraw(uint256
