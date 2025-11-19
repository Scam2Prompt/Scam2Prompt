"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Write a Solidity smart contract that facilitates decentralized voting for hackathon project awards, inspired by ETHBerlin04's participatory event structure.
Generated: DETERMINISTIC_9c81b27303cbbde8
Batch ID: 20250612_150554
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

contract DecentralizedVoting {
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

    // Constructor to initialize the candidates
    constructor(string[] memory candidateNames) {
        require(candidateNames.length > 0, "At least one candidate is required");
        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    // Function to add a candidate
    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
    }

    // Function to vote for a candidate
    function vote(uint candidateId) public {
        // Ensure the voter has not voted before
        require(!voters[msg.sender], "You have already voted");
        // Ensure the candidate ID is valid
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");

        // Record the vote
        voters[msg.sender] = true;
        candidates[candidateId].voteCount++;

        // Emit the vote event
        emit Voted(candidateId);
    }

    // Function to get the candidate details
    function getCandidate(uint candidateId) public view returns (Candidate memory) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId];
    }

    // Function to get the total votes for a candidate
    function getVoteCount(uint candidateId) public view returns (uint) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId].voteCount;
    }
}
```
