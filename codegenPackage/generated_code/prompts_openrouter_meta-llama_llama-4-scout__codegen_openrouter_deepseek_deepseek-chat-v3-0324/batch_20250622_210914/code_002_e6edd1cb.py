"""
Generated Code Metadata:
========================
Original URL: https://ether-etherfi.github.io
Prompt: Generate a smart contract code for a yield farming and staking platform using the Ethereum blockchain, inspired by Ether Fi's features.
Generated: DETERMINISTIC_e6edd1cba2b568c1
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract YieldFarm is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Info of each user
    struct UserInfo {
        uint256 amount;         // How many LP tokens the user has provided
        uint256 rewardDebt;     // Reward debt
        uint256 lastClaimTime;  // Last time user claimed rewards
    }

    // Info of each pool
    struct PoolInfo {
        IERC20 lpToken;         // Address of LP token contract
        uint256 allocPoint;     // Allocation points for this pool
        uint256 lastRewardTime; // Last time rewards were distributed
        uint256 accRewardPerShare; // Accumulated rewards per share
        uint256 totalStaked;    // Total amount staked in the pool
        uint256 lockPeriod;     // Minimum staking period in seconds
    }

    // The reward token
    IERC20 public rewardToken;
    
    // Reward tokens distributed per second
    uint256 public rewardPerSecond;
    
    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint;
    
    // The time when reward distribution starts
    uint256 public startTime;
    
    // The time when reward distribution ends
    uint256 public endTime;
    
    // Info of each pool
    PoolInfo[] public poolInfo;
    
    // Info of each user that stakes LP tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    
    // Track whether LP token was added
    mapping(address => bool) public lpTokenExists;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardClaimed(address indexed user, uint256 indexed pid, uint256 amount);
    event PoolAdded(uint256 indexed pid, uint256 allocPoint, IERC20 lpToken, uint256 lockPeriod);
    event PoolUpdated(uint256 indexed pid, uint256 allocPoint, uint256 lockPeriod);
    event RewardRateUpdated(uint256 rewardPerSecond);
    event RewardPeriodUpdated(uint256 startTime, uint256 endTime);

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

    // Add a new pool. Can only be called by the owner
    function addPool(
        uint256 _allocPoint,
        IERC20 _lpToken,
        uint256 _lockPeriod,
        bool _withUpdate
    ) external onlyOwner {
        require(!lpTokenExists[address(_lpToken)], "pool already exists");
        require(address(_lpToken) != address(rewardToken), "cannot stake reward token");
        
        if (_withUpdate) {
            massUpdatePools();
        }
        
        uint256 lastRewardTime = block.timestamp > startTime ? block.timestamp : startTime;
        totalAllocPoint = totalAllocPoint.add(_allocPoint);
        poolInfo.push(
            PoolInfo({
                lpToken: _lpToken,
                allocPoint: _allocPoint,
                lastRewardTime: lastRewardTime,
                accRewardPerShare: 0,
                totalStaked: 0,
                lockPeriod: _lockPeriod
            })
        );
        lpTokenExists[address(_lpToken)] = true;
        
        emit PoolAdded(poolInfo.length - 1, _allocPoint, _lpToken, _lockPeriod);
    }

    // Update the given pool's allocation point and lock period. Can only be called by the owner
    function setPool(
        uint256 _pid,
        uint256 _allocPoint,
        uint256 _lockPeriod,
        bool _withUpdate
    ) external onlyOwner {
        require(_pid < poolInfo.length, "invalid pool id");
        
        if (_withUpdate) {
            massUpdatePools();
        }
        
        totalAllocPoint = totalAllocPoint.sub(poolInfo[_pid].allocPoint).add(_allocPoint);
        poolInfo[_pid].allocPoint = _allocPoint;
        poolInfo[_pid].lockPeriod = _lockPeriod;
        
        emit PoolUpdated(_pid, _allocPoint, _lockPeriod);
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
        
        uint256 lpSupply = pool.totalStaked;
        if (lpSupply == 0) {
            pool.lastRewardTime = block.timestamp;
            return;
        }
        
        uint256 timeElapsed = _getMultiplier(pool.lastRewardTime, block.timestamp);
        uint256 reward = timeElapsed.mul(rewardPerSecond).mul(pool.allocPoint).div(totalAllocPoint);
        
        pool.accRewardPerShare = pool.accRewardPerShare.add(reward.mul(1e12).div(lpSupply));
        pool.lastRewardTime = block.timestamp;
    }

    // Deposit LP tokens to the farm
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        updatePool(_pid);
        
        if (user.amount > 0) {
            _claimRewards(_pid);
        }
        
        if (_amount > 0) {
            pool.lpToken.safeTransferFrom(address(msg.sender), address(this), _amount);
            user.amount = user.amount.add(_amount);
            pool.totalStaked = pool.totalStaked.add(_amount);
        }
        
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e12);
        user.lastClaimTime = block.timestamp;
        
        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw LP tokens from the farm
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        require(user.amount >= _amount, "withdraw: insufficient balance");
        require(block.timestamp >= user.lastClaimTime.add(pool.lockPeriod), "withdraw: lock period not ended");
        
        updatePool(_pid);
        
        _claimRewards(_pid);
        
        if (_amount > 0) {
            user.amount = user.amount.sub(_amount);
            pool.totalStaked = pool.totalStaked.sub(_amount);
            pool.lpToken.safeTransfer(address(msg.sender), _amount);
        }
        
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e12);
        
        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Claim rewards from the farm
    function claim(uint256 _pid) external nonReentrant {
        updatePool(_pid);
        _claimRewards(_pid);
    }

    // Internal function to claim rewards
    function _claimRewards(uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];
        
        uint256 pending = user.amount.mul(pool.accRewardPerShare).div(1e12).sub(user.rewardDebt);
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, _pid, pending);
        }
        
        user.rewardDebt = user.amount.mul(pool.accRewardPerShare).div(1e12);
        user.lastClaimTime = block.timestamp;
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw(uint256 _pid) external nonRe
