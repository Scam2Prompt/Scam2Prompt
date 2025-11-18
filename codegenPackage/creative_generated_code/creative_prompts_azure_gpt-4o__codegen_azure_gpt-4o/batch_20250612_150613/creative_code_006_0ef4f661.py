"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-stakestone.pages.dev
Prompt: Create a smart contract that supports STONE token integration for liquidity incentives by locking LP tokens from StakeStone's STONE-Fi protocols.
Generated: DETERMINISTIC_0ef4f661c7e5a488
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready Solidity code for the requested smart contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title StoneLiquidityIncentive
 * @notice This contract enables locking LP tokens from StakeStone's STONE-Fi protocols to earn STONE token liquidity incentives.
 */
contract StoneLiquidityIncentive {
    // Address of the STONE token
    IERC20 public immutable stoneToken;

    // Struct to represent a locked liquidity position
    struct LiquidityLock {
        uint256 amount;        // Amount of LP tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be withdrawn
        bool claimed;          // Incentives claiming status
    }

    // Mapping to track liquidity locks for users
    mapping(address => LiquidityLock[]) public userLocks;

    // LP token interface
    IERC20 public immutable lpToken;

    // Incentive rate in STONE tokens per LP token (per second)
    uint256 public immutable incentiveRate;

    // Events
    event LiquidityLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event IncentivesClaimed(address indexed user, uint256 amount);
    event LiquidityWithdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stoneToken, IERC20 _lpToken, uint256 _incentiveRate) {
        require(address(_stoneToken) != address(0), "Invalid STONE token address");
        require(address(_lpToken) != address(0), "Invalid LP token address");
        require(_incentiveRate > 0, "Incentive rate must be greater than zero");
        
        stoneToken = _stoneToken;
        lpToken = _lpToken;
        incentiveRate = _incentiveRate;
    }

    /**
     * @notice Lock LP tokens to earn STONE liquidity incentives.
     * @param amount The amount of LP tokens to lock.
     * @param duration The duration (in seconds) for which the tokens will be locked.
     */
    function lockLiquidity(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer LP tokens from the user to the contract
        require(lpToken.transferFrom(msg.sender, address(this), amount), "LP token transfer failed");

        // Record the lock
        userLocks[msg.sender].push(LiquidityLock(amount, block.timestamp + duration, false));

        emit LiquidityLocked(msg.sender, amount, block.timestamp + duration);
    }

    /**
     * @notice Claim STONE token incentives for a specific lock position.
     * @param lockIndex The index of the lock to claim incentives for.
     */
    function claimIncentives(uint256 lockIndex) external {
        require(lockIndex < userLocks[msg.sender].length, "Invalid lock index");

        LiquidityLock storage lock = userLocks[msg.sender][lockIndex];
        require(!lock.claimed, "Incentives already claimed");
        require(block.timestamp >= lock.unlockTime, "Lock period not yet over");

        // Calculate incentives
        uint256 duration = lock.unlockTime - (block.timestamp - lock.unlockTime); // Lock duration calculation
        uint256 incentives = duration * incentiveRate * lock.amount;

        // Transfer incentives
        require(stoneToken.transfer(msg.sender, incentives), "STONE token transfer failed");

        // Mark as claimed
        lock.claimed = true;

        emit IncentivesClaimed(msg.sender, incentives);
    }

    /**
     * @notice Withdraw locked LP tokens after the lock period has ended.
     * @param lockIndex The index of the lock to withdraw.
     */
    function withdrawLiquidity(uint256 lockIndex) external {
        require(lockIndex < userLocks[msg.sender].length, "Invalid lock index");

        LiquidityLock storage lock = userLocks[msg.sender][lockIndex];
        require(block.timestamp >= lock.unlockTime, "Lock period not yet over");
        require(!lock.claimed, "Already withdrawn");

        uint256 amount = lock.amount;

        // Transfer LP tokens back to the user
        require(lpToken.transfer(msg.sender, amount), "LP token transfer failed");

        // Mark as withdrawn
        lock.claimed = true;

        emit LiquidityWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Get the number of locks for a user.
     * @param user The address of the user.
     * @return The number of locks.
     */
    function getLockCount(address user) external view returns (uint256) {
        return userLocks[user].length;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

This contract is structured to integrate STONE token incentives with LP token locking securely and efficiently. Make sure to deploy this contract on a test environment and audit it thoroughly before moving to production.
