"""
Generated Code Metadata:
========================
Original URL: https://lynexfl.org
Prompt: Describe the process of locking LYNX tokens to receive veLYNX and how it affects voting for liquidity pools on Lynex.
Generated: DETERMINISTIC_b3d8b8332eb5edca
Batch ID: 20250612_160309
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
import "@openzeppelin/contracts/utils/math/Math.sol";

/**
 * @title veLYNX Token Locking Contract
 * @dev Allows users to lock LYNX tokens to receive veLYNX for voting on liquidity pools
 */
contract VeLynx is ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Lock {
        uint256 amount;
        uint256 unlockTime;
    }

    IERC20 public immutable lynxToken;
    uint256 public constant MIN_LOCK_TIME = 1 weeks;
    uint256 public constant MAX_LOCK_TIME = 4 * 365 days;
    uint256 public totalLocked;

    mapping(address => Lock) public locks;
    mapping(address => uint256) public votingPower;

    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event VotingPowerUpdated(address indexed user, uint256 votingPower);

    constructor(address _lynxToken) {
        require(_lynxToken != address(0), "Invalid token address");
        lynxToken = IERC20(_lynxToken);
    }

    /**
     * @dev Lock LYNX tokens to receive veLYNX voting power
     * @param amount Amount of LYNX tokens to lock
     * @param lockDuration Duration to lock tokens for (in seconds)
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lockDuration >= MIN_LOCK_TIME && lockDuration <= MAX_LOCK_TIME, "Invalid lock duration");
        
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount == 0, "Existing lock found");

        uint256 unlockTime = block.timestamp + lockDuration;
        userLock.amount = amount;
        userLock.unlockTime = unlockTime;
        totalLocked += amount;

        // Calculate voting power based on lock duration
        uint256 power = calculateVotingPower(amount, lockDuration);
        votingPower[msg.sender] = power;

        lynxToken.safeTransferFrom(msg.sender, address(this), amount);

        emit TokensLocked(msg.sender, amount, unlockTime);
        emit VotingPowerUpdated(msg.sender, power);
    }

    /**
     * @dev Withdraw locked LYNX tokens after unlock time
     */
    function withdrawTokens() external nonReentrant {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens still locked");

        uint256 amount = userLock.amount;
        totalLocked -= amount;

        // Reset user's lock and voting power
        delete locks[msg.sender];
        uint256 oldPower = votingPower[msg.sender];
        votingPower[msg.sender] = 0;

        lynxToken.safeTransfer(msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
        emit VotingPowerUpdated(msg.sender, 0);
    }

    /**
     * @dev Calculate voting power based on amount and lock duration
     * @param amount Amount of LYNX tokens
     * @param duration Lock duration in seconds
     * @return votingPower Calculated voting power
     */
    function calculateVotingPower(uint256 amount, uint256 duration) public pure returns (uint256) {
        // Linear voting power calculation based on lock duration
        // Max multiplier is 4 for 4 year lock
        uint256 multiplier = Math.min(4 * 1e18, (duration * 1e18) / (365 days));
        return (amount * multiplier) / 1e18;
    }

    /**
     * @dev Vote for a liquidity pool using veLYNX voting power
     * @param poolId ID of the liquidity pool to vote for
     * @param amount Amount of voting power to allocate
     */
    function voteForPool(uint256 poolId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(votingPower[msg.sender] >= amount, "Insufficient voting power");

        // In a real implementation, this would interact with the gauge system
        // For this example, we just deduct the voting power
        votingPower[msg.sender] -= amount;
        
        // Pool voting logic would go here
        // emit VoteCast(msg.sender, poolId, amount);
    }
}
```
