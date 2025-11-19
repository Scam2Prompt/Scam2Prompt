"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Describe how to implement a voting system for token holders in a decentralized governance model, similar to the one used by Pushd token holders.
Generated: DETERMINISTIC_e1495ae576fe5dd9
Batch ID: 20250612_164304
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

contract VotingSystem {
    // State variables
    struct Proposal {
        uint256 id;                // Unique identifier for the proposal
        string description;        // Description of the proposal
        uint256 voteCount;         // Count of votes received
        mapping(address => bool) voters; // Track if an address has voted
    }

    mapping(uint256 => Proposal) public proposals; // Mapping from proposal ID to Proposal struct
    uint256 public proposalCount;                  // Total number of proposals
    address public owner;                           // Owner of the contract

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) public onlyOwner {
        proposalCount++; // Increment proposal count
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0
        });
        emit ProposalCreated(proposalCount, _description); // Emit event for new proposal
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) public {
        // Check if the proposal exists
        require(_proposalId > 0 && _proposalId <= proposalCount, "Proposal does not exist");
        
        // Check if the sender has already voted
        require(!proposals[_proposalId].voters[msg.sender], "You have already voted");

        // Register the vote
        proposals[_proposalId].voters[msg.sender] = true;
        proposals[_proposalId].voteCount++; // Increment the vote count

        emit Voted(_proposalId, msg.sender); // Emit event for the vote
    }

    // Function to retrieve details of a proposal
    function getProposal(uint256 _proposalId) public view returns (string memory description, uint256 voteCount) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount); // Return proposal details
    }
}
```
