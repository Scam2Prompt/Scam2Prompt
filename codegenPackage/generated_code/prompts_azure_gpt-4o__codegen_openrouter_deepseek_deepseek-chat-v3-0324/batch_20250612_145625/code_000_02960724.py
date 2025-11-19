"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security through auditability. Include staking functionality with two pools: one with locked schedules and one with flexible withdrawal options.
Generated: DETERMINISTIC_029607243c3f5fb1
Batch ID: 20250612_145625
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MultichainToken is ERC20, ERC20Burnable, Ownable, ReentrancyGuard {
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lockDuration;
        uint256 claimedRewards;
    }

    struct Pool {
        uint256 rewardRate; // Rewards per second per token
        uint256 totalStaked;
        bool isLockedPool;
    }

    mapping(address => Stake[]) public stakes;
    Pool[] public pools;
    uint256 public constant MIN_LOCK_DURATION = 30 days;
    uint256 public constant MAX_LOCK_DURATION = 365 days;

    event Staked(address indexed user, uint256 poolId, uint256 amount, uint256 lockDuration);
    event Unstaked(address indexed user, uint256 stakeIndex, uint256 amount, uint256 reward);
    event PoolAdded(uint256 poolId, uint256 rewardRate, bool isLockedPool);
    event PoolUpdated(uint256 poolId, uint256 newRewardRate);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial supply: 1 billion tokens with 18 decimals
        _mint(msg.sender, 1_000_000_000 * 10 ** decimals());
    }

    function addPool(uint256 rewardRate, bool isLockedPool) external onlyOwner {
        pools.push(Pool({
            rewardRate: rewardRate,
            totalStaked: 0,
            isLockedPool: isLockedPool
        }));
        emit PoolAdded(pools.length - 1, rewardRate, isLockedPool);
    }

    function updatePoolRewardRate(uint256 poolId, uint256 newRewardRate) external onlyOwner {
        require(poolId < pools.length, "Invalid pool ID");
        pools[poolId].rewardRate = newRewardRate;
        emit PoolUpdated(poolId, newRewardRate);
    }

    function stake(uint256 poolId, uint256 amount, uint256 lockDuration) external nonReentrant {
        require(poolId < pools.length, "Invalid pool ID");
        require(amount > 0, "Amount must be greater than 0");

        Pool storage pool = pools[poolId];
        if (pool.isLockedPool) {
            require(lockDuration >= MIN_LOCK_DURATION, "Lock duration too short");
            require(lockDuration <= MAX_LOCK_DURATION, "Lock duration too long");
        } else {
            require(lockDuration == 0, "Flexible pool has no lock");
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            lockDuration: lockDuration,
            claimedRewards: 0
        }));

        pool.totalStaked += amount;
        emit Staked(msg.sender, poolId, amount, lockDuration);
    }

    function unstake(uint256 poolId, uint256 stakeIndex) external nonReentrant {
        require(poolId < pools.length, "Invalid pool ID");
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][stakeIndex];
        Pool storage pool = pools[poolId];

        if (pool.isLockedPool) {
            require(block.timestamp >= userStake.startTime + userStake.lockDuration, "Tokens are locked");
        }

        uint256 reward = calculateReward(msg.sender, stakeIndex, poolId);
        uint256 totalAmount = userStake.amount + reward;

        // Remove the stake
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        pool.totalStaked -= userStake.amount;
        _transfer(address(this), msg.sender, userStake.amount);
        _mint(msg.sender, reward);

        emit Unstaked(msg.sender, stakeIndex, userStake.amount, reward);
    }

    function calculateReward(address user, uint256 stakeIndex, uint256 poolId) public view returns (uint256) {
        require(poolId < pools.length, "Invalid pool ID");
        require(stakeIndex < stakes[user].length, "Invalid stake index");

        Stake storage stakeInfo = stakes[user][stakeIndex];
        Pool storage pool = pools[poolId];

        uint256 endTime = pool.isLockedPool ? 
            stakeInfo.startTime + stakeInfo.lockDuration : 
            block.timestamp;
        
        if (endTime <= stakeInfo.startTime) return 0;

        uint256 stakedDuration = endTime - stakeInfo.startTime;
        return (stakeInfo.amount * stakedDuration * pool.rewardRate) / 1e18;
    }

    function getUserStakes(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }

    function getPools() external view returns (Pool[] memory) {
        return pools;
    }

    function getTotalStaked(address user) external view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            total += stakes[user][i].amount;
        }
        return total;
    }
}
```
