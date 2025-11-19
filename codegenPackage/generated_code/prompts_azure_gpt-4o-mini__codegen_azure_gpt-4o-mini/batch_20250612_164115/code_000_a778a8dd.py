"""
Generated Code Metadata:
========================
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: How can I implement on-chain governance using the Agora platform for proposal voting?
Generated: DETERMINISTIC_a778a8ddebf1d19f
Batch ID: 20250612_164115
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

// Interface for the Agora platform
interface IAgora {
    function createProposal(string memory description) external returns (uint256);
    function vote(uint256 proposalId, bool support) external;
    function finalizeProposal(uint256 proposalId) external;
}

// On-chain governance contract using the Agora platform
contract OnChainGovernance is Ownable {
    using Counters for Counters.Counter;
    
    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool finalized;
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    Counters.Counter private proposalIdCounter;

    // Agora platform instance
    IAgora public agora;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);
    
    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, bool support, address voter);
    
    // Event emitted when a proposal is finalized
    event ProposalFinalized(uint256 indexed proposalId);

    // Constructor to set the Agora platform address
    constructor(IAgora _agora) {
        agora = _agora;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        uint256 proposalId = agora.createProposal(description);
        proposals[proposalId] = Proposal(proposalId, description, 0, 0, false);
        emit ProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");
        require(!proposals[proposalId].finalized, "Proposal already finalized");

        // Cast the vote using the Agora platform
        agora.vote(proposalId, support);

        // Update local proposal vote counts
        if (support) {
            proposals[proposalId].votesFor++;
        } else {
            proposals[proposalId].votesAgainst++;
        }

        emit VoteCast(proposalId, support, msg.sender);
    }

    // Function to finalize a proposal
    function finalizeProposal(uint256 proposalId) external onlyOwner {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");
        require(!proposals[proposalId].finalized, "Proposal already finalized");

        // Finalize the proposal using the Agora platform
        agora.finalizeProposal(proposalId);
        proposals[proposalId].finalized = true;

        emit ProposalFinalized(proposalId);
    }
}
```
