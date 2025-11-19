"""
Generated Code Metadata:
========================
Original URL: https://www-puffer.com
Prompt: Create a decentralized governance module for Puffer Finance's protocol using a suitable programming language, ensuring transparent decision-making and community involvement.
Generated: DETERMINISTIC_08a37804e2bd834f
Batch ID: 20250622_211032
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
 * @title GovernanceModule
 * @dev A decentralized governance module for Puffer Finance's protocol.
 * Allows community members to propose and vote on decisions transparently.
 */
contract GovernanceModule {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 voteCountFor;
        uint256 voteCountAgainst;
        uint256 creationTime;
        bool executed;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Minimum voting period (in seconds)
    uint256 public constant VOTING_PERIOD = 3 days;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 indexed id,
        string description,
        address indexed proposer,
        uint256 creationTime
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
     * @dev Create a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            proposer: msg.sender,
            voteCountFor: 0,
            voteCountAgainst: 0,
            creationTime: block.timestamp,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _description, msg.sender, block.timestamp);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        require(block.timestamp <= proposal.creationTime + VOTING_PERIOD, "Voting period has ended");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.voteCountFor++;
        } else {
            proposal.voteCountAgainst++;
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.creationTime + VOTING_PERIOD, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        // Logic for executing the proposal can be added here.
        // For example, calling another contract or updating protocol parameters.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get details of a proposal.
     * @param _proposalId The ID of the proposal to fetch.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
