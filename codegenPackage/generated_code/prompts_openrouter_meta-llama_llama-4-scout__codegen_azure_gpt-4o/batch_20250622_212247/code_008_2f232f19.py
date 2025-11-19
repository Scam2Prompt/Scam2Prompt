"""
Generated Code Metadata:
========================
Original URL: https://major-achievements.top
Prompt: Create a function in Solidity to calculate rewards for MAJOR owners based on their activity in the Major game on Telegram.
Generated: DETERMINISTIC_2f232f1944402234
Batch ID: 20250622_212247
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

/**
 * @title MajorGameRewards
 * @dev A contract to calculate rewards for MAJOR owners based on their activity in the Major game on Telegram.
 */
contract MajorGameRewards {
    // Mapping to store user activity points
    mapping(address => uint256) private activityPoints;

    // Mapping to store user rewards
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are calculated
    event RewardsCalculated(address indexed user, uint256 reward);

    // Modifier to ensure valid input
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Function to update activity points for a user.
     * @param user The address of the user.
     * @param points The number of activity points to add.
     */
    function updateActivityPoints(address user, uint256 points) external validAddress(user) {
        require(points > 0, "Points must be greater than zero");
        activityPoints[user] += points;
    }

    /**
     * @dev Function to calculate rewards based on activity points.
     * @param user The address of the user.
     * @return reward The calculated reward for the user.
     */
    function calculateRewards(address user) external validAddress(user) returns (uint256 reward) {
        uint256 points = activityPoints[user];
        require(points > 0, "No activity points available");

        // Example reward calculation logic: 1 reward per 10 activity points
        reward = points / 10;

        // Update rewards mapping
        rewards[user] += reward;

        // Reset activity points after reward calculation
        activityPoints[user] = 0;

        // Emit event
        emit RewardsCalculated(user, reward);

        return reward;
    }

    /**
     * @dev Function to get the current reward balance of a user.
     * @param user The address of the user.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) external view validAddress(user) returns (uint256) {
        return rewards[user];
    }

    /**
     * @dev Function to get the current activity points of a user.
     * @param user The address of the user.
     * @return The activity points of the user.
     */
    function getActivityPoints(address user) external view validAddress(user) returns (uint256) {
        return activityPoints[user];
    }
}
```
