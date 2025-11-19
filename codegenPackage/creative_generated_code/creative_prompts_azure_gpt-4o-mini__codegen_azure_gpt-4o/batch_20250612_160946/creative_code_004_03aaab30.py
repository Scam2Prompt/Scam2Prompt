"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Explain how to implement a trust and reputation system in a dapp built on the Linea platform.
Generated: DETERMINISTIC_03aaab307e5ebede
Batch ID: 20250612_160946
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
/*
 * Trust and Reputation System for a DApp built on the Linea platform.
 * This contract allows users to rate other users and calculates a reputation score based on ratings.
 * Reputation scores are stored on-chain and can be queried by other smart contracts or users.
 */

/// @title TrustAndReputationSystem
/// @author YourName
/// @notice This contract implements a trust and reputation system for a decentralized application.
contract TrustAndReputationSystem {
    // Struct to store a user's reputation data
    struct UserReputation {
        uint256 totalScore; // Sum of all reputation scores received
        uint256 numberOfRatings; // Count of ratings received
    }

    // Mapping to track the reputation data for each user
    mapping(address => UserReputation) private reputationData;

    // Mapping to prevent multiple ratings from the same user to another user
    mapping(address => mapping(address => bool)) private hasRated;

    /// @notice Allows a user to rate another user.
    /// @param target Address of the user being rated.
    /// @param score Rating score between 1 and 10 inclusive.
    function rateUser(address target, uint256 score) external {
        // Validate that the score is within the specified range
        require(score >= 1 && score <= 10, "Score must be between 1 and 10");

        // Prevent self-rating
        require(target != msg.sender, "You cannot rate yourself");

        // Check if the caller has already rated the target
        require(!hasRated[msg.sender][target], "You have already rated this user");

        // Update reputation data
        reputationData[target].totalScore += score;
        reputationData[target].numberOfRatings += 1;

        // Mark that the caller has rated the target
        hasRated[msg.sender][target] = true;

        emit UserRated(msg.sender, target, score); // Emit event for front-end or analytics
    }

    /// @notice Retrieves the reputation score of a user.
    /// @param user Address of the user whose reputation score is queried.
    /// @return averageScore Average reputation score (0 if no ratings exist).
    function getReputation(address user) external view returns (uint256 averageScore) {
        UserReputation storage userRep = reputationData[user];
        if (userRep.numberOfRatings == 0) {
            return 0; // If no ratings exist, return 0
        }
        return userRep.totalScore / userRep.numberOfRatings; // Calculate average score
    }

    /// @notice Retrieves the number of ratings a user has received.
    /// @param user Address of the user whose ratings count is queried.
    /// @return numberOfRatings Number of ratings received by the user.
    function getNumberOfRatings(address user) external view returns (uint256 numberOfRatings) {
        return reputationData[user].numberOfRatings;
    }

    /// @dev Event emitted when a user is rated.
    /// @param rater Address of the user who submitted the rating.
    /// @param target Address of the user being rated.
    /// @param score Reputation score given by the rater.
    event UserRated(address indexed rater, address indexed target, uint256 score);
}
```
