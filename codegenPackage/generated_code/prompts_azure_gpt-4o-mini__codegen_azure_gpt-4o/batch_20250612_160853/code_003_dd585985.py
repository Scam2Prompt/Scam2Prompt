"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a Solidity smart contract that allows users to vote on governance proposals within the Zushi ecosystem.
Generated: DETERMINISTIC_dd58598547177d8e
Batch ID: 20250612_160853
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
 * @title ZushiGovernance
 * @dev A smart contract for governance voting within the Zushi ecosystem.
 */
contract ZushiGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Total votes received
        bool active; // Whether the proposal is active
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Address of the contract owner
    address public owner;

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalClosed(uint256 id);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if a proposal is active
    modifier isActive(uint256 proposalId) {
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            voteCount: 0,
            active: true
        });

        emit ProposalCreated(proposalCounter, _description);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external isActive(_proposalId) {
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the vote
        hasVoted[_proposalId][msg.sender] = true;

        // Increment the vote count
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Function to close a proposal.
     * @param _proposalId The ID of the proposal to close.
     */
    function closeProposal(uint256 _proposalId) external onlyOwner isActive(_proposalId) {
        proposals[_proposalId].active = false;

        emit ProposalClosed(_proposalId);
    }

    /**
     * @dev Function to get details of a proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return id The ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The total votes received.
     * @return active Whether the proposal is active.
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            string memory description,
            uint256 voteCount,
            bool active
        )
    {
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
