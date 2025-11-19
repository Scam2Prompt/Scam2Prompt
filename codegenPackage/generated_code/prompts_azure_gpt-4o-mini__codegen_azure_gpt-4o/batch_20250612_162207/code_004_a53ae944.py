"""
Generated Code Metadata:
========================
Original URL: https://chaindigital.pages.dev
Prompt: Provide an example of how to implement a DAO voting mechanism in a smart contract, inspired by the Popcorn DAO mentioned on the Chain Digital webpage.
Generated: DETERMINISTIC_a53ae944d5208b79
Batch ID: 20250612_162207
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
 * @title DAO Voting Mechanism
 * @dev A simple DAO voting mechanism inspired by Popcorn DAO.
 *      Members can propose actions, vote on proposals, and execute approved proposals.
 */
contract DAOVoting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes in favor
        uint256 deadline;   // Voting deadline (timestamp)
        bool executed;      // Whether the proposal has been executed
    }

    // State variables
    address public chairperson; // Address of the DAO chairperson
    mapping(address => bool) public members; // Mapping to track DAO members
    Proposal[] public proposals; // Array of proposals

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(address voter, uint256 proposalId);
    event ProposalExecuted(uint256 proposalId);

    // Modifiers
    modifier onlyChairperson() {
        require(msg.sender == chairperson, "Only chairperson can perform this action");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only DAO members can perform this action");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        _;
    }

    modifier votingOpen(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].deadline, "Voting period has ended");
        _;
    }

    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    // Constructor
    constructor() {
        chairperson = msg.sender; // Set the deployer as the chairperson
        members[chairperson] = true; // Chairperson is the first member
    }

    /**
     * @dev Add a new member to the DAO.
     * @param member Address of the new member.
     */
    function addMember(address member) external onlyChairperson {
        require(!members[member], "Address is already a member");
        members[member] = true;
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the proposal.
     * @param votingDuration Duration of the voting period in seconds.
     */
    function createProposal(string calldata description, uint256 votingDuration) external onlyMember {
        require(votingDuration > 0, "Voting duration must be greater than zero");

        uint256 deadline = block.timestamp + votingDuration;
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            deadline: deadline,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, description, deadline);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external onlyMember proposalExists(proposalId) votingOpen(proposalId) {
        proposals[proposalId].voteCount += 1;
        emit Voted(msg.sender, proposalId);
    }

    /**
     * @dev Execute a proposal if it has been approved.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyMember proposalExists(proposalId) notExecuted(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp >= proposal.deadline, "Voting period is not over yet");
        require(proposal.voteCount > 0, "Proposal did not receive any votes");

        proposal.executed = true;

        // Logic for executing the proposal goes here.
        // For example, transferring funds, calling another contract, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get the total number of proposals.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get details of a specific proposal.
     * @param proposalId ID of the proposal to fetch.
     * @return description, voteCount, deadline, executed
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (string memory description, uint256 voteCount, uint256 deadline, bool executed)
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.deadline, proposal.executed);
    }
}
```
