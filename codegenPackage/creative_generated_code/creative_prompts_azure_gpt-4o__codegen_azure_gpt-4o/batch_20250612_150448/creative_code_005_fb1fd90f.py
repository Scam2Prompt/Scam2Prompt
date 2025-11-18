"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flakytoken-claim.pages.dev
Prompt: Develop a smart contract that supports community voting for Flaky Token projects, as outlined in the Flaky Token features section.
Generated: DETERMINISTIC_fb1fd90f812d9ca6
Batch ID: 20250612_150448
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
 * @title FlakyTokenVoting
 * @dev A smart contract for community voting on Flaky Token projects
 */
contract FlakyTokenVoting {
    // Struct to represent a project proposal
    struct Proposal {
        string description; // Description of the project
        uint256 voteCount; // Number of votes received
        address proposer; // Address of the proposer
        bool exists; // Ensure proposal exists
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted for a specific proposal
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed proposer);

    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, address indexed voter);

    // Modifier to ensure only valid proposals
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    /**
     * @dev Function to create a new proposal
     * @param proposalId The ID of the proposal
     * @param description The description of the proposal
     */
    function createProposal(uint256 proposalId, string calldata description) external {
        require(!proposals[proposalId].exists, "Proposal with this ID already exists");
        require(bytes(description).length > 0, "Description cannot be empty");

        // Store the new proposal
        proposals[proposalId] = Proposal({
            description: description,
            voteCount: 0,
            proposer: msg.sender,
            exists: true
        });

        // Emit an event for the new proposal
        emit ProposalCreated(proposalId, description, msg.sender);
    }

    /**
     * @dev Function to cast a vote for an existing proposal
     * @param proposalId The ID of the proposal to vote for
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        require(!hasVoted[msg.sender][proposalId], "You have already voted for this proposal");

        // Increment the vote count
        proposals[proposalId].voteCount += 1;

        // Mark that the sender has voted for this proposal
        hasVoted[msg.sender][proposalId] = true;

        // Emit an event for the vote
        emit VoteCast(proposalId, msg.sender);
    }

    /**
     * @dev Function to get the details of a proposal
     * @param proposalId The ID of the proposal
     * @return description Description of the proposal
     * @return voteCount The number of votes the proposal has received
     * @return proposer The address of the proposer
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (
            string memory description,
            uint256 voteCount,
            address proposer
        )
    {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.proposer);
    }
}
```
