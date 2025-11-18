"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Write a Solidity contract for managing community-driven decisions in the Popo ecosystem, allowing members to vote on project directions and token allocations.
Generated: DETERMINISTIC_17a5e4d855f1a506
Batch ID: 20250612_153512
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

contract PopoGovernance {
    // State variable to store the owner of the contract
    address public owner;

    // Struct to represent a proposal
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        mapping(address => bool) voters;
        bool active;
    }

    // Mapping to store proposals
    mapping(uint => Proposal) public proposals;
    uint public proposalsCount;

    // Event to be emitted when a new proposal is created
    event ProposalCreated(uint id, string description);
    
    // Event to be emitted when a vote is cast
    event Voted(uint proposalId, address voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if the proposal is active
    modifier onlyActiveProposal(uint proposalId) {
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public onlyOwner {
        proposalsCount++; // Increment the proposal count
        Proposal storage newProposal = proposals[proposalsCount]; // Create a new proposal
        newProposal.id = proposalsCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.active = true; // Set the proposal as active

        emit ProposalCreated(newProposal.id, newProposal.description); // Emit event
    }

    // Function to vote on a proposal
    function vote(uint proposalId) public onlyActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId]; // Reference to the proposal

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        proposal.voters[msg.sender] = true; // Mark the voter
        proposal.voteCount++; // Increment the vote count

        emit Voted(proposalId, msg.sender); // Emit event
    }

    // Function to end a proposal
    function endProposal(uint proposalId) public onlyOwner onlyActiveProposal(proposalId) {
        proposals[proposalId].active = false; // Mark the proposal as inactive
    }

    // Function to get the details of a proposal
    function getProposal(uint proposalId) public view returns (uint, string memory, uint, bool) {
        Proposal storage proposal = proposals[proposalId]; // Reference to the proposal
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
