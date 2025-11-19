"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Describe the steps to integrate a governance model for a mutual insurance cooperative like Nexus Mutual using Ethereum smart contracts.
Generated: DETERMINISTIC_43110c46c22a292c
Batch ID: 20250612_155956
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Governance contract for a mutual insurance cooperative
contract MutualInsuranceGovernance is Ownable {
    
    // Enum to define different governance states
    enum State { Active, Suspended, Closed }

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        State state;
        mapping(address => bool) hasVoted;
    }

    // Mapping from proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Events for logging proposal actions
    event ProposalCreated(uint256 id, address proposer, string description);
    event Voted(uint256 proposalId, address voter, bool inFavor);
    event ProposalFinalized(uint256 proposalId, bool passed);

    // Function to create a new proposal
    function createProposal(string calldata _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.votesFor = 0;
        newProposal.votesAgainst = 0;
        newProposal.state = State.Active;

        emit ProposalCreated(proposalCount, msg.sender, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId, bool _inFavor) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.state == State.Active, "Proposal is not active");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Record the vote
        proposal.hasVoted[msg.sender] = true;
        if (_inFavor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit Voted(_proposalId, msg.sender, _inFavor);
    }

    // Function to finalize a proposal based on votes
    function finalizeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.state == State.Active, "Proposal is not active");

        // Determine if the proposal passed
        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.state = State.Closed; // Proposal passed
            emit ProposalFinalized(_proposalId, true);
        } else {
            proposal.state = State.Suspended; // Proposal failed
            emit ProposalFinalized(_proposalId, false);
        }
    }

    // Function to retrieve the proposal details
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 votesFor,
        uint256 votesAgainst,
        State state
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.state
        );
    }
}
```
