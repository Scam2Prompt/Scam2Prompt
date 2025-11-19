"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Create a Solidity smart contract that supports secure online voting systems using blockchain technology, inspired by Gas Profit's emphasis on transparency and cryptographic security.
Generated: DETERMINISTIC_d70c4ca72fbd8d4a
Batch ID: 20250612_150130
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

contract SecureVoting {
    // Structure to hold candidate information
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
    // Owner of the contract
    address public owner;

    // Event to emit when a vote is cast
    event VoteCast(uint indexed candidateId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to add a candidate
    function addCandidate(string memory _name) public onlyOwner {
        require(bytes(_name).length > 0, "Candidate name cannot be empty");
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    // Function to vote for a candidate
    function vote(uint _candidateId) public {
        // Ensure the voter has not voted before
        require(!voters[msg.sender], "You have already voted");
        // Ensure the candidate ID is valid
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");

        // Record the vote
        voters[msg.sender] = true;
        candidates[_candidateId].voteCount++;

        // Emit the vote cast event
        emit VoteCast(_candidateId);
    }

    // Function to get the total votes for a candidate
    function getCandidateVotes(uint _candidateId) public view returns (uint) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[_candidateId].voteCount;
    }

    // Function to get candidate details
    function getCandidate(uint _candidateId) public view returns (uint, string memory, uint) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        Candidate memory candidate = candidates[_candidateId];
        return (candidate.id, candidate.name, candidate.voteCount);
    }
}
```
