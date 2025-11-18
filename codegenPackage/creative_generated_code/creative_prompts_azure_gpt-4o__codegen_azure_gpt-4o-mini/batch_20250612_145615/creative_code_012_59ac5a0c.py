"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: Generate a Solidity function to implement Lightchain AI’s decentralized governance voting system for community proposals.
Generated: DETERMINISTIC_59ac5a0cdfe6d69c
Batch ID: 20250612_145615
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

/**
 * @title GovernanceContract
 * @dev This contract implements a decentralized governance voting system
 * for community proposals using the Lightchain AI framework.
 */
contract GovernanceContract {
    struct Proposal {
        uint id;
        string description;
        uint voteCount;
        mapping(address => bool) voters;
        bool exists;
    }

    event ProposalCreated(uint indexed proposalId, string description);
    event Voted(uint indexed proposalId, address indexed voter);
    
    mapping(uint => Proposal) public proposals; // Stores proposals
    uint public proposalsCount; // Counter for proposals

    /**
     * @dev Creates a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        
        proposalsCount++;
        Proposal storage newProposal = proposals[proposalsCount];
        newProposal.id = proposalsCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.exists = true;

        emit ProposalCreated(proposalsCount, _description);
    }

    /**
     * @dev Votes for a proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        
        require(proposal.exists, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voters[msg.sender] = true; // Mark the voter as having voted
        proposal.voteCount++; // Increment the vote count

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Retrieves the details of a proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return id The ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The number of votes the proposal has received.
     */
    function getProposal(uint _proposalId) external view returns (uint id, string memory description, uint voteCount) {
        Proposal storage proposal = proposals[_proposalId];
        
        require(proposal.exists, "Proposal does not exist");
        
        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```
