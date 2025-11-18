"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Write a smart contract in Solidity to enable governance voting for ORB token holders on the Zealy platform, allowing them to make decisions on proposals.
Generated: DETERMINISTIC_d84c368cad53d0b1
Batch ID: 20250612_150858
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

/// @title Governance Voting Contract
/// @notice This contract allows ORB token holders to vote on proposals
/// @dev The contract uses a mapping to keep track of proposals and votes
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes received
        address creator; // Address of the proposal creator
        mapping(address => bool) votes; // Records whether an address has voted
    }

    // State variables
    address public owner; // Owner of the contract
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals

    // Events for logging
    event ProposalCreated(uint256 id, string description, address creator);
    event Voted(uint256 proposalId, address voter);

    /// @dev Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /// @dev Modifier to ensure proposal exists
    /// @param _proposalId The ID of the proposal
    modifier proposalExists(uint256 _proposalId) {
        require(_proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    /// @notice Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
    }

    /// @notice Create a new proposal
    /// @param _description The description of the proposal
    function createProposal(string calldata _description) external {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.creator = msg.sender;
        
        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /// @notice Vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    function vote(uint256 _proposalId) external proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the sender has already voted
        require(!proposal.votes[msg.sender], "You have already voted");

        // Record the vote
        proposal.votes[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /// @notice Get the current vote count for a proposal
    /// @param _proposalId The ID of the proposal
    /// @return The current vote count
    function getVoteCount(uint256 _proposalId) external view proposalExists(_proposalId) returns (uint256) {
        return proposals[_proposalId].voteCount;
    }

    /// @notice Get proposal details
    /// @param _proposalId The ID of the proposal
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The current vote count
    /// @return creator The address of the proposal creator
    function getProposalDetails(uint256 _proposalId) external view proposalExists(_proposalId) returns (uint256 id, string memory description, uint256 voteCount, address creator) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.creator);
    }
}
```
