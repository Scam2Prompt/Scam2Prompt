"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Create a smart contract that supports zkSwap Finance's governance model, allowing users to vote and create proposals via yZF tokens.
Generated: DETERMINISTIC_4972db42a87fcd62
Batch ID: 20250612_154728
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
 * @title Governance Contract for zkSwap Finance
 * @author zkSwap Development Team
 * @notice This contract facilitates proposal creation and voting using yZF tokens.
 */
contract zkSwapGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        address creator;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline; // Timestamp when the voting ends
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether a user has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // yZF token interface
    IERC20 public yZFToken;

    // Proposal counter for unique IDs
    uint256 public proposalCounter;

    // Events
    event ProposalCreated(uint256 id, string description, address creator, uint256 deadline);
    event VoteCast(uint256 id, address voter, bool voteFor, uint256 votingPower);
    event ProposalExecuted(uint256 id, bool success);

    // Modifier to ensure only yZF token holders can interact
    modifier onlyTokenHolder() {
        require(yZFToken.balanceOf(msg.sender) > 0, "You must hold yZF tokens to participate.");
        _;
    }

    /**
     * @notice Constructor to initialize the governance contract.
     * @param _yZFTokenAddress Address of the yZF token contract.
     */
    constructor(address _yZFTokenAddress) {
        require(_yZFTokenAddress != address(0), "Invalid token address.");
        yZFToken = IERC20(_yZFTokenAddress);
    }

    /**
     * @notice Function to create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Duration of the voting period in seconds.
     * @return Proposal ID.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyTokenHolder returns (uint256) {
        require(_duration > 0, "Duration must be greater than zero.");

        proposalCounter++;
        uint256 proposalId = proposalCounter;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            creator: msg.sender,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, msg.sender, block.timestamp + _duration);

        return proposalId;
    }

    /**
     * @notice Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _voteFor True to vote for, false to vote against.
     */
    function vote(uint256 _proposalId, bool _voteFor) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist.");
        require(block.timestamp <= proposal.deadline, "Voting period has ended.");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        uint256 voterBalance = yZFToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold yZF tokens to vote.");

        if (_voteFor) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _voteFor, voterBalance);
    }

    /**
     * @notice Function to execute a proposal after voting has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist.");
        require(block.timestamp > proposal.deadline, "Voting period has not ended.");
        require(!proposal.executed, "Proposal has already been executed.");

        // Simple majority logic: votesFor > votesAgainst
        bool success = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(_proposalId, success);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
