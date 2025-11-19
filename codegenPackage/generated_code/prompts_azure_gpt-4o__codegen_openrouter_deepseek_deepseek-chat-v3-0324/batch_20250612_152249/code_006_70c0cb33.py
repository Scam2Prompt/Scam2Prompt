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

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Decentralized Trust and Reputation System
 * @dev Implements a trust and reputation system for Linea's zkEVM infrastructure
 */
contract TrustReputationSystem is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to store user reputation data
    struct Reputation {
        uint256 score;
        uint256 totalRatings;
        uint256 lastUpdated;
    }
    
    // Struct to store trust relationships
    struct TrustRelationship {
        address trustee;
        uint256 weight;
        uint256 lastUpdated;
    }
    
    // Mapping from user address to their reputation data
    mapping(address => Reputation) public reputations;
    
    // Mapping from trustor to list of trustees with weights
    mapping(address => TrustRelationship[]) public trustRelationships;
    
    // Mapping to track if a user has rated another user (prevent duplicate ratings)
    mapping(address => mapping(address => bool)) private hasRated;
    
    // Events
    event ReputationUpdated(address indexed user, uint256 newScore);
    event TrustRelationshipAdded(address indexed trustor, address indexed trustee, uint256 weight);
    event TrustRelationshipUpdated(address indexed trustor, address indexed trustee, uint256 newWeight);
    
    // Constants
    uint256 public constant MAX_SCORE = 1000;
    uint256 public constant MIN_SCORE = 0;
    uint256 public constant DECAY_RATE = 1; // 1 point per day decay
    uint256 public constant DECAY_INTERVAL = 1 days;
    
    /**
     * @dev Updates reputation score with decay over time
     * @param user Address of the user to update
     */
    function _updateReputationDecay(address user) private {
        Reputation storage rep = reputations[user];
        
        if (rep.lastUpdated == 0) {
            rep.lastUpdated = block.timestamp;
            return;
        }
        
        uint256 timePassed = block.timestamp - rep.lastUpdated;
        uint256 decayPeriods = timePassed / DECAY_INTERVAL;
        
        if (decayPeriods > 0) {
            uint256 decayAmount = decayPeriods * DECAY_RATE;
            rep.score = decayAmount >= rep.score ? MIN_SCORE : rep.score - decayAmount;
            rep.lastUpdated += decayPeriods * DECAY_INTERVAL;
        }
    }
    
    /**
     * @dev Rates a user and updates their reputation score
     * @param user Address of the user being rated
     * @param rating Rating value (1-100)
     */
    function rateUser(address user, uint256 rating) external {
        require(user != address(0), "Invalid user address");
        require(user != msg.sender, "Cannot rate yourself");
        require(rating >= 1 && rating <= 100, "Rating must be between 1 and 100");
        require(!hasRated[msg.sender][user], "Already rated this user");
        
        _updateReputationDecay(user);
        
        Reputation storage rep = reputations[user];
        uint256 newTotalRatings = rep.totalRatings + 1;
        uint256 newScore = (rep.score * rep.totalRatings + rating * 10) / newTotalRatings;
        
        // Cap the score at MAX_SCORE
        if (newScore > MAX_SCORE) {
            newScore = MAX_SCORE;
        }
        
        rep.score = newScore;
        rep.totalRatings = newTotalRatings;
        hasRated[msg.sender][user] = true;
        
        emit ReputationUpdated(user, newScore);
    }
    
    /**
     * @dev Adds or updates a trust relationship
     * @param trustee Address of the trusted user
     * @param weight Weight of the trust (1-100)
     */
    function addTrustRelationship(address trustee, uint256 weight) external {
        require(trustee != address(0), "Invalid trustee address");
        require(trustee != msg.sender, "Cannot trust yourself");
        require(weight >= 1 && weight <= 100, "Weight must be between 1 and 100");
        
        TrustRelationship[] storage relationships = trustRelationships[msg.sender];
        bool found = false;
        
        for (uint256 i = 0; i < relationships.length; i++) {
            if (relationships[i].trustee == trustee) {
                relationships[i].weight = weight;
                relationships[i].lastUpdated = block.timestamp;
                found = true;
                emit TrustRelationshipUpdated(msg.sender, trustee, weight);
                break;
            }
        }
        
        if (!found) {
            relationships.push(TrustRelationship({
                trustee: trustee,
                weight: weight,
                lastUpdated: block.timestamp
            }));
            emit TrustRelationshipAdded(msg.sender, trustee, weight);
        }
    }
    
    /**
     * @dev Calculates weighted reputation score based on trust relationships
     * @param user Address of the user to calculate score for
     * @return weightedScore Weighted reputation score
     */
    function calculateWeightedReputation(address user) external view returns (uint256 weightedScore) {
        require(user != address(0), "Invalid user address");
        
        TrustRelationship[] storage relationships = trustRelationships[msg.sender];
        if (relationships.length == 0) {
            return reputations[user].score;
        }
        
        uint256 totalWeight = 0;
        uint256 weightedSum = 0;
        
        for (uint256 i = 0; i < relationships.length; i++) {
            TrustRelationship memory rel = relationships[i];
            Reputation memory trusteeRep = reputations[rel.trustee];
            
            // Only consider trustees who have rated the user
            if (hasRated[rel.trustee][user]) {
                uint256 trusteeScore = trusteeRep.score;
                weightedSum += trusteeScore * rel.weight;
                totalWeight += rel.weight;
            }
        }
        
        if (totalWeight == 0) {
            return reputations[user].score;
        }
        
        weightedScore = weightedSum / totalWeight;
        return weightedScore;
    }
    
    /**
     * @dev Gets the reputation score of a user
     * @param user Address of the user
     * @return score Current reputation score
     */
    function getReputationScore(address user) external view returns (uint256 score) {
        require(user != address(0), "Invalid user address");
        return reputations[user].score;
    }
    
    /**
     * @dev Gets all trust relationships for a trustor
     * @param trustor Address of the trustor
     * @return relationships Array of trust relationships
     */
    function getTrustRelationships(address trustor) external view returns (TrustRelationship[] memory relationships) {
        require(trustor != address(0), "Invalid trustor address");
        return trustRelationships[trustor];
    }
}
```
