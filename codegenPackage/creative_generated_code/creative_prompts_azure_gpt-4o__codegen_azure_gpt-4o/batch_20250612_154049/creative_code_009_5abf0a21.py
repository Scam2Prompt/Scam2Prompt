"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-it.web.app
Prompt: Create a Solidity-based governance model that incorporates Lightchain AI’s decentralized governance principles, enabling community-driven decision-making.
Generated: DETERMINISTIC_5abf0a2168ca99ee
Batch ID: 20250612_154049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Lightchain Governance Contract
 * @dev Implements decentralized governance principles for community-driven decision-making.
 */
contract LightchainGovernance {
    // Struct to represent a proposal made by the community
    struct Proposal {
        uint id;
        string title;
        string description;
        uint votesFor;
        uint votesAgainst;
        uint deadline;
        address proposer;
        bool executed;
    }

    // Mapping to store proposals by their ID
    mapping(uint => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint => mapping(address => bool)) public hasVoted;

    // Counter to generate unique IDs for proposals
    uint public proposalCount;

    // Minimum voting duration for proposals (in seconds)
    uint public constant MIN_VOTING_DURATION = 3 days;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint id,
        string title,
        string description,
        uint deadline,
        address proposer
    );

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint id, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint id, bool success);

    /**
     * @notice Allows a user to create a governance proposal.
     * @param _title Title of the proposal.
     * @param _description Detailed description of the proposal.
     */
    function createProposal(string memory _title, string memory _description) external {
        // Incrementing proposal count for unique ID
        proposalCount++;

        // Creating a new proposal and storing it
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + MIN_VOTING_DURATION,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCount, _title, _description, proposals[proposalCount].deadline, msg.sender);
    }

    /**
     * @notice Allows a user to vote on an active proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True for voting in favor, false for voting against.
     */
    function voteOnProposal(uint _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and is still active
        require(proposal.id != 0, "Proposal does not exist.");
        require(block.timestamp <= proposal.deadline, "Voting period has ended.");

        // Ensure the voter hasn't already voted on the proposal
        require(!hasVoted[_proposalId][msg.sender], "You already voted on this proposal.");

        // Record the vote
        hasVoted[_proposalId][msg.sender] = true;
        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit ProposalVoted(_proposalId, msg.sender, _support);
    }

    /**
     * @notice Executes a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists
        require(proposal.id != 0, "Proposal does not exist.");

        // Ensure the voting period has ended
        require(block.timestamp > proposal.deadline, "Voting period is still ongoing.");

        // Ensure the proposal hasn't already been executed
        require(!proposal.executed, "Proposal already executed.");

        // Mark the proposal as executed
        proposal.executed = true;

        // Determine proposal outcome based on votes
        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, success);

        // Further execution logic can be added here for successful proposals
    }

    /**
     * @notice Retrieves the details of a specific proposal.
     * @param _proposalId ID of the proposal to retrieve.
     * @return Proposal struct containing all details of the proposal.
     */
    function getProposal(uint _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
