"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cagacrypto-en.web.app
Prompt: Write a smart contract in Solidity for a decentralized governance system inspired by CAGA Crypto, allowing users to propose and vote on changes.
Generated: DETERMINISTIC_add1740936938c05
Batch ID: 20250612_151539
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
 * @title Decentralized Governance System
 * @dev Inspired by CAGA Crypto, allows users to propose and vote on changes.
 */
contract Governance {
    // Represents a proposal in the system
    struct Proposal {
        uint256 id; // Unique ID of the proposal
        string description; // Description of the proposal
        uint256 votesFor; // Count of votes in favor of the proposal
        uint256 votesAgainst; // Count of votes against the proposal
        bool executed; // Indicates whether the proposal has been executed
        address proposer; // Address of the user who proposed the idea
    }

    // Mapping of proposal IDs to Proposal data
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public nextProposalId;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, address indexed proposer);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Creates a new proposal.
     * @param description A brief description of the proposed change.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Proposal description cannot be empty");

        proposals[nextProposalId] = Proposal({
            id: nextProposalId,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            proposer: msg.sender
        });

        emit ProposalCreated(nextProposalId, description, msg.sender);

        nextProposalId++; // Increment the proposal ID counter
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True if voting in favor, false if voting against.
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < nextProposalId, "Invalid proposal ID");
        require(!proposals[proposalId].executed, "Proposal already executed");
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        // Record that the voter has voted
        hasVoted[proposalId][msg.sender] = true;

        // Update the vote counts
        if (support) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Executes a proposal if it has more votes in favor than against.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < nextProposalId, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal does not have majority support");

        // Mark the proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(proposalId);

        // Proposal execution logic would go here.
        // For simplicity, this example does not include further actions.
    }
}
```
