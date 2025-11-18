"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a Solidity contract to implement governance voting for $AI holders, allowing community decisions on interchain DApp development.
Generated: DETERMINISTIC_5efea35c1a1e5ca7
Batch ID: 20250612_152439
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
 * @dev This contract allows $AI token holders to participate in governance voting
 *      for interchain DApp development decisions.
 */
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 voteCount; // Total votes cast for this proposal
        mapping(address => bool) voters; // Track whether an address has voted
        bool active; // Indicates if the proposal is still active
    }

    // State variables
    address public owner; // Address of the contract owner
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    uint256 public proposalCount; // Counter for number of proposals

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    // Modifier to check if the proposal is active
    modifier proposalActive(uint256 proposalId) {
        require(proposals[proposalId].active, "Proposal is not active");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string calldata _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.active = true;

        emit ProposalCreated(newProposal.id, _description);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) proposalActive(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Close a proposal, making it inactive
     * @param proposalId ID of the proposal to close
     */
    function closeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        proposals[proposalId].active = false;
    }

    /**
     * @dev Get the details of a proposal
     * @param proposalId ID of the proposal
     * @return id ID of the proposal
     * @return description Description of the proposal
     * @return voteCount Total votes for the proposal
     * @return active Whether the proposal is active
     */
    function getProposal(uint256 proposalId) 
        external 
        view 
        proposalExists(proposalId) 
        returns (
            uint256 id,
            string memory description,
            uint256 voteCount,
            bool active
        ) 
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }
}
```
