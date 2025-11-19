"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Design a DAO structure for a community-driven web3 project, allowing users to govern themselves and make key decisions about the project's direction.
Generated: DETERMINISTIC_e0f316b2fcc06833
Batch ID: 20250622_205112
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
 * @title DAO Contract
 * @dev A decentralized autonomous organization (DAO) structure for a community-driven web3 project.
 * Allows users to propose and vote on decisions regarding the project's direction.
 */
contract CommunityDAO {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline; // Voting deadline (timestamp)
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Address of the DAO owner
    address public owner;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 id, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId, bool success);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Modifier to check if the voting period is active
    modifier votingActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].deadline, "Voting period has ended");
        _;
    }

    // Constructor to initialize the DAO
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than zero");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, block.timestamp + _duration);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external proposalExists(_proposalId) votingActive(_proposalId) {
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        Proposal storage proposal = proposals[_proposalId];

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Logic for executing the proposal can be added here
        // For simplicity, we just mark it as executed
        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Get details of a proposal.
     * @param _proposalId ID of the proposal to fetch.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId) external view proposalExists(_proposalId) returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
