"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Generate code for implementing trust and reputation systems in a decentralized application using Linea's zkEVM infrastructure.
Generated: DETERMINISTIC_70c0cb33e6711bb9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Trust and Reputation System
 * @dev Implements a trust and reputation system for decentralized applications using Linea's zkEVM infrastructure.
 * This contract allows users to rate other users and calculate their reputation scores.
 */
contract TrustAndReputation {
    // Struct representing a User's reputation data
    struct Reputation {
        uint256 totalScore; // Sum of all scores given to the user
        uint256 ratingCount; // Number of ratings received
    }

    // Mapping to store reputation data for each user
    mapping(address => Reputation) private reputations;

    // Mapping to track if a user has already rated another user
    mapping(address => mapping(address => bool)) private hasRated;

    // Event emitted when a user rates another user
    event UserRated(address indexed rater, address indexed ratedUser, uint256 score);

    // Modifier to ensure rating score is within valid bounds (e.g., 1-5)
    modifier validScore(uint256 score) {
        require(score >= 1 && score <= 5, "Score must be between 1 and 5");
        _;
    }

    /**
     * @dev Allows a user to rate another user.
     * @param _ratedUser Address of the user being rated.
     * @param _score Rating score given (between 1 and 5).
     */
    function rateUser(address _ratedUser, uint256 _score) external validScore(_score) {
        require(_ratedUser != msg.sender, "You cannot rate yourself");
        require(!hasRated[msg.sender][_ratedUser], "You have already rated this user");

        // Update reputation data for the rated user
        Reputation storage reputation = reputations[_ratedUser];
        reputation.totalScore += _score;
        reputation.ratingCount += 1;

        // Mark this user as having rated the ratedUser
        hasRated[msg.sender][_ratedUser] = true;

        // Emit UserRated event
        emit UserRated(msg.sender, _ratedUser, _score);
    }

    /**
     * @dev Retrieves the average reputation score of a user.
     * @param _user Address of the user whose reputation score is being queried.
     * @return Average reputation score (scaled to 2 decimal places).
     */
    function getReputationScore(address _user) external view returns (uint256) {
        Reputation memory reputation = reputations[_user];
        if (reputation.ratingCount == 0) {
            return 0; // No ratings yet
        }
        // Calculate average score as totalScore / ratingCount
        return (reputation.totalScore * 100) / reputation.ratingCount; // Scaled to 2 decimal places
    }

    /**
     * @dev Resets the reputation data for a user.
     * @param _user Address of the user whose reputation data is being reset.
     */
    function resetReputation(address _user) external {
        require(msg.sender == _user, "You can only reset your own reputation");
        reputations[_user] = Reputation(0, 0);
    }
}
```
