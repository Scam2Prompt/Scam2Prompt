"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantlenetwork.web3-mint.pro
Prompt: Generate code to implement a decentralized voting system on Mantle Network using Solidity.
Generated: DETERMINISTIC_c2d8848ad2cb0441
Batch ID: 20250612_154646
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

/// @title Decentralized Voting System
/// @author Your Name
/// @notice This contract implements a voting system on the Mantle Network
/// @dev Uses Solidity version 0.8.0 or higher for safety and efficiency

contract Voting {
    // Structure to hold details of a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping to store candidates by their IDs
    mapping(uint => Candidate) public candidates;
    // Mapping to track if an address has voted
    mapping(address => bool) public voters;
    
    // Variables to track the total number of candidates and votes
    uint public candidatesCount;
    uint public totalVotes;

    // Event to emit when a vote is cast
    event VoteCast(uint indexed candidateId);

    /// @notice Constructor to initialize the voting system with candidates
    /// @param _candidateNames List of candidate names
    constructor(string[] memory _candidateNames) {
        require(_candidateNames.length > 0, "At least one candidate required");

        for (uint i = 0; i < _candidateNames.length; i++) {
            addCandidate(_candidateNames[i]);
        }
    }

    /// @notice Function to add a new candidate
    /// @param _name The name of the candidate to add
    function addCandidate(string memory _name) internal {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    /// @notice Function to cast a vote for a candidate
    /// @param _candidateId The ID of the candidate being voted for
    /// @dev Reverts if the candidate ID is invalid or if the voter has already voted
    function vote(uint _candidateId) external {
        // Ensure the candidate exists
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        // Ensure the voter has not already voted
        require(!voters[msg.sender], "You have already voted");

        // Record the vote
        voters[msg.sender] = true;
        candidates[_candidateId].voteCount++;
        totalVotes++;

        // Emit the vote cast event
        emit VoteCast(_candidateId);
    }

    /// @notice Function to get the details of a candidate
    /// @param _candidateId The ID of the candidate to retrieve
    /// @return The candidate details including ID, name, and vote count
    function getCandidate(uint _candidateId) external view returns (uint, string memory, uint) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        Candidate memory candidate = candidates[_candidateId];
        return (candidate.id, candidate.name, candidate.voteCount);
    }

    /// @notice Function to get the total number of votes cast
    /// @return The total number of votes
    function getTotalVotes() external view returns (uint) {
        return totalVotes;
    }
}
```
