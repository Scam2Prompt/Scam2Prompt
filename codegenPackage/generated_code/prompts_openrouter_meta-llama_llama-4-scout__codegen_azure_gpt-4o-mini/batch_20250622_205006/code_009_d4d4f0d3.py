"""
Generated Code Metadata:
========================
Original URL: https://yawnsworld-io.web.app
Prompt: "Design a DAO (Decentralized Autonomous Organization) structure for the $YAWN community, including voting mechanisms, community milestones, and future direction proposals."
Generated: DETERMINISTIC_d4d4f0d38aa7eb55
Batch ID: 20250622_205006
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

// DAO contract for the $YAWN community
contract YawnDAO is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    Counters.Counter private proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;
    uint256 public totalProposals;
    uint256 public votingDuration; // Duration for voting in seconds
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the DAO
    constructor(uint256 _votingDuration) {
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();
        
        Proposal storage newProposal = proposals[newProposalId];
        newProposal.id = newProposalId;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        totalProposals++;
        emit ProposalCreated(newProposalId, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is not executed
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is not executed
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes to execute");

        // Execute the proposal (implementation depends on the proposal's nature)
        // For demonstration, we will just mark it as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");

        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }

    // Function to set a new voting duration
    function setVotingDuration(uint256 _newDuration) external onlyOwner {
        votingDuration = _newDuration;
    }
}
```
