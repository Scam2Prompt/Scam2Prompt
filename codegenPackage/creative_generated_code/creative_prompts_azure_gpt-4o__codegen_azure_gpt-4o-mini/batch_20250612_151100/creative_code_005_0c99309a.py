"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Create a function in Solidity to calculate and distribute $FOMO Points after each game or siege, based on user activity and contribution metrics, as detailed in TOCD's reward system.
Generated: DETERMINISTIC_0c99309aadf6b2be
Batch ID: 20250612_151100
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

contract FomoPoints {

    // Struct to hold user information
    struct User {
        uint256 points; // Accumulated FOMO Points
        uint256 activityScore; // Score based on user activity
    }

    // Mapping of user addresses to User struct
    mapping(address => User) private users;

    // Event to emit when points are distributed
    event PointsDistributed(address indexed user, uint256 points);

    // Function to calculate and distribute FOMO Points
    function distributeFomoPoints(address[] calldata participants) external {
        require(participants.length > 0, "No participants provided");

        uint256 totalPoints = calculateTotalPoints(participants);

        // Distributing points based on user activity and contribution
        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            require(participant != address(0), "Invalid address");

            uint256 userPoints = calculateUserPoints(participant);

            // Update user points
            users[participant].points += userPoints;

            // Emit event for each user
            emit PointsDistributed(participant, userPoints);
        }
    }

    // Internal function to calculate total points based on user activity
    function calculateTotalPoints(address[] calldata participants) internal view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < participants.length; i++) {
            total += calculateUserPoints(participants[i]);
        }
        return total;
    }

    // Internal function to calculate points for a single user based on activity score
    function calculateUserPoints(address userAddress) internal view returns (uint256) {
        User storage user = users[userAddress];

        // Example calculation logic; adjust as per your reward system
        return user.activityScore * 10; // For example: 10 points for each activity score unit
    }

    // Function to update user's activity score (can be called by an admin or the user themselves)
    function updateUserActivityScore(address userAddress, uint256 newScore) external {
        require(userAddress != address(0), "Invalid address");
        require(newScore > 0, "Activity score must be positive");

        users[userAddress].activityScore = newScore;
    }

    // Function to fetch user points
    function getUserPoints(address userAddress) external view returns (uint256) {
        require(userAddress != address(0), "Invalid address");
        return users[userAddress].points;
    }
}
```
