"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Create a Solidity function that calculates and distributes compounding staking rewards based on APY and lock term, as described in the SidusPad staking pools.
Generated: DETERMINISTIC_8d78bfc38179ff78
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SidusStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct Pool {
        uint256 apy; // APY in basis points (10000 = 100%)
        uint256 lockTerm; // Lock term in seconds
        uint256 totalStaked;
        uint256 lastRewardUpdate;
        uint256 rewardPerTokenStored;
    }

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakedTimestamp;
    }

    mapping(uint256 => Pool) public pools;
    mapping(uint256 => mapping(address => UserInfo)) public userInfo;

    event Staked(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdrawn(address indexed user, uint256 indexed pid, uint256 amount);
    event RewardPaid(address indexed user, uint256 indexed pid, uint256 reward);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    function addPool(uint256 pid, uint256 apy, uint256 lockTerm) external onlyOwner {
        require(pools[pid].apy == 0, "Pool already exists");
        pools[pid] = Pool({
            apy: apy,
            lockTerm: lockTerm,
            totalStaked: 0,
            lastRewardUpdate: block.timestamp,
            rewardPerTokenStored: 0
        });
    }

    function updatePool(uint256 pid) internal {
        Pool storage pool = pools[pid];
        if (block.timestamp <= pool.lastRewardUpdate) {
            return;
        }

        if (pool.totalStaked == 0) {
            pool.lastRewardUpdate = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - pool.lastRewardUpdate;
        uint256 reward = (pool.totalStaked * pool.apy * timeElapsed) / (365 days * 10000);
        
        pool.rewardPerTokenStored += (reward * 1e18) / pool.totalStaked;
        pool.lastRewardUpdate = block.timestamp;
    }

    function pendingReward(uint256 pid, address user) external view returns (uint256) {
        Pool storage pool = pools[pid];
        UserInfo storage user = userInfo[pid][msg.sender];

        uint256 rewardPerToken = pool.rewardPerTokenStored;
        if (block.timestamp > pool.lastRewardUpdate && pool.totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - pool.lastRewardUpdate;
            uint256 reward = (pool.totalStaked * pool.apy * timeElapsed) / (365 days * 10000);
            rewardPerToken += (reward * 1e18) / pool.totalStaked;
        }

        return (user.amount * rewardPerToken) / 1e18 - user.rewardDebt;
    }

    function stake(uint256 pid, uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        Pool storage pool = pools[pid];
        UserInfo storage user = userInfo[pid][msg.sender];

        updatePool(pid);

        if (user.amount > 0) {
            uint256 pending = (user.amount * pool.rewardPerTokenStored) / 1e18 - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardPaid(msg.sender, pid, pending);
            }
        }

        stakingToken.transferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * pool.rewardPerTokenStored) / 1e18;
        user.lastStakedTimestamp = block.timestamp;
        pool.totalStaked += amount;

        emit Staked(msg.sender, pid, amount);
    }

    function withdraw(uint256 pid, uint256 amount) external nonReentrant {
        Pool storage pool = pools[pid];
        UserInfo storage user = userInfo[pid][msg.sender];

        require(user.amount >= amount, "Withdraw amount exceeds balance");
        require(block.timestamp >= user.lastStakedTimestamp + pool.lockTerm, "Lock term not expired");

        updatePool(pid);

        uint256 pending = (user.amount * pool.rewardPerTokenStored) / 1e18 - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardPaid(msg.sender, pid, pending);
        }

        if (amount > 0) {
            user.amount -= amount;
            stakingToken.transfer(msg.sender, amount);
            pool.totalStaked -= amount;
        }

        user.rewardDebt = (user.amount * pool.rewardPerTokenStored) / 1e18;
        emit Withdrawn(msg.sender, pid, amount);
    }

    function emergencyWithdraw(uint256 pid) external nonReentrant {
        Pool storage pool = pools[pid];
        UserInfo storage user = userInfo[pid][msg.sender];

        uint256 amount = user.amount;
        user.amount = 0;
        user.rewardDebt = 0;

        stakingToken.transfer(msg.sender, amount);
        pool.totalStaked -= amount;

        emit Withdrawn(msg.sender, pid, amount);
    }

    function safeRewardTransfer(address to, uint256 amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (amount > rewardBalance) {
            rewardToken.transfer(to, rewardBalance);
        } else {
            rewardToken.transfer(to, amount);
        }
    }

    function updateApy(uint256 pid, uint256 newApy) external onlyOwner {
        updatePool(pid);
        pools[pid].apy = newApy;
    }

    function updateLockTerm(uint256 pid, uint256 newLockTerm) external onlyOwner {
        pools[pid].lockTerm = newLockTerm;
    }
}
```
