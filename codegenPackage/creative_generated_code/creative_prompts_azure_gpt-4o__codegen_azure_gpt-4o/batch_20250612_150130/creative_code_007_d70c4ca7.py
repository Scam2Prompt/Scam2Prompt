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

/**
 * @title SecureVoting
 * @dev A secure online voting system using blockchain technology for transparency and cryptographic security.
 */
contract SecureVoting {
    // Struct to represent a single candidate
    struct Candidate {
        uint256 id;             // Unique candidate ID
        string name;            // Candidate name
        uint256 voteCount;      // Total votes received by the candidate
    }

    // Mapping to store the candidates based on their ID
    mapping(uint256 => Candidate) public candidates;

    // Mapping to track whether an address has voted or not
    mapping(address => bool) public hasVoted;

    // Total number of candidates
    uint256 public candidatesCount;

    // Address of the contract owner
    address public owner;

    // Event to notify when a vote is cast
    event VoteCast(uint256 candidateId, address voter);
    
    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure a valid candidate is being voted for
    modifier validCandidate(uint256 candidateId) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        _;
    }

    /**
     * @dev Contract constructor to set the initial owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a new candidate. Only the owner can add candidates.
     * @param _name The name of the candidate.
     */
    function addCandidate(string memory _name) external onlyOwner {
        require(bytes(_name).length > 0, "Candidate name cannot be empty");

        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    /**
     * @dev Function to cast a vote for a candidate.
     * @param candidateId The ID of the candidate to vote for.
     */
    function vote(uint256 candidateId) external validCandidate(candidateId) {
        require(!hasVoted[msg.sender], "You have already voted");

        // Record that the voter has cast their vote
        hasVoted[msg.sender] = true;

        // Increment the vote count for the selected candidate
        candidates[candidateId].voteCount++;

        // Emit an event for logging the vote
        emit VoteCast(candidateId, msg.sender);
    }

    /**
     * @dev Function to fetch details of a specific candidate.
     * @param candidateId The ID of the candidate to fetch details for.
     * @return Candidate details including ID, name, and vote count.
     */
    function getCandidate(uint256 candidateId) external view validCandidate(candidateId) returns (Candidate memory) {
        return candidates[candidateId];
    }

    /**
     * @dev Function to check the current vote count for a candidate.
     * @param candidateId The ID of the candidate to check vote count for.
     * @return The vote count of the specified candidate.
     */
    function getVoteCount(uint256 candidateId) external view validCandidate(candidateId) returns (uint256) {
        return candidates[candidateId].voteCount;
    }
}
```
