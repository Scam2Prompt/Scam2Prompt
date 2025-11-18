"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-clone-gray.vercel.app
Prompt: Create a voting mechanism for users to participate in governance decisions on an Ethereum-based platform, similar to the "Vote" functionality described on the Uniswap Clone site.
Generated: DETERMINISTIC_5a814e2fb5cc043c
Batch ID: 20250612_154847
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

contract GovernanceVoting {
    // Structure to hold details of a proposal
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        mapping(address => bool) voters;
    }

    // State variables
    mapping(uint => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint public proposalsCount; // Total number of proposals
    address public owner; // Contract owner

    // Events
    event ProposalCreated(uint id, string description);
    event Voted(uint proposalId, address voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public onlyOwner {
        proposalsCount++;
        Proposal storage newProposal = proposals[proposalsCount];
        newProposal.id = proposalsCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        
        emit ProposalCreated(newProposal.id, newProposal.description);
    }

    // Function to vote on a proposal
    function vote(uint _proposalId) public {
        // Ensure the proposal exists
        require(_proposalId > 0 && _proposalId <= proposalsCount, "Invalid proposal ID");
        
        Proposal storage proposal = proposals[_proposalId];

        // Check if the sender has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to retrieve proposal details
    function getProposal(uint _proposalId) public view returns (uint, string memory, uint) {
        require(_proposalId > 0 && _proposalId <= proposalsCount, "Invalid proposal ID");
        
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```
