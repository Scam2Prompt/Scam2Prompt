"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaingpt-app.pages.dev
Prompt: Generate a Solidity smart contract for a DAO governance system using ChainGPT's Smart Contract Generator.
Generated: DETERMINISTIC_b4f11c2db643b05e
Batch ID: 20250612_154642
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
 * @title DAO Governance Contract
 * @dev A simple decentralized governance contract to manage proposals and votes.
 */
contract DAOGovernance {
    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        uint256 deadline;
    }

    // State variables
    address public owner; // Owner of the contract
    uint256 public proposalCount; // Counter for proposal IDs
    uint256 public votingDuration; // Duration of voting period (in seconds)
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    // Events
    event ProposalCreated(uint256 id, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 id, bool success);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    modifier activeProposal(uint256 proposalId) {
        require(proposals[proposalId].deadline >= block.timestamp, "Voting period has ended");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor
    constructor(uint256 _votingDuration) {
        owner = msg.sender;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        uint256 deadline = block.timestamp + votingDuration;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            deadline: deadline
        });

        emit ProposalCreated(proposalCount, _description, deadline);
    }

    /**
     * @dev Cast a vote on a proposal.
     * @param proposalId ID of the proposal.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support) external proposalExists(proposalId) activeProposal(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "Address has already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];
        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor += 1;
        } else {
            proposal.votesAgainst += 1;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param proposalId ID of the proposal.
     */
    function executeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.deadline, "Voting period is still active");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        // Determine the success of the proposal based on votes
        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(proposalId, success);
    }
}
```
