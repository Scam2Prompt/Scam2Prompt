"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonwell.site
Prompt: Generate a smart contract example for participating in Moonwell's governance using the WELL token, including voting on proposals.
Generated: DETERMINISTIC_bf9d12ff1bf03334
Batch ID: 20250612_145616
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

// @title Moonwell Governance Contract
// @dev This contract allows WELL token holders to participate in governance by voting on proposals.
contract MoonwellGovernance is Ownable {
    
    // Struct to represent a governance proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    IERC20 public wellToken; // WELL token contract address
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Proposals mapping

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description);
    
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the contract
    // @param _wellToken Address of the WELL token contract
    constructor(address _wellToken) {
        require(_wellToken != address(0), "Invalid WELL token address");
        wellToken = IERC20(_wellToken);
    }

    // Function to create a new proposal
    // @param _description Description of the proposal
    function createProposal(string memory _description) external onlyOwner {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    // @param _proposalId ID of the proposal to vote on
    function vote(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voters[msg.sender], "You have already voted");

        uint256 voterBalance = wellToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold WELL tokens to vote");

        proposal.voters[msg.sender] = true; // Mark voter as having voted
        proposal.voteCount += voterBalance; // Increment vote count by number of tokens held

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has received enough votes
    // @param _proposalId ID of the proposal to execute
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > (wellToken.totalSupply() / 2), "Not enough votes to execute");

        proposal.executed = true;

        // Logic for executing the proposal goes here
        // For example, transferring assets, updating state, etc.
    }
}
```
