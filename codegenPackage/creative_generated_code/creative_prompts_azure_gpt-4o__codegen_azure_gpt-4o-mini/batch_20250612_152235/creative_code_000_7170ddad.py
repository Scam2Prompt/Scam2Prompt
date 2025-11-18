"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megadrop-bouncebit.pages.dev
Prompt: Write a smart contract in Solidity to implement a leaderboard system for tracking user points in a blockchain-based rewards program, similar to Points Paradise.
Generated: DETERMINISTIC_7170ddadea96554e
Batch ID: 20250612_152235
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

contract Leaderboard {
    // Structure to hold user information
    struct User {
        uint256 points;
        uint256 rank;
    }

    // Mapping from user address to User struct
    mapping(address => User) private users;

    // A list of user addresses for ranking purposes
    address[] private userList;

    // Event emitted when points are updated
    event PointsUpdated(address indexed user, uint256 newPoints);

    // Function to add or update user points
    function updatePoints(address user, uint256 points) external {
        require(user != address(0), "Invalid user address");
        require(points >= 0, "Points cannot be negative");

        // Update the user's points
        if (users[user].points == 0) {
            // New user, add to user list
            userList.push(user);
        }
        users[user].points += points;

        emit PointsUpdated(user, users[user].points);

        // Recalculate ranks
        _recalculateRanks();
    }

    // Internal function to recalculate user ranks based on points
    function _recalculateRanks() internal {
        // Sort users by points
        uint256 userCount = userList.length;
        for (uint256 i = 0; i < userCount; i++) {
            for (uint256 j = i + 1; j < userCount; j++) {
                if (users[userList[i]].points < users[userList[j]].points) {
                    // Swap users in the user list
                    address temp = userList[i];
                    userList[i] = userList[j];
                    userList[j] = temp;
                }
            }
        }

        // Assign ranks based on the sorted list
        for (uint256 i = 0; i < userCount; i++) {
            users[userList[i]].rank = i + 1; // Rank starts from 1
        }
    }

    // Function to get user points
    function getUserPoints(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return users[user].points;
    }

    // Function to get user rank
    function getUserRank(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return users[user].rank;
    }

    // Function to get the top N users on the leaderboard
    function getTopUsers(uint256 n) external view returns (address[] memory) {
        require(n > 0, "Number of users must be greater than 0");
        require(n <= userList.length, "Not enough users");

        address[] memory topUsers = new address[](n);
        for (uint256 i = 0; i < n; i++) {
            topUsers[i] = userList[i];
        }
        return topUsers;
    }
}
```
