"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a governance voting system in Solidity for a DeFi platform, inspired by Tenderize's TEND token governance model.
Generated: DETERMINISTIC_ea457a0229dd19f6
Batch ID: 20250612_145913
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// GovernanceVoting contract allows token holders to propose and vote on governance decisions
contract GovernanceVoting is Ownable {
    using SafeMath for uint256;

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
    IERC20 public governanceToken; // The governance token used for voting
    uint256 public proposalCount; // Total number of proposals
    uint256 public votingDuration; // Duration of voting in seconds
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the governance token and voting duration
    constructor(IERC20 _governanceToken, uint256 _votingDuration) {
        governanceToken = _governanceToken;
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        uint256 endTime = block.timestamp.add(votingDuration);
        
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description, endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is still active
        require(proposal.id > 0, "Proposal does not exist");
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(governanceToken.balanceOf(msg.sender));

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal exists and is still active
        require(proposal.id > 0, "Proposal does not exist");
        require(block.timestamp >= proposal.endTime, "Voting is still active");
        require(!proposal.executed, "Proposal has already been executed");

        // Check if the proposal has enough votes (for example, more than 50% of total supply)
        uint256 totalSupply = governanceToken.totalSupply();
        require(proposal.voteCount > totalSupply.div(2), "Not enough votes to execute");

        // Mark the proposal as executed
        proposal.executed = true;

        // Execute the proposal logic here (this is a placeholder)
        // For example, transferring funds, changing parameters, etc.

        emit ProposalExecuted(_proposalId);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (uint256, string memory, uint256, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.endTime, proposal.executed);
    }
}
```
