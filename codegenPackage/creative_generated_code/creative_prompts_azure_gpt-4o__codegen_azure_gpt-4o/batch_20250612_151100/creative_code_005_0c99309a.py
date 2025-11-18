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

/**
 * @title FOMO Points Distribution
 * @dev This contract calculates and distributes FOMO Points based on user activity and contribution metrics.
 * It is designed for use in a reward system after each game or siege.
 */
contract FomoPointsDistributor {
    // Struct to hold user contribution details
    struct UserContribution {
        uint256 activityScore; // User's activity score
        uint256 contributionScore; // User's contribution score
    }

    // Mapping of user addresses to their contribution details
    mapping(address => UserContribution) public userContributions;

    // Mapping of user addresses to their FOMO Points
    mapping(address => uint256) public fomoPoints;

    /**
     * @dev Sets contribution metrics for a user.
     * @param user The user's wallet address.
     * @param activityScore The user's activity score.
     * @param contributionScore The user's contribution score.
     */
    function setContribution(
        address user,
        uint256 activityScore,
        uint256 contributionScore
    ) external {
        require(user != address(0), "Invalid user address");
        require(activityScore > 0, "Activity score must be greater than 0");
        require(contributionScore > 0, "Contribution score must be greater than 0");

        userContributions[user] = UserContribution(activityScore, contributionScore);
    }

    /**
     * @dev Calculates and distributes FOMO Points based on user metrics.
     * Assumes that the total available FOMO Points is predefined.
     * @param totalFomoPoints Total FOMO Points available for distribution.
     * @param users List of user addresses participating in the game/siege.
     */
    function distributeFomoPoints(uint256 totalFomoPoints, address[] memory users) external {
        require(totalFomoPoints > 0, "Total FOMO Points must be greater than 0");
        require(users.length > 0, "No users provided");

        // Calculate the total contribution weight
        uint256 totalWeight = 0;
        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            UserContribution memory contribution = userContributions[user];
            totalWeight += contribution.activityScore + contribution.contributionScore;
        }

        require(totalWeight > 0, "Total weight must be greater than 0");

        // Distribute FOMO Points to users based on their contribution weight
        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            UserContribution memory contribution = userContributions[user];

            uint256 userWeight = contribution.activityScore + contribution.contributionScore;

            // Calculate FOMO Points for the user
            uint256 userFomoPoints = (userWeight * totalFomoPoints) / totalWeight;

            // Update the user's FOMO Points
            fomoPoints[user] += userFomoPoints;
        }
    }

    /**
     * @dev Retrieves the FOMO Points of a specific user.
     * @param user The user's wallet address.
     * @return The FOMO Points of the user.
     */
    function getFomoPoints(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return fomoPoints[user];
    }
}
```
