"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://go-beam.pages.dev
Prompt: Write a DAO governance smart contract that allows BEAM token holders to vote on protocol upgrades, reflecting the decentralized management approach mentioned on the BEAM site.
Generated: DETERMINISTIC_6e49fd5e5b1936ab
Batch ID: 20250612_150622
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

// Importing OpenZeppelin utilities for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DAO Governance Contract for BEAM Token Holders
contract BeamDAO is Ownable {
    IERC20 public beamToken; // Reference to the BEAM token contract

    // Struct to represent a proposal
    struct Proposal {
        uint id;
        string description; // Description of the upgrade
        uint voteCount; // Total votes for this proposal
        mapping(address => bool) voters; // Track if address has voted
        bool executed; // Has the proposal been executed?
    }

    mapping(uint => Proposal) public proposals; // List of proposals
    uint public proposalCount; // Total number of proposals

    // Events
    event ProposalCreated(uint id, string description);
    event Voted(uint proposalId, address voter);
    event ProposalExecuted(uint proposalId);

    // Constructor to set the BEAM token address
    constructor(address _beamToken) {
        require(_beamToken != address(0), "Invalid token address");
        beamToken = IERC20(_beamToken);
    }

    // Function to create a new proposal
    function createProposal(string calldata _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote on a proposal
    function vote(uint _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "You have already voted");
        require(beamToken.balanceOf(msg.sender) > 0, "No BEAM tokens to vote");

        // Register vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > getTotalSupply() / 2, "Not enough votes"); // 50% quorum

        // Logic to execute the proposal would go here. For now, we just mark it as executed.
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to get the total supply of BEAM tokens
    function getTotalSupply() internal view returns (uint) {
        return beamToken.totalSupply();
    }
}
```
