"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Describe the steps to integrate a governance model for a mutual insurance cooperative like Nexus Mutual using Ethereum smart contracts.
Generated: DETERMINISTIC_43110c46c22a292c
Batch ID: 20250612_155956
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
 * @title GovernanceModel
 * @dev A governance model for a mutual insurance cooperative like Nexus Mutual, using Ethereum smart contracts.
 * Provides functionality for member voting, proposal management, and execution of approved proposals.
 */
contract GovernanceModel {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 votesFor; // Total votes in favor
        uint256 votesAgainst; // Total votes against
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
        uint256 endTime; // Voting deadline
    }

    // Mapping of proposalId to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether a member has voted for a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // List of members in the cooperative
    mapping(address => bool) public members;

    // Total number of proposals created
    uint256 public proposalCount;

    // Modifier to restrict access to members only
    modifier onlyMember() {
        require(members[msg.sender], "Only members can call this function");
        _;
    }

    // Modifier to ensure a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed id, address indexed proposer, string description, uint256 endTime);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed id);

    /**
     * @dev Constructor to initialize members.
     * @param initialMembers List of member addresses to initialize the cooperative.
     */
    constructor(address[] memory initialMembers) {
        for (uint256 i = 0; i < initialMembers.length; i++) {
            members[initialMembers[i]] = true;
        }
    }

    /**
     * @dev Function to create a new proposal.
     * @param description The proposal description.
     * @param duration Voting duration in seconds.
     */
    function createProposal(string memory description, uint256 duration) external onlyMember {
        require(duration > 0, "Duration must be greater than zero");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            proposer: msg.sender,
            executed: false,
            endTime: block.timestamp + duration
        });

        emit ProposalCreated(proposalId, msg.sender, description, block.timestamp + duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support) external onlyMember proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "You have already voted");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(msg.sender, proposalId, support);
    }

    /**
     * @dev Function to execute a proposal if it is approved.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyMember proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period is still ongoing");
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal was not approved");

        proposal.executed = true;

        // Logic for executing the proposal can be added here.
        // For now, we're only marking it as executed.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Function to add a new member to the cooperative. Only existing members can add others.
     * @param newMember The address of the new member to add.
     */
    function addMember(address newMember) external onlyMember {
        require(!members[newMember], "Address is already a member");
        members[newMember] = true;
    }

    /**
     * @dev Function to remove a member from the cooperative. Only existing members can remove others.
     * @param member The address of the member to remove.
     */
    function removeMember(address member) external onlyMember {
        require(members[member], "Address is not a member");
        members[member] = false;
    }
}
```
