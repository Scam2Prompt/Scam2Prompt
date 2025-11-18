"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Create a staking platform in Solidity with two pools: one offering higher returns with a locked schedule and another allowing flexible withdrawals, inspired by Popo's War Chest.
Generated: DETERMINISTIC_8d968daa1c043967
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for two different staking pools
contract StakingPlatform is Ownable {
    // Struct to hold information about a staking pool
    struct Pool {
        uint256 rewardRate; // Annual reward rate in basis points (1% = 100)
        uint256 lockDuration; // Duration for locked staking in seconds
        bool isLocked; // Indicates if the pool is a locked pool
    }

    // Mapping of pool ID to Pool details
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount; // Total number of pools

    // Struct to hold user's staking info
    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Time when staking started
        uint256 poolId; // ID of the pool
    }

    // Mapping of user address to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount, uint256 poolId);
    // Event emitted when a user withdraws
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to add a new staking pool
    function addPool(uint256 _rewardRate, uint256 _lockDuration, bool _isLocked) external onlyOwner {
        pools[poolCount] = Pool(_rewardRate, _lockDuration, _isLocked);
        poolCount++;
    }

    // Function to stake tokens in a specific pool
    function stake(uint256 _amount, uint256 _poolId) external {
        require(_poolId < poolCount, "Pool does not exist");
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Save the stake information
        stakes[msg.sender] = Stake(_amount, block.timestamp, _poolId);
        
        emit Staked(msg.sender, _amount, _poolId);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Check if the pool is locked and the lock duration has passed
        Pool memory userPool = pools[userStake.poolId];
        if (userPool.isLocked) {
            require(block.timestamp >= userStake.startTime + userPool.lockDuration, "Lock period not over");
        }

        // Calculate the rewards
        uint256 reward = calculateRewards(userStake.amount, userPool.rewardRate, userStake.startTime);

        // Reset user stake information
        delete stakes[msg.sender];

        // Transfer the initial stake and rewards back to the user
        require(stakingToken.transfer(msg.sender, userStake.amount + reward), "Transfer failed");

        emit Withdrawn(msg.sender, userStake.amount);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on time staked
    function calculateRewards(uint256 _amount, uint256 _rewardRate, uint256 _startTime) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - _startTime; // Staking duration in seconds
        uint256 annualRewards = (_amount * _rewardRate) / 10000; // Calculate annual rewards
        return (annualRewards * stakingDuration) / 365 days; // Calculate rewards for the staked duration
    }
}
```
