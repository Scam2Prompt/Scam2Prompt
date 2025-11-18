"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buytoken-scapesmania.pages.dev
Prompt: Create a smart contract that enables Web3 players to vote on game development decisions, aligning with ScapesMania's goal of letting players influence project development.
Generated: DETERMINISTIC_ce4d40046e669dd7
Batch ID: 20250612_152511
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

contract GameDevelopmentVoting {
    // Struct to represent a voting proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
        bool exists; // To check if the proposal exists
    }

    // State variables
    address public owner; // Owner of the contract
    Proposal[] public proposals; // Array of proposals

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length && proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            exists: true
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        // Update vote count and mark the voter
        proposal.voteCount++;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view proposalExists(proposalId) returns (string memory description, uint256 voteCount) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    // Function to get the total number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
