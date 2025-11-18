"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Write a smart contract to implement a voting mechanism similar to the Mitosis Rewards system.
Generated: DETERMINISTIC_b5012785b551fa8e
Batch ID: 20250612_150228
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
 * @title VotingContract
 * @dev Implements a voting mechanism similar to Mitosis Rewards system.
 * Users can vote on proposals, and weights can be optionally assigned to votes.
 */
contract VotingContract {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;   // Total votes received
        bool active;         // Status of the proposal
    }

    // Mapping to store votes for each address (address => proposal index => weight)
    mapping(address => mapping(uint256 => uint256)) public votes;

    // List of proposals
    Proposal[] public proposals;

    // Address of the contract owner
    address public owner;

    // Events to emit important actions
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(address indexed voter, uint256 proposalId, uint256 weight);
    event ProposalStatusChanged(uint256 proposalId, bool active);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if the proposal is active
    modifier isActive(uint256 proposalId) {
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposals.push(Proposal({description: _description, voteCount: 0, active: true}));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal with a specific weight.
     * @param proposalId The ID of the proposal to vote on.
     * @param weight The weight/amount of the vote.
     */
    function vote(uint256 proposalId, uint256 weight) external isActive(proposalId) {
        require(weight > 0, "Vote weight must be greater than 0");
        require(proposalId < proposals.length, "Invalid proposal ID");

        // Ensure the voter has not already voted on the proposal
        require(votes[msg.sender][proposalId] == 0, "You have already voted on this proposal");

        // Record the vote
        votes[msg.sender][proposalId] = weight;

        // Update the proposal's vote count
        proposals[proposalId].voteCount += weight;

        emit Voted(msg.sender, proposalId, weight);
    }

    /**
     * @dev Get details of a proposal by its ID.
     * @param proposalId The ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Total votes received.
     * @return active Status of the proposal.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, bool active) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.active);
    }

    /**
     * @dev Changes the status of a proposal (active/inactive).
     * @param proposalId The ID of the proposal.
     * @param status The new status of the proposal.
     */
    function changeProposalStatus(uint256 proposalId, bool status) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        proposals[proposalId].active = status;
        emit ProposalStatusChanged(proposalId, status);
    }

    /**
     * @dev Gets the total number of proposals.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
