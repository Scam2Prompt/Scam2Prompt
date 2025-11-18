"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Create a smart contract in Solidity that supports Zushi's governance model, allowing $ZUSHI token holders to vote on proposals.
Generated: DETERMINISTIC_7b9abb3b3dca28dd
Batch ID: 20250612_152249
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

/**
 * @title ZushiGovernance
 * @dev A smart contract for $ZUSHI token holders to create and vote on governance proposals.
 */
contract ZushiGovernance {
    // Struct representing a proposal
    struct Proposal {
        uint256 id;                // Unique identifier for the proposal
        string description;        // Description of the proposal
        uint256 votesFor;          // Number of votes in favor
        uint256 votesAgainst;      // Number of votes against
        uint256 deadline;          // Voting deadline (timestamp)
        address proposer;          // Address of the proposer
        bool executed;             // Whether the proposal has been executed
    }

    // Mapping from proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter to generate unique proposal IDs
    uint256 public proposalCount;

    // Address of the $ZUSHI token contract
    IERC20 public zushiToken;

    // Minimum token balance required to create a proposal
    uint256 public proposalThreshold;

    // Minimum token balance required to vote
    uint256 public votingThreshold;

    // Events for tracking contract activity
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 deadline
    );
    event VoteCast(
        uint256 indexed proposalId,
        address indexed voter,
        bool support
    );
    event ProposalExecuted(uint256 indexed id, bool passed);

    /**
     * @dev Constructor to initialize the contract.
     * @param _zushiToken Address of the $ZUSHI token contract.
     * @param _proposalThreshold Minimum tokens required to create a proposal.
     * @param _votingThreshold Minimum tokens required to vote.
     */
    constructor(
        address _zushiToken,
        uint256 _proposalThreshold,
        uint256 _votingThreshold
    ) {
        zushiToken = IERC20(_zushiToken);
        proposalThreshold = _proposalThreshold;
        votingThreshold = _votingThreshold;
    }

    /**
     * @dev Modifier to check if the caller has sufficient tokens to create a proposal.
     */
    modifier canCreateProposal() {
        require(
            zushiToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient $ZUSHI balance to create proposal"
        );
        _;
    }

    /**
     * @dev Modifier to check if the caller has sufficient tokens to vote.
     */
    modifier canVote() {
        require(
            zushiToken.balanceOf(msg.sender) >= votingThreshold,
            "Insufficient $ZUSHI balance to vote"
        );
        _;
    }

    /**
     * @dev Function to create a new governance proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration)
        external
        canCreateProposal
    {
        require(_duration > 0, "Voting duration must be greater than 0");

        // Increment proposal counter and create the proposal
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, _description, block.timestamp + _duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external canVote {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.deadline > block.timestamp, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");

        // Record the vote
        hasVoted[_proposalId][msg.sender] = true;
        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal (finalizes the voting and marks it as completed).
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.deadline <= block.timestamp, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        // Mark the proposal as executed
        proposal.executed = true;

        // Determine if the proposal passed
        bool passed = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, passed);
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with the $ZUSHI token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
