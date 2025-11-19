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

contract MajorRewards {
    // Struct to hold information about each MAJOR owner
    struct MajorOwner {
        uint256 totalActivity; // Total activity points accumulated
        uint256 rewardPoints;  // Total reward points earned
    }

    // Mapping to store MajorOwner data by address
    mapping(address => MajorOwner) private majorOwners;

    // Event to emit when rewards are calculated
    event RewardsCalculated(address indexed owner, uint256 rewardPoints);

    // Function to record activity for a MAJOR owner
    function recordActivity(address owner, uint256 activityPoints) external {
        require(owner != address(0), "Invalid address");
        require(activityPoints > 0, "Activity points must be greater than zero");

        // Update the total activity points for the owner
        majorOwners[owner].totalActivity += activityPoints;
    }

    // Function to calculate rewards based on activity
    function calculateRewards(address owner) external {
        require(owner != address(0), "Invalid address");
        
        MajorOwner storage ownerData = majorOwners[owner];
        
        // Ensure the owner has activity recorded
        require(ownerData.totalActivity > 0, "No activity recorded for this owner");

        // Calculate rewards based on total activity (1 reward point per 10 activity points)
        uint256 newRewardPoints = ownerData.totalActivity / 10;

        // Update the owner's reward points
        ownerData.rewardPoints += newRewardPoints;

        // Emit an event for the calculated rewards
        emit RewardsCalculated(owner, newRewardPoints);
    }

    // Function to retrieve the reward points of a MAJOR owner
    function getRewardPoints(address owner) external view returns (uint256) {
        require(owner != address(0), "Invalid address");
        return majorOwners[owner].rewardPoints;
    }

    // Function to retrieve the total activity of a MAJOR owner
    function getTotalActivity(address owner) external view returns (uint256) {
        require(owner != address(0), "Invalid address");
        return majorOwners[owner].totalActivity;
    }
}
```
