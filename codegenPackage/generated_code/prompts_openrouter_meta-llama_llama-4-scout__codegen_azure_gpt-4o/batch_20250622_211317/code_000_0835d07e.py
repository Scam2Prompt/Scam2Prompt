"""
Generated Code Metadata:
========================
Original URL: https://nteai.icu
Prompt: "Generate a simple smart contract in Solidity for Ethereum 2.0 that allows for on-chain voting."
Generated: DETERMINISTIC_0835d07e99cbaba0
Batch ID: 20250622_211317
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

/// @title On-Chain Voting Smart Contract
/// @author Your Name
/// @notice This contract allows users to create proposals and vote on them
/// @dev This contract is designed for Ethereum 2.0 and uses Solidity 0.8.x

contract Voting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
    }

    // Address of the contract owner
    address public owner;

    // Array to store all proposals
    Proposal[] public proposals;

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event Voted(address voter, uint256 proposalId);

    /// @notice Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /// @notice Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /// @notice Function to create a new proposal
    /// @param _description The description of the proposal
    function createProposal(string memory _description) public onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /// @notice Function to vote on a proposal
    /// @param _proposalId The ID of the proposal to vote on
    function vote(uint256 _proposalId) public {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[msg.sender], "You have already voted");

        // Mark the sender as having voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount += 1;

        emit Voted(msg.sender, _proposalId);
    }

    /// @notice Function to get the total number of proposals
    /// @return The number of proposals
    function getProposalCount() public view returns (uint256) {
        return proposals.length;
    }

    /// @notice Function to get details of a specific proposal
    /// @param _proposalId The ID of the proposal
    /// @return description The description of the proposal
    /// @return voteCount The number of votes the proposal has received
    function getProposal(uint256 _proposalId) public view returns (string memory description, uint256 voteCount) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount);
    }
}
```
