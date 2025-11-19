"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoins-io.web.app
Prompt: Create a smart contract in Solidity for staking $GBTC tokens, incorporating gamified staking mechanics and exponential rewards as described on the Green Bitcoin site.
Generated: DETERMINISTIC_3043e538b68fe36a
Batch ID: 20250612_145213
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract GreenBitcoinStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public gbtcToken;

    // Staking rewards per second
    uint256 public rewardsPerSecond;

    // Reward distribution start time
    uint256 public startTime;

    // Reward distribution end time
    uint256 public endTime;

    // Max reward multiplier
    uint256 public maxRewardMultiplier;

    // Minimum staking duration for rewards
    uint256 public minStakingDuration;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of staking pool information
    mapping(uint256 => PoolInfo) public poolInfo;

    // Total allocated tokens
    uint256 public totalAllocated;

    // Event emitted when user stakes tokens
    event Stake(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstake(address indexed user, uint256 indexed pid, uint256 amount);

    // Event emitted when rewards are claimed
    event ClaimRewards(address indexed user, uint256 indexed pid, uint256 rewards);

    // Struct for user information
    struct UserInfo {
        uint256 amount; // Staked amount
        uint256 rewardDebt; // Reward debt
        uint256 lastStakeTime; // Last stake time
    }

    // Struct for pool information
    struct PoolInfo {
        uint256 allocPoint; // Allocation points
        uint256 lastRewardTime; // Last reward time
    }

    // Constructor
    constructor(
        IERC20 _gbtcToken,
        uint256 _rewardsPerSecond,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _maxRewardMultiplier,
        uint256 _minStakingDuration
    ) public {
        gbtcToken = _gbtcToken;
        rewardsPerSecond = _rewardsPerSecond;
        startTime = _startTime;
        endTime = _endTime;
        maxRewardMultiplier = _maxRewardMultiplier;
        minStakingDuration = _minStakingDuration;
    }

    // Add a new staking pool
    function addPool(uint256 _allocPoint) external onlyOwner {
        require(_allocPoint > 0, "Invalid allocation points");

        poolInfo[uint256(poolInfo.length)] = PoolInfo({
            allocPoint: _allocPoint,
            lastRewardTime: block.timestamp
        });
    }

    // Stake tokens
    function stake(uint256 _pid, uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Transfer tokens from user to contract
        gbtcToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        if (user.amount > 0) {
            // Calculate and pay rewards if applicable
            uint256 rewards = getRewards(msg.sender, _pid);
            if (rewards > 0) {
                gbtcToken.safeTransfer(msg.sender, rewards);
                emit ClaimRewards(msg.sender, _pid, rewards);
            }
        }

        user.amount = user.amount.add(_amount);
        user.lastStakeTime = block.timestamp;

        // Update pool allocation
        totalAllocated = totalAllocated.add(_amount);
        pool.allocPoint = pool.allocPoint.add(_amount);

        emit Stake(msg.sender, _pid, _amount);
    }

    // Unstake tokens
    function unstake(uint256 _pid, uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");

        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Check if user has sufficient staked tokens
        require(user.amount >= _amount, "Insufficient staked tokens");

        // Calculate and pay rewards if applicable
        uint256 rewards = getRewards(msg.sender, _pid);
        if (rewards > 0) {
            gbtcToken.safeTransfer(msg.sender, rewards);
            emit ClaimRewards(msg.sender, _pid, rewards);
        }

        // Update user staking information
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount);

        // Update pool allocation
        totalAllocated = totalAllocated.sub(_amount);
        pool.allocPoint = pool.allocPoint.sub(_amount);

        // Transfer tokens from contract to user
        gbtcToken.safeTransfer(msg.sender, _amount);

        emit Unstake(msg.sender, _pid, _amount);
    }

    // Claim rewards
    function claimRewards(uint256 _pid) external {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[msg.sender];

        // Calculate rewards
        uint256 rewards = getRewards(msg.sender, _pid);

        // Pay rewards
        if (rewards > 0) {
            gbtcToken.safeTransfer(msg.sender, rewards);
            emit ClaimRewards(msg.sender, _pid, rewards);
        }
    }

    // Get user rewards
    function getRewards(address _user, uint256 _pid) internal view returns (uint256) {
        PoolInfo storage pool = poolInfo[_pid];
        UserInfo storage user = userInfo[_user];

        // Calculate reward multiplier
        uint256 rewardMultiplier = getRewardMultiplier(user.lastStakeTime);

        // Calculate rewards
        uint256 rewards = user.amount.mul(rewardsPerSecond).mul(rewardMultiplier).div(1e18);

        // Deduct reward debt
        rewards = rewards.sub(user.rewardDebt);

        return rewards;
    }

    // Get reward multiplier
    function getRewardMultiplier(uint256 _lastStakeTime) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp.sub(_lastStakeTime);

        // Exponential rewards
        uint256 rewardMultiplier = 1e18.add(stakingDuration.mul(1e16).div(minStakingDuration));

        // Cap reward multiplier
        return rewardMultiplier.min(maxRewardMultiplier);
    }

    // Update rewards per second
    function updateRewardsPerSecond(uint256 _newRewardsPerSecond) external onlyOwner {
        rewardsPerSecond = _newRewardsPerSecond;
    }

    // Update max reward multiplier
    function updateMaxRewardMultiplier(uint256 _newMaxRewardMultiplier) external onlyOwner {
        maxRewardMultiplier = _newMaxRewardMultiplier;
    }

    // Update min staking duration
    function updateMinStakingDuration(uint256 _newMinStakingDuration) external onlyOwner {
        minStakingDuration = _newMinStakingDuration;
    }
}
```
