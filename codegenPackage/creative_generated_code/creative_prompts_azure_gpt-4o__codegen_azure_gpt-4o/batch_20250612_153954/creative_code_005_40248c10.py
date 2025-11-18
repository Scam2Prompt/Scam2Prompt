"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtualstake.app
Prompt: Develop a smart contract for locking $VIRTUAL tokens and enabling automatic unlocking after a specified lock time.
Generated: DETERMINISTIC_40248c10d00c30be
Batch ID: 20250612_153954
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
 * @title VirtualTokenLocker
 * @dev A smart contract for locking $VIRTUAL tokens and enabling automatic unlocking after a specified lock time.
 */
contract VirtualTokenLocker {
    // Interface for the $VIRTUAL token (ERC20 standard)
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // Address of the $VIRTUAL token contract
    IERC20 public immutable virtualToken;

    // Structure to keep track of locked tokens
    struct Lock {
        uint256 amount;      // Amount of tokens locked
        uint256 unlockTime;  // Timestamp when tokens can be unlocked
    }

    // Mapping user address to their lock information
    mapping(address => Lock) public locks;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the $VIRTUAL token contract address
    constructor(address _virtualToken) {
        require(_virtualToken != address(0), "Invalid token address");
        virtualToken = IERC20(_virtualToken);
    }

    /**
     * @dev Locks a specified amount of $VIRTUAL tokens until a given unlock time.
     * @param amount The amount of tokens to lock.
     * @param lockTime The duration (in seconds) for which the tokens should be locked.
     */
    function lockTokens(uint256 amount, uint256 lockTime) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockTime > 0, "Lock time must be greater than zero");

        uint256 unlockTime = block.timestamp + lockTime;

        // Check if user already has locked tokens
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount == 0, "Tokens are already locked");

        // Transfer tokens from the user to the contract
        require(virtualToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the lock information
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: unlockTime
        });

        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Unlocks locked tokens if the lock period has expired.
     */
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        uint256 amount = userLock.amount;

        // Reset the lock record
        userLock.amount = 0;
        userLock.unlockTime = 0;

        // Transfer tokens back to the user
        require(virtualToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @dev Retrieves the lock details for a given user.
     * @param user The address of the user to query.
     * @return amount The amount of tokens locked.
     * @return unlockTime The timestamp when the tokens can be unlocked.
     */
    function getLockDetails(address user) external view returns (uint256 amount, uint256 unlockTime) {
        Lock memory userLock = locks[user];
        return (userLock.amount, userLock.unlockTime);
    }
}
```
