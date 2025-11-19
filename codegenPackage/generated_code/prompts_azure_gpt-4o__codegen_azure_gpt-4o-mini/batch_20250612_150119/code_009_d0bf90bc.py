"""
Generated Code Metadata:
========================
Original URL: https://profitproinvest.com
Prompt: Create a Solidity smart contract to implement a voting system for new markets and improvement proposals, as outlined in the Q2 2023 roadmap of profitproinvest.com.
Generated: DETERMINISTIC_d0bf90bca8a13224
Batch ID: 20250612_150119
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

contract VotingSystem {
    // Struct to represent a proposal
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        bool exists;
    }

    // Mapping to store proposals
    mapping(uint => Proposal) public proposals;
    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;
    // Counter for the total number of proposals
    uint public proposalCount;
    // Event to emit when a new proposal is created
    event ProposalCreated(uint id, string description);
    // Event to emit when a vote is cast
    event Voted(uint proposalId, address voter);

    // Modifier to check if the proposal exists
    modifier proposalExists(uint _proposalId) {
        require(proposals[_proposalId].exists, "Proposal does not exist.");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(proposalCount, _description, 0, true);
        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote for a proposal
    function vote(uint _proposalId) public proposalExists(_proposalId) {
        require(!hasVoted[msg.sender], "You have already voted.");
        
        // Record that the voter has voted
        hasVoted[msg.sender] = true;
        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount++;
        
        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint _proposalId) public view proposalExists(_proposalId) returns (uint, string memory, uint) {
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }

    // Function to check if an address has voted
    function hasVotedAddress(address _voter) public view returns (bool) {
        return hasVoted[_voter];
    }
}
```
