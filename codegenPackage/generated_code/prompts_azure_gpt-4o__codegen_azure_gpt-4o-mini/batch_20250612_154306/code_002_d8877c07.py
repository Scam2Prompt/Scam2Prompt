"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate Solidity code for creating a Decentralized Autonomous Organization (DAO) on Ethereum, incorporating governance mechanisms as described in the rise of DAOs on Ethereum.
Generated: DETERMINISTIC_d8877c071d205ac3
Batch ID: 20250612_154306
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// DAO contract
contract DAO is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public governanceToken; // Governance token used for voting
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposals
    uint256 public votingDuration; // Duration of voting period

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the DAO
    constructor(IERC20 _governanceToken, uint256 _votingDuration) {
        governanceToken = _governanceToken;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 newProposalId = proposalIdCounter.current();
        uint256 endTime = block.timestamp + votingDuration;

        Proposal storage newProposal = proposals[newProposalId];
        newProposal.id = newProposalId;
        newProposal.description = _description;
        newProposal.endTime = endTime;

        emit ProposalCreated(newProposalId, _description, endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is still active
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += governanceToken.balanceOf(msg.sender);

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is executable
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.endTime, "Voting is still active");
        require(!proposal.executed, "Proposal has already been executed");

        // Check if the proposal has enough votes (simple majority)
        require(proposal.voteCount > (governanceToken.totalSupply() / 2), "Not enough votes");

        // Execute the proposal (implementation depends on the proposal's nature)
        // For demonstration, we will just mark it as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
