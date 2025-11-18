"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodromefinancedapps.web.app
Prompt: Write a smart contract to lock AERO tokens and convert them into veAERO, enabling voting on token emissions and fee distribution.
Generated: DETERMINISTIC_aa51a2a426f28803
Batch ID: 20250612_154215
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
 * @title AeroTokenLocker
 * @dev Smart contract to lock AERO tokens and convert them into veAERO tokens.
 *      veAERO tokens enable voting on token emissions and fee distribution.
 */
contract AeroTokenLocker {
    // State variables
    IERC20 public immutable AERO; // Reference to the AERO token contract
    IERC20 public immutable veAERO; // Reference to the veAERO token contract

    mapping(address => uint256) public lockedBalances; // Tracks AERO tokens locked by each user
    mapping(address => uint256) public unlockTimes; // Tracks unlock time for each user

    uint256 public constant MIN_LOCK_DURATION = 1 weeks; // Minimum lock duration
    uint256 public constant MAX_LOCK_DURATION = 1 years; // Maximum lock duration

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize token contracts.
     * @param _AERO Address of the AERO token contract.
     * @param _veAERO Address of the veAERO token contract.
     */
    constructor(IERC20 _AERO, IERC20 _veAERO) {
        require(address(_AERO) != address(0), "Invalid AERO token address");
        require(address(_veAERO) != address(0), "Invalid veAERO token address");

        AERO = _AERO;
        veAERO = _veAERO;
    }

    /**
     * @dev Locks AERO tokens and mints veAERO tokens.
     * @param amount Amount of AERO tokens to lock.
     * @param duration Duration for locking tokens (must be between MIN_LOCK_DURATION and MAX_LOCK_DURATION).
     */
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration >= MIN_LOCK_DURATION && duration <= MAX_LOCK_DURATION, "Invalid lock duration");

        uint256 unlockTime = block.timestamp + duration;

        // Update state
        lockedBalances[msg.sender] += amount;
        unlockTimes[msg.sender] = unlockTime;

        // Transfer AERO tokens to the contract
        require(AERO.transferFrom(msg.sender, address(this), amount), "AERO transfer failed");

        // Mint veAERO tokens to the user (1:1 ratio for simplicity)
        require(veAERO.transfer(msg.sender, amount), "veAERO minting failed");

        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Unlocks AERO tokens after the lock duration has passed.
     */
    function unlockTokens() external {
        uint256 lockedAmount = lockedBalances[msg.sender];
        require(lockedAmount > 0, "No locked tokens to unlock");
        require(block.timestamp >= unlockTimes[msg.sender], "Tokens are still locked");

        // Reset state
        lockedBalances[msg.sender] = 0;
        unlockTimes[msg.sender] = 0;

        // Burn veAERO tokens (1:1 ratio for simplicity)
        require(veAERO.transferFrom(msg.sender, address(this), lockedAmount), "veAERO burn failed");

        // Transfer AERO tokens back to the user
        require(AERO.transfer(msg.sender, lockedAmount), "AERO transfer failed");

        emit TokensUnlocked(msg.sender, lockedAmount);
    }

    /**
     * @dev Returns the details of locked tokens for a user.
     * @param user Address of the user.
     * @return lockedAmount Amount of AERO tokens locked.
     * @return unlockTime Timestamp when tokens will unlock.
     */
    function getLockDetails(address user) external view returns (uint256 lockedAmount, uint256 unlockTime) {
        lockedAmount = lockedBalances[user];
        unlockTime = unlockTimes[user];
    }
}

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
