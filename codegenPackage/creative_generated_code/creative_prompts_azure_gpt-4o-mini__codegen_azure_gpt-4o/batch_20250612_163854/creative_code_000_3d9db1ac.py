"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-jlesgw0mi-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform mentioned on the Optimism Agora website?
Generated: DETERMINISTIC_3d9db1ac4582f445
Batch ID: 20250612_163854
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
 * @title On-Chain Governance using Agora on Optimism
 * @dev This contract is a basic implementation of an on-chain governance system using the Agora platform
 *      for the Optimism network. It allows community members to propose and vote on decisions.
 */
contract AgoraGovernance {
    // State variables
    address public owner; // Contract owner (admin)
    uint256 public proposalCount; // Count of proposals

    // Struct for a proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the proposal
        uint256 voteCount; // Total votes received
        bool executed; // Whether the proposal has been executed
        uint256 creationTime; // Time when the proposal was created
        uint256 deadline; // Voting deadline (timestamp)
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if a proposal is active
    modifier isProposalActive(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].deadline, "Voting period has ended");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Create a new proposal
     * @param _description Description of the proposal
     * @param _votingPeriod Duration of the voting period in seconds
     */
    function createProposal(string memory _description, uint256 _votingPeriod) external onlyOwner {
        require(_votingPeriod > 0, "Voting period must be greater than zero");

        uint256 proposalId = proposalCount++;
        uint256 deadline = block.timestamp + _votingPeriod;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCount: 0,
            executed: false,
            creationTime: block.timestamp,
            deadline: deadline
        });

        emit ProposalCreated(proposalId, _description, deadline);
    }

    /**
     * @notice Vote on an active proposal
     * @param proposalId ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external isProposalActive(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");

        // Register the vote
        proposals[proposalId].voteCount++;
        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @notice Execute a proposal after the voting period ends
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        // Mark the proposal as executed
        proposal.executed = true;

        // Here you can add logic to implement the outcome of the proposal
        // For example, transferring funds, setting variables, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Get details of a proposal
     * @param proposalId ID of the proposal to fetch
     * @return Proposal struct
     */
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        return proposals[proposalId];
    }
}
```
