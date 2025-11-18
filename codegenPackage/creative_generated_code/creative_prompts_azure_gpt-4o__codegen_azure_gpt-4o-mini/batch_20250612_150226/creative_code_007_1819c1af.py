"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defikingdoms.pages.dev
Prompt: Write a Solidity contract to enable governance voting in DeFi Kingdoms, ensuring compatibility with the DFK Chain.
Generated: DETERMINISTIC_1819c1af041bcc22
Batch ID: 20250612_150226
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
 * @title GovernanceVoting
 * @dev A contract for managing governance voting in DeFi Kingdoms
 *      on the DFK Chain.
 */
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool isActive;
    }

    // The address of the contract owner
    address public owner;

    // Mapping of proposal id to Proposal struct
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if a proposal is active
    modifier isActiveProposal(uint256 proposalId) {
        require(proposals[proposalId].isActive, "Proposal is not active");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new proposal.
     * @param description A brief description of the proposal.
     */
    function createProposal(string calldata description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.isActive = true;
        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The id of the proposal being voted on.
     */
    function vote(uint256 proposalId) external isActiveProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voters[msg.sender], "You have already voted");

        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev End a proposal.
     * @param proposalId The id of the proposal to end.
     */
    function endProposal(uint256 proposalId) external onlyOwner isActiveProposal(proposalId) {
        proposals[proposalId].isActive = false;
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId The id of the proposal to retrieve.
     * @return id The id of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The current vote count for the proposal.
     * @return isActive Whether the proposal is still active.
     */
    function getProposal(uint256 proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, bool isActive) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.isActive);
    }
}
```
