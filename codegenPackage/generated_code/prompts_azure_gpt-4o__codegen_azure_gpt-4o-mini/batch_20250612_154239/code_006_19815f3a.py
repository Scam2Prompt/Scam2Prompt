"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a Solidity implementation for decentralized governance that allows Bulldogito Coin holders to propose and vote on asset management strategies using their voting power.
Generated: DETERMINISTIC_19815f3a3d0e94e1
Batch ID: 20250612_154239
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
 * @title Bulldogito Governance Contract
 * @dev This contract allows Bulldogito Coin holders to propose and vote on asset management strategies.
 */
contract BulldogitoGovernance is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public bulldogitoToken; // Reference to the Bulldogito Coin token
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

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

    // Constructor to initialize the contract
    constructor(IERC20 _bulldogitoToken, uint256 _votingDuration) {
        bulldogitoToken = _bulldogitoToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal
     * @param description The description of the proposal
     */
    function createProposal(string calldata description) external {
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();
        uint256 endTime = block.timestamp + votingDuration;

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, msg.sender, description, endTime);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) votingActive(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Get the voting power of the voter
        uint256 votingPower = bulldogitoToken.balanceOf(msg.sender);
        require(votingPower > 0, "You have no voting power");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount += votingPower;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if voting has ended and it has enough votes
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) votingEnded(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > 0, "No votes were cast");

        // Logic to execute the proposal goes here
        // For example, transferring assets or changing state based on the proposal

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Set a new voting duration
     * @param newDuration The new voting duration in seconds
     */
    function setVotingDuration(uint256 newDuration) external onlyOwner {
        votingDuration = newDuration;
    }
}
```
