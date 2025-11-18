"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-popofrog.pages.dev
Prompt: Create a Solidity contract for a community-driven voting system where Popo Army members can vote on project decisions, aligning with Popo's community-backed philosophy.
Generated: DETERMINISTIC_8a7d323512947d3a
Batch ID: 20250612_150347
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

/// @title Popo Army Voting System
/// @notice A community-driven voting contract for Popo Army members to decide on project initiatives
contract PopoArmyVoting {
    // Struct to represent a voting proposal
    struct Proposal {
        string description;  // Description of the proposal
        uint256 voteCount;   // Current vote count
        mapping(address => bool) voters; // Track voters to prevent double voting
        bool active;         // Indicates if the proposal is active
    }

    // State variables
    address public owner; // The owner of the contract (could be the deployed account)
    Proposal[] public proposals; // Array of proposals
    uint256 public totalProposals; // Total number of proposals

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < totalProposals, "Proposal does not exist");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
    }

    /// @notice Create a new proposal
    /// @param description The description of the proposal
    function createProposal(string calldata description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.active = true;
        totalProposals++;

        emit ProposalCreated(totalProposals - 1, description);
    }

    /// @notice Vote for a proposal
    /// @param proposalId The ID of the proposal to vote on
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is not active");
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        // Record the voter's address
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /// @notice End a proposal and mark it as inactive
    /// @param proposalId The ID of the proposal to end
    function endProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is already inactive");

        proposal.active = false;
    }

    /// @notice Get details of a proposal
    /// @param proposalId The ID of the proposal to fetch
    /// @return description The description of the proposal
    /// @return voteCount The total vote count for the proposal
    /// @return active The active status of the proposal
    function getProposal(uint256 proposalId) external view proposalExists(proposalId)
        returns (string memory description, uint256 voteCount, bool active) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.active);
    }
}
```
