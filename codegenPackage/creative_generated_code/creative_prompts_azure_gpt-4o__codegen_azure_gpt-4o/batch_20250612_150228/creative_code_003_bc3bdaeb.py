"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Write a smart contract in Solidity that implements a decentralized governance system for Pushd token holders, allowing them to vote on platform changes and proposals. Include functionality for weighted voting based on token holdings.
Generated: DETERMINISTIC_bc3bdaeba0f00896
Batch ID: 20250612_150228
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
 * @title Pushd Governance Contract
 * @dev A decentralized governance system for Pushd token holders to vote on proposals.
 * Weighted voting implemented based on token holdings.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract PushdGovernance {
    // Struct representing a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteStart; // Start time of voting
        uint256 voteEnd; // End time of voting
        uint256 votesFor; // Weighted votes in favor
        uint256 votesAgainst; // Weighted votes against
        bool executed; // Whether the proposal has been executed
    }

    // Address of the Pushd token contract
    IERC20 public immutable pushdToken;

    // Array to store all proposals
    Proposal[] public proposals;

    // Mapping to track whether a voter has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 voteStart, uint256 voteEnd);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 weight);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId, bool success);

    /**
     * @dev Constructor to initialize the governance contract.
     * @param _pushdToken Address of the Pushd token contract.
     */
    constructor(address _pushdToken) {
        require(_pushdToken != address(0), "Invalid token address");
        pushdToken = IERC20(_pushdToken);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param _voteDuration Duration of the voting period in seconds.
     */
    function createProposal(string memory _description, uint256 _voteDuration) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_voteDuration > 0, "Vote duration must be greater than zero");

        uint256 voteStart = block.timestamp;
        uint256 voteEnd = block.timestamp + _voteDuration;

        proposals.push(Proposal({
            description: _description,
            voteStart: voteStart,
            voteEnd: voteEnd,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, _description, voteStart, voteEnd);
    }

    /**
     * @dev Cast a vote on a proposal.
     * @param _proposalId ID of the proposal.
     * @param _support True for voting in favor, false for voting against.
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.voteStart, "Voting has not started");
        require(block.timestamp <= proposal.voteEnd, "Voting has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        uint256 voterBalance = pushdToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Must hold Pushd tokens to vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        emit VoteCast(msg.sender, _proposalId, _support, voterBalance);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param _proposalId ID of the proposal.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp > proposal.voteEnd, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, success);

        // Additional logic for executing the proposal should be implemented here
    }

    /**
     * @dev Get the number of proposals created.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get details of a specific proposal.
     * @param _proposalId ID of the proposal.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId) external view returns (
        string memory description,
        uint256 voteStart,
        uint256 voteEnd,
        uint256 votesFor,
        uint256 votesAgainst,
        bool executed
    ) {
        require(_proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.description,
            proposal.voteStart,
            proposal.voteEnd,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.executed
        );
    }
}
```
