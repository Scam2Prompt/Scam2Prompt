"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinuairdrop.pages.dev
Prompt: Generate code for a governance voting system that allows $AI holders to participate in community decisions, ensuring compatibility across EVM and non-EVM chains.
Generated: DETERMINISTIC_101165c482eb5c77
Batch ID: 20250612_153401
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
 * @title Governance Voting System
 * @dev This contract allows $AI token holders to participate in community decisions.
 * It is designed to be compatible with both EVM-based and non-EVM chains that support Solidity.
 */
contract GovernanceVoting {

    // Address of the $AI token contract (ERC20 compatible)
    address public aiToken;

    // Structure to hold proposal information
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Mapping of proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a particular proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter to generate unique proposal IDs
    uint256 public proposalCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed id, string description, uint256 startTime, uint256 endTime);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed id, bool success);

    /**
     * @dev Modifier to ensure only $AI token holders can perform certain actions.
     */
    modifier onlyTokenHolder() {
        require(IERC20(aiToken).balanceOf(msg.sender) > 0, "Must hold $AI tokens to participate.");
        _;
    }

    /**
     * @dev Constructor to initialize the governance voting system.
     * @param _aiToken Address of the $AI token contract.
     */
    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid $AI token address.");
        aiToken = _aiToken;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description The description of the proposal.
     * @param _duration The voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyTokenHolder {
        require(bytes(_description).length > 0, "Proposal description cannot be empty.");
        require(_duration > 0, "Voting duration must be greater than zero.");

        proposalCounter++;
        uint256 currentTimestamp = block.timestamp;

        proposals[proposalCounter] = Proposal(
            proposalCounter,
            _description,
            0,
            0,
            currentTimestamp,
            currentTimestamp + _duration,
            false
        );

        emit ProposalCreated(proposalCounter, _description, currentTimestamp, currentTimestamp + _duration);
    }

    /**
     * @dev Function to cast a vote on a proposal.
     * @param _proposalId The ID of the proposal being voted on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.startTime, "Voting has not started yet.");
        require(block.timestamp <= proposal.endTime, "Voting has ended.");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.endTime, "Voting has not ended yet.");
        require(!proposal.executed, "Proposal has already been executed.");

        // Proposal execution logic can be implemented here (e.g., governance actions).
        // For this example, we simply mark the proposal as executed.
        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, success);
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
