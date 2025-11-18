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

/**
 * @title OptimismProposalVoting
 * @dev This contract tracks voting results for Optimism proposals while adhering to Agora's governance structure.
 */
contract OptimismProposalVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Proposal ID
        string description; // Proposal description
        uint256 yesVotes; // Number of votes in favor
        uint256 noVotes; // Number of votes against
        bool exists; // Boolean flag to check if the proposal exists
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, bool voteType, address voter);

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param proposalId The unique ID of the proposal.
     * @param description A brief description of the proposal.
     */
    function createProposal(uint256 proposalId, string memory description) external {
        require(!proposals[proposalId].exists, "Proposal ID already exists");

        // Create and store the new proposal
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            yesVotes: 0,
            noVotes: 0,
            exists: true
        });

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Function to cast a vote for a proposal.
     * @param proposalId The unique ID of the proposal to vote for.
     * @param voteType True for a "Yes" vote, false for a "No" vote.
     */
    function castVote(uint256 proposalId, bool voteType) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Increment the vote count based on the vote type
        if (voteType) {
            proposal.yesVotes++;
        } else {
            proposal.noVotes++;
        }

        emit VoteCast(proposalId, voteType, msg.sender);
    }

    /**
     * @dev Function to get the current voting results for a proposal.
     * @param proposalId The unique ID of the proposal.
     * @return yesVotes Number of "Yes" votes for the proposal.
     * @return noVotes Number of "No" votes for the proposal.
     */
    function getVotingResults(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (uint256 yesVotes, uint256 noVotes)
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.yesVotes, proposal.noVotes);
    }
}
```
