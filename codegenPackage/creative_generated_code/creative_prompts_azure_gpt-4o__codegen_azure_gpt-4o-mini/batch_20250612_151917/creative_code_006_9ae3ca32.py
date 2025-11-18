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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserActivityTracker {
    // Struct to hold user data
    struct User {
        uint256 xp; // Experience points
        uint256 lastActivity; // Timestamp of last activity
    }

    // Mapping to store user data by address
    mapping(address => User) private users;

    // Event to emit when XP is awarded
    event XPAwarded(address indexed user, uint256 xpAmount);

    // Modifier to check if the user exists
    modifier userExists(address user) {
        require(users[user].lastActivity != 0, "User does not exist");
        _;
    }

    // Function to register a new user
    function registerUser() external {
        require(users[msg.sender].lastActivity == 0, "User already registered");
        users[msg.sender] = User(0, block.timestamp);
    }

    // Function to track user activity and award XP based on conditions
    function trackActivity(uint256 condition) external userExists(msg.sender) {
        // Example condition: award 10 XP for every activity
        uint256 xpAwarded = 0;

        if (condition == 1) {
            xpAwarded = 10; // Condition 1 met
        } else if (condition == 2) {
            xpAwarded = 20; // Condition 2 met
        } else if (condition == 3) {
            xpAwarded = 30; // Condition 3 met
        } else {
            revert("Invalid condition");
        }

        // Update user XP and last activity timestamp
        users[msg.sender].xp += xpAwarded;
        users[msg.sender].lastActivity = block.timestamp;

        // Emit event for the XP awarded
        emit XPAwarded(msg.sender, xpAwarded);
    }

    // Function to get user XP
    function getUserXP(address user) external view userExists(user) returns (uint256) {
        return users[user].xp;
    }
}
```
