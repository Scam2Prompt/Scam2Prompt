"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Create a decentralized governance system in Solidity for a platform like Pushd, allowing token holders to vote on proposals and changes to platform features and policies.
Generated: DETERMINISTIC_4f89dc68c55b8563
Batch ID: 20250612_152249
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

/**
 * @title Decentralized Governance System
 * @dev This contract allows token holders to create and vote on proposals.
 */
contract Governance is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold proposal details
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public token; // ERC20 token used for voting
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 id, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalIdCounter.current(), "Proposal does not exist");
        _;
    }

    // Modifier to check if the voting period has ended
    modifier votingActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].endTime, "Voting has ended");
        _;
    }

    // Modifier to check if the voting period has ended
    modifier votingEnded(uint256 proposalId) {
        require(block.timestamp >= proposals[proposalId].endTime, "Voting is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the governance contract.
     * @param _token Address of the ERC20 token used for voting.
     * @param _votingDuration Duration for voting in seconds.
     */
    constructor(IERC20 _token, uint256 _votingDuration) {
        token = _token;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the proposal.
     */
    function createProposal(string calldata description) external onlyOwner {
        uint256 proposalId = proposalIdCounter.current();
        proposalIdCounter.increment();

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = description;
        newProposal.endTime = block.timestamp + votingDuration;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, description, newProposal.endTime);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) votingActive(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer tokens to the contract as a vote
        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold tokens to vote");
        
        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += voterBalance;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if voting has ended and it has enough votes.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) votingEnded(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes were cast");

        // Logic to execute the proposal goes here
        // For example, changing platform features or policies

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId ID of the proposal.
     * @return id, description, voteCount, endTime, executed status
     */
    function getProposal(uint256 proposalId) external view proposalExists(proposalId) returns (
        uint256 id,
        string memory description,
        uint256 voteCount,
        uint256 endTime,
        bool executed
    ) {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.endTime, proposal.executed);
    }
}
```
