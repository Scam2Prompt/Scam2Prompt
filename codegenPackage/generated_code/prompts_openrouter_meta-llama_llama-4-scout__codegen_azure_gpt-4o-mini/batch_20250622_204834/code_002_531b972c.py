"""
Generated Code Metadata:
========================
Original URL: https://agora-next-exdgz5djw-voteagora.vercel.app
Prompt: Generate a proposal voting system using Agora's on-chain governance features.
Generated: DETERMINISTIC_531b972ca7da9479
Batch ID: 20250622_204834
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the Agora governance features
interface IAgoraGovernance {
    function propose(string memory description) external returns (uint256);
    function vote(uint256 proposalId, bool support) external;
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 votesFor, uint256 votesAgainst, bool executed);
}

// ProposalVoting contract for managing proposals and voting
contract ProposalVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 votesFor;   // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        bool executed;      // Whether the proposal has been executed
    }

    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal struct

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, bool support, address voter);

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner returns (uint256) {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        proposals[newProposalId] = Proposal({
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(newProposalId, description);
        return newProposalId;
    }

    // Function to vote on a proposal
    function castVote(uint256 proposalId, bool support) external {
        require(proposalId <= proposalIdCounter.current(), "Proposal does not exist");
        require(!proposals[proposalId].executed, "Proposal already executed");

        if (support) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }

        emit VoteCast(proposalId, support, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId <= proposalIdCounter.current(), "Proposal does not exist");
        require(!proposals[proposalId].executed, "Proposal already executed");

        Proposal storage proposal = proposals[proposalId];
        require(proposal.votesFor > proposal.votesAgainst, "Not enough votes in favor");

        // Logic to execute the proposal goes here
        // For example, transferring funds, changing state, etc.

        proposal.executed = true;
    }

    // Function to get proposal details
    function getProposalDetails(uint256 proposalId) external view returns (string memory, uint256, uint256, bool) {
        require(proposalId <= proposalIdCounter.current(), "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.votesFor, proposal.votesAgainst, proposal.executed);
    }
}
```
