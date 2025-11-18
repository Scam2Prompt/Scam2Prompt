"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Develop a governance proposal in Solidity for OGV stakers to vote on reallocating funds across OUSD’s active yield strategies. Include timelock functionality for security.
Generated: DETERMINISTIC_968af369e2965511
Batch ID: 20250612_150613
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
 * @title GovernanceProposal
 * @notice This contract allows OGV stakers to vote on a proposal to reallocate funds
 *         across OUSD's active yield strategies. It includes a timelock mechanism
 *         for security and transparency.
 */
contract GovernanceProposal {
    // Define the proposal structure
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Votes in favor of the proposal
        uint256 votesAgainst; // Votes against the proposal
        uint256 deadline;   // Deadline for voting
        bool executed;      // Has the proposal been executed
    }

    // Variables
    address public admin; // Admin address to manage proposals
    uint256 public timelockDuration; // Timelock duration in seconds
    Proposal[] public proposals; // Array of proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted per proposal

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event VoteCast(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Modifier to check if a proposal exists
    modifier validProposal(uint256 proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _timelockDuration) {
        admin = msg.sender;
        timelockDuration = _timelockDuration;
    }

    /**
     * @notice Create a new governance proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyAdmin {
        uint256 deadline = block.timestamp + timelockDuration;
        proposals.push(Proposal({
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: deadline,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description, deadline);
    }

    /**
     * @notice Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True if voting in favor, false if against.
     */
    function vote(uint256 proposalId, bool support) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        hasVoted[proposalId][msg.sender] = true;
        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Execute a proposal after the timelock has expired.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyAdmin validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.deadline, "Timelock not expired");
        require(!proposal.executed, "Proposal already executed");

        // Logic to reallocate funds across OUSD's yield strategies goes here.
        // Placeholder for yield strategy reallocation logic.
        // Example: distributeFundsToStrategies(proposal.votesFor, proposal.votesAgainst);

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Update the timelock duration.
     * @param _timelockDuration The new timelock duration in seconds.
     */
    function updateTimelockDuration(uint256 _timelockDuration) external onlyAdmin {
        timelockDuration = _timelockDuration;
    }
}
```
