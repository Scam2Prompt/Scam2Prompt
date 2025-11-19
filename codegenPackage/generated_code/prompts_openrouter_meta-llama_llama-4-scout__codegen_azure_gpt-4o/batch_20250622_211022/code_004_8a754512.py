"""
Generated Code Metadata:
========================
Original URL: https://voting-consensys.app
Prompt: Implement a blockchain-based voting mechanism using ConsenSys, with a focus on transparency and tamper-proofing.
Generated: DETERMINISTIC_8a754512bd637a7c
Batch ID: 20250622_211022
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

/**
 * @title Blockchain-Based Voting System
 * @dev Implements a transparent and tamper-proof voting mechanism using Ethereum blockchain
 */
contract Voting {
    // Struct to represent a candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Struct to represent a voter
    struct Voter {
        bool hasVoted; // Tracks if the voter has already voted
        uint256 votedCandidateId; // Stores the candidate ID the voter voted for
    }

    // Mapping to store candidates by their ID
    mapping(uint256 => Candidate) public candidates;

    // Mapping to store voter information by their address
    mapping(address => Voter) public voters;

    // Total number of candidates
    uint256 public candidatesCount;

    // Address of the contract owner
    address public owner;

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed candidateId);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Function to add a candidate to the voting system
     * @param _name Name of the candidate
     */
    function addCandidate(string memory _name) public onlyOwner {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    /**
     * @dev Function to cast a vote for a candidate
     * @param _candidateId ID of the candidate to vote for
     */
    function vote(uint256 _candidateId) public {
        // Ensure the voter has not already voted
        require(!voters[msg.sender].hasVoted, "You have already voted");

        // Ensure the candidate ID is valid
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");

        // Record the voter's choice
        voters[msg.sender] = Voter(true, _candidateId);

        // Increment the vote count for the chosen candidate
        candidates[_candidateId].voteCount++;

        // Emit the vote cast event
        emit VoteCast(msg.sender, _candidateId);
    }

    /**
     * @dev Function to get the details of a candidate
     * @param _candidateId ID of the candidate
     * @return Candidate details (ID, name, vote count)
     */
    function getCandidate(uint256 _candidateId) public view returns (uint256, string memory, uint256) {
        // Ensure the candidate ID is valid
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");

        Candidate memory candidate = candidates[_candidateId];
        return (candidate.id, candidate.name, candidate.voteCount);
    }

    /**
     * @dev Function to check if a voter has voted
     * @param _voter Address of the voter
     * @return Boolean indicating whether the voter has voted
     */
    function hasVoted(address _voter) public view returns (bool) {
        return voters[_voter].hasVoted;
    }
}
```
