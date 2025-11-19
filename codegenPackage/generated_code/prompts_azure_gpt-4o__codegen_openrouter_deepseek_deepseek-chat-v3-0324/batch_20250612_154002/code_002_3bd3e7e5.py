"""
Generated Code Metadata:
========================
Original URL: https://defi-farming.net
Prompt: Generate Solidity code for a simple DeFi farming smart contract that allows users to deposit tokens and earn yield over time.
Generated: DETERMINISTIC_3bd3e7e5837002e3
Batch ID: 20250612_154002
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

contract DeFiFarm is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Info of each user
    struct UserInfo {
        uint256 amount;         // How many tokens the user has provided
        uint256 rewardDebt;     // Reward debt (see explanation below)
    }

    // Info of the farming pool
    struct PoolInfo {
        IERC20 stakingToken;    // Address of staking token contract
        IERC20 rewardToken;     // Address of reward token contract
        uint256 allocPoint;     // Allocation points for this pool
        uint256 lastRewardTime; // Last block time when rewards were distributed
        uint256 accRewardPerShare; // Accumulated rewards per share, times 1e18
        uint256 totalStaked;    // Total tokens staked in the pool
    }

    // Reward tokens per second
    uint256 public rewardPerSecond;

    // Info of each pool
    PoolInfo[] public poolInfo;
    // Info of each user that stakes tokens
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;
    // Total allocation points. Must be the sum of all allocation points in all pools
    uint256 public totalAllocPoint = 0;
    // The time when farming starts
    uint256 public startTime;
    // The time when farming ends
    uint256 public endTime;

    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardPerSecondUpdated(uint256 oldRewardPerSecond, uint256 newRewardPerSecond);
    event PoolAdded(uint256 indexed pid, address stakingToken, address rewardToken, uint256 allocPoint);

    constructor(
        uint256 _rewardPerSecond,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_startTime >= block.timestamp, "start time must be in future");
        require(_endTime > _startTime, "end time must be after start time");

        rewardPerSecond = _rewardPerSecond;
        startTime = _startTime;
        endTime = _endTime;
    }

    // Add a new staking token to the pool
    function addPool(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _allocPoint,
        bool _withUpdate
    ) external onlyOwner {
        if (_withUpdate) {
            massUpdatePools();
        }

        uint256 lastRewardTime = block.timestamp > startTime ? block.timestamp : startTime;
        totalAllocPoint += _allocPoint;
        poolInfo.push(
            PoolInfo({
                stakingToken: _stakingToken,
                rewardToken: _rewardToken,
                allocPoint: _allocPoint,
                lastRewardTime: lastRewardTime,
                accRewardPerShare: 0,
                totalStaked: 0
            })
        );

        emit PoolAdded(poolInfo.length - 1, address(_stakingToken), address(_rewardToken), _allocPoint);
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

        uint256 multiplier = getMultiplier(pool.lastRewardTime, block.timestamp);
        if (multiplier == 0) return;

        uint256 reward = (multiplier * rewardPerSecond * pool.allocPoint) / totalAllocPoint;
        pool.accRewardPerShare += (reward * 1e18) / pool.totalStaked;
        pool.lastRewardTime = block.timestamp;
    }

    // Return reward multiplier over the given _from to _to time
    function getMultiplier(uint256 _from, uint256 _to) public view returns (uint256) {
        if (_to <= startTime || _from >= endTime) {
            return 0;
        }
        if (_from <= startTime && _to <= endTime) {
            return _to - startTime;
        }
        if (_from >= startTime && _to <= endTime) {
            return _to - _from;
        }
        if (_from <= startTime && _to >= endTime) {
            return endTime - startTime;
        }
        if (_from >= startTime && _to >= endTime) {
            return endTime - _from;
        }
        return 0;
    }

    // Deposit staking tokens to farm for reward tokens
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        updatePool(_pid);

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.accRewardPerShare) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending, _pid);
            }
        }

        if (_amount > 0) {
            pool.stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
            user.amount += _amount;
            pool.totalStaked += _amount;
        }

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e18;
        emit Deposit(msg.sender, _pid, _amount);
    }

    // Withdraw staking tokens from farm
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        require(user.amount >= _amount, "withdraw: amount exceeds balance");

        updatePool(_pid);

        uint256 pending = (user.amount * pool.accRewardPerShare) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending, _pid);
        }

        if (_amount > 0) {
            user.amount -= _amount;
            pool.totalStaked -= _amount;
            pool.stakingToken.safeTransfer(msg.sender, _amount);
        }

        user.rewardDebt = (user.amount * pool.accRewardPerShare) / 1e18;
        emit Withdraw(msg.sender, _pid, _amount);
    }

    // Withdraw without caring about rewards. EMERGENCY ONLY
    function emergencyWithdraw(uint256 _pid) external nonReentrant {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_pid][msg.sender];

        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;

        pool.totalStaked -= amount;
        pool.stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, _pid, amount);
    }

    // Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
    function safeRewardTransfer(address _to, uint256 _amount, uint256 _pid) internal {
        PoolInfo storage pool = poolInfo[_pid];
        uint256 rewardBal = pool.rewardToken.balanceOf(address(this));
        if (_amount > rewardBal) {
            pool.rewardToken.safeTransfer(_to, rewardBal);
        } else {
            pool.rewardToken.safeTransfer(_to, _amount);
        }
    }

    // Update reward per second
    function setRewardPerSecond(uint256 _rewardPerSecond) external onlyOwner {
        massUpdatePools();
        emit RewardPerSecondUpdated(rewardPerSecond, _rewardPerSecond);
        rewardPerSecond = _rewardPerSecond;
    }

    // Update end time
    function setEndTime(uint256 _endTime) external onlyOwner {
        require(_endTime > block.timestamp, "end time must be in future");
        require(_endTime > startTime, "end time must be after start time");
        endTime = _endTime;
    }

    // Withdraw reward tokens (emergency only)
    function emergencyRew
