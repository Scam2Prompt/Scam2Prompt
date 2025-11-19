"""
Generated Code Metadata:
========================
Original URL: https://voting-consensys.app
Prompt: Write a voting system using Ethereum and ConsenSys, focusing on secure authentication and authorization.
Generated: DETERMINISTIC_339582b14c173084
Batch ID: 20250622_211022
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
 * @title VotingSystem
 * @dev A secure voting system using Ethereum blockchain.
 *      This contract allows authenticated users to vote on proposals.
 */
contract VotingSystem {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
    }

    // Mapping to store registered voters
    mapping(address => bool) public registeredVoters;

    // Mapping to track if a voter has already voted
    mapping(address => bool) public hasVoted;

    // Array to store all proposals
    Proposal[] public proposals;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    // Modifier to ensure the caller is a registered voter
    modifier onlyRegisteredVoter() {
        require(registeredVoters[msg.sender], "You must be a registered voter to perform this action.");
        _;
    }

    // Event emitted when a new proposal is added
    event ProposalAdded(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId);

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new voter.
     * @param voter Address of the voter to register.
     */
    function registerVoter(address voter) external onlyOwner {
        require(!registeredVoters[voter], "Voter is already registered.");
        registeredVoters[voter] = true;
    }

    /**
     * @dev Add a new proposal to the voting system.
     * @param description Description of the proposal.
     */
    function addProposal(string memory description) external onlyOwner {
        proposals.push(Proposal({description: description, voteCount: 0}));
        emit ProposalAdded(proposals.length - 1, description);
    }

    /**
     * @dev Cast a vote for a specific proposal.
     * @param proposalId ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external onlyRegisteredVoter {
        require(!hasVoted[msg.sender], "You have already voted.");
        require(proposalId < proposals.length, "Invalid proposal ID.");

        // Mark the voter as having voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the proposal
        proposals[proposalId].voteCount += 1;

        emit VoteCast(msg.sender, proposalId);
    }

    /**
     * @dev Get the details of a specific proposal.
     * @param proposalId ID of the proposal to retrieve.
     * @return description Description of the proposal.
     * @return voteCount Number of votes received by the proposal.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    /**
     * @dev Get the total number of proposals.
     * @return count Total number of proposals.
     */
    function getProposalCount() external view returns (uint256 count) {
        return proposals.length;
    }
}
```
