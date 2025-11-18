"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate Solidity code for an EVM-compatible smart contract that supports locking $AI tokens in the Diamond Hands app with multiplier rewards based on lock duration.
Generated: DETERMINISTIC_605139cf6b3be567
Batch ID: 20250612_152439
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

/**
 * @title DiamondHandsAI
 * @dev A smart contract for locking $AI tokens with multiplier rewards based on lock duration.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DiamondHandsAI {
    // Address of the $AI token contract
    IERC20 public immutable aiToken;

    // Struct to store lock information for a user
    struct LockInfo {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
        uint256 multiplier; // Reward multiplier for the lock
    }

    // Mapping of user address to their lock information
    mapping(address => LockInfo) public locks;

    // Multiplier mapping for lock durations (in seconds)
    mapping(uint256 => uint256) public durationMultipliers;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 duration, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _aiToken Address of the $AI token contract.
     */
    constructor(IERC20 _aiToken) {
        require(address(_aiToken) != address(0), "Invalid token address");
        aiToken = _aiToken;

        // Initialize multiplier values for lock durations
        durationMultipliers[30 days] = 105; // 5% reward
        durationMultipliers[90 days] = 115; // 15% reward
        durationMultipliers[180 days] = 130; // 30% reward
        durationMultipliers[365 days] = 150; // 50% reward
    }

    /**
     * @dev Lock $AI tokens for a specific duration to earn rewards.
     * @param _amount Amount of tokens to lock.
     * @param _duration Lock duration in seconds (must match a predefined duration).
     */
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Lock amount must be greater than zero");
        require(durationMultipliers[_duration] > 0, "Invalid lock duration");
        require(locks[msg.sender].amount == 0, "Existing lock must be unlocked first");

        uint256 unlockTime = block.timestamp + _duration;
        uint256 multiplier = durationMultipliers[_duration];

        // Transfer tokens from the user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update lock information for the user
        locks[msg.sender] = LockInfo(_amount, unlockTime, multiplier);

        emit TokensLocked(msg.sender, _amount, _duration, multiplier);
    }

    /**
     * @dev Unlock tokens and claim rewards after the lock duration.
     */
    function unlockTokens() external {
        LockInfo memory userLock = locks[msg.sender];

        require(userLock.amount > 0, "No tokens to unlock");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Calculate reward based on multiplier
        uint256 reward = (userLock.amount * userLock.multiplier) / 100;
        uint256 totalAmount = userLock.amount + reward;

        // Reset user lock data
        delete locks[msg.sender];

        // Transfer tokens and rewards back to the user
        require(aiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, userLock.amount, reward);
    }

    /**
     * @dev Retrieve lock details for a specific user.
     * @param _user Address of the user to query.
     * @return LockInfo struct containing lock details.
     */
    function getLockInfo(address _user) external view returns (LockInfo memory) {
        return locks[_user];
    }
}
```
