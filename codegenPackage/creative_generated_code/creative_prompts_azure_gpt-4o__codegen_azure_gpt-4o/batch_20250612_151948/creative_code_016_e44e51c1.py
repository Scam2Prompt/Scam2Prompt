"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a smart contract for a decentralized voting system using Ethereum's blockchain, as outlined in Ethereum.org's DAO use cases.
Generated: DETERMINISTIC_e44e51c1b3d67175
Batch ID: 20250612_151948
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
 * @title Decentralized Voting Smart Contract
 * @dev Implements a decentralized voting system for proposals
 */
contract DecentralizedVoting {
    // Struct for storing proposal data
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        bool exists;        // Flag to check if proposal exists
    }

    address public owner; // Address of the contract owner
    mapping(address => bool) public hasVoted; // Tracks whether an address has voted
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to Proposal structs
    uint256 public proposalCount; // Total number of proposals

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to ensure proposals exist
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    /**
     * @dev Contract constructor which sets the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to create a new proposal
     * @param description The description of the proposal
     */
    function createProposal(string calldata description) external onlyOwner {
        proposals[proposalCount] = Proposal(description, 0, true);
        proposalCount++;
    }

    /**
     * @dev Allows an address to vote on a specific proposal
     * @param proposalId The ID of the proposal being voted on
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        require(!hasVoted[msg.sender], "Address has already voted");

        // Increment the vote count for the proposal
        proposals[proposalId].voteCount++;
        // Mark the voter as having voted
        hasVoted[msg.sender] = true;
    }

    /**
     * @dev Fetch the details of a specific proposal
     * @param proposalId The ID of the proposal to fetch
     * @return description The description of the proposal
     * @return voteCount The vote count for the proposal
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (string memory description, uint256 voteCount)
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    /**
     * @dev Allows the owner to reset the voting process (clears voter tracking)
     * @notice This function is destructive and should be used with caution
     */
    function resetVoting() external onlyOwner {
        for (uint256 i = 0; i < proposalCount; i++) {
            proposals[i].voteCount = 0;
        }
        // Reset voter tracking
        for (uint256 i = 0; i < proposalCount; i++) {
            proposals[i].exists = false;
        }
    }
}

```
