"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank-xp.pages.dev
Prompt: Create a smart contract snippet that tracks user activity and awards XP based on conditions like those outlined on DeBank XP.
Generated: DETERMINISTIC_9ae3ca326f38ce9d
Batch ID: 20250612_151917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a smart contract written in Solidity that tracks user activity and awards XP based on specific conditions.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title UserActivityTracker
 * @dev A smart contract to track user activity and award XP based on certain conditions.
 */
contract UserActivityTracker {
    // Track user XP
    mapping(address => uint256) private userXP;

    // Track last activity timestamp for users
    mapping(address => uint256) private lastActivity;

    // Constant XP points for specific activities
    uint256 public constant LOGIN_XP = 10; // Award for logging in
    uint256 public constant TRANSACTION_XP = 25; // Award for completing a transaction
    uint256 public constant DAILY_ACTIVE_XP = 50; // Award for daily active users

    // Event emitted whenever XP is awarded
    event XP_Awarded(address indexed user, uint256 xp);

    /**
     * @dev Modifier to ensure a valid address is provided.
     */
    modifier validAddress(address user) {
        require(user != address(0), "Invalid user address");
        _;
    }

    /**
     * @dev Modifier to ensure the caller is the same as the user being tracked.
     */
    modifier onlySelf(address user) {
        require(msg.sender == user, "Caller is not the user");
        _;
    }

    /**
     * @dev Function to log user activity and award XP for logging in.
     * @param user The address of the user.
     */
    function logActivity(address user) external validAddress(user) onlySelf(user) {
        uint256 currentTimestamp = block.timestamp;

        // Award XP for logging in
        userXP[user] += LOGIN_XP;
        emit XP_Awarded(user, LOGIN_XP);

        // Check if the user is active daily; award daily active XP
        if (lastActivity[user] != 0 && (currentTimestamp - lastActivity[user] >= 1 days)) {
            userXP[user] += DAILY_ACTIVE_XP;
            emit XP_Awarded(user, DAILY_ACTIVE_XP);
        }

        // Update the last activity timestamp
        lastActivity[user] = currentTimestamp;
    }

    /**
     * @dev Function to award XP for completing a transaction.
     * @param user The address of the user.
     */
    function completeTransaction(address user) external validAddress(user) onlySelf(user) {
        userXP[user] += TRANSACTION_XP;
        emit XP_Awarded(user, TRANSACTION_XP);
    }

    /**
     * @dev Function to retrieve the current XP of a user.
     * @param user The address of the user.
     * @return The total XP of the user.
     */
    function getUserXP(address user) external view validAddress(user) returns (uint256) {
        return userXP[user];
    }
}
```
