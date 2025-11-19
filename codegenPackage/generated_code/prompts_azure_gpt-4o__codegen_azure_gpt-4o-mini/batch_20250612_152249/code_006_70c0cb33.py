"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: Generate code for implementing trust and reputation systems in a decentralized application using Linea's zkEVM infrastructure.
Generated: DETERMINISTIC_70c0cb33e6711bb9
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Trust and Reputation System for a Decentralized Application
contract TrustReputationSystem is Ownable {
    using SafeMath for uint256;

    // Struct to hold user reputation data
    struct UserReputation {
        uint256 trustScore; // Trust score of the user
        uint256 totalReviews; // Total number of reviews received
        mapping(address => bool) hasReviewed; // Track if a user has reviewed
    }

    // Mapping of user addresses to their reputation data
    mapping(address => UserReputation) private userReputations;

    // Event emitted when a review is submitted
    event ReviewSubmitted(address indexed reviewer, address indexed reviewedUser, uint256 score);

    // Function to submit a review for a user
    // score: The score given by the reviewer (1 to 5)
    function submitReview(address _reviewedUser, uint256 _score) external {
        require(_reviewedUser != msg.sender, "You cannot review yourself");
        require(_score >= 1 && _score <= 5, "Score must be between 1 and 5");
        require(!userReputations[_reviewedUser].hasReviewed[msg.sender], "You have already reviewed this user");

        // Update the reviewed user's reputation
        UserReputation storage reputation = userReputations[_reviewedUser];
        reputation.trustScore = reputation.trustScore.add(_score);
        reputation.totalReviews = reputation.totalReviews.add(1);
        reputation.hasReviewed[msg.sender] = true;

        emit ReviewSubmitted(msg.sender, _reviewedUser, _score);
    }

    // Function to get the trust score of a user
    // Returns the trust score and total reviews
    function getTrustScore(address _user) external view returns (uint256 trustScore, uint256 totalReviews) {
        UserReputation storage reputation = userReputations[_user];
        return (reputation.trustScore, reputation.totalReviews);
    }

    // Function to reset a user's reputation (only owner can call)
    function resetUserReputation(address _user) external onlyOwner {
        delete userReputations[_user];
    }

    // Function to check if a user has reviewed another user
    function hasReviewed(address _reviewedUser) external view returns (bool) {
        return userReputations[_reviewedUser].hasReviewed[msg.sender];
    }
}
```
