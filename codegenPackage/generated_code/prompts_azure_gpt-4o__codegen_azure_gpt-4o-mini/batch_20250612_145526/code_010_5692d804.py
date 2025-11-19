"""
Generated Code Metadata:
========================
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a Solidity contract to implement EarthMeta's governance mechanism, allowing users to vote on virtual city policies using $EMT tokens.
Generated: DETERMINISTIC_5692d804f611ffcc
Batch ID: 20250612_145526
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
 * @title EarthMeta Governance Contract
 * @dev This contract allows users to vote on virtual city policies using $EMT tokens.
 */
contract EarthMetaGovernance is Ownable {
    using Counters for Counters.Counter;

    // Structure to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        mapping(address => bool) voters; // Track if an address has voted
        bool executed; // Status of proposal execution
    }

    // State variables
    IERC20 public emtToken; // Reference to the $EMT token contract
    Counters.Counter private proposalIdCounter; // Counter for proposal IDs
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    uint256 public votingDuration; // Duration for voting in seconds

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the voting period is active
    modifier onlyDuringVoting(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].voteCount + votingDuration, "Voting period has ended");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _emtToken, uint256 _votingDuration) {
        emtToken = _emtToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();
        Proposal storage newProposal = proposals[proposalId];
        newProposal.description = description;
        newProposal.voteCount = block.timestamp; // Set the start time for voting

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external onlyDuringVoting(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Check if the voter has already voted
        require(!proposal.voters[msg.sender], "You have already voted");

        // Transfer $EMT tokens from the voter to the contract
        uint256 voterBalance = emtToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold $EMT tokens to vote");
        
        // Update the proposal's vote count
        proposal.voteCount += voterBalance;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if the voting period has ended.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];

        // Ensure the proposal has not been executed and the voting period has ended
        require(!proposal.executed, "Proposal has already been executed");
        require(block.timestamp >= proposal.voteCount + votingDuration, "Voting period is still active");

        // Logic to execute the proposal can be added here

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}
```
