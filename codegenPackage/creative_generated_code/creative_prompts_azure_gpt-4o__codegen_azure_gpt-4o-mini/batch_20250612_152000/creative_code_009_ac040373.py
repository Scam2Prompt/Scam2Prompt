"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Develop a blockchain-based voting system for DAOs, inspired by TrustPad's decentralized governance model.
Generated: DETERMINISTIC_ac04037397070e90
Batch ID: 20250612_152000
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

// Interface for the governance token
interface IGovernanceToken {
    function balanceOf(address account) external view returns (uint256);
}

// Main contract for the DAO voting system
contract DAOVoting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount; // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
        bool isActive; // Status of the proposal
    }

    // Governance token contract
    IGovernanceToken public governanceToken;
    
    // Array of proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the governance token address
    constructor(address tokenAddress) {
        governanceToken = IGovernanceToken(tokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory description) external {
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            isActive: true
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        // Validate proposal ID
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        // Ensure proposal is active
        require(proposal.isActive, "Proposal is no longer active");

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Ensure the voter has enough governance tokens to vote
        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Insufficient governance tokens");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += voterBalance; // Increment vote count by the voter's token balance
        emit Voted(proposalId, msg.sender);
    }

    // Function to close a proposal
    function closeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        // Check if the proposal is active
        require(proposal.isActive, "Proposal is already closed");
        proposal.isActive = false; // Mark the proposal as closed
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, bool isActive) {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.isActive);
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```

### Important Notes:
- Make sure to deploy the governance token contract first and pass its address to the `DAOVoting` contract constructor.
- The `IGovernanceToken` interface is a minimal implementation. Depending on the actual governance token you use, you might want to expand this interface.
- The contract does not handle complex scenarios like voting weight distribution or multi-signature governance. Such features can be added as needed.
