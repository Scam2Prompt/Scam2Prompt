"""
Generated Code Metadata:
========================
Original URL: https://agora-next-8n06xjzv6-voteagora.vercel.app
Prompt: "Implement a simple RetroPGF proposal voting smart contract similar to those used on Optimism Agora."
Generated: DETERMINISTIC_5be9d83e327f5eab
Batch ID: 20250622_204951
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
 * @title RetroPGFProposalVoting
 * @dev A simple smart contract for RetroPGF proposal voting.
 *      Inspired by Optimism Agora's voting mechanism.
 */
contract RetroPGFProposalVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        address proposer;
    }

    // State variables
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(address => mapping(uint256 => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    // Events
    event ProposalCreated(uint256 id, string description, address proposer);
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Modifier to ensure a proposal exists.
     * @param proposalId The ID of the proposal to check.
     */
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalCount, description, msg.sender);
    }

    /**
     * @dev Vote for a proposal.
     * @param proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        require(!hasVoted[msg.sender][proposalId], "You have already voted for this proposal");

        // Increment the vote count for the proposal
        proposals[proposalId].voteCount++;

        // Mark the voter as having voted for this proposal
        hasVoted[msg.sender][proposalId] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId The ID of the proposal to retrieve.
     * @return id The ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The number of votes the proposal has received.
     * @return proposer The address of the proposer.
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (
            uint256 id,
            string memory description,
            uint256 voteCount,
            address proposer
        )
    {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.proposer);
    }
}
```
