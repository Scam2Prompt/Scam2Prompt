"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a smart contract for a decentralized voting system using Ethereum's blockchain, as outlined in Ethereum.org's DAO use cases.
Generated: DETERMINISTIC_e44e51c1b3d67175
Batch ID: 20250612_151948
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

// A smart contract for a decentralized voting system
contract DecentralizedVoting {

    // Struct to represent a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping from candidate ID to Candidate
    mapping(uint => Candidate) public candidates;

    // Mapping to track whether an address has voted
    mapping(address => bool) public voters;

    // Total number of candidates
    uint public candidatesCount;

    // Event to emit when a vote is cast
    event Voted(address indexed voter, uint indexed candidateId);

    // Constructor to initialize candidates
    constructor(string[] memory candidateNames) {
        require(candidateNames.length > 0, "At least one candidate is required");
        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    // Function to add a new candidate
    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
    }

    // Function to cast a vote for a candidate
    function vote(uint candidateId) public {
        // Ensure that the voter has not already voted
        require(!voters[msg.sender], "You have already voted.");

        // Ensure that the candidate ID is valid
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");

        // Record that the voter has voted
        voters[msg.sender] = true;

        // Increment the vote count for the candidate
        candidates[candidateId].voteCount++;

        // Emit the vote event
        emit Voted(msg.sender, candidateId);
    }

    // Function to get the vote count for a candidate
    function getVoteCount(uint candidateId) public view returns (uint) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[candidateId].voteCount;
    }

    // Function to get the list of candidates
    function getCandidates() public view returns (Candidate[] memory) {
        Candidate[] memory candidateList = new Candidate[](candidatesCount);
        for (uint i = 1; i <= candidatesCount; i++) {
            candidateList[i - 1] = candidates[i];
        }
        return candidateList;
    }
}
```
