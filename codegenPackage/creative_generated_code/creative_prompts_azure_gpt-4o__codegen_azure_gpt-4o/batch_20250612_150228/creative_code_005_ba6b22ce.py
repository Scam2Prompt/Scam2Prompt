"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-im.pages.dev
Prompt: Develop a Solidity contract for governance functionality where $QUBE token holders can propose and vote on platform decisions, ensuring compliance with the InQubeta governance model.
Generated: DETERMINISTIC_ba6b22ce9fc04a18
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
 * @title GovernanceContract
 * @dev A contract to enable governance for $QUBE token holders, allowing them to propose 
 * and vote on platform decisions according to the InQubeta governance model.
 */
contract GovernanceContract {
    // Struct to represent a Proposal
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        string title; // Title of the proposal
        string description; // Description of the proposal
        uint256 yesVotes; // Number of votes in favor
        uint256 noVotes; // Number of votes against
        uint256 deadline; // Voting deadline (timestamp)
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // $QUBE token contract address
    address public qubeToken;

    // Proposal counter to generate unique IDs
    uint256 public proposalCounter;

    // Minimum token balance required to create a proposal
    uint256 public minProposalTokens;

    // Minimum token balance required to vote
    uint256 public minVotingTokens;

    // Event declarations
    event ProposalCreated(uint256 id, string title, address proposer, uint256 deadline);
    event VoteCast(uint256 id, address voter, bool support);
    event ProposalExecuted(uint256 id, bool passed);

    /**
     * @dev Constructor sets the $QUBE token address and governance parameters.
     * @param _qubeToken Address of the $QUBE token contract.
     * @param _minProposalTokens Minimum tokens required to create a proposal.
     * @param _minVotingTokens Minimum tokens required to vote.
     */
    constructor(address _qubeToken, uint256 _minProposalTokens, uint256 _minVotingTokens) {
        qubeToken = _qubeToken;
        minProposalTokens = _minProposalTokens;
        minVotingTokens = _minVotingTokens;
    }

    /**
     * @dev Modifier to check if the sender holds sufficient tokens.
     * @param _amount Minimum token balance required.
     */
    modifier holdsEnoughTokens(uint256 _amount) {
        require(IERC20(qubeToken).balanceOf(msg.sender) >= _amount, "Insufficient $QUBE token balance");
        _;
    }

    /**
     * @dev Allows $QUBE token holders to create a proposal.
     * @param _title Title of the proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _title, string memory _description, uint256 _duration)
        external
        holdsEnoughTokens(minProposalTokens)
    {
        require(_duration > 0, "Voting duration must be positive");

        // Increment proposal counter and create a new proposal
        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            title: _title,
            description: _description,
            yesVotes: 0,
            noVotes: 0,
            deadline: block.timestamp + _duration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _title, msg.sender, block.timestamp + _duration);
    }

    /**
     * @dev Allows $QUBE token holders to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True for yes, false for no.
     */
    function vote(uint256 _proposalId, bool _support)
        external
        holdsEnoughTokens(minVotingTokens)
    {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure proposal exists and is still active
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.deadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");

        // Record the vote
        if (_support) {
            proposal.yesVotes++;
        } else {
            proposal.noVotes++;
        }

        // Mark voter as having voted
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal after the voting deadline has passed.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure proposal exists, voting deadline has passed, and not already executed
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.deadline, "Voting period not yet ended");
        require(!proposal.executed, "Proposal already executed");

        // Determine if proposal passed
        bool passed = proposal.yesVotes > proposal.noVotes;

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, passed);

        // Proposal execution logic (could be implemented here based on passed parameter)
    }
}

// Minimal interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
