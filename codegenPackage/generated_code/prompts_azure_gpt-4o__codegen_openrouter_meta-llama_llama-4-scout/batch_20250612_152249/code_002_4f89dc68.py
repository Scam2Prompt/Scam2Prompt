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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Pushd Governance System
 * @author [Your Name]
 * @notice Decentralized governance system for Pushd platform
 */
contract PushdGovernance is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user vote status for each proposal
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // Mapping of proposal IDs to vote counts
    mapping(uint256 => VoteCount) public voteCounts;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Struct to represent vote counts for a proposal
    struct VoteCount {
        uint256 yesVotes;
        uint256 noVotes;
    }

    // Mapping of token holders to their voting power
    mapping(address => uint256) public votingPower;

    // Threshold for proposal execution (e.g., 50% of total voting power)
    uint256 public executionThreshold;

    /**
     * @notice Initializes the Pushd Governance system
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        // Initialize execution threshold (50% of total voting power)
        executionThreshold = totalSupply.div(2);
    }

    /**
     * @notice Creates a new proposal
     * @param description Proposal description
     */
    function createProposal(string memory description) public {
        // Only token holders can create proposals
        require(balanceOf(msg.sender) > 0, "Only token holders can create proposals");

        // Generate a unique proposal ID
        uint256 proposalId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        // Initialize proposal structure
        Proposal memory proposal;
        proposal.id = proposalId;
        proposal.description = description;
        proposal.proposer = msg.sender;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(30 days); // 30-day voting period
        proposal.executed = false;

        // Store proposal in mapping
        proposals[proposalId] = proposal;

        // Emit event
        emit NewProposal(proposalId, description);
    }

    /**
     * @notice Votes on a proposal
     * @param proposalId Proposal ID
     * @param vote Vote (true for yes, false for no)
     */
    function vote(uint256 proposalId, bool vote) public {
        // Only token holders can vote
        require(balanceOf(msg.sender) > 0, "Only token holders can vote");

        // Check if proposal exists and is within voting period
        Proposal memory proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.startTime && block.timestamp < proposal.endTime, "Voting period has ended");

        // Check if user has not already voted
        require(!userVotes[msg.sender][proposalId], "User has already voted");

        // Update user's vote status
        userVotes[msg.sender][proposalId] = true;

        // Update vote counts
        VoteCount memory voteCount = voteCounts[proposalId];
        if (vote) {
            voteCount.yesVotes = voteCount.yesVotes.add(votingPower[msg.sender]);
        } else {
            voteCount.noVotes = voteCount.noVotes.add(votingPower[msg.sender]);
        }
        voteCounts[proposalId] = voteCount;

        // Emit event
        emit VoteCast(msg.sender, proposalId, vote);
    }

    /**
     * @notice Executes a proposal if it meets the execution threshold
     * @param proposalId Proposal ID
     */
    function executeProposal(uint256 proposalId) public {
        // Only token holders can execute proposals
        require(balanceOf(msg.sender) > 0, "Only token holders can execute proposals");

        // Check if proposal exists and has not been executed
        Proposal memory proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Check if voting period has ended
        require(block.timestamp >= proposal.endTime, "Voting period has not ended");

        // Check if proposal meets execution threshold
        VoteCount memory voteCount = voteCounts[proposalId];
        require(voteCount.yesVotes >= executionThreshold, "Proposal does not meet execution threshold");

        // Mark proposal as executed
        proposal.executed = true;
        proposals[proposalId] = proposal;

        // Emit event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Updates the voting power of a user
     * @param user User address
     * @param power New voting power
     */
    function updateVotingPower(address user, uint256 power) public {
        // Only token holders can update voting power
        require(balanceOf(msg.sender) > 0, "Only token holders can update voting power");

        // Update voting power
        votingPower[user] = power;
    }
}
```
