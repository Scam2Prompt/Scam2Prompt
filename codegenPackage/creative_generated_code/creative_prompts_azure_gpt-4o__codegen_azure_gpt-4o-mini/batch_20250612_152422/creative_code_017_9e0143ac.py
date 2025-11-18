"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralized-metis.pages.dev
Prompt: Generate code to implement an on-chain voting system for a decentralized application using Metis's governance model.
Generated: DETERMINISTIC_9e0143acf51adce4
Batch ID: 20250612_152422
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

contract Voting {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    struct Voter {
        bool hasVoted;
        uint vote;
    }

    mapping(uint => Candidate) public candidates; // Mapping of candidate ID to Candidate struct
    mapping(address => Voter) public voters; // Mapping of voter addresses to Voter struct
    uint public candidatesCount;
    uint public totalVotes;

    // Event to signal that a new candidate has been added
    event CandidateAdded(uint id, string name);
    // Event to signal that a vote has been cast
    event Voted(address indexed voter, uint indexed candidateId);

    // Constructor to initialize candidates
    constructor(string[] memory candidateNames) {
        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    // Function to add a new candidate
    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
        emit CandidateAdded(candidatesCount, name);
    }

    // Function to cast a vote for a candidate
    function vote(uint candidateId) public {
        // Check if the address has already voted
        require(!voters[msg.sender].hasVoted, "You have already voted.");
        // Check if the candidate ID is valid
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");

        // Record the vote
        voters[msg.sender].hasVoted = true;
        voters[msg.sender].vote = candidateId;

        // Update the vote count for the candidate
        candidates[candidateId].voteCount++;
        totalVotes++;

        emit Voted(msg.sender, candidateId);
    }

    // Function to get candidate details
    function getCandidate(uint candidateId) public view returns (Candidate memory) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[candidateId];
    }

    // Function to get the total number of votes
    function getTotalVotes() public view returns (uint) {
        return totalVotes;
    }

    // Function to check if a voter has voted
    function hasVoted() public view returns (bool) {
        return voters[msg.sender].hasVoted;
    }
}
```
