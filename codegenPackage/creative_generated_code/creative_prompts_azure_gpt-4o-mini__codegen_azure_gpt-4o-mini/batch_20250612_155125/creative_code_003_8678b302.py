"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Provide an example of how to implement a governance voting system for the RACA DAO using a blockchain framework.
Generated: DETERMINISTIC_8678b3022368ba24
Batch ID: 20250612_155125
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

// Governance Voting contract for RACA DAO
contract RacaVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool exists;
    }

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);

    // State variables
    Counters.Counter private _proposalIdCounter;
    mapping(uint256 => Proposal) private proposals;

    // Modifiers
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external onlyOwner {
        _proposalIdCounter.increment();
        uint256 proposalId = _proposalIdCounter.current();

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        
        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view proposalExists(proposalId) returns (uint256, string memory, uint256) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }

    // Function to get total proposals created
    function getTotalProposals() external view returns (uint256) {
        return _proposalIdCounter.current();
    }
}
```

This smart contract creates a simple governance voting system for a decentralized autonomous organization (DAO) using Solidity. The contract allows the owner to create proposals and enables voting by other participants. Each proposal can be voted on only once by each address, ensuring transparency and integrity in the voting process.
