"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: "Write a smart contract for a blockchain-based solution using Solidity, incorporating the concepts of proof-of-concept and full stack development."
Generated: DETERMINISTIC_d5f0193c99f11641
Batch ID: 20250622_210650
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

/// @title A Simple Voting Smart Contract
/// @author Your Name
/// @notice This contract allows users to create and participate in a voting process
/// @dev This is a proof-of-concept implementation for educational purposes

contract Voting {
    // Struct to represent a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping to store candidates
    mapping(uint => Candidate) public candidates;
    // Mapping to track whether an address has voted
    mapping(address => bool) public voters;
    // Total number of candidates
    uint public candidatesCount;
    // Event to emit when a vote is cast
    event Voted(uint indexed candidateId);

    /// @notice Constructor to initialize the contract with candidates
    constructor(string[] memory candidateNames) {
        require(candidateNames.length > 0, "At least one candidate is required");
        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    /// @notice Function to add a candidate
    /// @param name The name of the candidate
    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
    }

    /// @notice Function to vote for a candidate
    /// @param candidateId The ID of the candidate to vote for
    /// @dev Reverts if the candidate ID is invalid or if the voter has already voted
    function vote(uint candidateId) public {
        require(!voters[msg.sender], "You have already voted");
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");

        // Record that the voter has voted
        voters[msg.sender] = true;
        // Increment the vote count for the candidate
        candidates[candidateId].voteCount++;

        // Emit the Voted event
        emit Voted(candidateId);
    }

    /// @notice Function to get the vote count of a candidate
    /// @param candidateId The ID of the candidate
    /// @return The number of votes the candidate has received
    function getVoteCount(uint candidateId) public view returns (uint) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId].voteCount;
    }

    /// @notice Function to get the details of a candidate
    /// @param candidateId The ID of the candidate
    /// @return The candidate's ID, name, and vote count
    function getCandidate(uint candidateId) public view returns (uint, string memory, uint) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        Candidate memory candidate = candidates[candidateId];
        return (candidate.id, candidate.name, candidate.voteCount);
    }
}
```
