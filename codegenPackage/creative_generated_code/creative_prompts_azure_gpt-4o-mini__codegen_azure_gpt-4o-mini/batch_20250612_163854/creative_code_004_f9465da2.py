"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Provide an example of a smart contract that integrates with Agora for managing voting on Optimism proposals.
Generated: DETERMINISTIC_f9465da2ad56bb80
Batch ID: 20250612_163854
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract VotingContract is Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _proposalIdCounter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
    }

    // Mapping from proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track votes per address
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        require(bytes(description).length > 0, "Description cannot be empty");

        uint256 proposalId = _proposalIdCounter.current();
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            executed: false
        });

        _proposalIdCounter.increment();
        emit ProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id == proposalId, "Proposal does not exist");
        require(!hasVoted[proposalId][msg.sender], "You have already voted");
        require(!proposal.executed, "Proposal already executed");

        // Cast vote
        proposal.voteCount += 1;
        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.id == proposalId, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");

        // Placeholder logic for proposal execution
        // Actual implementation will depend on the proposal requirements

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Function to get proposal details
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");
        return proposals[proposalId];
    }
}
```
