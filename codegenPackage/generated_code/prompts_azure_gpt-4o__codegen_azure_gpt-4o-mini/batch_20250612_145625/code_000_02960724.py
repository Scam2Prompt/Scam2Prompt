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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MultiChainToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Staking pool structure
    struct StakingPool {
        uint256 totalStaked;
        uint256 lockDuration; // Duration for locked staking
        uint256 rewardRate;   // Reward rate for staking
    }

    // Staking pools
    StakingPool public lockedPool;
    StakingPool public flexiblePool;

    // User staking information
    struct UserStake {
        uint256 amount;
        uint256 startTime;
        bool isLocked; // Indicates if the stake is in the locked pool
    }

    mapping(address => UserStake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, bool isLocked);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the token and pools
    constructor() ERC20("MultiChainToken", "MCT") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to owner

        // Initialize locked staking pool
        lockedPool = StakingPool({
            totalStaked: 0,
            lockDuration: 30 days,
            rewardRate: 10 // 10% reward rate
        });

        // Initialize flexible staking pool
        flexiblePool = StakingPool({
            totalStaked: 0,
            lockDuration: 0,
            rewardRate: 5 // 5% reward rate
        });
    }

    // Function to stake tokens in either pool
    function stake(uint256 amount, bool isLocked) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update user stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;
        stakes[msg.sender].isLocked = isLocked;

        // Update total staked in the respective pool
        if (isLocked) {
            lockedPool.totalStaked = lockedPool.totalStaked.add(amount);
        } else {
            flexiblePool.totalStaked = flexiblePool.totalStaked.add(amount);
        }

        emit Staked(msg.sender, amount, isLocked);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        UserStake memory userStake = stakes[user];
        uint256 rewardRate = userStake.isLocked ? lockedPool.rewardRate : flexiblePool.rewardRate;
        uint256 duration = block.timestamp.sub(userStake.startTime);
        
        // Calculate reward based on duration and rate
        return userStake.amount.mul(rewardRate).mul(duration).div(365 days).div(100);
    }

    // Function to unstake tokens
    function unstake() external nonReentrant {
        UserStake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        // Check if the user is trying to unstake from the locked pool
        if (userStake.isLocked) {
            require(block.timestamp >= userStake.startTime + lockedPool.lockDuration, "Tokens are locked");
        }

        // Calculate rewards and transfer tokens back to user
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount.add(reward);

        // Reset user stake information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;

        // Update total staked in the respective pool
        if (userStake.isLocked) {
            lockedPool.totalStaked = lockedPool.totalStaked.sub(userStake.amount);
        } else {
            flexiblePool.totalStaked = flexiblePool.totalStaked.sub(userStake.amount);
        }

        // Transfer tokens and rewards to user
        _transfer(address(this), msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```
