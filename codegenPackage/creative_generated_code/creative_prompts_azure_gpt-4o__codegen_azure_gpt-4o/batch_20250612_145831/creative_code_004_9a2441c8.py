"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Generate a governance voting smart contract for an EVM-compatible blockchain that supports Singularity Finance's voting process, including vote periods and result announcements.
Generated: DETERMINISTIC_9a2441c8f4138cd4
Batch ID: 20250612_145831
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
 * @title GovernanceVoting
 * @dev A smart contract for managing governance voting process in an EVM-compatible blockchain.
 *      Supports Singularity Finance's voting process with vote periods and result announcements.
 */
contract GovernanceVoting {
    // Structure to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 startTime;  // Voting start time
        uint256 endTime;    // Voting end time
        uint256 votesFor;   // Votes in favor of the proposal
        uint256 votesAgainst; // Votes against the proposal
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track which address has voted for a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 startTime, uint256 endTime);
    event VoteCast(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId, bool passed);

    // Modifier to ensure the function is called during the voting period
    modifier duringVotingPeriod(uint256 proposalId) {
        require(
            block.timestamp >= proposals[proposalId].startTime &&
            block.timestamp <= proposals[proposalId].endTime,
            "Not within voting period"
        );
        _;
    }

    // Modifier to ensure the function is called after the voting period has ended
    modifier afterVotingPeriod(uint256 proposalId) {
        require(block.timestamp > proposals[proposalId].endTime, "Voting period has not ended");
        _;
    }

    // Modifier to ensure a proposal has not been executed
    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the proposal.
     * @param votingDuration Duration of the voting period in seconds.
     */
    function createProposal(string memory description, uint256 votingDuration) external {
        require(votingDuration > 0, "Voting duration must be greater than 0");

        uint256 proposalId = proposalCounter;
        proposalCounter++;

        proposals[proposalId] = Proposal({
            description: description,
            startTime: block.timestamp,
            endTime: block.timestamp + votingDuration,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(proposalId, description, block.timestamp, block.timestamp + votingDuration);
    }

    /**
     * @dev Cast a vote for or against a proposal.
     * @param proposalId ID of the proposal.
     * @param support True if voting in favor, false if voting against.
     */
    function vote(uint256 proposalId, bool support) external duringVotingPeriod(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "Already voted");

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
     * @dev Execute a proposal after the voting period has ended.
     *      Announces the result of the voting process.
     * @param proposalId ID of the proposal.
     */
    function executeProposal(uint256 proposalId) external afterVotingPeriod(proposalId) notExecuted(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        bool passed = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(proposalId, passed);
    }

    /**
     * @dev Retrieve proposal details.
     * @param proposalId ID of the proposal.
     * @return description Description of the proposal.
     * @return startTime Start time of the voting period.
     * @return endTime End time of the voting period.
     * @return votesFor Votes in favor of the proposal.
     * @return votesAgainst Votes against the proposal.
     * @return executed Whether the proposal has been executed.
     */
    function getProposal(uint256 proposalId)
        external
        view
        returns (
            string memory description,
            uint256 startTime,
            uint256 endTime,
            uint256 votesFor,
            uint256 votesAgainst,
            bool executed
        )
    {
        Proposal memory proposal = proposals[proposalId];
        return (
            proposal.description,
            proposal.startTime,
            proposal.endTime,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.executed
        );
    }
}
```
