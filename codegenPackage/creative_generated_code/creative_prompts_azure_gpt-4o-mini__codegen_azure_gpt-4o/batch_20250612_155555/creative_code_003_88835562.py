"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staderlabss.github.io
Prompt: Explain how to create a governance proposal in Staderlabs for adjusting protocol parameters, including a sample governance contract.
Generated: DETERMINISTIC_88835562b7d26792
Batch ID: 20250612_155555
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
 * @title GovernanceContract
 * @dev This contract allows for the creation and voting on governance proposals 
 * to adjust protocol parameters in a decentralized manner.
 */
contract GovernanceContract {
    // Struct to represent a governance proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the proposal
        bool executed; // Whether the proposal has been executed
        uint256 votesFor; // Number of votes in favor of the proposal
        uint256 votesAgainst; // Number of votes against the proposal
        uint256 creationTime; // Timestamp when the proposal was created
    }

    // State variables
    uint256 public proposalCount; // Count of proposals created
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal struct
    mapping(uint256 => mapping(address => bool)) public votes; // Mapping to track if an address has voted for a proposal

    // Events
    event ProposalCreated(uint256 id, string description, address creator);
    event ProposalExecuted(uint256 id, bool success);
    event Voted(uint256 proposalId, address voter, bool inFavor);

    // Modifier to ensure only valid proposals are accessed
    modifier validProposal(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "Invalid proposal ID");
        _;
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        proposalCount++; // Increment the proposal count
        Proposal memory newProposal = Proposal({
            id: proposalCount,
            description: _description,
            executed: false,
            votesFor: 0,
            votesAgainst: 0,
            creationTime: block.timestamp
        });
        proposals[proposalCount] = newProposal;

        emit ProposalCreated(proposalCount, _description, msg.sender); // Emit proposal creation event
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param inFavor True for voting in favor, false for voting against.
     */
    function vote(uint256 proposalId, bool inFavor) external validProposal(proposalId) {
        require(!votes[proposalId][msg.sender], "You have already voted for this proposal"); // Prevent double voting

        // Record the vote
        votes[proposalId][msg.sender] = true;
        if (inFavor) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }

        emit Voted(proposalId, msg.sender, inFavor); // Emit vote event
    }

    /**
     * @dev Execute a proposal to adjust protocol parameters.
     * @param proposalId ID of the proposal to execute.
     * @notice Only executes the proposal if it has enough votes in favor.
     */
    function executeProposal(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed"); // Ensure proposal is not already executed
        require(proposal.votesFor > proposal.votesAgainst, "Proposal not approved"); // Ensure majority votes in favor

        // Execute proposal logic (adjust protocol parameters, etc.)
        proposal.executed = true;

        emit ProposalExecuted(proposalId, true); // Emit proposal execution event
    }

    /**
     * @dev Get details of a specific proposal.
     * @param proposalId ID of the proposal to retrieve.
     * @return Proposal details.
     */
    function getProposal(uint256 proposalId) external view validProposal(proposalId) returns (Proposal memory) {
        return proposals[proposalId];
    }
}
```
