"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Create a decentralized voting system in Solidity that aligns with the governance model described for Global Miracle Coin, using the LYCAN Chain infrastructure.
Generated: DETERMINISTIC_8185ea6ca9798b5c
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title Decentralized Voting System for Global Miracle Coin
 * @author [Your Name]
 * @notice This contract implements a decentralized voting system for Global Miracle Coin
 * @dev This contract uses LYCAN Chain infrastructure and follows best practices for security and accessibility
 */
contract DecentralizedVotingSystem is AccessControl, ReentrancyGuard {
    using Strings for uint256;

    // Define roles for access control
    bytes32 public constant VOTER_ROLE = keccak256("VOTER_ROLE");
    bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");

    // Mapping of voters to their voting power
    mapping(address => uint256) public voterVotingPower;

    // Mapping of proposals to their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voters to their votes
    mapping(uint256 => mapping(address => Vote)) public votes;

    // Total number of proposals
    uint256 public totalProposals;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a voter casts a vote
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 proposalId;
        string proposalDescription;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Struct to represent a vote
    struct Vote {
        bool vote; // true for yes, false for no
        bool cast;
    }

    /**
     * @dev Initializes the contract
     */
    constructor() {
        // Set up access control roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(PROPOSER_ROLE, msg.sender);

        // Initialize total proposals to 0
        totalProposals = 0;
    }

    /**
     * @dev Creates a new proposal
     * @param proposalDescription Description of the proposal
     */
    function createProposal(string memory proposalDescription) public onlyRole(PROPOSER_ROLE) {
        // Create a new proposal
        Proposal memory proposal;
        proposal.proposalId = totalProposals;
        proposal.proposalDescription = proposalDescription;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        // Store the proposal
        proposals[totalProposals] = proposal;

        // Emit event
        emit NewProposal(totalProposals, proposalDescription);

        // Increment total proposals
        totalProposals++;
    }

    /**
     * @dev Casts a vote on a proposal
     * @param proposalId ID of the proposal
     * @param vote Vote (true for yes, false for no)
     */
    function castVote(uint256 proposalId, bool vote) public nonReentrant {
        // Check if the proposal exists
        require(proposals[proposalId].proposalId == proposalId, "Proposal does not exist");

        // Check if the voter has voting power
        require(voterVotingPower[msg.sender] > 0, "Voter has no voting power");

        // Check if the voter has not already voted
        require(!votes[proposalId][msg.sender].cast, "Voter has already voted");

        // Update the voter's vote
        votes[proposalId][msg.sender] = Vote(vote, true);

        // Update the proposal's vote count
        if (vote) {
            proposals[proposalId].yesVotes += voterVotingPower[msg.sender];
        } else {
            proposals[proposalId].noVotes += voterVotingPower[msg.sender];
        }

        // Emit event
        emit VoteCast(proposalId, msg.sender, vote);
    }

    /**
     * @dev Executes a proposal if it has passed
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) public nonReentrant {
        // Check if the proposal exists
        require(proposals[proposalId].proposalId == proposalId, "Proposal does not exist");

        // Check if the proposal has not already been executed
        require(!proposals[proposalId].executed, "Proposal has already been executed");

        // Check if the proposal has passed
        require(proposals[proposalId].yesVotes > proposals[proposalId].noVotes, "Proposal has not passed");

        // Mark the proposal as executed
        proposals[proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Sets the voting power of a voter
     * @param voter Address of the voter
     * @param votingPower Voting power of the voter
     */
    function setVoterVotingPower(address voter, uint256 votingPower) public onlyRole(DEFAULT_ADMIN_ROLE) {
        voterVotingPower[voter] = votingPower;
    }

    /**
     * @dev Grants the voter role to an account
     * @param account Address of the account
     */
    function grantVoterRole(address account) public onlyRole(DEFAULT_ADMIN_ROLE) {
        _grantRole(VOTER_ROLE, account);
    }

    /**
     * @dev Revokes the voter role from an account
     * @param account Address of the account
     */
    function revokeVoterRole(address account) public onlyRole(DEFAULT_ADMIN_ROLE) {
        _revokeRole(VOTER_ROLE, account);
    }
}
```
