"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Create a decentralized voting system in Solidity that aligns with the governance model described for Global Miracle Coin, using the LYCAN Chain infrastructure.
Generated: DETERMINISTIC_8185ea6ca9798b5c
Batch ID: 20250612_152358
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

/// @title Decentralized Voting System
/// @notice This contract allows users to create and participate in voting on proposals
/// @dev This system is designed for the Global Miracle Coin governance model using the LYCAN Chain infrastructure

contract DecentralizedVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;            // Unique identifier for the proposal
        string description;    // Description of the proposal
        address creator;       // Address of the proposal creator
        uint256 voteCount;     // Total votes received for the proposal
        bool exists;           // Flag to check if proposal exists
    }

    // Mapping of proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track votes by address for each proposal
    mapping(uint256 => mapping(address => bool)) public votes;

    // Counter for the total number of proposals
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed creator);

    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    /// @notice Create a new proposal
    /// @param _description The description of the proposal
    /// @return proposalId The ID of the created proposal
    function createProposal(string memory _description) public returns (uint256 proposalId) {
        proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            creator: msg.sender,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalId, _description, msg.sender);
    }

    /// @notice Vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    /// @dev Reverts if the proposal does not exist or if the sender has already voted
    function vote(uint256 _proposalId) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!votes[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the vote
        votes[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Get the details of a proposal
    /// @param _proposalId The ID of the proposal to get details for
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return creator The address of the proposal creator
    /// @return voteCount The total number of votes for the proposal
    function getProposal(uint256 _proposalId) public view returns (uint256 id, string memory description, address creator, uint256 voteCount) {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.creator, proposal.voteCount);
    }
}
```
