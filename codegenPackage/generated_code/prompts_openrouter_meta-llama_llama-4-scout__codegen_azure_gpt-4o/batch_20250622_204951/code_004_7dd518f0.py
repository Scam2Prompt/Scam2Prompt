"""
Generated Code Metadata:
========================
Original URL: https://agora-next-8n06xjzv6-voteagora.vercel.app
Prompt: "Design a basic implementation of an on-chain governance system inspired by Agora’s features."
Generated: DETERMINISTIC_7dd518f0b6d0269a
Batch ID: 20250622_204951
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
 * @title OnChainGovernance
 * @dev A basic implementation of an on-chain governance system inspired by Agora's features.
 */
contract OnChainGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCountYes; // Number of "Yes" votes
        uint256 voteCountNo; // Number of "No" votes
        uint256 deadline; // Voting deadline (timestamp)
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Minimum duration for voting (in seconds)
    uint256 public constant MIN_VOTING_DURATION = 1 days;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 id,
        string description,
        uint256 deadline,
        address proposer
    );

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId, bool success);

    /**
     * @dev Create a new proposal.
     * @param _description The description of the proposal.
     * @param _duration The duration of the voting period (in seconds).
     */
    function createProposal(string memory _description, uint256 _duration)
        external
    {
        require(
            _duration >= MIN_VOTING_DURATION,
            "Voting duration must be at least the minimum duration"
        );

        proposalCounter++;
        uint256 proposalId = proposalCounter;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCountYes: 0,
            voteCountNo: 0,
            deadline: block.timestamp + _duration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, block.timestamp + _duration, msg.sender);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _vote True for "Yes", False for "No".
     */
    function vote(uint256 _proposalId, bool _vote) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");

        hasVoted[_proposalId][msg.sender] = true;

        if (_vote) {
            proposal.voteCountYes++;
        } else {
            proposal.voteCountNo++;
        }

        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        // Check if the proposal passed
        bool success = proposal.voteCountYes > proposal.voteCountNo;

        emit ProposalExecuted(_proposalId, success);

        // Additional logic for executing the proposal can be added here
        // For example, transferring funds, updating state, etc.
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId The ID of the proposal.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            string memory description,
            uint256 voteCountYes,
            uint256 voteCountNo,
            uint256 deadline,
            address proposer,
            bool executed
        )
    {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");

        return (
            proposal.id,
            proposal.description,
            proposal.voteCountYes,
            proposal.voteCountNo,
            proposal.deadline,
            proposal.proposer,
            proposal.executed
        );
    }
}
```
