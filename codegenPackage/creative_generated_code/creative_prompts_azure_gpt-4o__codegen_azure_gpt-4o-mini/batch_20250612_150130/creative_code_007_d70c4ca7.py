"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gasprofitsoftware.com
Prompt: Create a Solidity smart contract that supports secure online voting systems using blockchain technology, inspired by Gas Profit's emphasis on transparency and cryptographic security.
Generated: DETERMINISTIC_d70c4ca72fbd8d4a
Batch ID: 20250612_150130
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

contract SecureVoting {
    // Struct to represent a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping from candidate ID to Candidate struct
    mapping(uint => Candidate) public candidates;

    // Mapping to track if an address has voted
    mapping(address => bool) public voters;

    // Total number of candidates
    uint public candidatesCount;

    // Event to emit when a vote is cast
    event Voted(uint indexed candidateId);

    // Constructor to initialize candidates
    constructor(string[] memory candidateNames) {
        require(candidateNames.length > 0, "At least one candidate required");
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
    function vote(uint candidateId) external {
        // Ensure the candidate exists
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        // Ensure the voter has not already voted
        require(!voters[msg.sender], "Voter has already voted");

        // Record the vote
        voters[msg.sender] = true;
        candidates[candidateId].voteCount++;

        // Emit the voting event
        emit Voted(candidateId);
    }

    // Function to get the details of a candidate
    function getCandidate(uint candidateId) external view returns (Candidate memory) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId];
    }

    // Function to get the total votes for a candidate
    function getVoteCount(uint candidateId) external view returns (uint) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId].voteCount;
    }

    // Function to get the total number of candidates
    function getCandidatesCount() external view returns (uint) {
        return candidatesCount;
    }
}
```
