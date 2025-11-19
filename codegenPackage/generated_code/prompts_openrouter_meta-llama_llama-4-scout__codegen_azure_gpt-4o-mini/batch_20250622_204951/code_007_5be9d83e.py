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

contract RetroPGFProposalVoting {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool exists;
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track whether an address has voted for a proposal
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    // Counter for proposal IDs
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Function to create a new proposal
    function createProposal(string memory _description) public {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote for a proposal
    function vote(uint256 _proposalId) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[msg.sender][_proposalId], "You have already voted for this proposal");

        // Record the vote
        hasVoted[msg.sender][_proposalId] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) public view returns (uint256, string memory, uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        Proposal memory proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount);
    }

    // Function to get the total number of proposals
    function getTotalProposals() public view returns (uint256) {
        return proposalCount;
    }
}
```
