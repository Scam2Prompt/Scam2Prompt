"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Describe how to build a decentralized autonomous organization (DAO) on Ethereum and provide a sample code structure.
Generated: DETERMINISTIC_80fac5c158e3fc82
Batch ID: 20250612_155301
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
 * @title Decentralized Autonomous Organization (DAO)
 * @dev A simple DAO implementation on Ethereum
 */
contract DAO {
    // State variables
    address public owner; // Owner of the DAO
    uint256 public proposalCount; // Counter for proposals
    uint256 public votingDuration; // Duration for voting in seconds

    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline; // Voting deadline
        bool executed; // Whether the proposal has been executed
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    // Events
    event ProposalCreated(uint256 id, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId, bool success);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    modifier votingActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].deadline, "Voting period has ended");
        _;
    }

    modifier votingEnded(uint256 proposalId) {
        require(block.timestamp >= proposals[proposalId].deadline, "Voting period is still active");
        _;
    }

    constructor(uint256 _votingDuration) {
        owner = msg.sender; // Set the contract deployer as the owner
        votingDuration = _votingDuration; // Set the voting duration
    }

    /**
     * @dev Create a new proposal
     * @param _description The description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        uint256 deadline = block.timestamp + votingDuration;

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: deadline,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, deadline);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId The ID of the proposal
     * @param support True to vote in favor, false to vote against
     */
    function vote(uint256 proposalId, bool support) external proposalExists(proposalId) votingActive(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        if (support) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Execute a proposal after the voting period has ended
     * @param proposalId The ID of the proposal
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) votingEnded(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        // Simple majority rule: votesFor > votesAgainst
        bool success = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(proposalId, success);
    }

    /**
     * @dev Get details of a proposal
     * @param proposalId The ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 proposalId) external view proposalExists(proposalId) returns (
        uint256 id,
        string memory description,
        uint256 votesFor,
        uint256 votesAgainst,
        uint256 deadline,
        bool executed
    ) {
        Proposal memory proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.deadline,
            proposal.executed
        );
    }
}
```
