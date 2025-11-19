"""
Generated Code Metadata:
========================
Original URL: https://aave-v3.github.io
Prompt: Design a smart contract for Aave's decentralized governance model, allowing users to vote on proposals and upgrades to the protocol.
Generated: DETERMINISTIC_79b9937048874a93
Batch ID: 20250622_212302
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

/**
 * @title AaveGovernance
 * @dev A smart contract for decentralized governance in the Aave protocol.
 * Allows users to create proposals, vote on them, and execute upgrades if approved.
 */
contract AaveGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if a user has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Minimum voting period (in seconds)
    uint256 public constant MIN_VOTING_PERIOD = 3 days;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 indexed id,
        string description,
        address indexed proposer,
        uint256 deadline
    );

    // Event emitted when a vote is cast
    event VoteCast(
        uint256 indexed proposalId,
        address indexed voter,
        bool support
    );

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Modifier to ensure the proposal exists.
     * @param proposalId The ID of the proposal.
     */
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    /**
     * @dev Modifier to ensure the proposal is still active.
     * @param proposalId The ID of the proposal.
     */
    modifier proposalActive(uint256 proposalId) {
        require(
            block.timestamp < proposals[proposalId].deadline,
            "Voting period has ended"
        );
        _;
    }

    /**
     * @dev Modifier to ensure the proposal is not already executed.
     * @param proposalId The ID of the proposal.
     */
    modifier proposalNotExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            proposer: msg.sender,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + MIN_VOTING_PERIOD,
            executed: false
        });

        emit ProposalCreated(proposalId, description, msg.sender, proposals[proposalId].deadline);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support)
        external
        proposalExists(proposalId)
        proposalActive(proposalId)
    {
        require(!hasVoted[proposalId][msg.sender], "Already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal if it is approved.
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId)
        external
        proposalExists(proposalId)
        proposalNotExecuted(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];

        require(
            block.timestamp >= proposal.deadline,
            "Voting period has not ended"
        );
        require(
            proposal.votesFor > proposal.votesAgainst,
            "Proposal not approved"
        );

        proposal.executed = true;

        // Logic for executing the proposal (e.g., upgrading the protocol) goes here.
        // This is left as a placeholder since the specific implementation depends on the protocol's requirements.

        emit ProposalExecuted(proposalId);
    }
}
```
