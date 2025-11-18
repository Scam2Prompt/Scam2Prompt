"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Provide code to create a blockchain-based voting system for a community project, referencing the Keyboard Cat smart contract address.
Generated: DETERMINISTIC_b4957da682643e24
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

/**
 * @title Blockchain-Based Voting System
 * @dev Implements a simple voting system for a community project.
 *      References the Keyboard Cat smart contract address for verification purposes.
 */
contract CommunityVoting {
    // Address of the Keyboard Cat smart contract for reference
    address public keyboardCatContractAddress;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes the proposal has received
    }

    // Array to store all proposals
    Proposal[] public proposals;

    // Mapping to track if an address has already voted
    mapping(address => bool) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _keyboardCatContractAddress Address of the Keyboard Cat smart contract.
     */
    constructor(address _keyboardCatContractAddress) {
        require(_keyboardCatContractAddress != address(0), "Invalid Keyboard Cat contract address");
        keyboardCatContractAddress = _keyboardCatContractAddress;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description A description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        // Create a new proposal and add it to the proposals array
        proposals.push(Proposal({description: _description, voteCount: 0}));

        // Emit the ProposalCreated event
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Function to vote for a proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[msg.sender], "You have already voted");

        // Mark the sender's address as having voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the selected proposal
        proposals[_proposalId].voteCount += 1;

        // Emit the VoteCast event
        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Function to retrieve the total number of proposals.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Function to get details of a specific proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return description The description of the proposal.
     * @return voteCount The number of votes the proposal has received.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount);
    }
}
```
