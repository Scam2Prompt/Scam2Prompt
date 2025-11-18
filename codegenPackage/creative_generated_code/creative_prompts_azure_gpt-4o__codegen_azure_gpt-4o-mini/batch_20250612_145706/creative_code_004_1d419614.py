"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Generate a function in Solidity that tracks voting results for Optimism proposals, ensuring compatibility with Agora's governance structure.
Generated: DETERMINISTIC_1d419614dea3fe79
Batch ID: 20250612_145706
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

contract OptimismVoting {
    // Enum to represent the state of a proposal
    enum ProposalState { Active, Closed }

    // Structure to represent a voting proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        uint256 voteCountFor; // Count of votes in favor
        uint256 voteCountAgainst; // Count of votes against
        ProposalState state; // Current state of the proposal
        mapping(address => bool) hasVoted; // Track whether an address has voted
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Counter for proposal IDs
    uint256 public proposalCounter;

    // Event to emit when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event to emit when a vote is cast
    event VoteCast(uint256 indexed proposalId, address voter, bool support);

    // Function to create a new proposal
    function createProposal(string calldata description) external {
        proposalCounter++;
        Proposal storage newProposal = proposals[proposalCounter];
        newProposal.id = proposalCounter;
        newProposal.description = description;
        newProposal.state = ProposalState.Active;

        emit ProposalCreated(proposalCounter, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        // Ensure the proposal exists
        require(proposalId > 0 && proposalId <= proposalCounter, "Proposal does not exist.");
        
        Proposal storage proposal = proposals[proposalId];
        
        // Ensure the proposal is still active
        require(proposal.state == ProposalState.Active, "Proposal voting is closed.");
        
        // Check if the voter has already voted
        require(!proposal.hasVoted[msg.sender], "You have already voted.");

        // Record the vote
        proposal.hasVoted[msg.sender] = true;
        
        // Count the vote
        if (support) {
            proposal.voteCountFor++;
        } else {
            proposal.voteCountAgainst++;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to close a proposal and finalize results
    function closeProposal(uint256 proposalId) external {
        // Ensure the proposal exists
        require(proposalId > 0 && proposalId <= proposalCounter, "Proposal does not exist.");

        Proposal storage proposal = proposals[proposalId];

        // Ensure the proposal is currently active
        require(proposal.state == ProposalState.Active, "Proposal is already closed.");

        // Set the proposal state to closed
        proposal.state = ProposalState.Closed;
    }

    // Function to get the results of a closed proposal
    function getProposalResults(uint256 proposalId) external view returns (uint256 votesFor, uint256 votesAgainst, ProposalState state) {
        // Ensure the proposal exists
        require(proposalId > 0 && proposalId <= proposalCounter, "Proposal does not exist.");

        Proposal storage proposal = proposals[proposalId];
        
        // Return the proposal results
        return (proposal.voteCountFor, proposal.voteCountAgainst, proposal.state);
    }
}
```
