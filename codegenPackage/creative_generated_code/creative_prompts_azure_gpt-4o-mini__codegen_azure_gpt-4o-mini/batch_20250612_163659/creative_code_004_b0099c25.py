"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Illustrate how to implement a voting mechanism for token holders in the Pushd decentralized governance system using Solidity.
Generated: DETERMINISTIC_b0099c2517e784cf
Batch ID: 20250612_163659
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

/// @title Pushd Governance Voting System
/// @notice This contract implements a voting mechanism for token holders
/// @dev Only token holders can participate in the voting process

contract PushdGovernance {
    // Structure to hold information about each proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes received for this proposal
        mapping(address => bool) voters; // Track whether an address has voted
        bool exists; // Flag to check if the proposal exists
    }

    // State variables
    address public owner; // Owner of the contract
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public proposalCount; // Total number of proposals

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed id, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Creates a new proposal
    /// @param _description Description of the proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            exists: true
        });
        emit ProposalCreated(proposalCount, _description);
    }

    /// @notice Allows token holders to vote on a proposal
    /// @param proposalId ID of the proposal to vote on
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Register the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /// @notice Retrieves the details of a proposal
    /// @param proposalId ID of the proposal to retrieve
    /// @return id Proposal ID, description, vote count
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (uint256 id, string memory description, uint256 voteCount)
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```
