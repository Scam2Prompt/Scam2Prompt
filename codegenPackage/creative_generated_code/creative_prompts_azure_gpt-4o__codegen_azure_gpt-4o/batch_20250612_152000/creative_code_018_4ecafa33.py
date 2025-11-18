"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Write a Solidity contract to implement a voting system for Metis Community Ecosystem Governance (CEG) with decentralized decision-making.
Generated: DETERMINISTIC_4ecafa3328f57e77
Batch ID: 20250612_152000
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
 * @title Metis Community Ecosystem Governance Voting Contract
 * @dev A decentralized voting system for governance within the Metis community ecosystem.
 */
contract MetisCEGVoting {
    // Structure that stores details about a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Proposal description
        uint256 voteCount; // Number of votes received
        bool executed; // Whether the proposal has been executed or not
    }

    // Mapping from proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted for a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter to generate proposal IDs
    uint256 private proposalCount;

    // Address of the contract owner
    address public owner;

    // Events for logging important contract activities
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to ensure proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to create a new proposal.
     * @param description Proposal description
     */
    function createProposal(string memory description) external onlyOwner {
        require(bytes(description).length > 0, "Description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Allows an address to vote on a specific proposal.
     * @param proposalId Proposal ID to vote on
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted");
        require(!proposals[proposalId].executed, "Proposal has already been executed");

        proposals[proposalId].voteCount += 1;
        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Executes a proposal if certain criteria are met (e.g., majority votes).
     * @param proposalId Proposal ID to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        require(!proposals[proposalId].executed, "Proposal already executed");

        // Placeholder logic: Assuming majority is achieved if voteCount > 1
        require(proposals[proposalId].voteCount > 1, "Not enough votes to execute");

        proposals[proposalId].executed = true;

        emit ProposalExecuted(proposalId);

        // Add your on-chain execution logic here if needed.
    }

    /**
     * @dev Returns details of a specific proposal.
     * @param proposalId Proposal ID to retrieve
     * @return id Proposal ID
     * @return description Proposal description
     * @return voteCount Number of votes received
     * @return executed Whether the proposal has been executed
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (uint256 id, string memory description, uint256 voteCount, bool executed)
    {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
