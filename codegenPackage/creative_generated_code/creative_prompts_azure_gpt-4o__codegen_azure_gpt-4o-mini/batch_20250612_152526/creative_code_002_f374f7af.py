"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Create a governance voting system for a decentralized application using the Community Ecosystem Governance (CEG) framework on Metis. Include code that integrates with Metis's decentralized voting features.
Generated: DETERMINISTIC_f374f7af1c8345ea
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@metis.io/governance-framework/contracts/Governance.sol";
import "@metis.io/governance-framework/contracts/Token.sol";

contract CommunityGovernance {
    Governance public governance; // Governance contract instance
    Token public token; // Token instance for voting

    // Proposal structure to hold proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    uint256 public proposalCount; // Counter for proposals

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    
    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Constructor to initialize governance and token
    constructor(address _governanceAddress, address _tokenAddress) {
        governance = Governance(_governanceAddress);
        token = Token(_tokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public {
        require(governance.isActive(msg.sender), "Only active members can create proposals.");
        
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) public {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist."); // Ensure proposal exists
        require(!proposal.executed, "Proposal already executed."); // Ensure proposal not executed
        require(!proposal.voters[msg.sender], "You have already voted."); // Ensure voter hasn't voted

        uint256 voterTokenBalance = token.balanceOf(msg.sender); // Get voter's token balance
        require(voterTokenBalance > 0, "You must hold tokens to vote."); // Ensure voter is eligible

        proposal.voters[msg.sender] = true; // Mark voter as having voted
        proposal.voteCount += voterTokenBalance; // Increment vote count by voter's token balance

        emit VoteCast(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) public {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id != 0, "Proposal does not exist."); // Ensure proposal exists
        require(!proposal.executed, "Proposal already executed."); // Ensure proposal not executed
        require(proposal.voteCount > (token.totalSupply() / 2), "Not enough votes to execute."); // Check if proposal passed

        // Execute the proposal (implementation will depend on specific governance rules)
        // Example: governance.executeAction(proposal.action);

        proposal.executed = true; // Mark proposal as executed
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) public view returns (uint256, string memory, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.executed);
    }
}
```
