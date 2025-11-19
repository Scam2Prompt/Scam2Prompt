"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Create a decentralized voting system in Solidity that aligns with the governance model described for Global Miracle Coin, using the LYCAN Chain infrastructure.
Generated: DETERMINISTIC_8185ea6ca9798b5c
Batch ID: 20250612_152358
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

/// @title Decentralized Voting System for Global Miracle Coin
/// @author Your Name
/// @notice This contract allows users to create and participate in votes
/// @dev The contract uses a simple governance model for voting on proposals

contract Voting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
    }

    // State variables
    address public owner; // Owner of the contract
    Proposal[] public proposals; // Array of proposals
    uint256 public totalProposals; // Total number of proposals

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < totalProposals, "Proposal does not exist");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /// @notice Create a new proposal
    /// @param _description The description of the proposal
    function createProposal(string memory _description) public onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.voteCount = 0;
        totalProposals++;

        emit ProposalCreated(totalProposals - 1, _description);
    }

    /// @notice Vote for a proposal
    /// @param proposalId The ID of the proposal to vote for
    function vote(uint256 proposalId) public proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /// @notice Get the details of a proposal
    /// @param proposalId The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The number of votes received
    function getProposal(uint256 proposalId) 
        public 
        view 
        proposalExists(proposalId) 
        returns (string memory description, uint256 voteCount) 
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    /// @notice Get the total number of proposals
    /// @return The total number of proposals created
    function getTotalProposals() public view returns (uint256) {
        return totalProposals;
    }
}
```
