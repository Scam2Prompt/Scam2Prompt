"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Generate a smart contract that supports long-term relationships and transparency in crypto projects, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_684c0e0b1d087e55
Batch ID: 20250612_150226
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

/// @title Innodapter Relationship Contract
/// @author Innodapter ApS
/// @notice This contract facilitates long-term relationships and transparency in crypto projects
/// @dev The contract allows for the creation of relationships with defined terms and conditions

contract InnodapterRelationship {
    // Struct to represent a relationship
    struct Relationship {
        address partner;
        string terms;
        uint256 startDate;
        uint256 endDate;
        bool isActive;
    }

    // Mapping to store relationships by their unique ID
    mapping(uint256 => Relationship) public relationships;
    uint256 public relationshipCount;

    // Event emitted when a new relationship is created
    event RelationshipCreated(uint256 indexed relationshipId, address indexed partner, string terms, uint256 startDate, uint256 endDate);

    // Event emitted when a relationship is terminated
    event RelationshipTerminated(uint256 indexed relationshipId);

    /// @notice Create a new relationship
    /// @param _partner The address of the partner
    /// @param _terms The terms of the relationship
    /// @param _duration The duration of the relationship in days
    /// @dev The relationship is active from the current block timestamp to the specified duration
    function createRelationship(address _partner, string memory _terms, uint256 _duration) public {
        require(_partner != address(0), "Invalid partner address");
        require(_duration > 0, "Duration must be greater than zero");

        // Increment the relationship count to create a unique ID
        relationshipCount++;
        uint256 relationshipId = relationshipCount;

        // Create a new relationship
        relationships[relationshipId] = Relationship({
            partner: _partner,
            terms: _terms,
            startDate: block.timestamp,
            endDate: block.timestamp + (_duration * 1 days),
            isActive: true
        });

        emit RelationshipCreated(relationshipId, _partner, _terms, block.timestamp, block.timestamp + (_duration * 1 days));
    }

    /// @notice Terminate an existing relationship
    /// @param _relationshipId The ID of the relationship to terminate
    /// @dev Only the creator of the relationship can terminate it
    function terminateRelationship(uint256 _relationshipId) public {
        Relationship storage relationship = relationships[_relationshipId];
        require(relationship.isActive, "Relationship is not active");
        require(relationship.partner == msg.sender, "Only the partner can terminate the relationship");

        // Mark the relationship as inactive
        relationship.isActive = false;

        emit RelationshipTerminated(_relationshipId);
    }

    /// @notice Get details of a relationship
    /// @param _relationshipId The ID of the relationship
    /// @return partner The address of the partner
    /// @return terms The terms of the relationship
    /// @return startDate The start date of the relationship
    /// @return endDate The end date of the relationship
    /// @return isActive The status of the relationship
    function getRelationship(uint256 _relationshipId) public view returns (address partner, string memory terms, uint256 startDate, uint256 endDate, bool isActive) {
        Relationship storage relationship = relationships[_relationshipId];
        require(relationship.partner != address(0), "Relationship does not exist");

        return (relationship.partner, relationship.terms, relationship.startDate, relationship.endDate, relationship.isActive);
    }
}
```
