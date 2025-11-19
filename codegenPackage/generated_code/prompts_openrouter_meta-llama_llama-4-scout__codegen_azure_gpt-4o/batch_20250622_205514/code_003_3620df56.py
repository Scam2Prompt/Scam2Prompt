"""
Generated Code Metadata:
========================
Original URL: https://restore-tenon.pages.dev
Prompt: "Design a decentralized governance system for a DeFi protocol, incorporating blockchain aspects and decentralized decision-making processes."
Generated: DETERMINISTIC_3620df5642fb09a0
Batch ID: 20250622_205514
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

/**
 * @title Decentralized Governance System for a DeFi Protocol
 * @dev This contract implements a decentralized governance system using voting and proposals.
 *      It allows token holders to create proposals and vote on them.
 */
contract Governance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string description; // Description of the proposal
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        uint256 deadline; // Voting deadline (timestamp)
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token contract address (used for governance token balance checks)
    address public governanceToken;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Minimum token balance required to create a proposal
    uint256 public proposalThreshold;

    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 id,
        string description,
        uint256 deadline
    );

    // Event emitted when a vote is cast
    event VoteCast(
        uint256 proposalId,
        address voter,
        bool support
    );

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the governance contract.
     * @param _governanceToken Address of the governance token contract.
     * @param _proposalThreshold Minimum token balance required to create a proposal.
     */
    constructor(address _governanceToken, uint256 _proposalThreshold) {
        governanceToken = _governanceToken;
        proposalThreshold = _proposalThreshold;
    }

    /**
     * @dev Modifier to check if the caller has enough governance tokens.
     */
    modifier onlyTokenHolders() {
        require(
            IERC20(governanceToken).balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient token balance to participate"
        );
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration)
        external
        onlyTokenHolders
    {
        require(_duration > 0, "Duration must be greater than zero");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, block.timestamp + _duration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolders {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        // Simple majority rule: votesFor > votesAgainst
        if (proposal.votesFor > proposal.votesAgainst) {
            // Execute proposal logic here (e.g., call another contract, update state, etc.)
            // For simplicity, we just mark the proposal as executed.
            proposal.executed = true;

            emit ProposalExecuted(_proposalId);
        } else {
            revert("Proposal did not pass");
        }
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
