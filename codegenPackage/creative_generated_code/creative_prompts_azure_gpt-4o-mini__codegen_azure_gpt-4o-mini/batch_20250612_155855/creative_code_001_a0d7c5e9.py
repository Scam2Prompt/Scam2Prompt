"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: How can I implement a voting mechanism in a smart contract for the BULLDOGITO community to decide on new companies to join their ecosystem?
Generated: DETERMINISTIC_a0d7c5e94628d049
Batch ID: 20250612_155855
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

contract BulldogitoVoting {
    // Struct to represent a proposal
    struct Proposal {
        string companyName; // Name of the company proposed
        uint256 voteCount; // Number of votes for the proposal
        bool exists; // Check if proposal exists
    }

    // Mapping from proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string companyName);
    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Counter for proposals
    uint256 public proposalCount;

    // Function to create a new proposal
    function createProposal(string memory _companyName) public {
        require(bytes(_companyName).length > 0, "Company name must not be empty");
        
        uint256 proposalId = proposalCount++;
        proposals[proposalId] = Proposal({
            companyName: _companyName,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalId, _companyName);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) public {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount++;
        // Mark that this address has voted on the proposal
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender);
    }

    // Function to get the vote count of a proposal
    function getVoteCount(uint256 _proposalId) public view returns (uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return proposals[_proposalId].voteCount;
    }

    // Function to check if an address has voted on a proposal
    function hasVotedOnProposal(uint256 _proposalId, address _voter) public view returns (bool) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return hasVoted[_proposalId][_voter];
    }
}
```
