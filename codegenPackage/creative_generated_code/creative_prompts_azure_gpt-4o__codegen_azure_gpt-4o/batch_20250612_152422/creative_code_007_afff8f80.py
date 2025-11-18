"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralized-metis.pages.dev
Prompt: Write a smart contract that incorporates decentralized voting mechanisms aligned with Metis's Community Ecosystem Governance (CEG) framework.
Generated: DETERMINISTIC_afff8f805bc69c00
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

/**
 * @title Decentralized Voting Smart Contract
 * @dev Implements a decentralized voting mechanism aligned with Metis's Community Ecosystem Governance (CEG) framework.
 */
contract DecentralizedVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Address of the contract owner
    address public owner;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 startTime, uint256 endTime);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new proposal
     * @param description The description of the proposal
     * @param duration The duration of the voting period in seconds
     * @return proposalId The ID of the created proposal
     */
    function createProposal(string memory description, uint256 duration) external onlyOwner returns (uint256 proposalId) {
        uint256 id = uint256(keccak256(abi.encodePacked(block.timestamp, description, msg.sender)));
        proposals[id] = Proposal({
            id: id,
            description: description,
            voteCount: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(id, description, block.timestamp, block.timestamp + duration);
        return id;
    }

    /**
     * @dev Function to cast a vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     */
    function castVote(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp >= proposal.startTime, "Voting has not started yet");
        require(block.timestamp <= proposal.endTime, "Voting has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted");

        proposal.voteCount += 1;
        hasVoted[proposalId][msg.sender] = true;

        emit VoteCast(proposalId, msg.sender);
    }

    /**
     * @dev Function to execute a proposal
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal has already been executed");

        // Custom logic for proposal execution goes here
        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Function to retrieve proposal details
     * @param proposalId The ID of the proposal
     * @return description The description of the proposal
     * @return voteCount The number of votes the proposal has received
     * @return startTime The start time of the voting period
     * @return endTime The end time of the voting period
     * @return executed Whether the proposal has been executed
     */
    function getProposalDetails(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (
            string memory description,
            uint256 voteCount,
            uint256 startTime,
            uint256 endTime,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.startTime, proposal.endTime, proposal.executed);
    }
}
```
