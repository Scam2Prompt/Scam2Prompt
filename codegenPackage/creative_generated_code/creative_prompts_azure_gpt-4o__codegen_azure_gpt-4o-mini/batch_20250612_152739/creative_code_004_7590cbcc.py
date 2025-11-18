"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Provide code for a DAO (Decentralized Autonomous Organization) smart contract that allows participants to vote on proposals and earn token discounts and yield opportunities, inspired by AllianceBlock's participative economy model.
Generated: DETERMINISTIC_7590cbcc2c33c1b2
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for proposal structure
interface IProposal {
    struct Proposal {
        address proposer;
        string description;
        uint256 voteCount;
        mapping(address => bool) hasVoted;
        bool completed;
    }
}

// DAO Smart Contract
contract DecentralizedAutonomousOrganization is Ownable, IProposal {
    // State variables
    IERC20 public votingToken; // Token used for voting
    Proposal[] public proposals; // Array to store proposals
    mapping(address => uint256) public discounts; // Discounts based on participation

    // Events
    event ProposalCreated(uint256 proposalId, address proposer, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalCompleted(uint256 proposalId, bool success);

    // Constructor to set the voting token
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    // Function to create a new proposal
    function createProposal(string memory description) external {
        Proposal storage newProposal = proposals.push();
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.completed = false;

        emit ProposalCreated(proposals.length - 1, msg.sender, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.hasVoted[msg.sender], "You have already voted");
        proposal.hasVoted[msg.sender] = true;

        // Increment vote count
        proposal.voteCount += 1;
        discounts[msg.sender] += 1; // Increment discount for participation

        emit Voted(proposalId, msg.sender);
    }

    // Function to complete a proposal
    function completeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.completed, "Proposal already completed");

        proposal.completed = true;
        // Example logic to determine success (can be customized)
        bool success = proposal.voteCount > (totalSupply() / 2); // Simple majority
        emit ProposalCompleted(proposalId, success);
    }

    // Function to get the total supply of voting tokens (for majority calculation)
    function totalSupply() public view returns (uint256) {
        return votingToken.totalSupply();
    }

    // Function to get details of a proposal
    function getProposal(uint256 proposalId) external view returns (
        address proposer,
        string memory description,
        uint256 voteCount,
        bool completed
    ) {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        
        return (proposal.proposer, proposal.description, proposal.voteCount, proposal.completed);
    }

    // Function to claim discounts (This is a placeholder function)
    function claimDiscount() external {
        require(discounts[msg.sender] > 0, "No discounts available");
        // Logic to apply discounts goes here (e.g., redeem for tokens)
        discounts[msg.sender] = 0; // Reset discount after claiming
    }
}
```
