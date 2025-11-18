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

// Smart Contract for Decentralized Voting aligned with Metis's Community Ecosystem Governance (CEG) framework

contract DecentralizedVoting {
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        mapping(address => bool) voters; // Track voters for this proposal
    }

    address public chairperson; // The address of the chairperson
    Proposal[] public proposals;  // Array to hold proposals
    mapping(address => bool) public hasVoted; // Track if an address has voted

    // Events for logging
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to restrict actions to the chairperson
    modifier onlyChairperson() {
        require(msg.sender == chairperson, "Only the chairperson can perform this action.");
        _;
    }

    // Constructor to initialize the chairperson
    constructor() {
        chairperson = msg.sender; // Set the contract deployer as the chairperson
    }

    // Function to create a new proposal
    function createProposal(string memory description) public onlyChairperson {
        Proposal memory newProposal;
        newProposal.description = description;
        newProposal.voteCount = 0;

        proposals.push(newProposal);
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote for a proposal
    function vote(uint256 proposalId) public {
        // Check if the proposal ID is valid
        require(proposalId < proposals.length, "Invalid proposal ID.");
        // Check if the voter has already voted
        require(!hasVoted[msg.sender], "You have already voted.");

        // Mark as voted and record the vote
        hasVoted[msg.sender] = true;
        proposals[proposalId].voteCount++;
        proposals[proposalId].voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the current vote count for a proposal
    function getVoteCount(uint256 proposalId) public view returns (uint256) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        return proposals[proposalId].voteCount;
    }

    // Function to get the description of a proposal
    function getProposal(uint256 proposalId) public view returns (string memory) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        return proposals[proposalId].description;
    }

    // Function to check if an address has voted
    function hasVotedForProposal(uint256 proposalId, address voter) public view returns (bool) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        return proposals[proposalId].voters[voter];
    }
}
```
