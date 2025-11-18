"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextoolsnode.pages.dev
Prompt: Generate code to implement a governance voting system for DeFi tokens, inspired by DEXTools' roadmap plans for governance features.
Generated: DETERMINISTIC_10fc952d47ab4108
Batch ID: 20250612_153526
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
 * @title Governance Voting System for DeFi Tokens
 * @dev This contract allows token holders to create proposals and vote on them.
 * Inspired by DEXTools' roadmap plans for governance features.
 */
contract Governance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token contract interface
    IERC20 public token;

    // Proposal counter for unique IDs
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed id, bool passed);

    // Constructor to set the token contract
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Modifier to ensure proposals are active.
     * @param proposalId ID of the proposal to check.
     */
    modifier isProposalActive(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].deadline, "Proposal voting period has ended");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param description Description of the proposal.
     * @param votingDuration Duration for voting in seconds.
     */
    function createProposal(string memory description, uint256 votingDuration) external {
        require(votingDuration > 0, "Voting duration must be greater than zero");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + votingDuration,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.timestamp + votingDuration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support True if voting in favor, false if voting against.
     */
    function vote(uint256 proposalId, bool support) external isProposalActive(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "Already voted on this proposal");
        require(token.balanceOf(msg.sender) > 0, "No tokens to vote");

        if (support) {
            proposals[proposalId].votesFor += token.balanceOf(msg.sender);
        } else {
            proposals[proposalId].votesAgainst += token.balanceOf(msg.sender);
        }

        hasVoted[proposalId][msg.sender] = true;
        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        bool passed = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(proposalId, passed);

        // Logic to execute the proposal can be added here if needed.
    }
}

// Interface for ERC20 token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
