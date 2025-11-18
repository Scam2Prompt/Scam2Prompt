"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: Create a smart contract that supports proposal creation within a DAO, inspired by the features showcased on the MetaDAO demo page.
Generated: DETERMINISTIC_29d75c711e3dbfa9
Batch ID: 20250612_150545
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

// Struct to represent a proposal
struct Proposal {
    uint256 id;
    string description;
    address proposer;
    uint256 voteCount;
    bool isActive;
}

// Smart contract for a Decentralized Autonomous Organization (DAO)
contract DAO is Ownable {
    using Counters for Counters.Counter;

    // Events for logging proposal creation and voting
    event ProposalCreated(uint256 id, string description, address indexed proposer);
    event Voted(uint256 proposalId, address indexed voter);
    event ProposalExecuted(uint256 proposalId);

    // State variables
    Counters.Counter private proposalIdCounter; // Counter for unique proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    mapping(address => mapping(uint256 => bool)) public votes; // Mapping to track votes by address

    // Modifier to check if a proposal is active
    modifier onlyActiveProposal(uint256 proposalId) {
        require(proposals[proposalId].isActive, "Proposal is not active");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();

        proposals[newProposalId] = Proposal({
            id: newProposalId,
            description: _description,
            proposer: msg.sender,
            voteCount: 0,
            isActive: true
        });

        emit ProposalCreated(newProposalId, _description, msg.sender);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external onlyActiveProposal(proposalId) {
        require(!votes[msg.sender][proposalId], "You have already voted on this proposal");

        // Cast the vote
        votes[msg.sender][proposalId] = true;
        proposals[proposalId].voteCount += 1;

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 proposalId) external onlyActiveProposal(proposalId) {
        require(proposals[proposalId].voteCount > 0, "No votes cast for this proposal");

        // Mark the proposal as executed
        proposals[proposalId].isActive = false;

        emit ProposalExecuted(proposalId);
    }

    // Function to get details of a proposal
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        return proposals[proposalId];
    }

    // Function to get the total number of proposals
    function getTotalProposals() external view returns (uint256) {
        return proposalIdCounter.current();
    }
}
```
